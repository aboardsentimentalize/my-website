# My Website

A static website deployed via GitHub Pages.

## Project Structure

```
my-website/
└── build/           # Static site files
    ├── index.html
    ├── about.html
    └── ...
```

## Deployment

Changes are made directly to the files in the `build/` directory. GitHub Actions automatically merges `claude/` branches into `main` and deploys the updated `build/` folder to GitHub Pages.

## Automated Workflows

This repository uses GitHub Actions to automatically create and merge pull requests for branches prefixed with `claude/`.

✅ Fully automated - no manual intervention required!
