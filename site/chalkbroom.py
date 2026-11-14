#!/usr/bin/env python3
"""chalkbroom.py - convert an image to a 16-bit column stream for the chalk broom.

Ohm, 2026-11-14.

Pipeline: image -> crop/resize to 16 px tall -> threshold -> slice into 16-bit columns.

Output format (.cbw):
    magic   'CBW1'      4 bytes
    width   uint16 LE   number of columns
    height  uint8       always 16
    -- then width * 2 bytes, one uint16 LE per column --
        bit 0 = chalk 0 ... bit 15 = chalk 15
        bit SET = chalk DOWN (drawing)

Usage:
    python3 chalkbroom.py input.png out.cbw
    python3 chalkbroom.py input.png out.cbw --height 16 --invert --preview

--preview prints the bitmap as ASCII so you can check it before pushing a broom.
"""
import sys, argparse, struct

try:
    from PIL import Image
except ImportError:
    sys.exit("Pillow not installed. pip install pillow")

def load(path):
    return Image.open(path).convert("L")

def to_bitmap(img, height=16, invert=False, threshold=128):
    w, h = img.size
    new_w = max(1, round(w * (height / h)))
    small = img.resize((new_w, height), Image.LANCZOS)
    px = small.load()
    rows = []
    for y in range(height):
        row = [1 if px[x, y] < threshold else 0 for x in range(new_w)]
        rows.append(row)
    if invert:
        rows = [[1 - b for b in r] for r in rows]
    return rows, new_w

def to_columns(rows, width, height=16):
    cols = []
    for x in range(width):
        v = 0
        for y in range(height):
            if rows[y][x]:
                v |= (1 << y)
        cols.append(v)
    return cols

def write_cbw(path, cols, height=16):
    with open(path, "wb") as f:
        f.write(b"CBW1")
        f.write(struct.pack("<H", len(cols)))
        f.write(struct.pack("<B", height))
        for c in cols:
            f.write(struct.pack("<H", c))

def preview(rows, width):
    print("+" + "-" * width + "+")
    for r in rows:
        print("|" + "".join("#" if b else " " for b in r) + "|")
    print("+" + "-" * width + "+")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input")
    ap.add_argument("output")
    ap.add_argument("--height", type=int, default=16)
    ap.add_argument("--invert", action="store_true", help="white becomes chalk")
    ap.add_argument("--threshold", type=int, default=128)
    ap.add_argument("--preview", action="store_true")
    a = ap.parse_args()

    img = load(a.input)
    rows, w = to_bitmap(img, a.height, a.invert, a.threshold)
    cols = to_columns(rows, w, a.height)
    write_cbw(a.output, cols, a.height)
    if a.preview:
        preview(rows, w)
    print(f"wrote {a.output}: {len(cols)} columns x {a.height}, {len(cols)*2} bytes payload")

if __name__ == "__main__":
    main()
