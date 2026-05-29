#!/bin/bash
set -e
echo "SIN-Hermes-Websearch-SerpAPI-Pool-Bundle"
BUNDLE="$HOME/.hermes/bundles/serpapi-pool"
mkdir -p "$BUNDLE" "$HOME/.hermes/scripts"
cp scripts/serpapi-pool.py "$HOME/.hermes/scripts/"
chmod +x "$HOME/.hermes/scripts/serpapi-pool.py"
echo "Installed: ~/.hermes/scripts/serpapi-pool.py"
echo ""
echo "Usage:"
echo "  python3 ~/.hermes/scripts/serpapi-pool.py         # get best key"
echo "  python3 ~/.hermes/scripts/serpapi-pool.py status  # show pool"
