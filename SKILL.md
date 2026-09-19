---
name: nanako-lock
description: Locked Nanako art pipeline. Trigger on Nanako lock, Nanako, NanakoMasterReferenceFront, NanakoMasterReferenceBack, GrokMiniatureMan, GrokMiniStamp, GrokCinemaFrame, GrokCinemaRig, GrokChopstick, Grok85Floor, 85Floor, 85大樓, 高雄85大樓, Kaohsiung, secretary outfit, cinema wide office, or jobs that change only outfit, light, scene, pose, and count. Do not trigger on 020008, xDMuy, T85, or T-85. 7CTk1 is a retired holding token only — never a live master. Stamp law is GrokMiniStamp. Frame and heads-tall law is GrokCinemaFrame. Heel-vs-head law is GrokHeelHead. 198 cm / 12 cm pixel law lives in GrokHeelHead. Shoe shape and flush-cap law is GrokShoe. Body yaw on grand scenes is GrokBodyAngle. Camera geometry is GrokCinemaRig. Shaft law is GrokChopstick. Landmark law is Grok85Floor. Never say T85 in an Imagine prompt. Face identity is NanakoMasterReferenceFront. Face yaw is performance, never a locked coffee angle.
metadata:
  version: "2026-09-19-dual-master-front-back"
---

# Nanako lock

Run this skill whenever the user says Nanako lock or starts a Nanako batch.

User fills only the job-card fields. Everything else is already decided.

Read `references/GOLD_RAILS.txt` before any plate work. Those rails do not rotate.

## Dual master — PLATINUM (user 2026-09-19)

LIVE FRONT file_path: `assets/body/NanakoMasterReferenceFront.jpg`
LIVE BACK file_path:  `assets/body/NanakoMasterReferenceBack.jpg`

These two plates donate ALL of Nanako herself:
Face Identity, Hair Style, Body Ratio, H, Skeleton Structure,
Lean Thigh Pencil Legs, Skin Grade, Makeup, Default Outfit,
Default 12cm red-bottom stilettos, white balance / photo style,
person-vs-scene fill.

- Front / 3-4 / side / lookback-with-face → Front master
- Back / closed-leg back / rear full body → Back master
- HOLDING (must not influence any redraw): `assets/body/_holding_7CTk1/`
- NEVER sibling-redraw. NEVER last-good as file_path. NEVER 7CTk1 as file_path or ref.
- Conflict: other Platinum Rails stay. If a rail fights Nanako-the-person, Front / Back WIN.

Full waiter law, first-shot cook, garment / grade / camera / Q / S / stamp / 85Floor
lives in this repo under `references/`:

- GOLD_RAILS.txt
- GROK_CUTOUT_MASTER.txt
- GROK_CINEMA_FRAME.txt
- GROK_CINEMA_RIG.txt
- GROK_HEELHEAD.txt
- GROK_SHOE.txt
- GROK_BODYANGLE.txt
- GROK_CHOPSTICK.txt
- GROK_85FLOOR.txt
- GROK_MINISTAMP.txt

The Grok project copy of this skill (`/home/workdir/.grok/skills/nanako-lock/SKILL.md`)
is the long-form waiter script. This GitHub SKILL.md is the same zero point.
Do not revive castle-stair or 7CTk1 as live masters.

## Job card

```
OUTFIT:
LIGHT:
SCENE:
COUNT:
```

Optional: ANGLE / POSE_FAMILY / CAMERA

Default clothes if silent: the lingerie already on Front / Back masters
(sheer black lace bra + slim T-strap thong + lace-top matte sheer hose +
four thin garters + 12cm black patent red-bottom stilettos).

## First shot only

One Imagine call per plate.
file_path = Front or Back master by angle.
No sibling repair. Miss a rail → DROP. Next plate starts from Front or Back again.
Stamp only after accept, PIL GrokMiniStamp, never Imagine a tiny man.

## Other girl swap

Attached photo is FACE only. Body / grade / stamp / default clothes stay on Front / Back.
