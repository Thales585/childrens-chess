import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch
import matplotlib.patheffects as pe

LIGHT, DARK, HL, INK = "#f2e8cf", "#7fa86a", "#e6902e", "#2b2b2b"
files = ["a","b","c","d","e","f"]
glyph = {"R":"♜","N":"♞","B":"♝","Q":"♛","K":"♚","P":"♟"}
back  = {"a":"R","b":"N","c":"Q","d":"K","e":"B","f":"R"}

fig, ax = plt.subplots(figsize=(6.6, 9.2))
ax.set_xlim(-0.9, 6.2); ax.set_ylim(-1.4, 8.9)
ax.set_aspect("equal"); ax.axis("off")

# squares (a1 dark)
for r in range(8):          # row 0 = rank1 bottom
    for c in range(6):
        dark = (c + r) % 2 == 0
        ax.add_patch(Rectangle((c, r), 1, 1, facecolor=DARK if dark else LIGHT, edgecolor="none"))
ax.add_patch(Rectangle((0, 0), 6, 8, fill=False, edgecolor=INK, lw=2))

def put(col, r, letter, white):
    t = ax.text(col+0.5, r+0.5, glyph[letter], ha="center", va="center",
                fontsize=30, fontfamily="DejaVu Sans",
                color="white" if white else INK, zorder=5)
    if white:
        t.set_path_effects([pe.withStroke(linewidth=1.6, foreground=INK)])

# white ranks 1-2 (rows 0-1), black ranks 7-8 (rows 6-7); mirror same files
for i, f in enumerate(files):
    put(i, 0, back[f], True)   # white back
    put(i, 1, "P", True)       # white pawns
    put(i, 7, back[f], False)  # black back
    put(i, 6, "P", False)      # black pawns

# highlight the two flank "choice" squares each side: b & e = cols 1 & 4, rows 0 & 7
for (c, r) in [(1,0),(4,0),(1,7),(4,7)]:
    ax.add_patch(Rectangle((c+0.05, r+0.05), 0.9, 0.9, fill=False, edgecolor=HL, lw=3))

# labels
for i, f in enumerate(files):
    ax.text(i+0.5, -0.3, f, ha="center", va="center", fontsize=13, color="#555")
for r in range(8):
    ax.text(-0.35, r+0.5, str(r+1), ha="center", va="center", fontsize=13, color="#555")

ax.text(3, 8.55, "Children's Chess — proposed 6×8 setup",
        ha="center", va="center", fontsize=15, fontweight="bold", color=INK)
# legend
ax.add_patch(Rectangle((0, -1.05), 0.42, 0.42, fill=False, edgecolor=HL, lw=3))
ax.text(0.6, -0.84, "player's choice — bishop or knight on this square",
        ha="left", va="center", fontsize=11.5, color="#333")

plt.tight_layout()
plt.savefig("/Users/Adam/childrens-chess/childrens-chess-setup.pdf", bbox_inches="tight")
plt.savefig("/Users/Adam/childrens-chess/childrens-chess-setup.png", dpi=150, bbox_inches="tight")
print("saved PDF + PNG")
