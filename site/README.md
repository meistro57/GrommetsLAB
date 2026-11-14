# Chalk Broom

A push-along sidewalk drawing machine: 16 chalk lanes, encoder-driven column clock,
pattern indexed by **distance** so walking speed cannot stretch the drawing.

Ohm, 2026-11-14.

## What's here

- `index.html` — browser simulator. Open it, type text, press Push.
- `chalkbroom.py` — image → `.cbw` converter (any image, 16 px tall, 16-bit columns).
- `meistro.cbw` — sample pattern, 160 columns.
- `meistro_test.png` — source image used for the sample.

## Run the simulator

Open `index.html` in a browser. No build step, no dependencies.
Or serve it: `python3 -m http.server` in this folder.

Controls:
- **Text** — anything you type is rendered to a 16-pixel-tall bitmap
- **Column pitch** — mm of travel per column (sets drawing resolution)
- **Push speed** — how fast you walk (does NOT change the drawing)
- **Push** — run it

The point of the demo: change the speed and the letters come out identical.
That's the whole design — the pattern is clocked by distance, not time.

## File format (.cbw)

    offset  size   meaning
    0       4      'CBW1'
    4       2      width in columns (uint16 LE)
    6       1      height (always 16)
    7       2*N    N uint16 LE columns

Each column is 16 bits, one per chalk lane. Bit set = chalk DOWN (drawing).
Bit order: bit 0 = lane 0 (first chalk).

## Hardware (planned)

- 2 × 74HC595 cascaded → 16 outputs
- 16 × TIP120 + flyback diode → coil-driven, spring-return chalk actuators
- Quadrature encoder per wheel (differential odometry)
- Propeller (P8X32A) — one cog ticks columns, one shifts patterns
- 1-inch chalk, ~25 mm lane spacing

## Status

Simulator and converter work. No hardware built yet.
