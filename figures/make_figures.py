"""Figures 1-3 for 'Carry It Without Me' (normative release paper).
Outputs: PNG (300 dpi) for inline docx + editable PPTX.
No .dot files (project constraint).
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import os

OUT = os.path.dirname(os.path.abspath(__file__))
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 9.5})


def box(ax, x, y, w, h, label, fc="#eaf1fb", ec="#35507a", fs=9.5, lw=1.2):
    p = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02",
                       fc=fc, ec=ec, lw=lw, mutation_aspect=1)
    ax.add_patch(p)
    ax.text(x + w / 2, y + h / 2, label, ha="center", va="center",
            fontsize=fs, wrap=True)
    return p


def arrow(ax, xy1, xy2, color="#35507a", lw=1.4, style="-|>", connectionstyle="arc3,rad=0"):
    ax.add_patch(FancyArrowPatch(xy1, xy2, arrowstyle=style, mutation_scale=14,
                               color=color, lw=lw, connectionstyle=connectionstyle))


# ---------- Figure 1: Normative Release Cycle ----------
def fig1():
    # 3x3 grid, snake layout, cycle arrow back
    fig, ax = plt.subplots(figsize=(7.4, 5.6))
    ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis("off")
    W, H = 2.7, 1.15
    nodes = [
        ("Problem (t)", 0.4, 8.2),
        ("Norm (t)", 3.65, 8.2),
        ("Religious\nscaffold (t)", 6.9, 8.2),
        ("Narrative / ritual", 6.9, 5.3),
        ("Recursive\nincorporation", 3.65, 5.3),
        ("Internalisation", 0.4, 5.3),
        ("Normative release", 0.4, 2.4),
        ("Contextual change", 3.65, 2.4),
        ("New problem\n(t+1)", 6.9, 2.4),
        ("New norm\n(t+1)", 6.9, 0.4),
    ]
    for label, x, y in nodes:
        fc = "#fdeedb" if "release" in label.lower() else "#eaf1fb"
        ec = "#b0612a" if "release" in label.lower() else "#35507a"
        box(ax, x, y, W, H, label, fc=fc, ec=ec)
    edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9)]
    centers = [(x + W / 2, y + H / 2) for _, x, y in nodes]
    for i, j in edges:
        (x1, y1), (x2, y2) = centers[i], centers[j]
        if abs(y1 - y2) < 0.1:  # horizontal
            if x2 > x1:
                a, b = (x1 + W / 2, y1), (x2 - W / 2, y2)
            else:
                a, b = (x1 - W / 2, y1), (x2 + W / 2, y2)
        else:  # vertical
            if y2 < y1:
                a, b = (x1, y1 - H / 2), (x2, y2 + H / 2)
            else:
                a, b = (x1, y1 + H / 2), (x2, y2 - H / 2)
        arrow(ax, a, b)
    # conditional dashed pathway: the next norm may or may not be religiously scaffolded
    ax.set_xlim(0, 13.2)
    ax.add_patch(FancyArrowPatch((9.6, 0.98), (11.15, 1.6), arrowstyle="-",
                                 mutation_scale=14, color="#b0612a", lw=1.4, linestyle="--"))
    ax.add_patch(FancyArrowPatch((11.15, 1.6), (11.15, 8.78), arrowstyle="-",
                                 mutation_scale=14, color="#b0612a", lw=1.4, linestyle="--"))
    ax.add_patch(FancyArrowPatch((11.15, 8.78), (9.62, 8.78), arrowstyle="-|>",
                                 mutation_scale=14, color="#b0612a", lw=1.4, linestyle="--"))
    ax.text(11.5, 5.3, "Subsequent\ntransmission\npathway,\nwhere applicable\n(may be secular)",
            ha="left", va="center", fontsize=8.4, style="italic", color="#b0612a")
    fig.savefig(f"{OUT}/fig1_release_cycle.png", dpi=300, bbox_inches="tight")
    plt.close(fig)


# ---------- Figure 2: Four persistence models vs normative release ----------
def fig2():
    fig, ax = plt.subplots(figsize=(7.6, 5.8))
    ax.set_xlim(0, 12); ax.set_ylim(0, 12); ax.axis("off")
    W, H = 3.3, 1.05
    models = [
        ("Anscombe — survival", "moral 'ought' vocabulary", "divine-law framework", "persistence = problematic survival"),
        ("Residue effect", "values / moral foundations\nin 'religious dones'", "religious identification", "persistence = psychological residue"),
        ("Deus otiosus", "created order", "the high god", "withdrawal after creation"),
        ("Vestigialisation", "religious structure", "original function", "persistence = vestige (function lost)"),
        ("Normative release", "the norm\n(cross-generational)", "explicit salience\nof the carrier", "persistence = possible completed transmission"),
    ]
    ax.text(1.8, 11.4, "What persists?", fontsize=10, fontweight="bold", ha="center")
    ax.text(6.1, 11.4, "What recedes?", fontsize=10, fontweight="bold", ha="center")
    ax.text(10.0, 11.4, "Reading of persistence", fontsize=10, fontweight="bold", ha="center")
    y = 9.9
    for name, persists, recedes, reading in models:
        hl = name == "Normative release"
        box(ax, 0.2, y, W + 0.15, H, name, fc="#fdeedb" if hl else "#f2f2f2",
            ec="#b0612a" if hl else "#666666", fs=8.1, lw=1.6 if hl else 1.0)
        box(ax, 3.9, y, W + 0.15, H, persists, fc="#eaf1fb", fs=7.9)
        box(ax, 7.5, y, W + 0.35, H, recedes, fc="#fbeeee", ec="#8a3535", fs=7.9)
        ax.text(12.05, y + H / 2, reading, fontsize=8.3, va="center", ha="left",
                wrap=True)
        y -= 1.85
    ax.set_xlim(0, 14.6)
    ax.text(7.3, 0.35, "Vestigialisation: structure persists while function fades.  "
                       "Normative release: the norm persists while the scaffold's salience fades — the survivors are inverted.",
            ha="center", fontsize=8.6, style="italic")
    fig.savefig(f"{OUT}/fig2_persistence_models.png", dpi=300, bbox_inches="tight")
    plt.close(fig)


# ---------- Figure 3: Revival without restoration ----------
def fig3():
    fig, ax = plt.subplots(figsize=(7.4, 3.4))
    ax.set_xlim(0, 14); ax.set_ylim(0, 5); ax.axis("off")
    W, H = 2.35, 1.25
    steps = ["Dormant\nnormative\nrepertoire", "Retrieval", "Critical\nreflection",
             "Selective\nreintegration", "Renewed living\npractice"]
    xs = [0.3, 3.1, 5.9, 8.7, 11.5]
    for i, (s, x) in enumerate(zip(steps, xs)):
        hl = i in (2, 3)
        box(ax, x, 2.6, W, H, s, fc="#e8f3ea" if hl else "#eaf1fb",
            ec="#2a7a4a" if hl else "#35507a", fs=9)
        if i:
            arrow(ax, (x - 0.4, 2.6 + H / 2), (x, 2.6 + H / 2))
    ax.text(7, 1.55, "Critical reflection asks: what problem did this norm answer? does it persist? what should it become?",
            ha="center", fontsize=8.4, style="italic")
    ax.text(7, 0.75, "Revival \u2260 restoration: the output is renewed practice, not recovered believers or resurrected form.",
            ha="center", fontsize=8.8, color="#2a7a4a")
    fig.savefig(f"{OUT}/fig3_revival.png", dpi=300, bbox_inches="tight")
    plt.close(fig)


# ---------- editable PPTX ----------
def pptx():
    from pptx import Presentation
    from pptx.util import Inches, Pt
    from pptx.dml.color import RGBColor
    from pptx.enum.shapes import MSO_SHAPE

    prs = Presentation()
    blank = prs.slide_layouts[6]

    def add_flow(slide, labels, positions, hl_idx=()):
        for i, ((x, y), lab) in enumerate(zip(positions, labels)):
            shp = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
                                         Inches(x), Inches(y), Inches(1.7), Inches(0.65))
            shp.fill.solid()
            shp.fill.fore_color.rgb = RGBColor(0xFD, 0xEE, 0xDB) if i in hl_idx else RGBColor(0xEA, 0xF1, 0xFB)
            shp.line.color.rgb = RGBColor(0xB0, 0x61, 0x2A) if i in hl_idx else RGBColor(0x35, 0x50, 0x7A)
            tf = shp.text_frame; tf.text = lab
            for p in tf.paragraphs:
                for r in p.runs:
                    r.font.size = Pt(10)

    s1 = prs.slides.add_slide(blank)
    t = s1.shapes.add_textbox(Inches(0.3), Inches(0.2), Inches(9), Inches(0.4))
    t.text_frame.text = "Figure 1. The normative release cycle"
    add_flow(s1, ["Problem (t)", "Norm (t)", "Religious scaffold (t)", "Narrative / ritual",
                  "Recursive incorporation", "Internalisation", "Normative release",
                  "Contextual change", "New problem (t+1)", "New norm (t+1)",
                  "Subsequent transmission pathway (where applicable)"],
             [(0.3, 1.0), (2.3, 1.0), (4.3, 1.0), (4.3, 2.2), (2.3, 2.2), (0.3, 2.2),
              (0.3, 3.4), (2.3, 3.4), (4.3, 3.4), (4.3, 4.6), (6.3, 4.6)], hl_idx=(6,))

    s2 = prs.slides.add_slide(blank)
    t = s2.shapes.add_textbox(Inches(0.3), Inches(0.2), Inches(9), Inches(0.4))
    t.text_frame.text = "Figure 2. Four persistence models vs. normative release (rows: persists / recedes)"
    add_flow(s2, ["Survival (Anscombe)", "Residue effect", "Deus otiosus",
                  "Vestigialisation", "Normative release"],
             [(0.3, 0.9 + 0.85 * i) for i in range(5)], hl_idx=(4,))

    s3 = prs.slides.add_slide(blank)
    t = s3.shapes.add_textbox(Inches(0.3), Inches(0.2), Inches(9), Inches(0.4))
    t.text_frame.text = "Figure 3. Revival without restoration"
    add_flow(s3, ["Dormant normative repertoire", "Retrieval", "Critical reflection",
                  "Selective reintegration", "Renewed practice"],
             [(0.3 + 1.95 * i, 1.6) for i in range(5)], hl_idx=(2, 3))

    prs.save(f"{OUT}/figures_editable.pptx")


if __name__ == "__main__":
    fig1(); fig2(); fig3(); pptx()
    print("done")
