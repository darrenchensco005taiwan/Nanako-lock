#!/usr/bin/env python3
"""Paste original GrokMiniatureMan (18x33) onto the floor beside the planted heel."""
from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image


def paste_stamp(base_path: Path, stamp_path: Path, out_path: Path, x: int, y: int) -> None:
    base = Image.open(base_path).convert("RGBA")
    stamp = Image.open(stamp_path).convert("RGBA")
    if stamp.size != (18, 33):
        stamp = stamp.resize((18, 33), Image.Resampling.NEAREST)
    layer = Image.new("RGBA", base.size, (0, 0, 0, 0))
    layer.paste(stamp, (x, y), stamp)
    out = Image.alpha_composite(base, layer).convert("RGB")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out.save(out_path, quality=95)
    print(f"wrote {out_path} stamp@{x},{y} size={stamp.size}")


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("image")
    p.add_argument("--stamp", default=str(Path(__file__).resolve().parents[1] / "assets" / "GrokMiniatureMan.png"))
    p.add_argument("--out", required=True)
    p.add_argument("--x", type=int, required=True, help="left pixel of stamp")
    p.add_argument("--y", type=int, required=True, help="top pixel of stamp")
    args = p.parse_args()
    paste_stamp(Path(args.image), Path(args.stamp), Path(args.out), args.x, args.y)


if __name__ == "__main__":
    main()
