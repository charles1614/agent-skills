# Environment-Specific Guidance

The core skill-creation workflow (draft → test → review → improve → repeat) is the same everywhere. This guide covers how to adapt the mechanics to different agent environments.

## Agents with subagent / parallel execution

Environments like Claude Code, Codex, Cowork, or any agent that supports spawning independent child sessions.

**Running test cases**: Spawn all runs (with-skill AND baseline) in parallel. Launch everything at once so it all finishes around the same time.

**Grading**: Spawn independent grader sessions for each run.

**Blind comparison**: Works as described — spawn an independent comparator session.

**Timeouts**: If you run into severe problems with timeouts, run test prompts in series rather than in parallel.

## Agents without subagents

Environments like Claude.ai, Cursor, or other single-session agents where you can't spawn independent child sessions.

**Running test cases**: No parallel execution. For each test case, read the skill's SKILL.md, then follow its instructions to accomplish the test prompt yourself. Do them one at a time. This is less rigorous than independent sessions (you wrote the skill and you're also running it, so you have full context), but it's a useful sanity check — and the human review step compensates. Skip the baseline runs — just use the skill to complete the task as requested.

**Benchmarking**: Skip the quantitative benchmarking — it relies on baseline comparisons which aren't meaningful without independent sessions. Focus on qualitative feedback from the user.

**The iteration loop**: Same as before — improve the skill, rerun the test cases, ask for feedback — just without the browser reviewer in the middle. You can still organize results into iteration directories on the filesystem if you have one.

**Blind comparison**: Requires independent sessions. Skip it.

## Headless / no-browser environments

Environments like Codex, Cowork, CI pipelines, or remote servers without a display.

**Eval viewer**: Use `--static <output_path>` to write a standalone HTML file instead of starting a server. Then provide a link that the user can open in their browser.

**Feedback**: Since there's no running server, the viewer's "Submit All Reviews" button will download `feedback.json` as a file. Copy it into the workspace directory for the next iteration.

**Important**: Always generate the eval viewer using `generate_review.py` *before* evaluating outputs yourself. Get results in front of the human as soon as possible — do not write custom HTML.

## Reviewing results without a browser or filesystem

If you can't open a browser and don't have a filesystem (e.g., a chat-only environment), present results directly in the conversation. For each test case, show the prompt and the output. If the output is a file the user needs to see (like a .docx or .xlsx), save it to the filesystem and tell them where it is so they can download and inspect it. Ask for feedback inline: "How does this look? Anything you'd change?"

## Description optimization

The automated description optimization loop (`scripts/run_loop.py`) currently requires the `claude` CLI tool (specifically `claude -p`). If your environment doesn't have access to this CLI, skip the automated optimization.

You can still optimize descriptions manually: write trigger eval queries, test them by asking real users or running the skill yourself with different prompts, and iteratively improve the description based on what triggers correctly vs. what doesn't. See the Agent Skills spec's guide on optimizing descriptions for the methodology.

## Packaging

The `package_skill.py` script works anywhere with Python and a filesystem:

```bash
python -m scripts.package_skill <path/to/skill-folder>
```

Direct the user to the resulting `.skill` file path so they can install it.

If your environment supports presenting files directly to the user, do so. Otherwise, tell them the file path.

## Updating an existing skill

The user might be asking you to update an existing skill, not create a new one. In this case:

- **Preserve the original name.** Note the skill's directory name and `name` frontmatter field — use them unchanged. E.g., if the installed skill is `research-helper`, output `research-helper.skill` (not `research-helper-v2`).
- **Copy to a writeable location before editing.** The installed skill path may be read-only. Copy to `/tmp/skill-name/`, edit there, and package from the copy.
- **If packaging manually, stage in `/tmp/` first**, then copy to the output directory — direct writes may fail due to permissions.
