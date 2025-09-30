# Average Calculator Workshop Code Base

### Developers: Ismiel & Jillian 

This repository now supports a simplified workshop focusing on: FastAPI basics, adding a small NiceGUI frontend, test-driven iteration, and CI (GitHub Actions). The original Postgres + CRUD Todo example has been replaced to reduce cognitive load.

## Quick Start

### 1. Clone & Setup
```bash
git clone https://github.com/<org>/<team-repo>.git
cd <team-repo>
python -m venv .venv && source .venv/bin/activate  # Win: .venv\Scripts\activate
pip install --upgrade pip uv
uv pip install .  # installs project via pyproject (editable not required here)
```

### 2. Run Locally (API + UI)
```bash
uvicorn app.main:app --reload
```
Open API health: http://127.0.0.1:8000/health
Open UI (NiceGUI): http://127.0.0.1:8000/

### 3. Run Tests
```bash
pytest
```

### 4. Lint & Type Check
```bash
ruff check .
mypy .
```

### 5. Example cURL (Average Endpoint)
```bash
curl -X POST http://localhost:8000/average -H 'Content-Type: application/json' -d '{"values":[1,2,3,4]}'
```

## Structure
```
app/
  __init__.py
  main.py          # FastAPI + NiceGUI, /health, /average
tests/
  test_health.py
  test_average.py
```

## Notes
- No database: computations are in-memory.
- Frontend built with NiceGUI mounted onto FastAPI app.
- Validation handled by Pydantic (empty list rejected with 422).

## Iteration Ideas (Workshop Extensions)
- Add /median endpoint (use statistics.median) and show UI toggle.
- Add /mode or /stddev.
- Add simple input history (in-memory list with cap).
- Add client-side validation and error highlighting in UI.
- Add coverage reporting & badge.

## Versioned Iteration Flow (Workshop)
Releases progress through staged learning goals:
- v0.1.0: FastAPI skeleton with /health, CI, Dockerfile
- v0.2.0: NiceGUI shell (title + subtitle)
- v0.3.0: Average form & basic computation
- v0.3.1: Non-numeric input guard (bug fix)

Each step pairs a structural or UX enhancement with a semantic version bump via conventional commits + automated release workflow.

## Automated Releases (Semantic Versioning)
This project can optionally use python-semantic-release to automatically:
- Parse conventional commit messages (Angular style: feat, fix, chore, docs, ci, refactor, perf, test)
- Determine the next semantic version (major.minor.patch)
- Create a Git tag (e.g. v0.2.0) and GitHub Release with changelog entries

### Commit Message Format
```
feat: add median endpoint
fix: handle empty values list edge case
chore(ci): tweak lint step
docs: update workshop script
```

BREAKING changes can be flagged by adding `!` after the type or the phrase `BREAKING CHANGE:` in the body.

### Release Workflow
The GitHub Actions workflow `.github/workflows/release.yml` runs on pushes to `main`:
1. Installs dependencies with dev extras (`.[dev]`).
2. Runs `semantic-release version` to compute & tag the new version.
3. Runs `semantic-release publish` to generate/update `CHANGELOG.md` and create a GitHub Release.

To enable it, ensure commits follow the conventional format. Non-conforming commits will be ignored for version bumps (only patch if chores/fixes/feats exist since last tag).


## Docker Usage

### Build & Run Locally
```bash
docker build -t average-app .
docker run -p 8000:8000 average-app
```
Open: http://localhost:8000/ (UI) and /health

### With Docker Compose (optional) — Not usually needed now
Compose file no longer required since no database; you can still create one if you later add Redis or other services.

### Deploying on Render (Docker)
1. Push repo with `Dockerfile` to GitHub.
2. In Render Dashboard: New > Web Service > pick repository.
3. Environment: Docker.
4. No special env vars required. Health check path: `/health`.
5. Deploy. If platform provides PORT env var, Dockerfile already adapts.

### Image / Build Tips
- The Dockerfile uses a multi-stage uv build to produce a wheel for deterministic deploys.
- For faster local iterative dev you can still run: `uvicorn app.main:app --reload`.
- Add `--no-cache-dir` if you later revert to plain pip installs.

