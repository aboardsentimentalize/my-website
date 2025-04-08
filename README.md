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
