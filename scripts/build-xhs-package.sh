#!/usr/bin/env bash
# Build a .py-free copy of the skill for hosts that forbid Python uploads
# (e.g. some skill marketplaces). The skill computes odds by hand using the
# no-vig steps in references/modeling.md, so dropping scripts/ loses nothing
# functionally.
#
# Usage: scripts/build-xhs-package.sh [output_dir]
#   default output_dir: dist/world-cup-match-predictor-noscript

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="$REPO_ROOT/skills/world-cup-match-predictor"
OUT="${1:-$REPO_ROOT/dist/world-cup-match-predictor-noscript}"

rm -rf "$OUT"
mkdir -p "$OUT"

# Copy the skill, excluding the scripts/ folder and any python artifacts.
cp -R "$SRC/." "$OUT/"
rm -rf "$OUT/scripts" "$OUT"/**/__pycache__ 2>/dev/null || true
find "$OUT" -name '__pycache__' -type d -prune -exec rm -rf {} + 2>/dev/null || true
find "$OUT" -name '*.py' -delete 2>/dev/null || true
find "$OUT" -name '*.pyc' -delete 2>/dev/null || true

echo "Built py-free skill package at: $OUT"
echo "Files:"
find "$OUT" -type f | sed "s|$OUT/|  |" | sort

# Guard: fail loudly if any .py slipped through.
if find "$OUT" -name '*.py' | grep -q .; then
  echo "ERROR: .py files remain in the package" >&2
  exit 1
fi
echo "OK: no .py files in package"
