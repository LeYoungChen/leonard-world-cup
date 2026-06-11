#!/usr/bin/env bash
# Build a Xiaohongshu-ready copy of the skill for hosts that only accept
# Markdown / text files (no .py, no .yaml). The skill computes odds by hand
# using the no-vig steps in references/modeling.md, so dropping scripts/ and
# agents/ loses nothing functionally.
#
# Usage: scripts/build-xhs-package.sh [output_dir]
#   default output_dir: dist/leonard-world-cup

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="$REPO_ROOT/skills/world-cup-match-predictor"
OUT="${1:-$REPO_ROOT/dist/leonard-world-cup}"

rm -rf "$OUT"
mkdir -p "$OUT"

# Copy the skill, then strip everything Xiaohongshu will not accept:
# scripts/ (.py), agents/ (.yaml), and any python artifacts. Keep Markdown only.
cp -R "$SRC/." "$OUT/"
rm -rf "$OUT/scripts" "$OUT/agents"
find "$OUT" -name '__pycache__' -type d -prune -exec rm -rf {} + 2>/dev/null || true
find "$OUT" -type f ! -name '*.md' -delete 2>/dev/null || true

echo "Built Markdown-only skill package at: $OUT"
echo "Files:"
find "$OUT" -type f | sed "s|$OUT/|  |" | sort

# Guard: fail loudly if any non-Markdown file slipped through.
if find "$OUT" -type f ! -name '*.md' | grep -q .; then
  echo "ERROR: non-Markdown files remain in the package" >&2
  find "$OUT" -type f ! -name '*.md' >&2
  exit 1
fi
echo "OK: package contains Markdown files only"
