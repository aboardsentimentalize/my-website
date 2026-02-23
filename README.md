# My Website

A simple static website built with Python Flask and Frozen-Flask.

## Project Structure

```
my-website/
├── app.py              # Flask application
├── freeze.py          # Script to generate static files
├── requirements.txt   # Python dependencies
├── templates/        # HTML templates
│   ├── base.html
│   ├── index.html
│   └── about.html
└── build/           # Generated static files
    ├── index.html
    └── about.html
```

## Development

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run development server:
   ```bash
   python app.py
   ```

3. Generate static files:
   ```bash
   python freeze.py
   ```

## Deployment

The site is deployed on Netlify. The `build` directory contains the static files that should be deployed.

## Automated Workflows

This repository uses GitHub Actions to automatically create and merge pull requests for branches prefixed with `claude/`.

✅ Fully automated - no manual intervention required!

## Direct Workflow (Web ↔ Local, no PR)

For working directly between Claude Code on the web and your local machine without going through PRs on `main`, use branches prefixed with `claude/direct-`.

These branches are **excluded** from the auto-PR/merge workflows, so pushes stay on the branch.

### Setup (first time, local)

```bash
git fetch origin claude/direct-<name>
git checkout claude/direct-<name>
```

### Sync loop

**Pull web changes locally:**
```bash
git pull origin claude/direct-<name>
```

**Push local changes to web:**
```bash
git push origin claude/direct-<name>
```

In Claude Code web, each new session will pick up the latest commits on the branch automatically.

### When ready to deploy

Merge the branch to `main` manually (or open a PR) when you want the changes to go live:
```bash
git checkout main
git merge claude/direct-<name>
git push origin main
```
