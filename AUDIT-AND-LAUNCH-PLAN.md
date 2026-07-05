# Children's Chess — Audit & Launch Plan

**2026-07-05.** Audit by Claude (Opus 4.8). *Note: a Fable-5 independent audit was
requested but Fable hit a session/rate limit (resets ~02:20 Europe/London) and could not
run — this is my own review; a Fable cross-check is still worth running afterwards.*

> **Biggest single risk to the App Store goal:** Apple **Guideline 4.2 (minimum
> functionality).** A thin wrapper around a simple hot-seat web game is a *known, common
> rejection*. The game must feel like a real, self-contained app (offline, no browser
> chrome, polish) and ideally offer more than two-humans-one-screen — a **computer
> opponent** is the most important single addition. Plan for this from the start.

---

## Part 1 — Audit

### A. Chess-rule correctness — **PASS, minor gaps only**
Verified by tracing the code and live tests (opening = 14 legal moves; en passant target
set and expires correctly; stalemate, checkmate, insufficient material, threefold, and the
draw-after-move colouring all behaved correctly).

- **No game-breaking bugs found.** Move generation, king-safety filtering, and the four
  draw types are correct for this 6×8 variant.
- *Minor gap (low):* insufficient-material only auto-draws lone kings or K+single-minor. It
  won't auto-draw e.g. K+B vs K+B (same-colour bishops) — the game just continues. Fine
  for kids; note for completeness.
- *Recommend:* a tiny **unit-test file** for the engine (10–15 positions: mate, stalemate,
  ep, promotion, each draw type) before adding features, so future changes can't silently
  break the rules.

### B. Accessibility — **the weakest area; matters doubly for a kids' app**
1. **[HIGH] Colour-only coaching.** Red / green / amber dots carry meaning by colour
   alone — invisible to colour-blind children (~1 in 12 boys). **Fix:** add a *shape or
   icon* to each state (e.g. ⚠ on the red "squander" dot, ✓ on the green "salvage" dot),
   so the meaning survives without colour.
