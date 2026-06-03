# World Cup Match Predictor Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a portable World Cup match prediction skill/workflow with professional probability modeling guidance, clickable source requirements, table/visual output formats, and a deterministic odds-normalization helper.

**Architecture:** Keep the public repository self-contained under `skills/world-cup-match-predictor/`, with a Codex-compatible `SKILL.md`, portable references, and Python scripts/tests. Also install a copy into `${CODEX_HOME:-$HOME/.codex}/skills/world-cup-match-predictor` after validation.

**Tech Stack:** Markdown, Python 3 standard library, `unittest`, Git, GitHub REST API.

---

### Task 1: Odds Normalization Script

**Files:**
- Create: `skills/world-cup-match-predictor/scripts/normalize_odds.py`
- Create: `tests/test_normalize_odds.py`

- [ ] **Step 1: Write failing tests**

Create tests for decimal odds conversion, no-vig normalization, invalid odds rejection, and rounded percentage correction.

- [ ] **Step 2: Run tests to verify RED**

Run: `python3 -m unittest tests/test_normalize_odds.py -v`
Expected: FAIL because `normalize_odds.py` does not exist.

- [ ] **Step 3: Implement script**

Implement a standard-library Python CLI and reusable functions:

- `raw_implied_probabilities(odds)`
- `normalize_no_vig(raw)`
- `to_percentages(probabilities, decimals=1)`
- CLI accepts three decimal odds and emits JSON.

- [ ] **Step 4: Run tests to verify GREEN**

Run: `python3 -m unittest tests/test_normalize_odds.py -v`
Expected: PASS.

### Task 2: Skill Markdown Resources

**Files:**
- Create: `skills/world-cup-match-predictor/SKILL.md`
- Create: `skills/world-cup-match-predictor/references/modeling.md`
- Create: `skills/world-cup-match-predictor/references/public-positioning.md`
- Create: `skills/world-cup-match-predictor/references/output-formats.md`
- Create: `skills/world-cup-match-predictor/agents/openai.yaml`
- Create: `tests/test_skill_structure.py`

- [ ] **Step 1: Write failing structure tests**

Test required files, frontmatter fields, cross-agent language, clickable source requirements, safety language, and reference navigation.

- [ ] **Step 2: Run tests to verify RED**

Run: `python3 -m unittest tests/test_skill_structure.py -v`
Expected: FAIL because skill markdown files do not exist.

- [ ] **Step 3: Implement skill resources**

Write concise, portable skill instructions and references aligned to the Chinese design spec.

- [ ] **Step 4: Run tests to verify GREEN**

Run: `python3 -m unittest tests/test_skill_structure.py -v`
Expected: PASS.

### Task 3: Validation And Local Installation

**Files:**
- Modify: `${CODEX_HOME:-$HOME/.codex}/skills/world-cup-match-predictor/*`

- [ ] **Step 1: Run Python tests**

Run: `python3 -m unittest discover -s tests -v`
Expected: PASS.

- [ ] **Step 2: Run Codex skill validator**

Run: `python3 /Users/chen/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/world-cup-match-predictor`
Expected: PASS.

- [ ] **Step 3: Install local copy**

Copy `skills/world-cup-match-predictor` into `${CODEX_HOME:-$HOME/.codex}/skills/world-cup-match-predictor`.

- [ ] **Step 4: Validate installed copy**

Run: `python3 /Users/chen/.codex/skills/.system/skill-creator/scripts/quick_validate.py ${CODEX_HOME:-$HOME/.codex}/skills/world-cup-match-predictor`
Expected: PASS.

### Task 4: Public GitHub Repository

**Files:**
- Create: `.gitignore`
- Create: `README.md`

- [ ] **Step 1: Initialize git repository**

Run: `git init`

- [ ] **Step 2: Add repo docs**

Create README with usage, safety, source-link requirements, and cross-agent guidance.

- [ ] **Step 3: Run full verification**

Run all tests and skill validator.

- [ ] **Step 4: Commit**

Commit implementation with message `feat: add world cup match predictor skill`.

- [ ] **Step 5: Create public GitHub repository and push**

Use local GitHub authentication from `~/.config/gh/hosts.yml` with the GitHub REST API if available. Create a public repo named `world-cup-match-predictor`, add remote, and push `main`.

---

## Self-Review

Spec coverage:

- Cross-agent compatibility: Task 2 and README.
- Professional modeling: `references/modeling.md`.
- Public packaging and safety: `references/public-positioning.md` and `SKILL.md`.
- Clickable source requirement: `SKILL.md`, `output-formats.md`, structure tests.
- Tables/visuals/JSON: `output-formats.md`.
- Deterministic odds helper: Task 1.
- Local installation and public repo: Tasks 3 and 4.

No placeholders are intentionally left in implementation tasks.
