# Build brief for Fable — Children's Chess MVP

**One-shot spec. Everything you need is here; don't re-explore the whole tree.** Paper-safe,
kid-safe, no backend, no tracking. Deliverable: an updated **single self-contained file**
`/Users/Adam/childrens-chess/index.html` (keep it zero-build so it drops straight onto
itch.io / GitHub Pages). Do NOT break the existing rules engine — reuse it.

## What already exists (reuse, don't rewrite)
`index.html` (~290 lines, one file). Working 6×8 variant: 6 pawns, 1 bishop + 1 knight,
rooks corners, queen c, king d; player picks bishop side. Verified-correct engine with
these reusable functions: `pseudo`, `legalMovesOn(b,c,ep)` / `legalMoves(c)`,
`apply(b,mv,promo)→{nb,captured}`, `inCheck(b,c)`, `material(c)`, `drawAfterMove(mv)`,
`render()`, `onClick`, `doMove(mv,promo)`, `evaluate(key)`, `refreshHints()`, `initBoard()`.
Features already built: red/green/amber draw-warning dots + coaching toggle, live material
score, salvaged/squandered draw messages, all four draw types. **Keep all of it.**

## Jobs (in priority order)

### 1. Villain AI opponent  ← the big one
- Add a start-screen mode choice: **"2 Players"** (existing hot-seat) or **"Play the Villain"**.
- Human = hero = **White (moves first)**. Villain = Black, plays automatically after the
  human's move (small delay + a taunt).
- Three difficulties: **Easy · Hard · Extra-Hard.**
  - Use **negamax + alpha-beta** over the existing `legalMoves`/`apply`/`material`. Order
    moves captures-first for speed. Board is tiny — depth 4 is instant.
  - **Easy:** depth 1, and a ~40% "blunder" chance (play a random legal move) so a young
    child wins often. Eval = material only.
  - **Hard:** depth 3, eval = material + small centre/mobility bonus.
  - **Extra-Hard:** depth 4, same eval plus light piece-activity terms. Should rarely lose.
- Keep the UI responsive (compute in a `setTimeout`/`requestAnimationFrame` so the board
  doesn't freeze; a "Villain is thinking…" line is fine).

### 2. The villain character (fictional — NOT a real person)
- A **greedy fictional tyrant who covets the hero's pieces** ("another one for my
  hoard!"). Propose a name + one-line persona (working title *"The Collector"* — improve
  it). Cartoonish greed, kid-appropriate, no real politics/violence.
- **Escalating menace by difficulty** (Easy = blustering/comic, Extra-Hard = coldly
  confident) via short taunts on: capturing a piece, giving check, winning, and losing
  ("my hoard!"). Keep them short and fun.

### 3. Win streaks (session only)
- Track the hero's **current win streak vs the villain** and **best streak this session**.
- Store in **`sessionStorage`** so it survives reloads but **resets when the game/tab is
  closed** (this is the intended behaviour: "when the game is closed it starts again").
- Show it in the panel ("🔥 Win streak: 3"). Reset to 0 on a loss or draw.

### 4. Colour theme toggle (settings)
- Default = current **cream/olive** board. Add an alternate **purple/pink "villain"**
  palette, switchable in a small settings menu. Just swap the CSS custom properties
  (`--light`, `--dark`, accents) — don't touch layout.

### 5. Table-stakes fixes for the web beta (from the audit)
- **Responsive board:** squares are fixed 64px (→ 384px wide, overflows a 375px phone).
  Make square size fluid, e.g. `clamp(40px, 14vw, 64px)`, so the board always fits. Test
  at 375px width.
- **Colour-blind cue:** the coaching dots use colour alone. Add a **shape/icon** so the
  meaning survives without colour — e.g. red-squander = ⚠/△, green-salvage = ✓, amber = ◇.

### 6. Monetisation + audience hooks (parent-facing, no backend)
- A small, unobtrusive footer/menu with two **outbound links** (placeholders — the user
  will paste real URLs): **"☕ Support us"** (Ko-fi/Buy-Me-a-Coffee) and **"✉ Parents:
  join for early access"** (mailing-list signup). Word them for **parents, not kids.**
- **No analytics, no third-party scripts, no data collection in the app itself.** Keep it
  offline-capable and network-silent except those two user-initiated link-outs.

## Hard constraints
- One file, zero build step, works offline, no tracking/ads/network calls.
- Don't regress the existing engine or the draw/coaching features.
- Mobile-first; touch already works (click = tap). Keep touch targets ≥44px.
- Brand name still TBD (leads: *Chessquire / Chesslings*) — use a neutral title for now.

## Definition of done
Opens on a start screen (2 Players / Play the Villain + difficulty). Villain plays legal,
difficulty-appropriate chess with taunts. Streak tracks and resets on close. Theme toggles.
Board fits a phone. Dots readable without colour. Support + early-access links present.
Everything runs from the single file with no server.
