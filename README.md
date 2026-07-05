# Children's Chess (working title — brand TBD: *Chessquire* / *Chesslings*)

A gentler chess for young players — **"what padel is to tennis"**: easier to start, faster,
and fun from the first game, without needing to learn full chess.

> Status: **MVP in development.** Web-first (itch.io + link), iOS later. Single
> self-contained `index.html`, no backend, no tracking, kid-safe.

## The variant
- **6 wide × 8 deep** board (a "midi-chess" — bigger than classic 5×5/6×6 minichess).
- **6 pawns**, **one bishop + one knight** each, rooks in the corners, queen on **c**, king
  on **d**.
- Each player **picks which side their bishop starts** — which also fixes its colour
  (a real little strategic choice).
- Standard piece moves, two-step pawns, en passant, promotion at the far row. No castling.

## What makes it a teaching toy, not just a small chessboard
- **Move dots that coach**: a move that would stalemate/draw lights **red when you're
  ahead** (you're about to squander a win) and **green when you're behind** (grab the
  draw). A **coaching toggle** hides the words but keeps the colours as the child improves.
- **Live material score** (pawn 1 · knight/bishop 3 · rook 5 · queen 9) — teaches piece
  value with every capture.
- **Gentle draws**: a heads-up before stalemate, and every draw is framed as who
  **"salvaged a draw"** vs who **"squandered a win."**

## Roadmap (MVP)
- [ ] **Villain AI opponent** (fictional greedy tyrant; Easy / Hard / Extra-Hard) — see
  [`FABLE-BRIEF.md`](FABLE-BRIEF.md).
- [ ] Session **win-streaks** (reset when the game is closed).
- [ ] **Theme toggle** (apricot/blueberry ↔ purple/pink "villain" palette).
- [ ] Table-stakes for beta: responsive board for phones, colour-blind-safe move cues.
- [ ] Parent-facing **tip jar** (pay-what-you-want) + early-access mailing list.

## Files
- `index.html` — the whole game (open in any browser to play).
- `FABLE-BRIEF.md` — the build spec for the next feature pass.
- `AUDIT-AND-LAUNCH-PLAN.md` — code/UX/accessibility audit + the path to web beta & App Store.
- `childrens-chess-setup.pdf` / `.png` — the starting-position diagram.

## Monetisation & IP posture
Pay-what-you-want donations (parent-facing), no ads/tracking. The defensible IP is the
**brand + character + execution**, not the rules (chess rules and board sizes aren't
protectable). Names, art, and the villain character are the things to trademark/copyright.

*Not affiliated with chess.com, ChessKid, or any existing chess brand.*
