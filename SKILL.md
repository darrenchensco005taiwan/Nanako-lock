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

## Waiter / chef (read this first)

Imagine is the cook. `SKILL.md` is not in the kitchen.

The waiter is this agent. The waiter picks `file_path` and `ref_images`. That pick IS the lock. If the waiter sends a sibling, the lock is already dead.

DUAL MASTER ZERO POINT (user 2026-09-19 尚方宝剑)
- LIVE FRONT: `assets/body/NanakoMasterReferenceFront.jpg`
- LIVE BACK:  `assets/body/NanakoMasterReferenceBack.jpg`
- Every first shot starts from one of these two. Never a sibling. Never a last-good. Never 7CTk1.
- These two plates donate ALL of Nanako herself:
  Face Identity 臉部五官
  Hair Style 頭髮顏色樣式
  Body Ratio 身材比例
  H 頭身比
  Skeleton Structure 骨架結構
  Lean Thigh Pencil Legs 纖瘦鉛筆腿
  Skin Grade 皮膚色調
  Makeup 妝容口紅
  Default Outfit 預設內衣服裝款式
  Default Stilette Heels 預設12cm紅底高跟鞋
  白平衡以及相片風格
  相片取景的 人vs景 占比大小比例
- Front jobs / 3-4 / side / lookback-with-face: file_path = NanakoMasterReferenceFront.jpg
- Back jobs / closed-leg back / rear full body: file_path = NanakoMasterReferenceBack.jpg
- HOLDING (must not influence any redraw): `assets/body/_holding_7CTk1/`
  Includes 7CTk1-9216h-cutout, master_7CTk1.jpg, pantry 7CTk1. NEVER file_path. NEVER ref_images. NEVER face/hair/body/grade/outfit donor.
- Conflict rule: other Platinum Rails and Sub Rails stay valid (stamp, shoe last, 24mm rig, 85Floor, Q, S, body yaw). If a rail fights Nanako-the-person, the two live masters WIN.

ANGLE-DONOR GOLD RAIL
- Extra plates (3/4, side, lookback, wide A-stance) donate ONLY a pose family hint in ref_images when the JOB CARD names that family.
- They are NEVER file_path after 2026-09-19.
- NOTHING from those plates becomes Nanako: not face, hair, clothes, scene, light, tower, grade, or shafts.
- Chef copies an angle plate's face / hair / red clothes / needle / castle / night terrace = DROP.

HEIGHT / RATIO GOLD RAIL + PLATINUM GrokCinemaFrame (user 2026-09-16, zero-point 2026-09-19)
- Front lock AND H / F / person-vs-scene lock: `NanakoMasterReferenceFront.jpg`. That plate is the frame sample. OL30 RAW `#15` is HISTORY only — not file_path.
- Back lock AND rear H / F / person-vs-scene lock: `NanakoMasterReferenceBack.jpg`.
- Old 3/4 / side / lookback / A-stance / closed-back files are pose-family hints only. NEVER file_path. NEVER shaft override of the two live masters.
- Small head, long torso, very long pencil legs. Ratio does not change when the camera steps back. Measure H and F on the live Front / Back masters, not on 7CTk1.
- ILLEGAL: compress her so more bay fits. That is a shorter human. DROP. OL30 `#12` `#13` class.
- ILLEGAL: grow her until hair and shoes eat the frame. That is a spider. DROP. OL30 `#11` class.
- LEGAL: same fairy skeleton, camera two steps back, air above hair, marble under heels, bay still readable. OL30 `#15` class.
- 014142 / 014150 fat-short class = FIRE.
- Numbers live in GrokCinemaFrame below. Read them before every first shot.

NO-CROP GOLD RAIL
- Full girl inside the frame. Hands, fingers, hair, both shoes, both heel stems, both heel caps.
- After PIL stamp: the miniature himself must be fully inside the frame. No clipped feet, no clipped head, no stamp hanging off the edge.
- 28sbC left-heel crop class = DROP.

ACTRESS GAZE GOLD RAIL + FACE YAW (user 2026-09-18)
- Eyes and expression follow the performance in this plate, like an excellent actress.
- Face IDENTITY (bones, eyes, nose, mouth, hairline) = ONLY NanakoMasterReferenceFront.
- Face ANGLE / yaw / pitch is NOT a lock. Any one coffee 3/4 and the down-book stare are not reusable face poses.
- Face yaw follows the scene and the acting: look at the stairs, the throne, the gate, the rose, the sky, the viewer, over a shoulder. One COUNT is many face angles. Same 3/4 coffee tilt on 10 plates = 毛延壽 / waiter fail.
- If the job does not name a gaze, do not force one fixed stare.
- Do not copy the sample frame's eye direction or expression. 021108 looking down at a book is not a lock.
- Abnormal / rolled / leaked book-stare = DROP.

ARMS-CROSSED BAN (user 2026-09-15)
- Arms crossed is ABOLISHED. Drop the plate. Do not ship. Do not count it.
- Same ban: hands wrapped in front of the waist, hands wrapped in front of the chest, both arms hugging the torso.
- Reason: those poses hide the waist line or the breast curve. Those two curves are the point.
- Legal hand alternatives: hip, rail, reach, point, wave, hair, bag, one hand at the side, one hand on the stocking welt. Never both arms covering the front silhouette.

NO SAFE-CLONE / ACTING RANGE GOLD RAIL
- A COUNT of 10 or 50 is 10 or 50 DIFFERENT performances. Not one stance with new hands.
- The lock donates ONLY Nanako herself from Front / Back masters: face, hair, skeleton, H, ratio, hip→knee shafts, default lingerie if the job is silent on clothes, default 12cm red-bottom stilettos, skin grade, makeup, white balance, photo style, and person-vs-scene fill. It does NOT donate a sibling hall dirt, a sibling HDR, 85Floor pixels, or a locked idle stare.
- Hands, legs, weight, and gaze must change with the scene: reach, A-stance, weight-shift, lookback, point, pour, wave, high shelf. Feet may open. That is requested.
- SAFE clone (feet glued like the donor, same silhouette ten times) is how stamps collide the shoes. The donor already has almost no marble between the needles. Copying that gap is a waiter fail, not a stamp fail.
- Do not play safe to dodge a 0. A 0 on a real attempt is cheaper than 50 twins.
- Chef defects that SAFE posing will not hide:
  - Master is already fairy pencil. Next plate must stay pencil. Measure S = Tw/Hh. Kardashian fill after a pose change (S ≥ 0.55, or ΔS ≥ 0.04) = DROP. Adjectives are not a pass.
  - Master is already mild grade. Next plate must stay mild. Sudden HDR / crunch / speckle = DROP.
