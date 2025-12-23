#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

const GALLERY_DIR = path.join(__dirname, '../build/images/gallery');
const GALLERY_HTML = path.join(__dirname, '../build/gallery.html');
const MANIFEST_PATH = path.join(__dirname, '../build/gallery-images.json');

// Function to get all image files in a directory
function getImageFiles(dir) {
  if (!fs.existsSync(dir)) return [];

  const files = fs.readdirSync(dir);
  return files
    .filter(file => /\.(jpg|jpeg|png|gif|webp)$/i.test(file))
    .sort()
    .map(file => `images/gallery/${path.basename(dir)}/${file}`);
}

// Extract existing data-play to folder name mapping from HTML
function getPlayMappings() {
  const html = fs.readFileSync(GALLERY_HTML, 'utf8');
  const playMappings = {};

  // Find all gallery-item divs with data-play and extract folder name from img src
  const regex = /<div class="gallery-item" data-play="([^"]+)"[\s\S]*?<img src="images\/gallery\/([^/]+)\//g;
  let match;

  while ((match = regex.exec(html)) !== null) {
    const playId = match[1];
    const folderName = match[2];
    playMappings[folderName] = playId;
  }

  return playMappings;
}

// Scan all play folders
function scanGalleryFolders() {
  const playMappings = getPlayMappings();

  const folders = fs.readdirSync(GALLERY_DIR)
    .filter(item => {
      const fullPath = path.join(GALLERY_DIR, item);
      return fs.statSync(fullPath).isDirectory();
    });

  const playImages = {};

  folders.forEach(folder => {
    // Use the existing play ID from HTML, or fall back to normalized folder name
    const playId = playMappings[folder] || folder.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
    const images = getImageFiles(path.join(GALLERY_DIR, folder));

    if (images.length > 0) {
      playImages[playId] = images;
    }
  });

  return playImages;
}

// Update gallery.html with the new playImages object
function updateGalleryHtml(playImages) {
  let html = fs.readFileSync(GALLERY_HTML, 'utf8');

  // Generate the playImages JavaScript object
  const playImagesLines = Object.entries(playImages).map(([key, images]) => {
    const imagesList = images.map(img => `'${img}'`).join(',\n                    ');
    return `                '${key}': [\n                    ${imagesList}\n                ]`;
  });

  const playImagesCode = `const fallbackPlayImages = {
${playImagesLines.join(',\n')}
            };`;

  // Replace the existing playImages object
  const regex = /const fallbackPlayImages = \{[\s\S]*?\};/;

  if (!regex.test(html)) {
    console.error('Could not find playImages object in gallery.html');
    process.exit(1);
  }

  html = html.replace(regex, playImagesCode);

  fs.writeFileSync(GALLERY_HTML, html, 'utf8');
  console.log('✓ Updated gallery.html with image list');

  // Print summary
  console.log('\nGallery images by play:');
  Object.entries(playImages).forEach(([play, images]) => {
    console.log(`  ${play}: ${images.length} image${images.length !== 1 ? 's' : ''}`);
  });
}

function writeManifest(playImages) {
  fs.writeFileSync(MANIFEST_PATH, JSON.stringify(playImages, null, 2));
  console.log(`✓ Wrote manifest to ${path.relative(path.join(__dirname, '..'), MANIFEST_PATH)}`);
}

// Main execution
try {
  console.log('Scanning gallery folders...');
  const playImages = scanGalleryFolders();

  if (Object.keys(playImages).length === 0) {
    console.log('No images found in gallery folders');
    process.exit(0);
  }

  writeManifest(playImages);
  updateGalleryHtml(playImages);
  console.log('\n✓ Gallery update complete!');
} catch (error) {
  console.error('Error updating gallery:', error.message);
  process.exit(1);
}
