---
name: nanako-lock
description: Locked Nanako art pipeline. Trigger on Nanako lock, Nanako, 茶水間, pantry, coffee machine, GrokMiniatureMan, GrokMiniStamp, secretary outfit, or jobs that change only outfit, light, scene, pose, and count. Do not trigger on 020008, xDMuy, T85, or T-85. Live masters are four jpg files only. Not OL uses NanakoMasterReferenceFront_lingerie.jpg. OL smile uses NanakoMasterReferenceFront_OL_smile.jpg. OL not smiling uses NanakoMasterReferenceFront_OL_nonsmile.jpg. Face hidden uses NanakoMasterReferenceBack_lingerie.jpg. Photo examples in the prompt win. Stamp law is GrokMiniStamp. Never say T85 in an Imagine prompt.
metadata:
  version: "2026-10-04-four-masters"
---

# Nanako lock

Compiled 2026-10-04. This file wins. Version 2026-09-19 and 2026-09-30-pantryOL-14sdwxn are abolished.

## Live masters

Photo example in the prompt wins. Otherwise:

| Job | file_path |
|---|---|
| Not OL, face seen | `assets/body/NanakoMasterReferenceFront_lingerie.jpg` |
| Not OL, face hidden | `assets/body/NanakoMasterReferenceBack_lingerie.jpg` |
| OL, smile asked | `assets/body/NanakoMasterReferenceFront_OL_smile.jpg` |
| OL, smile not asked | `assets/body/NanakoMasterReferenceFront_OL_nonsmile.jpg` |
| OL, face hidden | `assets/body/NanakoMasterReferenceBack_lingerie.jpg` for skeleton only. Clothes stay OL. |

OL means office lady, secretary, blazer, pantry, 茶水間, coffee machine.

The lingerie front is the new tvl3k. Do not start from `NanakoMasterReferenceFront.jpg`.

Write note: `references/WRITE_2026-10-04_0328.txt`. Do not read WRITE_2026-09-25_2004.txt. That name is deleted.

## Donates

Face bones, hair, skin, grade, H, skeleton, hip-to-knee pencil shafts, and the clothes on that plate unless the job names a change. No HDR. No orange. No yellow. No beautify. No smaller face. No pointed chin. Day or night does not recolor her.

## Does not donate

Head position, yaw, gaze, expression, and action are free. Do not clone the donor neck. No baked tiny man. Stamp is PIL after accept.

## Abolished — never file_path, never ref

`NanakoMasterReferenceFront.jpg`, `NanakoMasterReferenceFront_tvl3k-4096h.jpg`, pantry, 14_sdwxn, WideStand, tCKrf, KInUD bust, 7CTk1, 020008, castle-stair, xDMuy as a body, last output, the 68–76% fill band.

## First shot

One Imagine call. No second pass. A miss is dropped.

4:5 unless named. 9:16 banned unless named. File path is the table row. Scene or garment ref only if the job names it. 85Floor only if the job names 高雄 / 85大樓.

1. Face and hair from that file. No beautify.
2. Pencil hip-to-knee from that file. Gap stays. Side view stays as thin as the front plate.
3. Scene, light, clothes, action from the job card.
4. Negative: wrong face, pointed chin, small face, HDR, orange, yellow, short, fat, no gap, press-frame, cropped hands or shoes.

## Drop

Press-frame, shortened, fattened, thicker than the chosen plate, HDR, orange, yellow, pointed chin, smaller face, unnamed 9:16.

## Clothes

Not OL, if silent: lace sheer bra, micro thong with two bead cords, lace-top sheer stockings, glossy stilettos, red sole. Default black. A named color applies to the set. Sole stays red.

OL, if silent: the clothes on the chosen OL plate.

## Stamp

After accept. grok-ministamp. 18×24. `Sy = Ny - 24 + 1`. Left `Sx = Nx - 27`. Right `Sx = Nx + 9`. Never change Y to dodge.

## Pipeline

1. Job card.
2. Example wins, else the table.
3. One shot.
4. Drop. Do not repair.
5. Next plate uses the same rule.
6. Stamp accepts only.
7. Name `GrokYYYYMMDD_HHMMSS.jpg`.
