# Agent Skills

A collection of reusable agent skills following the open [Agent Skills specification](https://agentskills.io). Skills are directories containing a `SKILL.md` file that teach coding agents how to complete specialized tasks in a repeatable way.

## Install

Use the [skills CLI](https://github.com/vercel-labs/skills) to install skills from this repository:

```bash
# Install all skills
npx skills add charles1614/agent-skills

# Install a specific skill
npx skills add charles1614/agent-skills --skill skill-creator

# Install to a specific agent
npx skills add charles1614/agent-skills -a claude-code -y

# List available skills
npx skills add charles1614/agent-skills --list
```

## Available Skills

| Skill | Description |
| ----- | ----------- |
| [skill-creator](./skills/skill-creator) | Create new skills, modify and improve existing skills, and measure skill performance |
| [paper-reader](./skills/paper-reader) | Read AI/CS academic papers (local PDF or arxiv) and generate detailed Chinese analysis reports in Markdown and LaTeX |

More skills coming soon.

## Supported Agents

Skills can be installed to any of these agents:

| Agent | `--agent` | Project Path | Global Path |
| ----- | --------- | ------------ | ----------- |
| Amp, Kimi Code CLI, Replit, Universal | `amp`, `kimi-cli`, `replit`, `universal` | `.agents/skills/` | `~/.config/agents/skills/` |
| Antigravity | `antigravity` | `.agents/skills/` | `~/.gemini/antigravity/skills/` |
| Augment | `augment` | `.augment/skills/` | `~/.augment/skills/` |
| IBM Bob | `bob` | `.bob/skills/` | `~/.bob/skills/` |
| Claude Code | `claude-code` | `.claude/skills/` | `~/.claude/skills/` |
| OpenClaw | `openclaw` | `skills/` | `~/.openclaw/skills/` |
| Cline, Warp | `cline`, `warp` | `.agents/skills/` | `~/.agents/skills/` |
| CodeBuddy | `codebuddy` | `.codebuddy/skills/` | `~/.codebuddy/skills/` |
| Codex | `codex` | `.agents/skills/` | `~/.codex/skills/` |
| Command Code | `command-code` | `.commandcode/skills/` | `~/.commandcode/skills/` |
| Continue | `continue` | `.continue/skills/` | `~/.continue/skills/` |
| Cortex Code | `cortex` | `.cortex/skills/` | `~/.snowflake/cortex/skills/` |
| Crush | `crush` | `.crush/skills/` | `~/.config/crush/skills/` |
| Cursor | `cursor` | `.agents/skills/` | `~/.cursor/skills/` |
| Deep Agents | `deepagents` | `.agents/skills/` | `~/.deepagents/agent/skills/` |
| Droid | `droid` | `.factory/skills/` | `~/.factory/skills/` |
| Firebender | `firebender` | `.agents/skills/` | `~/.firebender/skills/` |
| Gemini CLI | `gemini-cli` | `.agents/skills/` | `~/.gemini/skills/` |
| GitHub Copilot | `github-copilot` | `.agents/skills/` | `~/.copilot/skills/` |
| Goose | `goose` | `.goose/skills/` | `~/.config/goose/skills/` |
| Junie | `junie` | `.junie/skills/` | `~/.junie/skills/` |
| iFlow CLI | `iflow-cli` | `.iflow/skills/` | `~/.iflow/skills/` |
| Kilo Code | `kilo` | `.kilocode/skills/` | `~/.kilocode/skills/` |
| Kiro CLI | `kiro-cli` | `.kiro/skills/` | `~/.kiro/skills/` |
| Kode | `kode` | `.kode/skills/` | `~/.kode/skills/` |
| MCPJam | `mcpjam` | `.mcpjam/skills/` | `~/.mcpjam/skills/` |
| Mistral Vibe | `mistral-vibe` | `.vibe/skills/` | `~/.vibe/skills/` |
| Mux | `mux` | `.mux/skills/` | `~/.mux/skills/` |
| OpenCode | `opencode` | `.agents/skills/` | `~/.config/opencode/skills/` |
| OpenHands | `openhands` | `.openhands/skills/` | `~/.openhands/skills/` |
| Pi | `pi` | `.pi/skills/` | `~/.pi/agent/skills/` |
| Qoder | `qoder` | `.qoder/skills/` | `~/.qoder/skills/` |
| Qwen Code | `qwen-code` | `.qwen/skills/` | `~/.qwen/skills/` |
| Roo Code | `roo` | `.roo/skills/` | `~/.roo/skills/` |
| Trae | `trae` | `.trae/skills/` | `~/.trae/skills/` |
| Trae CN | `trae-cn` | `.trae/skills/` | `~/.trae-cn/skills/` |
| Windsurf | `windsurf` | `.windsurf/skills/` | `~/.codeium/windsurf/skills/` |
| Zencoder | `zencoder` | `.zencoder/skills/` | `~/.zencoder/skills/` |
| Neovate | `neovate` | `.neovate/skills/` | `~/.neovate/skills/` |
| Pochi | `pochi` | `.pochi/skills/` | `~/.pochi/skills/` |
| AdaL | `adal` | `.adal/skills/` | `~/.adal/skills/` |

## Creating Skills

All skills in this repository follow the rules defined in the [Agent Skills specification](https://agentskills.io) ([source](https://github.com/agentskills/agentskills)). Specifically, refer to the **[skill-creation docs](https://github.com/agentskills/agentskills/tree/main/docs/skill-creation)**:

- [Quickstart](./agentskills/docs/skill-creation/quickstart.mdx) — how to create a skill from scratch
- [Best Practices](./agentskills/docs/skill-creation/best-practices.mdx) — guidelines for writing effective skills
- [Using Scripts](./agentskills/docs/skill-creation/using-scripts.mdx) — bundling scripts with skills
- [Optimizing Descriptions](./agentskills/docs/skill-creation/optimizing-descriptions.mdx) — writing descriptions that trigger reliably
- [Evaluating Skills](./agentskills/docs/skill-creation/evaluating-skills.mdx) — testing and measuring skill performance

Each skill is a directory with a `SKILL.md` file containing YAML frontmatter:

```markdown
---
name: my-skill
description: What this skill does and when to use it
---

# My Skill

Instructions for the agent to follow when this skill is activated.
```

Required fields:
- `name` — unique identifier (lowercase, hyphens allowed)
- `description` — brief explanation of what the skill does

## References

- [agentskills/](./agentskills) — submodule from [agentskills/agentskills](https://github.com/agentskills/agentskills), the spec and skill-creation docs
- [Agent Skills specification](https://agentskills.io) — the open standard that all skills follow
- [vercel-labs/skills](https://github.com/vercel-labs/skills) — the CLI for installing and managing skills (`npx skills add`)
- [skills.sh](https://skills.sh) — discover community skills

## License

MIT
