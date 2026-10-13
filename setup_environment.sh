#!/bin/bash
set -e

echo "=== Python Fundamentals Assessment: Environment Setup ==="

if ! command -v python3 >/dev/null 2>&1; then
    echo "Python 3 was not found. Please install Python 3 and run this script again."
    exit 1
fi

echo "Using: $(python3 --version)"

if ! python3 -m pip --version >/dev/null 2>&1; then
    echo "pip is not available for Python 3. Please install pip and try again."
    exit 1
fi

python3 -m pip install --user pytest
echo
echo "Setup complete."
echo "Run tests with: python3 -m pytest tests/test_fundamentals.py -v"
