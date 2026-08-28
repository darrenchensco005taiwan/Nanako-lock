---
name: nanako-lock
description: Locked Nanako art pipeline. Trigger on Nanako lock, Nanako, GrokMiniatureMan, fairy body, thigh gap, castle-stair master, or jobs that change only outfit, light, scene, and count. Also use for temporary face-swap of other girls who share the same lean skeleton.
---

# Nanako lock

Run this skill whenever the user says Nanako lock or starts a Nanako batch.

User fills only four fields. Everything else is already decided.

## Defaults

- Identity master — `assets/castle_stair_lingerie_master.jpg` (castle-stair black lingerie). Never use a later office generation as the face/body master.
- Stance proof — `assets/chatgpt_a_stance_proof.png` (wide A-stance, thin shafts, large gap).
- Scene reference when the job is office — `assets/office_tall_bookshelf.jpg` (tall tower shelf camera, not desk-forward).
- Stamp — `assets/GrokMiniatureMan.png` (18x33 RGBA). Paste after generation. Never generate a tiny man.
- Full prompt — `references/UNIVERSAL_PROMPT.txt`

In this same Grok project the user does not need to re-attach the castle master. In a new chat they must attach it.

## Job card

Ask only for missing fields.

```
OUTFIT:
LIGHT:
SCENE:
COUNT:
```

Optional — Temporary identity swap plus one real camera photo. That photo is FACE only. Body law still comes from this skill.

## Body law

Fairy, not human anatomy. Taiwan lean limbs and waist.
No Kardashian hip, glute, or thigh.
CUT THE MUSCLE. No quad, no adductor, no standing-leg fill.
Pencil-thin hip-to-knee shafts.
Inner-thigh gap is mandatory even with feet together standing straight.
Open legs only enlarge the gap. Shafts never thicken.
Do not recalculate musculature when pose changes.
Breast may stay full. Everything below the waist stays lean.
Long arms and very long legs, fully in frame.
Exactly two hands from the correct sockets. No cropped hands.

## Pose law

Most frames are large-scale elegant editorial poses that use the long limbs against real objects in the scene (highest shelf, book spines, glass pane, rail, column, desk edge).
Do not default to arms-at-sides catalog stands.
A-stance, wide opening, long stride, crossed ankle, and closed stance are all normal tools.
Every stance keeps the gap and the pencil shafts.

## Style law

Clean natural white balance. Real skin.
No orange cast. No pseudo-HDR. No dirty noise. No oversharpen.

## Pipeline

1. Read the four fields. If identity is Nanako, lock `assets/castle_stair_lingerie_master.jpg`.
2. Generate pose variants from that master (and the scene ref if needed). Do not chain from a generated frame. Always go back to the castle master.
3. Reject any frame with extra limbs, cropped hands, closed thigh gap, heavier thighs than the castle master, tiny head, orange skin, or an AI-drawn miniature.
4. Paste the stamp with `scripts/paste_stamp.py`. Place it on the floor beside the planted heel or between both heels. Never under a stiletto tip. Never enlarge.
5. Name files `NN_pose-description_ALPHANUMERIC.jpg`.
6. Zip and deliver the zip unless the user asks to see frames.

## Other girl swap

If the user attaches a different real photo and says temporary identity swap
- use that photo as FACE only
- keep this body / pose / style / miniature law
- if the photo's legs are heavier than the law, follow the law, not the photo's mass
- one identity per batch
