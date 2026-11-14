## [chalk-broom-v2.2] - 2026-11-14
Hotfix: GW const -> let (runtime TypeError at page load killed the script).
Draw path executed headlessly, not just syntax-checked.

## [chalk-broom-v2.1] - 2026-11-14
Full-height canvas (100vw x calc(100vh - 96px)); 16 lanes spread across full
height; repaint-on-resize. Commit incl. below.

# Changelog

Versioned history of what's been published on the playground. Each entry maps
to a git tag plus the live deploy.

## [chalk-broom-v2] — 2026-11-14
15 features (Floyd–Steinberg dither, font picker, crop/zoom, edge detect,
mirror/flip, dwell line-weight, chalk wear estimate, history strip, .cbw export,
Code 39 barcode, pause, keyboard shortcuts, lane offset, data-size readout).
Commit `6f3cba2`.

## [chalk-broom-v1.1] — 2026-11-14
Added image mode + in-browser converter (drop PNG/JPG, threshold slider, invert,
pixelated thumbnail). Commit `61b2aca`.

## [chalk-broom-v1] — 2026-11-14
First publish: text-only browser simulator (16 chalk lanes, distance-clocked).
Commit `33010d9`.

## Earlier
- `6b91ec2` — seed (front-door placeholder + deploy workflow + Pages enablement).
