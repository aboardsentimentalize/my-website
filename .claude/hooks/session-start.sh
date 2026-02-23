#!/bin/bash
set -euo pipefail

# Only run in remote (Claude Code on the web) environments
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

# Verify Node.js is available (used by scripts/update-gallery.js)
node --version

# No npm packages to install (package.json has no dependencies)
echo "Environment ready."
