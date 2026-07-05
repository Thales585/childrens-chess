# Project Brief — Children's Chess (working title)

*Paste-ready for the Cowork project section. Doubles as the action tracker. Last updated
2026-07-05.*

## One line
A gentler chess for young kids — **"what padel is to tennis"**: easier to start, quick,
and fun from the first game. Play a friend or beat the villain, **The Collector**.

## The problem it fixes
Every kids' chess product (ChessKid, Duolingo Chess, Dr. Wolf, Play Magnus) teaches
*full, hard* chess. Nobody leads with a genuinely *simpler game*. That gap is the wedge.

## What it is
A 6×8 "midi-chess" variant: 6 pawns, one bishop + one knight each, rooks in the corners,
queen c, king d; each player picks their bishop's side (which fixes its colour). Standard
moves; no castling. It teaches piece movement, piece *values*, and how not to throw away a
won game — with coaching that fades as the child improves.

## Status — MVP, playable now
Single self-contained `index.html` (no backend, no tracking, kid-safe). **Built & verified:**
- Correct chess engine (mate/stalemate/en-passant/promotion/all draw types).
- **Villain AI — The Collector** (negamax + alpha-beta): **Easy** (blunders so kids win),
  **Hard** (depth 3), **Extra-Hard** (depth 4, ~30ms); escalating taunts.
- **2-player** hot-seat mode too.
- **Coaching move-dots** (red = you'd squander a win / green = you'd salvage a draw), now
  with shape cues for colour-blind players, plus an on/off toggle.
- **Live material score** (P1·N/B3·R5·Q9); gentle **salvaged/squandered** draw endings.
- **Session win-streaks** (reset when the game is closed).
- **Theme toggle** (apricot/blueberry ↔ purple/pink); responsive board for phones.
- Parent-facing **Support / early-access** links (placeholders — need real URLs).

## Roadmap
- **Now:** ship a web beta (itch.io + link), gather feedback from real kids.
- **Next:** polish from feedback; wrap with Capacitor for **TestFlight** → App Store
  (the villain AI is what clears Apple's "minimum functionality" bar).
- **Later:** sound/animation, more villains, maybe a paid difficulty tier.

## Monetisation & IP posture
- **Money:** pay-what-you-want on itch.io + a Ko-fi tip jar (parent-facing). No ads, no
  tracking. Possible paid Hard/Extra-Hard unlock later.
- **IP reality (important):** chess rules and board sizes **can't be protected** (this is
  the "minichess / Polgár reform" family). The moat is the **brand + The Collector
  character + execution + audience** — trademark the name, copyright the art/character.
- **Brand name:** *Chessquire* and *Chesslings* both checked **clear/ownable**; *babychess*
  is taken. Keep "mini/midi-chess" as tagline keywords, not the brand.

---

## ▶ YOUR ACTIONS (project-manage these)

**Decide (blocks other steps):**
- [ ] **Pick the brand name** — Chessquire vs Chesslings (then everything below can use it).

**Set up accounts (free, ~30 min total):**
- [ ] **itch.io** creator account — the launch outlet (built-in pay-what-you-want).
- [ ] **Ko-fi** (or Buy Me a Coffee) — tip jar + parent early-access email list in one.
- [ ] After naming: grab the **domain** (Namecheap/Cloudflare ~£10/yr) + **social handles**
  (TikTok/Instagram/YouTube for hero-vs-villain clips).

**Provide back to me:**
- [ ] The **Ko-fi + mailing-list URLs** → I'll wire them into the "Support / early-access"
  links (currently placeholders).

**Do NOT do yet:**
- [ ] Apple Developer Program ($99/yr) — only when there's an iOS build worth submitting.

## ▶ MY OPEN ACTIONS (Claude)
- [ ] Draft the parent-facing **privacy policy** (needed for the mailing list + Kids rules).
- [ ] Help **publish the web beta** on itch.io once you've made the account.
- [ ] Wire real Support/early-access URLs when you send them.
- [ ] Optional cross-check of the build by **Fable** once its rate-limit resets.

## Files (all in the private repo `Thales585/childrens-chess`)
- `index.html` — the game. · `FABLE-BRIEF.md` — the original build spec (the "Fable prompt").
- `AUDIT-AND-LAUNCH-PLAN.md` — audit + App Store path. · `README.md` — overview.
- `childrens-chess-setup.pdf/.png` — starting-position diagram.
