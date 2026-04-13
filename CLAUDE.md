# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repo Is

A personal collection of reusable agent skills following the open [Agent Skills specification](https://agentskills.io). Skills are directories under `skills/` containing a `SKILL.md` file that teaches coding agents how to complete specialized tasks.

The `agentskills/` directory is a **git submodule** from [agentskills/agentskills](https://github.com/agentskills/agentskills) — the spec and skill-creation docs live there.

## Repository Structure

- `skills/<skill-name>/SKILL.md` — each skill's instructions and YAML frontmatter (`name`, `description` required)
- `skills/<skill-name>/` may also contain `scripts/`, `references/`, `assets/`, `eval-viewer/`
- `agentskills/` — submodule with the Agent Skills specification and documentation
- `.claude-plugin/marketplace.json` — plugin manifest referencing skills for distribution

## Skill Anatomy

Every skill is a directory with a `SKILL.md` containing YAML frontmatter:

```yaml
---
name: my-skill
description: What this skill does and when to use it
---
```

Skills use progressive disclosure: metadata is always in context, SKILL.md body loads on trigger, bundled resources (`scripts/`, `references/`, `assets/`) load as needed.

## Key Skill: skill-creator

The main skill in this repo (`skills/skill-creator/`) is a meta-skill for creating and improving other skills. It includes:

- `scripts/` — Python scripts for eval aggregation (`aggregate_benchmark.py`), description optimization (`run_loop.py`, `run_eval.py`, `improve_description.py` — these require `claude` CLI), skill packaging (`package_skill.py`), and validation (`quick_validate.py`)
- `eval-viewer/` — `generate_review.py` builds an HTML viewer for human review of skill test outputs
- `references/` — subagent instructions (`grader.md`, `comparator.md`, `analyzer.md`), JSON schemas (`schemas.md`), environment adaptation guide, and description optimization guide
- `assets/eval_review.html` — HTML template for trigger-eval review

## Commands

```bash
# Install skills from this repo via the skills CLI
npx skills add charles1614/agent-skills
npx skills add charles1614/agent-skills --skill skill-creator

# Run skill-creator scripts (from repo root)
python -m scripts.aggregate_benchmark <workspace>/iteration-N --skill-name <name>
python -m scripts.run_loop --eval-set <path> --skill-path <path> --model <model-id> --max-iterations 5
python -m scripts.package_skill <path/to/skill-folder>

# Generate eval viewer
python skills/skill-creator/eval-viewer/generate_review.py <workspace>/iteration-N --skill-name "name" --benchmark <path>/benchmark.json
```

## Working With Skills

- Skill descriptions should be slightly "pushy" to combat under-triggering — include both what the skill does AND specific contexts/keywords for when to use it.
- Keep SKILL.md under 500 lines; use `references/` files for overflow with clear pointers.
- Prefer explaining **why** over rigid MUST/NEVER directives — LLMs respond better to reasoning than commands.
- When editing skills, generalize from specific test feedback rather than overfitting to examples.
