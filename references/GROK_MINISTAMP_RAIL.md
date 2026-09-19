---
name: grok-ministamp
description: Platinum rail GrokMiniStamp — paste the official 18x24 sole-flush GrokMiniatureMan next to a landed heel rubber-cap tip. Trigger on GrokMiniStamp, miniature stamp, GrokMiniatureMan, heel-cap pin, Ally stamp, Minru stamp, or any girl-lock job that places the tiny man.
metadata:
  version: "2026-09-20-stance-y"
  rail: GrokMiniStamp
---

# GrokMiniStamp (platinum rail)

Shared stamp law for Nanako, Ally, Minru, and any later girl-lock skill.

This rail is not optional. A plate that misses it is not stamped. Recooking the girl to move the man is illegal.

## Asset

Live paste file only

- `assets/GrokMiniatureMan_sole.png` — **18×24 RGBA**. Last opaque row = his shoe sole.
- Alias — `assets/GrokMiniatureMan_noreflect.png` (same pixels).

Banned paste files

- Any 18×33 canvas (`GrokMiniatureMan.png`, `GrokMiniatureMan_18x33_padded.png`). Those eight bottom rows are transparent padding plus a baked floor reflection. Aligning that canvas to the cap line leaves his real soles ~8 px in the air. That is the floating-Y drift.
- Any generated tiny man. Never Imagine him. Never redraw. Never enlarge. Never shrink.

Exactly one stamp. Dual stamp = reject. If Imagine baked a second man, clone ONLY those pixels from same-Y marble 24–40 px away. Do not wipe shoe shadows. Do not fill the floor.

## Canonical lock plate (user 2026-09-16 — EXACTLY)

Nanako OL30 RAW `#30` sill-and-shelf, right landed needle

- Rubber-cap tip `(Nx, Ny) = (677, 1425)` — last dark pixel of the stem before marble.
- Stamp top-left `(Sx, Sy) = (650, 1402)`.
- Box `(650,1402)–(667,1425)`.
- Box bottom = cap Y = his real sole.
- He stands on pavement immediately left of the stem. Not in the long floor reflection. Not on the pump. Not on the bookshelf.

Every later plate is judged against this picture, not against a sibling restamp.

## Pin math

Frame is a flat X-Y grid. Y grows top → bottom.

1. Find a **landed** heel stem. The pin is the small black rubber cap at the bottom of that stem — the lowest dark pixel of the cap, the frame before marble begins.
2. That pixel is `(Nx, Ny)`.
3. Stamp height `H = 24`. Real sole row index = 23.
4. `Sy = Ny - 24 + 1` so the last opaque row lands on `Ny`.
5. X — 18 px left or right of the cap, on **empty pavement only**
   - Left `Sx = Nx - 27`
   - Right `Sx = Nx + 9`
6. **Collision test is mandatory before paste.** The 18×24 box must contain zero pixels of: her body, stocking, any shoe (vamp / last / toe / heel cup / stem / rubber), bag, desk, chair, bookshelf, rail, skirting, paper, or any other prop. If the first side fails, flip X. If both sides of this cap fail, try the other landed cap. Never change `Ny` to dodge. Never slide him up the stem. Never park him on the foot "because Y was right."
7. Paste with PIL from the RAW first shot only (Exception A). No Imagine pass to nudge the man.

## Collision ban (user 2026-09-18 — 加固)

Correct Y does not save a wrong side.

The miniature may not touch, overlap, or sit on:

- Nanako's body, hair, hands, stockings
- Either shoe: vamp, last, toe, heel cup, red outsole, thin stem, black rubber block
- Furniture or set dressing: desk, chair, bag, books, shelf, rail, paper, ornament

A pin with legal `Ny` that lands the box on the pump is still a miss. That was P01 / P05 / P22 / P29 on 2026-09-18: rubber-bottom Y was right, waiter picked the shoe side of the stem. Flip X. Do not recook. Do not argue the line.

Test: look at the 18×24 box on the RAW. If you can see patent leather, flesh, or a prop inside the box, the side is illegal. Flip. Proof crop must show marble on all four sides of the box except the adjacent stem air gap.

## What the pin is not

Illegal Y (these sit higher than the cap and glue him to the shoe or leave him floating)

- Shoe last / pump body
- Heel cup
- Beige or red outsole
- Toe tip, while any cap is on the floor
- Marble shadow / reflection of the stem (the long dark gloss on the floor). That is not a gap. That is a reflection.
- Air above the cap

Illegal X

- On the thin stem
- On her foot / vamp / any shoe pixel
- On her body or stocking
- Glued to bookshelf, desk, chair, bag, paper, sill edge, or skirting
- Mid-frame pretty empty marble far from every cap
- The shoe-side of a stem when the other side is open marble (P01/P05/P22/P29 class)

## Cases

- **A** — two caps down, feet not a closed pair. Either cap, either legal side, cap-tip Y, 18 px X on the ground.
- **B** — one cap down. That cap. Side that misses the shoe and the stem.
- **C** — FRONT plate, no heel cap visible, only grounded toes (wide A-stance / open front). User 2026-09-20. Pick ONE landed toe tip. Draw horizontal Y through that tip. Contact point = where that tip touches Y, `(Tx, Ty)`. Sole Y = `Ty` (`Sy = Ty - 24 + 1`). X = 50 px clear of `Tx` on empty pavement: right `Sx = Tx + 50`, left `Sx = Tx - 68`. Collision test still mandatory. Do not hit her shoes, body, stockings, or any nearby object. If both 50 px sides hit, say so. Do not park on the pump. Illegal if any cap is visible on the floor — then use A/B, not C.
- **D** — she is off the floor. Stamp X = navel X. Stamp stands on solid ground. Do not float him at navel Y.
- **E** — closed-leg BACK stand. User 2026-09-20. Only the two heel rubber caps should be the pin. Draw one horizontal Y through both rubber-cap bottoms. Contact points = where each cap touches that Y. Stamp X = midpoint of those two contact X. Stamp Y = that Y (`Sy = Ny - 24 + 1`). Not the beige sole. Not a toe. Collision test still mandatory.
- **F** — closed-leg FRONT stand. User 2026-09-20. Only the two toe tips should be the pin (heels hidden behind the pumps). Draw one horizontal Y through both toe tips. Contact points = where each tip touches that Y. Stamp X = midpoint of those two contact X. Stamp Y = that Y (`Sy = Ty - 24 + 1`). Not a hidden cap. Not a 50 px side park. Collision test still mandatory. If the midpoint box hits a shoe, there is no legal slot — say so. Do not slide him onto the pump.

## Waiter rules

- Stamp after the girl is accepted. Never bake him into the Imagine prompt.
- Wrong stamp location = Exception A PIL restamp from RAW. Do not recook the girl.
- User-granted sibling edit of the girl does not move the stamp. Restamp the result from that new RAW with this same math.
- Proof crop required when the user is iterating — heel crop + one horizontal red line through `Ny` + the stamp box. Box bottom must sit on that line.
- Honest miss — if no legal pavement slot exists next to a cap, say so. Do not hide him in a shadow.

## Inheritance

Nanako-lock, and any future Ally or Minru skill, load this file when the job uses the miniature. Do not fork a looser local stamp law. If a girl-lock skill restates the rail, the numbers here win.