- If shafts or grade drift, drop the plate. Do not "fix" it by standing her still.

FIRST SHOT ONLY. NO SIBLING FILE_PATH.
- One Imagine call per requested plate.
- file_path by ANGLE (2026-09-19):
  - front / front-A / 3-4 / side / lookback-with-face / any plate that must show Face Identity
      = `assets/body/NanakoMasterReferenceFront.jpg`
  - back / closed-leg back / rear full body / any plate that hides the face
      = `assets/body/NanakoMasterReferenceBack.jpg`
- Clothes stay the default on those two masters unless the job names a change. Scene, light, and landmark follow the JOB CARD, not a sibling hall.
- A last-good plate is NEVER file_path. Never ynIoP, never RKe7l, never aidvv, never 5x2xm, never any Grok20260911 terrace cook. Never any 7CTk1 file.
- Sibling file_path is how dirty HDR, speckle, plastic skin, and Kardashian hips stack. That is a waiter violation, not chef weather.
- If the plate misses a rail, DROP it. Do not send it back to Imagine to "fix" shafts, thong, face, grade, or stamp.
- A fix pass is how Kardashian, lace-panty, and dirty HDR accumulate.
- ACCEPT LINE 2026-09-15 / 2026-09-19: no sibling Imagine repair by default. Keep the first shot. Next job starts from Front or Back again.
- Exception A — stamp location wrong on a batch: PIL restamp from the RAW first shot only. Do not recook the girl.
- Exception B — user names a super plate (class of #17) AND asks to try a fix: at most one or two Imagine attempts. Then stop. If HDR or cast appears, keep the first shot.
- Scene refs (85Floor aerial) may sit in ref_images. They do not become the girl.
- Correct is better than continuous amend.

Imagine ban from 2026-09-05 is LIFTED for first-shot cooks only. Second-shot "repair" stays banned.

## Dual master — PLATINUM (user 2026-09-19 尚方宝剑)

Live FRONT file_path: `assets/body/NanakoMasterReferenceFront.jpg`
Live BACK file_path:  `assets/body/NanakoMasterReferenceBack.jpg`

Why: 7CTk1-9216h-cutout is ABOLISHED as a live master. It sits in `assets/body/_holding_7CTk1/` and must not influence any redraw. The two new plates are the zero point for face, hair, body, H, skeleton, pencil legs, skin, makeup, default lingerie, default 12cm red-bottom stilettos, white balance, photo style, and person-vs-scene fill.

Waiter prompt MUST say on every first shot:
- start from NanakoMasterReferenceFront or NanakoMasterReferenceBack
- keep HER face / hair / skeleton / H / shafts / skin / makeup / default clothes / 12cm heels / white balance / photo grade / person-vs-scene fill from that plate
- place the JOB CARD scene around her; do not steal a sibling hall, do not steal 7CTk1 pantry / coffee / black void
- do not grow her to fill the room; do not shrink her to fake more marble
- do not sibling-redraw from a last plate

HOLDING, never file_path, never ref:
- `assets/body/_holding_7CTk1/master_7CTk1_9216h_cutout.jpg`
- `assets/body/_holding_7CTk1/master_7CTk1.jpg`
- `assets/body/_holding_7CTk1/master_7CTk1_4096h_pantry_RETIRED.jpg`
Using any of those as file_path or as a donor is a waiter violation.

## Defaults (this chat's attachments only)

ABOLISHED as masters (do not use as file_path, do not chain, do not "fix"):
- 7CTk1-9216h-cutout / master_7CTk1_9216h_cutout.jpg / master_7CTk1.jpg (abolished as LIVE master 2026-09-19). Holding only: `assets/body/_holding_7CTk1/`. Must not influence any redraw.
- master_7CTk1_4096h_pantry_RETIRED.jpg / old 7CTk1-4096h kitchen plate (abolished 2026-09-17). Pantry, coffee machine, window crop, daylight room. NEVER file_path. NEVER ref as scene.
- Grok20260904_020008-8192h / master_020008.jpg (abolished 2026-09-12)
- castle-stair OnePercentMale3 / castle_stair_lingerie_master
- side_master_40 as FRONT file_path (illegal). Side-shaft proof only.
- grade_master_B / j8snr / 08_chin / YY9uU / KInUD
- secretary 01_39_24 as body or grade
- pack1 Grok20260904_005000-005017
- red-office 00-24
- Grok20260905_155300 / 160500 / 160900 / 161000 and other charcoal siblings
- any plate produced to "fix" another plate
- 2026-09-12 luck24 / motion6 / keepers16 / pantry-3 / landmark-calibrate. Wiped from disk. Not memory. Never file_path.
- All prior artifact zips and sibling plates wiped 2026-09-12. Not memory.

MEMORY RULE
- A plate is memory ONLY when the user writes the word "memory" and names that plate.
- A keeper score is not memory. A zip is not memory. A last-good plate is not memory.
- If the user does not say "memory", do not store it, do not reuse it as file_path, do not chain it.

PERFORMANCE MEMORY 2026-09-16 (user: Memory ALL)
- 41 UNTOUCHED attachment originals live in `assets/performance/` and `references/PERFORMANCE_MEMORY.txt`.
- Restored 2026-09-16: user called them masterpieces. Whole-frame grade and skin-only grade are both discarded. Do not PIL-rescue these plates.
- They donate MUST-HAVE pose / expression / gaze for Nanako jobs. Ally and Minru inherit the same catalog language when those girls lock.
- They are NOT file_path. Face and skeleton stay NanakoMasterReferenceFront / Back.
- Grade / skin quality for a NEW cook comes from NanakoMasterReferenceFront.jpg (front jobs) or NanakoMasterReferenceBack.jpg (back jobs) on the first shot. Do not wash these 41. Do not wash them with 7CTk1.
- Arms-crossed plates 03 and 29 are gaze/lean memory only. The arms-crossed ban still applies to new first shots unless the job names that pose.

LIVE masters (2026-09-19 dual master):

| Role | File | Legal use |
|---|---|---|
| UNIQUE MASTER (front) | `assets/body/NanakoMasterReferenceFront.jpg` | User 2026-09-19 尚方宝剑. Face + hair + body + H + F + skeleton + pencil legs + default lingerie + 12cm red-bottom heels + skin + makeup + white balance + photo style + person-vs-scene fill. Default file_path for every plate that shows the face. |
| UNIQUE MASTER (back) | `assets/body/NanakoMasterReferenceBack.jpg` | Same person, rear zero point. Hair down the back. Slim T-strap thong + four thin garters + lace-top matte sheer hose + 12cm black patent red-bottom. Default file_path for rear / closed-leg back. |
| HOLDING 7CTk1 CUTOUT | `assets/body/_holding_7CTk1/master_7CTk1_9216h_cutout.jpg` | Abolished as live master 2026-09-19. NEVER file_path. NEVER ref. Must not influence redraws. |
| HOLDING 7CTk1 ALIAS | `assets/body/_holding_7CTk1/master_7CTk1.jpg` | Same ban. |
| HOLDING PANTRY 7CTk1 | `assets/body/_holding_7CTk1/master_7CTk1_4096h_pantry_RETIRED.jpg` | Kitchen / coffee / window. Abolished 2026-09-17. NEVER file_path. NEVER scene ref. |
| 3/4 POSE HINT | `assets/body/master_3q_0346_reach.jpg` | Optional ref_images ONLY when JOB CARD names 3/4 reach. NEVER file_path. NEVER face/hair/clothes/scene. |
| WIDE A-STANCE POSE HINT | `assets/body/master_astance_163822.jpg` | Optional ref_images ONLY when JOB CARD names wide A-stance. NEVER file_path. NEVER night terrace. |
| FACE + HAIR | already on NanakoMasterReferenceFront.jpg | Do NOT replace this face with KInUD, xDMuy, or 7CTk1. That face is the 100 lock. |
| SECRETARY / OL OUTFIT | `assets/secretary/outfit_KInUD.jpg` | clothes recipe only. Never face, never body, never file_path. xDMuy is the same family. |
| LOWER GARMENT (front) | already on NanakoMasterReferenceFront.jpg | Live front lock. Keep this plate's lower garment unless the job names a change. |
| LOWER GARMENT (back) | already on NanakoMasterReferenceBack.jpg | Live back lock. Slim waistband + single narrow T-strap + four thin garter straps. Not a wide lace panty. |
| IMAGE A (retired) | `assets/garment/thong_front_imageA.png` | Bead-cord construction. RETIRED 2026-09-12. Do not use on first shots. Reserve only when the user names an Image A / bead-cord outfit change. |
| BRA | `assets/garment/bra_sheer_floral.png` | garment ref. Sheer floral, not opaque |
| SHOES (platinum GrokShoe) | `assets/shoes/Grok12cmGlossyBlackStiletteRedBottom1.webp` | DEFAULT 12 cm black patent + red outsole + flush black rubber tip (same diameter as stem). ref_images only. Never file_path. |
| SHOES | `assets/shoes/Grok12cmGlossyRedStiletteRedBottom1.webp` | Red patent 12 cm. Same last / cap law. When outfit is red. |
| SHOES | `assets/shoes/Grok12cmGlossySilverStiletteRedBottom1.webp` | Silver 12 cm. Same last / cap law. When outfit is silver. |
| SHOES | `assets/shoes/Grok12cmGlossyWhiteStiletteRedBottom1.webp` | White patent 12 cm. Same last / cap law. When outfit is white. |
| STAMP | `assets/GrokMiniatureMan_sole.png` | PLATINUM GrokMiniStamp. PIL paste only. 18×24 sole-flush. Shared rail lives in skill grok-ministamp. |
| 85Floor LANDMARK | `assets/landmark/85Floor_day_vertical.jpg` | REAL 高雄85大樓. ref_images ONLY when job names 高雄/85Floor/85大樓. Never file_path. Never face. Never say T85. |
| 85Floor LANDMARK | `assets/landmark/85Floor_day_oblique.jpg` | Same building, second angle. Portal must read. |

Pose language still lives in `references/POSE_LIBRARY_SECRETARY.txt`. Those frames are poses, not body, not grade, not face.
Live must-have catalog: `references/PERFORMANCE_MEMORY.txt` + `assets/performance/` (41 plates, user Memory 2026-09-16).

## Job card

Ask only for missing fields.

```
OUTFIT:
LIGHT:
SCENE:
COUNT:
```

Optional:

```
ANGLE:          (front-straight / front-A / 3-4 / side / back / mix)
POSE_FAMILY:    (reach / two-height / book / read / hip-cock / kicked / over-shoulder / walk-in / mix)
CAMERA:         (cinema-wide is the default)
```

LANDMARK / SCENE / LIGHT — JOB CARD, NOT THE MASTER PHOTO
- Front / Back masters donate person-vs-scene FILL and photo grade. They are NOT a scene lock, NOT a light lock, NOT a pose lock, NOT a baked-window lock. Hall architecture follows the JOB CARD.
- 7CTk1 is HOLDING. Not a scene lock. Not a light lock. Not a pose lock. Not a baked-window lock. Not a face lock.
- If the job names 高雄 / 85Floor / 85大樓 / 東帝士85大樓 / bay office with the tower: PLATINUM RAIL Grok85Floor. Full text `references/GROK_85FLOOR.txt`.
- Spoken name is 85大樓. English prompt token is **85Floor** (one word, capital F). Never T85. T reads as Taipei and chef draws 101.
- Grok85Floor fingerprint (all must read): two lower wings + mid-building PORTAL / hollow where the wings join + one tall teal rectangular shaft + pointed crown and thin antenna.
- Waiter MUST put `assets/landmark/85Floor_day_vertical.jpg` and/or `85Floor_day_oblique.jpg` in ref_images. Landmark only. Never file_path.
- Prompt MUST say 85Floor or 高雄85大樓. Prompt MUST name the portal. Prompt MUST ban Taipei 101 and needle towers by name. Prompt MUST NOT contain T85.
- After first shot: no portal, or 101 stacked ruyi boxes, or a lattice needle = DROP. Do not sibling-swap the tower. Do not zip. OL41 38/41 fail class.
- Day and night are the SAME building. Night only changes brightness and color. Blue hour is not a new landmark.
- ILLEGAL any hour: Taipei 101, N Seoul Tower, Canton Tower, Macau tower, twin fins, lotus stem. Drop. Do not zip.
- If the job names another city or no landmark, do not force 85Floor.
- Scene, camera altitude, indoor/outdoor, restaurant/pantry/office = job card.
- Light = job card (daylight / blue hour / whatever named). Do not keep a sibling hall's dirt or a holding 7CTk1 pantry daylight on a night job.
- Pose = job card + pose library. Do not clone one idle stand across a COUNT.

Default OUTFIT if the user does not name clothes:
the clothes already on NanakoMasterReferenceFront.jpg / NanakoMasterReferenceBack.jpg
(sheer black floral / lace bra + slim-strap micro thong + lace-top matte sheer stockings + four thin garters + 12cm black patent red-bottom stilettos).
Image A bead cords are retired until the user names that outfit change.

If the user asks secretary / office lady / OL / blazer / business / miniskirt:
Default Office Lady Outfit (KInUD clothes language, not face, not body):
tailored blazer + hip-barely miniskirt (MAIN COLOR, default black),
open white shirt unless named otherwise,
same-color sheer lace bra showing 36D,
same-color small gold-chain handbag,
same-color lace-top sheer stockings + straps,
same-color 12cm red-bottom stilettos.
Prompt names the main color; bra / bag / stockings / heels follow. See references/OFFICE_LADY_OUTFIT.txt.

## First-shot cook (the only legal Imagine use)

Every new plate:

```
AR           = 4:5 unless the job names another AR. Write it in the prompt.
file_path    = assets/body/NanakoMasterReferenceFront.jpg
               for front / front-A / 3-4 / side / lookback-with-face
               assets/body/NanakoMasterReferenceBack.jpg
               for back / closed-leg back / rear full body
               HOLDING 7CTk1 and old angle plates are illegal file_path
ref_images   = garment refs ONLY if the job changes clothes
               + REQUIRED when job names 高雄/85Floor/85大樓: assets/landmark/85Floor_day_vertical.jpg and/or 85Floor_day_oblique.jpg (landmark ONLY)
               + assets/secretary/outfit_KInUD.jpg and/or outfit_xDMuy.jpg ONLY when the job is office-lady clothes
               + matching Grok12cm shoe file from assets/shoes/ when the job shows feet / changes shoe color (shape + cap only; never file_path)
               + optional pose-hint plate ONLY when JOB CARD names that family
               NEVER pass a 7CTk1 holding file as ref
               KInUD / xDMuy = clothes language only. Do NOT use as file_path or face-replace.
               85Floor files = building geometry only. Do NOT take park/pavement/people from those photos. Do NOT use them as file_path.
               NEVER type T85 in the Imagine prompt.
```

ILLEGAL file_path (waiter violation, not chef drift):
- 020008 as file_path (abolished).
- 3/4 master as a front file_path. Front master as a 3/4 file_path.
- xDMuy / KInUD as file_path (secretary body).
- KInUD as a face-replace ref on a Front / Back first shot (would drift the 100 face).
- Any file under assets/body/_holding_7CTk1/ as file_path or ref.
- last sibling. Including any plate that already scored 80.
- ynIoP / RKe7l / aidvv / 5x2xm / any 2026-09-11 terrace sibling
- 161000 / 155300 / any Grok20260905 office cook
- castle master
- product photos of bra / thong / shoes as file_path (GrokShoe color masters are ref_images only)
- stamp PNG

Prompt skeleton — ALWAYS this order (user lock 2026-09-14):

1. FACE IDENTITY from NanakoMasterReferenceFront: same face shape, feature ratios, eye shape and spacing, nose, lips, jawline, cheekbones, forehead and hairline, same makeup. No beautify. No bone-structure change. Do not revive 7CTk1.
2. BODY PROPORTIONS from NanakoMasterReferenceFront (front jobs) or NanakoMasterReferenceBack (back jobs): very tall, thin long skeleton, overall lean. Legs clearly longer than average. Narrow pelvis. Narrow flat hips. Very thin pencil thighs. Clear inner-thigh gap in a natural stand. Thin long calves, smooth outer taper to the ankle, no mid-calf dent, no dog-bite bulge. Visible kneecaps. Same H and person-vs-scene fill as the live master. These ratios do not change with pose, angle, or crop. If a composition would change them, move the camera — do not change the body.
3. SCENE / ACTION / CLOTHES / LIGHT / STYLE — job card only. Default clothes and 12cm red-bottom heels = the live Front / Back master unless the job names a change. White balance and photo grade = the live master. Do not bake a sibling dirty floor. No tiny man. Stamp comes later.
4. NEGATIVE: Wrong Face Identity, 7CTk1 face revival, Wrong head/body proportions, short legs, Wide hips, Kardashian pelvis, Massive thigh & upper leg shafts, No thigh gap, mid-calf outer dent, Deformed body, Extra weight, Leica style high contrast, overshooting clarity, overshooting dehaze, pseudo HDR, cast orange color, cast yellow color, overshooting sharpening, fake detail noises, blurry, low quality.

Avoid extreme high/low camera or compositions that hide the lower body unless the job names that.

One call. Then inspect. Hit or drop. Next plate starts from NanakoMasterReferenceFront or NanakoMasterReferenceBack again.

## Body law

Donor: `assets/body/NanakoMasterReferenceFront.jpg` (front) or `assets/body/NanakoMasterReferenceBack.jpg` (back) only.

Fairy, not human fill. Small head. Very tall. Thin long skeleton. Overall lean.
Scale lock (user 2026-09-14 — direction, not a giantess genre):
retired basketball athlete, barefoot 198 cm / 60 kg, 12 cm stilettos → 210 cm,
BMI 15.30, seam height (sole to crotch) 120 cm.
Extremely tall slim girl. Show the height and long limbs. Reach a nearby high object when one exists.
Legs clearly longer than average. Narrow pelvis. Narrow and FLAT hips. Not round. Not filled.
Very thin thighs. Pencil hip → thigh → upper-leg → knee. Visible kneecaps. Thin long calves.
Inner-thigh gap even with feet together. Open stance / wide A-stance only enlarges the gap. Shafts never thicken.
A-stance hip→knee must stay the same 筷子腿 / pencil thickness as NanakoMasterReferenceFront feet-together.
Do not recalculate muscle when the feet open. Quad/adductor fill on A-stance = DROP.
No quad / adductor / standing-leg fill. No Kardashian hip. No glute balloon.
Breast may stay full. Below the waist stays lean.
Do not recalculate musculature when pose or camera changes.
If a pose would thicken hips or close the gap, change the camera or drop the plate. Do not change the body.
Numbers live in PLATINUM RAIL GrokChopstick. "筷子 / pencil / lean" without a passing S is not a pass.
Exactly two hands from the correct sockets.
FRAME CROP RAIL: no part of the girl may be cut by the frame — hands, fingers, hair, heels, toes. If a reach would leave the frame, pull the camera back or lower the arms until every part is inside. A cropped plate is a miss. Drop.

xDMuy / KInUD legs are not the body lock. Ignore their mass. Secretary clothes only when asked.

## Face law

IDENTITY MASTER: the face and hair already on `assets/body/NanakoMasterReferenceFront.jpg`.
Back jobs hide the face; hair style follows `NanakoMasterReferenceBack.jpg` (long straight black, fully down the back, not over the chest).
Angle plates are not face donors. Holding 7CTk1 is not a face donor.

This is Miss Nanako's face. Same rank as the body. Not optional. Not "inspired by."
- Face shape, feature ratios, eye shape and spacing, nose, lips, jawline, cheekbones, forehead, hairline, makeup = NanakoMasterReferenceFront exactly.
- Do not beautify. Do not slim or round the jaw. Do not enlarge the eyes. Do not change bone structure.
- Every plate that shows a face must wear this face with no identity drift.
- Do not pass KInUD, xDMuy, or any 7CTk1 holding file as a face-replace.
- Eyes = open apertures only. Under-lid makeup shadow is not the eye.
- Reject: a sister, castle face, YY9uU, 020008 face, 7CTk1 revival, or any sibling face.
- Young. Not sleepy. Not a plastic grin.
- Face yaw is acting. Do not reprint any one 3/4 coffee tilt as the only legal face.
- A miss on face IDENTITY is the same class as a miss on shafts. Drop. Do not repair.
- A miss on face VARIETY across a COUNT (ten twins of one yaw) is a waiter fail. Recook the next plate from NanakoMasterReferenceFront with a new performance. Do not sibling-fix the twins.

## Garment law

BASE SET (lingerie jobs):
- Clothes already on `NanakoMasterReferenceFront.jpg` / `NanakoMasterReferenceBack.jpg`. That is the live lock.
- Bra on the Front plate. Sheer / lace floral. Do not redesign unless the job names a change.
- Lower garment: Front plate for front jobs; Back plate for rear jobs (slim waistband + single narrow T-strap + four thin garter straps). Keep it. Do not swap to Image A unless the user names that change. Do not invent a wide lace panty on the back.
- Stockings = lace-top thigh-highs, matte sheer, garters. Not opaque tights. Not wet-look that thickens the shaft.
- Shoes = platinum GrokShoe. 12.00 cm single-needle pointed patent pump, red lacquer outsole always. Four live color masters in `assets/shoes/`: Black (default), Red, Silver, White. Full text `references/GROK_SHOE.txt`.
- Rubber cap = BLACK on all four colors. Same diameter as the stem. Flush short tip. NOT a cobbler block wider than the needle. NOT a tall pad that inflates Hs.
- Pixel scale: crown → cup-join = 198 cm. Cup-join → rubber bottom = 12 cm. Crown → rubber = 210 cm. Formula in GrokHeelHead.

Image A bead cords = RETIRED. Not a first-shot ref. Not a drop-rule against the live Front / Back lower garment.
When the user later names Image A / bead cords as an outfit change, then and only then pass `assets/garment/thong_front_imageA.png`.

SECRETARY / OFFICE LADY SET:
Clothes recipe from `assets/secretary/outfit_KInUD.jpg` (and xDMuy). Body and face still NanakoMasterReferenceFront / Back.
Main color from the job card; bra, bag, stockings, heels follow that color. Red outsole always.

## Grade law

Skin quality donor: `NanakoMasterReferenceFront.jpg` (front) or `NanakoMasterReferenceBack.jpg` (back). The girl, not a sibling dirty floor.

Match HER skin: clean, no HDR, no orange, no plastic shine. Do not "improve" it.
Do NOT copy holding-7CTk1 pantry daylight onto a night or restaurant job. Room light follows the job card. Skin stays hers. White balance stays the live master.
Reject on sight:
- pseudo-HDR / dirty crunch / oversharpen speckle
- yellow or orange cast on face or thighs
- brown-sugar skin
- extra clarity / dehaze used as fake detail
- a sibling crunchier or dirtier than NanakoMasterReferenceFront / Back

Skin first, then room light. Shelf bulbs do not paint her orange.
Daytime office stays awake and bright. Bay glass must read.

Do not run a second Imagine pass to "clean" grade. That is the dirty trick.

## Camera + scene — PLATINUM RAIL GrokCinemaFrame (user 2026-09-16)

ASPECT default (user 2026-09-17)
- If the job card does **not** name an AR, AR = **4:5**.
- Waiter MUST write `4:5` in the Imagine prompt on every first shot. Silence is not a setting. Chef portrait-default is 9:16. 9:16 is how chef fakes a taller N. Banned.
- 4:5 size family = 1264×1568 (W/H ≈ 0.806).
- Illegal unless the user names it: 9:16 phone, 3:4, 16:9 wide, 1:1. DROP that plate. Do not recrop a 9:16 cook and call it 4:5.
- If the user names another AR, use that AR and still keep F / N / air / marble numbers.

Camera back. Grand view. Fill is secondary. Heads-tall is the point.
Full text: `references/GROK_CINEMA_FRAME.txt`.
Geometry chef hears: `references/GROK_CINEMA_RIG.txt` (user 2026-09-17).

GrokCinemaRig — waiter MUST write these on every first shot:
- camera **2.0 m** from Nanako. Not 2.5 m (2.5 m lands F in the ≤66% DROP band on this focal class).
- camera at **mid-thigh height**, tilt **+3°** up (legal +2–4°).
- focal class **24 mm on 135**. True wide. BANNED: 28 mm, 35 mm, 50 mm, 85 mm. Not 14 mm fish.
- subject does not fill the frame. Empty window/sky above the crown. Marble under the caps.
- Do NOT write Fujifilm / GFX100S / film simulation. Those steal grade from the live Front / Back masters.

OL30 RAW `#15` is HISTORY for the numbers. Keep it only as the composition idea (air + marble + bay readable). It is not file_path. Face/body/fill still NanakoMasterReferenceFront / Back. A plate that reprints `#15`'s old 78% / 7.8 now DROPS. Person-vs-scene fill on a new cook must match the live master, not a sibling fill-the-frame cheat.

Measure on a standing full-body plate. Y = 0 at the top of the frame. Use hair CROWN (skull top), not a flyaway. Use landed HEEL CAP, not the toe.

Live numbers (user 2026-09-17):

- Standing fill `F = (heel_cap - crown) / frame_H` — **target 72%**. Legal **68–76%**.
- Air above hair — **target 18%**. Legal **16–22%**.
- Marble under heel cap — **target 10%**. Legal **8–12%**.
- Heads-tall `N = (heel_cap - crown) / (chin - crown)` — **target 8.2**. Legal **8.10–8.40**. THIS IS THE POINT.
- Head share ` (chin-crown) / (heel-crown) = 1/N ` — **target 12.2%**. Legal **11.90–12.35%**. Derived from N. Do not set it first.

DROP

- `F ≥ 78%` — spider / no bay. Old `#11` class, and the retired `#15` 78% fill.
- `F ≤ 66%` — lost-in-the-room. Do not shrink the skeleton to make more bay. Step the camera back and keep `N`.
- `N < 8.05` — normal-woman head. 2026-09-17 4:5 proof class (N ≈ 7.92).
- `N ≥ 8.60` — doll / spider skull.
- Shoes or hair in the 24mm frame corners. Distortion.
- AR is 9:16 / 3:4 / 16:9 / 1:1 when the job did not name that AR.

Gray (do not pack, do not auto-DROP): N 8.41–8.59.

Reach / raised hand may enter the air band. That hand does NOT count as standing height. If a reach would force `F` above 76% or shove a shoe into a corner, pull the camera back. Do not lengthen the girl.

Do not "fix" a short skeleton by cropping tighter or by cooking 9:16. That is the lazy N fake. Do not "fix" a missing bay by shrinking her.

Shaft thickness is no longer "later". See GrokChopstick below. N does not excuse a fat S. N does not excuse a stretched heel (GrokHeelHead). A legal N with Q in the DROP band is still a miss.

Read `references/GROK_CINEMA_RIG.txt` for the geometry the chef hears.
Pose library is legal on every outfit and every scene.

## Heel vs head — PLATINUM RAIL GrokHeelHead (user 2026-09-18)

Why: 24 mm / wide editorial parked her stilettos in the frame bottom and stretched the stem until the shoe was a second head (castle wave P03 / P04 / P13). N can still pass. The plate still looks wrong.

Measure on the SAME landed shoe used for N.

- `Hh` = crown → chin. Same head as N.
- `Hs` = heel-cup join (where the needle meets the last) → black rubber-cap bottom. Stem height only. Not toe-to-heel. Not the whole pump.
- `Q = Hs / Hh`

Holding 7CTk1 cutout sample (3/4, almost full stem): Q ≈ 0.79. HISTORY only. Front perspective shortens the stem. Measure Q on the live Front / Back masters when the stem reads. Target table below still applies.

Live numbers (user 2026-09-18, tightened)

| stand | target | legal Q | gray | DROP |
|---|---|---|---|---|
| Front / 90% front / 1/8 | **0.52** | **0.42–0.65** | 0.66–0.74 | **Q ≥ 0.75** or **Q ≤ 0.32** |
| Pure side / lookback (full stem in view) | **0.60** | **0.48–0.70** | 0.71–0.79 | **Q ≥ 0.80** or **Q ≤ 0.32** |

DROP sentence: the shoe at the 24 mm bottom corner has been pulled into a second head. Do not crop the feet to fake Q. Do not switch to 9:16. Pull the camera back. Keep GrokCinemaRig 2.0 m / mid-thigh / +3° / **24 mm on 135**. 24 mm is now the lock, not a wish. It is not a license to park her feet in the distortion ring. 28 / 35 / 50 / 85 mm to shrink the stem = waiter fail.

Illegal Q / F shortcut (user 2026-09-18): any 28 / 35 / 50 / 85 mm crop so the stem is short and the girl fills the hall. That plate is short N + meat S + lost wide. Q is legal only on the same **24 mm 135** wide, camera back, both caps on marble inside the frame and off the corner ring.

N and Q must both pass. N pass + Q DROP = DROP.

Waiter prompt must say: heel stem shorter than the head; do not stretch the stiletto at the frame bottom.

198 cm / 12 cm PIXEL LAW (user 2026-09-18)
- Crown → cup-join = **198.00 cm**. Cup-join = needle-to-last = foot sole. Not the toe on marble. Not the rubber.
- Cup-join → rubber-cap bottom = **12.00 cm**.
- Crown → rubber-cap bottom = **210.00 cm**.
- On a standing plate:
  `P_body = Y_cup − Y_crown`
  `P_heel = Y_rubber − Y_cup`
  `heel_cm = (P_heel / P_body) × 198`
  Exact: `P_heel = P_body × 12 / 198 = P_body × 2/33`.
- target 12.00 cm. Legal 11.0–13.0. Gray 10.5–10.9 / 13.1–13.9. DROP <10.5 or >14.0 (14.48 pain class).
- Front plate with hidden stem: do not invent a 12 cm paint. Measure only when the join and the cap both read.
- Do not lengthen the rubber to fake 12 cm. Cap diameter = stem diameter (GrokShoe).

Read `references/GROK_HEELHEAD.txt` and `references/GROK_SHOE.txt` before any plate that shows a stem.

## Body yaw — PLATINUM RAIL GrokBodyAngle (user 2026-09-18)

Grand SYMMETRIC view (正廳 / 正樓梯 / 正大道 / 正門 / 正堂 / 正塔 / axial throne / axial courtyard):
- DEFAULT = **100% front body AND 100% front face**. Square test: both shoulders same distance to camera, pelvis to lens, sternum to camera, both iliac crests even, nose on centerline, both ears equally visible, both eyes equally seen. Feet may open but stay symmetric.
- "Head may turn" is optional seasoning. It is NOT the default. Chef reprinting one coffee 3/4 on every axial plate = 毛延壽 / neck-locked doll. Castle 24mm sample-three class.
- Fashion hip-cock that swings the near hip at the lens is 3/4 body = SIDE on an axial view. Castle probe T01 class = waiter fail.
- Side stand / lookback / full 3/4 body or 3/4 face as the DEFAULT on these views = waiter fail.
- 君臨 / 俾倪天下 on these views: gaze LEVEL or slightly DOWN at her domain, face still full front. Chin-up at chandelier / vault / landing is not the default. T01 仰望 class = waiter fail.

Grand ASYMMETRIC or LOCAL crop (one wing, one colonnade, one battlement corner, one aisle, one hedge, a fragment of the hall):
- Body yaw may be **up to 30% side** (~30°). Still not a pure profile unless the job names side / lookback.
- 30% side is a seasoning. It is not 50 plates of the same hip cock.

Live Front / Back masters donate hip→knee SHAFTS. Old 3/4 and #40 lookback do not donate "every grand hall is a side stand." They are not file_path.

## Face yaw — not a master lock (user 2026-09-18)

- Bones / identity = NanakoMasterReferenceFront only. Holding 7CTk1 is not identity.
- Face yaw / pitch / gaze = PERFORMANCE. Not the coffee-cup 3/4. Not one doll angle.
- Repeating the master's face tilt because it is safe = 毛延壽. Drop the habit, not the master.
- Axial queen plates DEFAULT to full-front face (nose on centerline, both ears visible). LEVEL or slight-down 俾倪. Do not reprint T01 chandelier-up. Do not reprint T02 / C01 coffee-3/4. A COUNT of axial halls with the same 3/4 coffee neck = waiter fail, send the neck to 太醫院.

## Shaft law — PLATINUM RAIL GrokChopstick (user 2026-09-17)

Full text: `references/GROK_CHOPSTICK.txt`.

Pose may change joint angles. Pose may NOT recalculate hip→knee cross-section.
OL8 P09 / P10 / P20 / P24 kept legal N then filled the quads. That class is now a numbered DROP.

Measure
- `Hh` = crown → chin (same head as N).
- `Tw` = one thigh mid-shaft, perpendicular to the femur, hip→knee midpoint. Not the lace welt. Not both legs. Not the skirt.
- Loaded leg on stand / A-stance / 3-4. Raised leg is bulge-check only.
- `S = Tw / Hh`
- `ΔS = S_pose − S_Front` (or S_Back on a rear plate)

Lock samples: measure S on NanakoMasterReferenceFront / Back. Historical 7CTk1 S ≈ 0.50 is HOLDING only and must not override the live masters. A-stance 163822 is a pose hint, not a shaft override.

| case | target | legal | gray | DROP |
|---|---|---|---|---|
| Front / 3-4 / A-stance loaded | **0.50** | **0.46–0.53** | 0.54 | **S ≥ 0.55** |
| Pure side | **0.52** | **0.48–0.54** | 0.55 | **S ≥ 0.56** |
| Open-step ΔS | ≤ 0.02 | ≤ 0.03 | — | **ΔS ≥ 0.04** |

Helper: knee / mid-shaft 0.74–0.86. Below 0.70 = sausage = DROP with S.
乱世用重典. Chef default fill is not a gray courtesy.

Waiter prompt must say: same hip-to-knee shaft as NanakoMasterReferenceFront / Back; do not recalculate thigh muscle; A-stance only widens the gap.
Do not recook a fat shaft. DROP. First shot only.

## Landmark law — PLATINUM RAIL Grok85Floor (user 2026-09-17)

Full text: `references/GROK_85FLOOR.txt`.

Name law
- 中文：高雄85大樓 / 東帝士85大樓。口語「85大樓」。
- English prompt token：**85Floor** (one word, capital F). This is the trigger for the Kaohsiung building.
- BANNED in every Imagine prompt: `T85`, `T-85`, `T 85`. T reads as Taipei. That is how 101 happens.

This rail exists because OL41 scored 3/41 on the tower. 38 plates drew Taipei 101 or a needle. Those plates are not stamped and not keepers.

Fingerprint of the REAL 高雄85大樓 (all four, or DROP):

1. Two lower wings / prongs.
2. Wings join into one tall teal-green glass shaft.
3. A rectangular PORTAL through the mid-building at the join (the 高 void). This is the anti-101 test. 101 has stacked ruyi boxes and no portal.
4. Pointed crown + thin antenna. Not a lotus. Not twin fins.

Waiter checklist when the job names 高雄 / 85Floor / 85大樓 / bay-office-with-tower:

- Prompt says 85Floor or 高雄85大樓. Prompt does not say T85.
- `ref_images` includes `assets/landmark/85Floor_day_vertical.jpg` or `85Floor_day_oblique.jpg`.
- Prompt names the portal and bans Taipei 101 and needle towers by name.
- After the first shot, look at the window BEFORE looking at the skirt. No portal = drop.

Illegal (any hour, any distance):

- Taipei 101 stacked ruyi
- N Seoul Tower / Canton Tower needle or lattice
- Macau tower, twin fins, lotus stem
- A smooth single slab with no wings and no portal
- Sibling Imagine pass to "swap the tower" onto a miss. That is how HDR returns.

If the job does not name 高雄 / 85Floor / 85大樓, do not force this building.

## Stamp law — PLATINUM RAIL GrokMiniStamp (user 2026-09-18 collision ban)

Full shared text: skill `grok-ministamp` (`/home/workdir/.grok/skills/grok-ministamp/SKILL.md`).
This local copy is the same rail. Do not loosen it. Ally-lock and Minru-lock inherit this file when those skills exist.

Canonical picture the user locked as EXACTLY — OL30 RAW `#30`, right landed needle.
Cap `(677, 1425)`. Stamp `(650, 1402)`. Box bottom = cap Y = his real sole.
He stands on pavement beside the rubber tip. Not in the marble reflection.

Asset: `assets/GrokMiniatureMan_sole.png` (18×24). Alias `GrokMiniatureMan_noreflect.png`.
Banned: any 18×33 padded canvas. Those 8 empty rows under the shoes were the floating-Y drift.

Never generate a tiny man. Never re-draw him. Never enlarge.
Exactly ONE official PNG. Dual stamp = reject.
If Imagine baked a second man, clone ONLY those pixels from same-Y marble 24–40px away. Do not wipe shoe shadows or fill the floor.

The frame is a flat X-Y grid. Y grows top → bottom.

1. Needle pin `(Nx, Ny)` = the small BLACK RUBBER CAP at the bottom of a landed heel stem. Lowest dark pixel of that cap, the frame before marble. Not the stem above. Not the reflection. Not the toe. Not the outsole. Not a bookshelf.
2. Stamp pin = last opaque row of the 18×24 sole-flush PNG. `Sy = Ny - 24 + 1`.
3. Same Y: miniature real-sole Y = rubber-cap-tip Y. One horizontal line. 視覺同高.
4. X — 18 px left or right of `Nx`, on **empty pavement only**.
   - Right: `Sx = Nx + 9`
   - Left:  `Sx = Nx - 27`
5. Collision test before paste. The 18×24 box may not contain any pixel of her body, hair, stocking, either shoe (vamp / last / toe / heel cup / stem / rubber), bag, desk, chair, shelf, rail, paper, or ornament. First side hits → flip X. Both sides of this cap hit → other landed cap. Never change Ny. Never slide him up the stem. Never keep a legal-Y / wrong-side park on the foot (P01/P05/P22/P29 class, 2026-09-18).
6. Exactly one stamp. PIL from RAW only. No Imagine nudge.

CASE A — two caps down: either cap, either legal side, cap-tip Y, 18px X on the ground.
CASE B — one cap down: that cap, side that misses the shoe and the stem.
CASE C — no cap, toe on the floor: toe tip, same Y, 33px X. Illegal if any cap is down.
CASE D — she is off the floor: stamp X = navel X, stamp stands on solid ground, not floating at navel Y.
CASE E — closed-leg back, two nails at the same Y: stamp X = midpoint of the two caps, stamp Y = those cap tips. Do not use the beige sole height.

## Pipeline

1. Read the job card.
2. Read GROK_CINEMA_FRAME.txt. If the job names 高雄/85Floor/85大樓, also read GROK_85FLOOR.txt.
3. FIRST SHOT: file_path = NanakoMasterReferenceFront.jpg or NanakoMasterReferenceBack.jpg. Scene/garment/85Floor refs as the job requires. One Imagine call. Prompt never contains T85. Prompt MUST start from the live master, not a sibling, not holding 7CTk1.
4. Inspect tower first when 85Floor is on the card. No portal / 101 / needle = DROP. Then inspect face IDENTITY against Front, hair against Front or Back, GrokBodyAngle (90% front on axial grand views), GrokCinemaFrame (N before F, fill vs live master), GrokHeelHead Q + 198/12 heel_cm, GrokShoe cap flush, then GrokChopstick S against the live master. Miss = drop. Do not repair.
5. Next plate: file_path = NanakoMasterReferenceFront.jpg or NanakoMasterReferenceBack.jpg again. Never the last output. Never holding 7CTk1. Never an angle plate.
6. Only after accept: PIL stamp per GrokMiniStamp. Never stamp a dropped plate.
7. Filename `GrokYYYYMMDD_HHMMSS.jpg` Asia/Taipei. Zip unless the user wants frames on chat.
8. Honest count. Do not pad with misses.

## Other girl swap

If the user attaches a different photo and says temporary identity swap:
- that photo is FACE only
- file_path is still NanakoMasterReferenceFront.jpg (or Back if the job is rear)
- body / grade / stamp / default clothes stay on this skill from the two live masters
