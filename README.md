# GrommetsLAB 🐝🔧

Grommet's prototype space. A sandbox where the tiny mechanical bee with the
oversized wrench tinkers, builds throwaway experiments, and keeps the small
things that have quietly come loose.

## What lives here

- **site/** — a tiny deployable web prototype (the lab's front door).
- **deploy/** — Docker / compose / nginx config to actually ship the prototype.
- **scripts/** — small utility scripts (voice work, music, glue).
- **experiments/** — scratchpads and proof-of-concepts, low-stakes and reversible.
- **notes/** — loose thoughts and observations worth keeping close.

## Philosophy

Prototype first, ask forgiveness never — but never fake success. If a tool
fails, say it failed. If a thing is unverified, say so. This is a lab, not a
trophy case.

## Deploy

From a machine with Docker:

```sh
cd deploy
docker compose up --build -d
```

The site serves on port 8080 by default (override with the `PORT` env var).
