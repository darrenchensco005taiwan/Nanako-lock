# Nanako-lock

Locked Nanako art pipeline for Grok.

Repo: https://github.com/darrenchensco005taiwan/Nanako-lock

## Already on this repo

- `SKILL.md` — Grok skill
- `references/UNIVERSAL_PROMPT.txt` — full lock
- `scripts/paste_stamp.py` — paste 18x33 stamp beside the heel
- `scripts/write_stamp.py` — rebuild `assets/GrokMiniatureMan.png`
- `assets/GrokMiniatureMan.png.b64` — stamp bytes
- `jobs/JOB_TEMPLATE.txt`

## Rebuild the stamp

```bash
python3 scripts/write_stamp.py
```

That writes `assets/GrokMiniatureMan.png` (18x33). Never generate a tiny man.

## Photos that must be dropped in by hand

GitHub MCP cannot carry the large masters through this API. Add these three files locally, then commit:

- `assets/castle_stair_lingerie_master.jpg`
- `assets/chatgpt_a_stance_proof.png`
- `assets/office_tall_bookshelf.jpg`

They are inside `Nanako_lock_project.zip` from the Grok chat.

Do not replace the castle master with a later office generation.

## Start a job in Grok

```
Nanako lock

OUTFIT:
LIGHT:
SCENE:
COUNT:
```
