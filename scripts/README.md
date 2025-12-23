# Gallery Update Script

This script automatically scans the gallery folders and updates the gallery page with all images.

## Usage

After adding new images to any play folder in `build/images/gallery/`, run:

```bash
npm run update-gallery
```

Or directly:

```bash
node scripts/update-gallery.js
```

## How It Works

1. Scans all folders in `build/images/gallery/`
2. Finds all image files (.jpg, .jpeg, .png, .gif, .webp) in each folder
3. Automatically updates the `playImages` object in `build/gallery.html`
4. Images appear in alphabetical order

## Adding Images to a Play

1. Navigate to the play's folder: `build/images/gallery/[Play Name]/`
2. Add your image files (any common image format)
3. Run `npm run update-gallery`
4. Commit and push the changes

The gallery will automatically display all images with navigation arrows!

## Example

To add photos to "Birthday Candles":

```bash
# Add images to the folder
cp new-photo-1.jpg "build/images/gallery/Birthday Candles/"
cp new-photo-2.jpg "build/images/gallery/Birthday Candles/"

# Update the gallery
npm run update-gallery

# Commit and push
git add .
git commit -m "Add new Birthday Candles photos"
git push
```

That's it! No manual code editing required.