2. **[MED] No keyboard play** and **no ARIA / screen-reader labels** on squares (they're
   `div`s with `onclick`; pieces are bare Unicode glyphs). Add `aria-label`s ("white
   knight on b1", "empty c3, legal move") and focusable squares.
3. **[LOW] Contrast:** the coordinate labels (`#00000066`) and the neutral slate dot on
   dark-green squares are a bit faint.

### C. Kid-UX & mobile readiness — **needs work before any phone beta**
1. **[HIGH] Board is a fixed 384px wide** (6 × 64px). On a 375px iPhone it overflows →
   horizontal scroll. **Fix:** size squares responsively (e.g. `min(64px, 15.5vw)` or a
   CSS `clamp`), so the board always fits the screen. This is table-stakes for mobile.
2. **[MED] No undo.** Children misclick constantly; a one-step undo hugely reduces
   frustration (very much in the "padel" spirit).
3. **[MED] Hot-seat orientation.** Black plays from the top, pieces "upside down" to them.
   A **flip-board** option (or auto-flip on turn) helps two kids across a table.
4. **[LOW] Setup screen is text-heavy** for a 5-year-old — consider icon buttons showing a
   light/dark bishop rather than "b-file / e-file" words.
5. **[LOW] No sound / animation.** Kids love feedback; a soft move/capture sound and a
   slide animation add a lot of delight (nice-to-have).

### D. Code quality — **fine now, plan to modularise**
- One self-contained ~290-line file with global state: perfect for this stage, and a great
  property for a web beta (zero build step). **But** once you add an AI opponent, sound,
  settings, and multiple screens, split into modules (`engine.js`, `ui.js`, `ai.js`) and
  add the test file. Don't refactor prematurely — do it when the second big feature lands.

---

## Part 2 — Path to online beta and the App Store

### 1. Fastest web beta — **today, ~$0**
The game is a single static file, so:
- **Option A (simplest): Netlify drop.** Go to app.netlify.com/drop and drag the
  `childrens-chess` folder in → instant public URL. No account strictly needed for a quick
  share; free account to keep it.
- **Option B: GitHub Pages.** `git init` the folder, push to a new GitHub repo, enable
  Pages on the `main` branch → `https://<user>.github.io/childrens-chess/`. Gives you
  version history too. *(I can set this up for you on request.)*
- Either gives a link to test with real kids **this week** — do this first; the feedback
  will shape everything below.

### 2. iOS path — **recommendation: Capacitor**
| Option | What it is | Verdict for a solo/AI effort |
|---|---|---|
| **PWA** (installable web app) | "Add to Home Screen" | Good for Android; Apple support is weak and **you can't list a PWA in the App Store**. Not sufficient for the goal. |
| **Capacitor wrapper** ⭐ | Wraps the existing HTML/JS in a native shell (WKWebView) with native APIs | **Recommended.** Keeps all your current code, produces a real `.ipa` for the App Store, supports offline, sound, haptics. Least work for the goal. |
| **Native SwiftUI rewrite** | Rebuild the game in Swift | Best performance/feel and safest vs 4.2, but throws away working code and needs Swift skills. Overkill now. |

Capacitor needs: your Mac (✓ you're on macOS), **Xcode** (free), Node.js (✓ installed).

### 3. Apple requirements & risks (a children's app gets extra scrutiny)
- **Apple Developer Program: $99/year** — required before you can submit or use external
  TestFlight.
- **Guideline 4.2 (minimum functionality)** — *the* risk (see top). Mitigate by shipping
  it as a genuine app: **offline play, no browser chrome, a computer opponent with a few
  difficulty levels, polish (sound/animation), maybe simple progress/achievements.** Two
  humans on one screen alone is likely to be rejected as "not enough."
- **Kids Category (Guidelines 1.3 & 5.1.4 / COPPA):** if you target under-13, you must:
  **no third-party analytics, ads, or tracking**; a **published privacy policy** (even if
  "we collect nothing"); parental-gate any external links/purchases; set an accurate **age
  rating**. Easiest compliance posture: **collect nothing, no network calls at all** — the
  game already does this, so *keep it that way.*
- **Assets:** app icon (many sizes), screenshots per device, name, description, keywords.

### 4. Beta distribution — TestFlight
- After the Capacitor build is in App Store Connect: **internal TestFlight** (up to 100
  testers you invite) needs no Apple review — fastest way to get it on real iPhones.
- **External TestFlight** (up to 10,000 via a public link) requires a light Apple review
  (usually ~1–2 days).

### 5. Prioritised punch-list
**Before a WEB beta (this week):**
- [ ] Responsive board sizing so it fits a phone (C1). *Table stakes.*
- [ ] Shape/icon on the coaching dots, not colour alone (B1). *Table stakes for kids.*
- [ ] Host it (Netlify/Pages).

**Before TestFlight (iOS beta):**
- [ ] Capacitor wrap + app icon + offline confirmed.
- [ ] One-step **undo** and **flip-board** (C2, C3).
- [ ] Engine unit-test file (A).
- [ ] Basic sound (nice-to-have but cheap delight).

**Before public App Store submission:**
- [ ] **Computer opponent** with difficulty levels (the 4.2 clincher). *Table stakes.*
- [ ] Privacy policy page + Kids Category compliance review; confirm zero tracking.
- [ ] ARIA labels / keyboard (B2) — quality bar.
- [ ] Screenshots, description, age rating, final polish.

### 6. Rough timeline & cost (solo + AI assistance)
- Web beta: **same day**, $0.
- Mobile-responsive + accessibility fixes: **1–2 days**.
- Capacitor wrap + first TestFlight build: **2–4 days** (first-time Xcode setup included).
- Computer opponent + polish to clear 4.2: **1–3 weeks** (the bulk of the work).
- Kids-compliance + store assets: **1–2 days**.
- **Total to a submittable kids' app: ~3–6 focused weeks + $99/yr.** Apple review after
  submission: days to ~2 weeks, allow for one rejection round.

---

### Suggested immediate next steps
1. Fix the two web-beta table-stakes items (responsive board + non-colour dot cue).
2. Put it online (I can `git init` + push to GitHub Pages now if you'd like).
3. Test with real children; gather feedback.
4. In parallel, start the **computer opponent** — it's both the best kid feature *and* the
   thing most likely to get you past App Store review.
5. Re-run the **Fable-5 cross-check** on this plan after the rate-limit resets.
