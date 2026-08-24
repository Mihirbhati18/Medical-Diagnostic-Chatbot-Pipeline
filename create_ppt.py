"""
Graph Algorithms PPT Generator
Bellman-Ford vs Ford-Fulkerson  — full comparison presentation
"""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

# ─── Color Palette ──────────────────────────────────────────────────
DARK_BG       = RGBColor(0x0F, 0x0F, 0x1A)
SLIDE_BG      = RGBColor(0x12, 0x12, 0x2B)
ACCENT_BLUE   = RGBColor(0x00, 0xD4, 0xFF)
ACCENT_PURPLE = RGBColor(0x7C, 0x3A, 0xED)
ACCENT_PINK   = RGBColor(0xEC, 0x48, 0x99)
ACCENT_GREEN  = RGBColor(0x10, 0xB9, 0x81)
ACCENT_ORANGE = RGBColor(0xF5, 0x9E, 0x0B)
ACCENT_RED    = RGBColor(0xEF, 0x44, 0x44)
WHITE         = RGBColor(0xFF, 0xFF, 0xFF)
LIGHT_GRAY    = RGBColor(0xA0, 0xA0, 0xC0)
CARD_BG       = RGBColor(0x1E, 0x1E, 0x3A)
CARD_BORDER   = RGBColor(0x30, 0x30, 0x55)


def set_slide_bg(slide, color):
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = color


def add_shape(slide, left, top, width, height, fill_color, border_color=None, border_width=Pt(0)):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill_color
    if border_color:
        shape.line.color.rgb = border_color
        shape.line.width = border_width
    else:
        shape.line.fill.background()
    shape.adjustments[0] = 0.05
    return shape


def add_bar(slide, left, top, width, height, color):
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()
    return shape


def add_circle(slide, left, top, size, fill_color):
    shape = slide.shapes.add_shape(MSO_SHAPE.OVAL, left, top, size, size)
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill_color
    shape.line.fill.background()
    return shape


def set_text(shape, text, fs=18, color=WHITE, bold=False, align=PP_ALIGN.LEFT, font="Calibri"):
    tf = shape.text_frame
    tf.clear()
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = text
    p.font.size = Pt(fs)
    p.font.color.rgb = color
    p.font.bold = bold
    p.font.name = font
    p.alignment = align


def add_para(tf, text, fs=16, color=WHITE, bold=False, align=PP_ALIGN.LEFT, font="Calibri"):
    p = tf.add_paragraph()
    p.text = text
    p.font.size = Pt(fs)
    p.font.color.rgb = color
    p.font.bold = bold
    p.font.name = font
    p.alignment = align
    p.space_before = Pt(3)
    p.space_after = Pt(3)
    return p


def bullet(tf, text, fs=15, color=LIGHT_GRAY, bold=False, level=0, font="Calibri"):
    p = tf.add_paragraph()
    p.text = text
    p.font.size = Pt(fs)
    p.font.color.rgb = color
    p.font.bold = bold
    p.font.name = font
    p.level = level
    p.space_before = Pt(3)
    p.space_after = Pt(3)
    return p


# =====================================================================
prs = Presentation()
prs.slide_width  = Inches(13.333)
prs.slide_height = Inches(7.5)
SW = prs.slide_width
SH = prs.slide_height


# =================================================================
# SLIDE 1 — TITLE
# =================================================================
sl = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(sl, DARK_BG)
add_bar(sl, Inches(0), Inches(0), SW, Inches(0.06), ACCENT_BLUE)

add_circle(sl, Inches(10.5), Inches(1.2), Inches(2.5), ACCENT_PURPLE)
add_circle(sl, Inches(11.2), Inches(2.0), Inches(1.8), ACCENT_BLUE)

tb = sl.shapes.add_textbox(Inches(1), Inches(1.8), Inches(9), Inches(1.2))
tf = tb.text_frame; tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "Graph Algorithms"
p.font.size = Pt(52); p.font.color.rgb = WHITE; p.font.bold = True; p.font.name = "Calibri"

add_bar(sl, Inches(1), Inches(3.15), Inches(3.5), Inches(0.05), ACCENT_BLUE)

tb = sl.shapes.add_textbox(Inches(1), Inches(3.4), Inches(10), Inches(0.8))
tf = tb.text_frame; tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "Bellman-Ford  vs  Ford-Fulkerson Algorithm"
p.font.size = Pt(28); p.font.color.rgb = ACCENT_BLUE; p.font.name = "Calibri"

tb = sl.shapes.add_textbox(Inches(1), Inches(4.5), Inches(9), Inches(1.2))
tf = tb.text_frame; tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "A deep-dive into two fundamental graph algorithms: finding shortest paths vs maximizing network flow  --  with BFS & DFS foundations."
p.font.size = Pt(16); p.font.color.rgb = LIGHT_GRAY; p.font.name = "Calibri"

tb = sl.shapes.add_textbox(Inches(1), Inches(6.4), Inches(5), Inches(0.5))
tf = tb.text_frame
p = tf.paragraphs[0]
p.text = "Presented by: Mihir & Ahana"
p.font.size = Pt(14); p.font.color.rgb = LIGHT_GRAY; p.font.name = "Calibri"


# =================================================================
# SLIDE 2 — TABLE OF CONTENTS
# =================================================================
sl = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(sl, DARK_BG)
add_bar(sl, Inches(0), Inches(0), SW, Inches(0.06), ACCENT_PURPLE)

tb = sl.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(8), Inches(0.8))
set_text(tb, "Table of Contents", fs=36, color=WHITE, bold=True)
add_bar(sl, Inches(0.8), Inches(1.3), Inches(2.5), Inches(0.04), ACCENT_PURPLE)

topics = [
    ("01", "What is a Graph?", ACCENT_BLUE),
    ("02", "Breadth-First Search (BFS)", ACCENT_GREEN),
    ("03", "Depth-First Search (DFS)", ACCENT_PURPLE),
    ("04", "BFS vs DFS -- Quick Comparison", ACCENT_PINK),
    ("05", "Bellman-Ford Algorithm -- Concept", ACCENT_ORANGE),
    ("06", "Bellman-Ford -- Worked Example", ACCENT_ORANGE),
    ("07", "Ford-Fulkerson Algorithm -- Concept", ACCENT_BLUE),
    ("08", "Ford-Fulkerson -- Worked Example", ACCENT_BLUE),
    ("09", "Bellman-Ford vs Ford-Fulkerson -- Head to Head", ACCENT_PINK),
    ("10", "What if We Swap Them?", ACCENT_RED),
    ("11", "Time & Space Complexity", ACCENT_GREEN),
    ("12", "Real-World Applications", ACCENT_PURPLE),
    ("13", "Summary & Key Takeaways", ACCENT_ORANGE),
]

for i, (num, topic, color) in enumerate(topics):
    y = 1.7 + i * 0.42
    c = add_circle(sl, Inches(1.0), Inches(y), Inches(0.35), color)
    set_text(c, num, fs=11, color=WHITE, bold=True, align=PP_ALIGN.CENTER)
    tb = sl.shapes.add_textbox(Inches(1.55), Inches(y + 0.02), Inches(9), Inches(0.35))
    set_text(tb, topic, fs=16, color=WHITE)


# =================================================================
# SLIDE 3 — WHAT IS A GRAPH?
# =================================================================
sl = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(sl, DARK_BG)
add_bar(sl, Inches(0), Inches(0), SW, Inches(0.06), ACCENT_BLUE)

tb = sl.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(8), Inches(0.8))
set_text(tb, "What is a Graph?", fs=36, color=WHITE, bold=True)
add_bar(sl, Inches(0.8), Inches(1.25), Inches(2.5), Inches(0.04), ACCENT_BLUE)

# Left card
card = add_shape(sl, Inches(0.8), Inches(1.7), Inches(5.5), Inches(5.0), CARD_BG, CARD_BORDER, Pt(1))
tf = card.text_frame; tf.word_wrap = True
p = tf.paragraphs[0]; p.text = "Definition"; p.font.size = Pt(22); p.font.color.rgb = ACCENT_BLUE; p.font.bold = True; p.font.name = "Calibri"

bullet(tf, "A graph G = (V, E) is a collection of vertices (nodes) connected by edges")
bullet(tf, "Vertices = entities (cities, routers, people)")
bullet(tf, "Edges = connections / relationships between entities")
bullet(tf, "")
add_para(tf, "Types of Graphs:", fs=20, color=ACCENT_GREEN, bold=True)
bullet(tf, "Directed -- edges have a direction (A -> B)")
bullet(tf, "Undirected -- edges go both ways (A -- B)")
bullet(tf, "Weighted -- edges have a cost/capacity")
bullet(tf, "Unweighted -- all edges are equal")
bullet(tf, "Flow Network -- directed + weighted with source/sink")

# Right card
card2 = add_shape(sl, Inches(6.8), Inches(1.7), Inches(5.7), Inches(5.0), CARD_BG, CARD_BORDER, Pt(1))
tf2 = card2.text_frame; tf2.word_wrap = True
p = tf2.paragraphs[0]; p.text = "Key Terminology"; p.font.size = Pt(22); p.font.color.rgb = ACCENT_PURPLE; p.font.bold = True; p.font.name = "Calibri"

bullet(tf2, "Adjacency -- two nodes connected by an edge")
bullet(tf2, "Degree -- number of edges touching a node")
bullet(tf2, "Path -- sequence of edges from one node to another")
bullet(tf2, "Cycle -- a path that starts and ends at the same node")
bullet(tf2, "Weight -- numerical cost assigned to an edge")
bullet(tf2, "")
add_para(tf2, "For This Presentation:", fs=18, color=ACCENT_ORANGE, bold=True)
bullet(tf2, "Bellman-Ford uses weighted directed graphs")
bullet(tf2, "Ford-Fulkerson uses flow networks")
bullet(tf2, "  (directed graphs with capacity on each edge)")
bullet(tf2, "BFS & DFS work on any graph type")


# =================================================================
# SLIDE 4 — BFS
# =================================================================
sl = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(sl, DARK_BG)
add_bar(sl, Inches(0), Inches(0), SW, Inches(0.06), ACCENT_GREEN)

tb = sl.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(10), Inches(0.8))
set_text(tb, "Breadth-First Search (BFS)", fs=36, color=WHITE, bold=True)
add_bar(sl, Inches(0.8), Inches(1.25), Inches(2.5), Inches(0.04), ACCENT_GREEN)

card = add_shape(sl, Inches(0.8), Inches(1.7), Inches(6.0), Inches(5.2), CARD_BG, CARD_BORDER, Pt(1))
tf = card.text_frame; tf.word_wrap = True
p = tf.paragraphs[0]; p.text = "How BFS Works"; p.font.size = Pt(22); p.font.color.rgb = ACCENT_GREEN; p.font.bold = True; p.font.name = "Calibri"

bullet(tf, "Explores all neighbors at the CURRENT depth first", color=WHITE, bold=True)
bullet(tf, "Then moves to the next depth level")
bullet(tf, 'Uses a Queue (FIFO) -- "First In, First Out"')
bullet(tf, "Guarantees shortest path in unweighted graphs")
bullet(tf, "")
add_para(tf, "Algorithm Steps:", fs=18, color=ACCENT_BLUE, bold=True)
bullet(tf, "1. Enqueue source, mark as visited")
bullet(tf, "2. Dequeue front node, process it")
bullet(tf, "3. Enqueue all unvisited neighbors")
bullet(tf, "4. Repeat until queue is empty")

# Properties
card2 = add_shape(sl, Inches(7.2), Inches(1.7), Inches(5.3), Inches(2.4), CARD_BG, CARD_BORDER, Pt(1))
tf2 = card2.text_frame; tf2.word_wrap = True
p = tf2.paragraphs[0]; p.text = "Key Properties"; p.font.size = Pt(20); p.font.color.rgb = ACCENT_ORANGE; p.font.bold = True; p.font.name = "Calibri"
bullet(tf2, "Data Structure: Queue (FIFO)")
bullet(tf2, "Time Complexity: O(V + E)")
bullet(tf2, "Space Complexity: O(V)")
bullet(tf2, "Shortest path: Yes (unweighted)")

# Role in Ford-Fulkerson
card3 = add_shape(sl, Inches(7.2), Inches(4.35), Inches(5.3), Inches(2.55), CARD_BG, ACCENT_BLUE, Pt(2))
tf3 = card3.text_frame; tf3.word_wrap = True
p = tf3.paragraphs[0]; p.text = "BFS in Ford-Fulkerson"; p.font.size = Pt(20); p.font.color.rgb = ACCENT_BLUE; p.font.bold = True; p.font.name = "Calibri"
add_para(tf3, "Ford-Fulkerson uses BFS to find", fs=15, color=LIGHT_GRAY)
add_para(tf3, "augmenting paths in the residual graph.", fs=15, color=LIGHT_GRAY)
add_para(tf3, "", fs=6, color=DARK_BG)
add_para(tf3, "When BFS is used, the algorithm is", fs=15, color=LIGHT_GRAY)
add_para(tf3, "called Edmonds-Karp (optimized variant).", fs=15, color=ACCENT_GREEN, bold=True)
add_para(tf3, "This guarantees polynomial runtime.", fs=14, color=LIGHT_GRAY)


# =================================================================
# SLIDE 5 — DFS
# =================================================================
sl = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(sl, DARK_BG)
add_bar(sl, Inches(0), Inches(0), SW, Inches(0.06), ACCENT_PURPLE)

tb = sl.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(10), Inches(0.8))
set_text(tb, "Depth-First Search (DFS)", fs=36, color=WHITE, bold=True)
add_bar(sl, Inches(0.8), Inches(1.25), Inches(2.5), Inches(0.04), ACCENT_PURPLE)

card = add_shape(sl, Inches(0.8), Inches(1.7), Inches(6.0), Inches(5.2), CARD_BG, CARD_BORDER, Pt(1))
tf = card.text_frame; tf.word_wrap = True
p = tf.paragraphs[0]; p.text = "How DFS Works"; p.font.size = Pt(22); p.font.color.rgb = ACCENT_PURPLE; p.font.bold = True; p.font.name = "Calibri"

bullet(tf, "Explores as DEEP as possible along each branch", color=WHITE, bold=True)
bullet(tf, "Backtracks when hitting a dead end")
bullet(tf, 'Uses a Stack (LIFO) or Recursion -- "Last In, First Out"')
bullet(tf, "Does NOT guarantee shortest path")
bullet(tf, "")
add_para(tf, "Algorithm Steps:", fs=18, color=ACCENT_BLUE, bold=True)
bullet(tf, "1. Push source onto stack, mark visited")
bullet(tf, "2. Pop top node, process it")
bullet(tf, "3. Push one unvisited neighbor, go deeper")
bullet(tf, "4. Backtrack when no unvisited neighbors remain")

card2 = add_shape(sl, Inches(7.2), Inches(1.7), Inches(5.3), Inches(2.4), CARD_BG, CARD_BORDER, Pt(1))
tf2 = card2.text_frame; tf2.word_wrap = True
p = tf2.paragraphs[0]; p.text = "Key Properties"; p.font.size = Pt(20); p.font.color.rgb = ACCENT_ORANGE; p.font.bold = True; p.font.name = "Calibri"
bullet(tf2, "Data Structure: Stack (LIFO) / Recursion")
bullet(tf2, "Time Complexity: O(V + E)")
bullet(tf2, "Space Complexity: O(V)")
bullet(tf2, "Shortest path: No")

card3 = add_shape(sl, Inches(7.2), Inches(4.35), Inches(5.3), Inches(2.55), CARD_BG, ACCENT_ORANGE, Pt(2))
tf3 = card3.text_frame; tf3.word_wrap = True
p = tf3.paragraphs[0]; p.text = "DFS in Ford-Fulkerson"; p.font.size = Pt(20); p.font.color.rgb = ACCENT_ORANGE; p.font.bold = True; p.font.name = "Calibri"
add_para(tf3, "Original Ford-Fulkerson uses DFS", fs=15, color=LIGHT_GRAY)
add_para(tf3, "to find augmenting paths.", fs=15, color=LIGHT_GRAY)
add_para(tf3, "", fs=6, color=DARK_BG)
add_para(tf3, "DFS-based path finding can lead to", fs=15, color=LIGHT_GRAY)
add_para(tf3, "non-termination with irrational capacities!", fs=15, color=ACCENT_RED, bold=True)
add_para(tf3, "That's why Edmonds-Karp (BFS) is preferred.", fs=14, color=LIGHT_GRAY)


# =================================================================
# SLIDE 6 — BFS vs DFS QUICK COMPARISON
# =================================================================
sl = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(sl, DARK_BG)
add_bar(sl, Inches(0), Inches(0), SW, Inches(0.06), ACCENT_PINK)

tb = sl.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(10), Inches(0.8))
set_text(tb, "BFS vs DFS -- Quick Comparison", fs=36, color=WHITE, bold=True)
add_bar(sl, Inches(0.8), Inches(1.25), Inches(2.5), Inches(0.04), ACCENT_PINK)

rows = [
    ("Feature",         "BFS",                            "DFS"),
    ("Data Structure",  "Queue (FIFO)",                   "Stack (LIFO) / Recursion"),
    ("Traversal",       "Level by level (breadth)",       "Branch by branch (depth)"),
    ("Shortest Path",   "Yes (unweighted)",               "No"),
    ("Memory",          "High (all neighbors in queue)",  "Low (current path only)"),
    ("Completeness",    "Always finds a solution",        "May get stuck (infinite graphs)"),
    ("Used In",         "Ford-Fulkerson (Edmonds-Karp)",  "Ford-Fulkerson (original)"),
    ("Complexity",      "O(V + E)",                       "O(V + E)"),
]

rh = 0.55
sy = 1.6
cw = [Inches(3.0), Inches(4.5), Inches(4.5)]
cx = [Inches(0.6), Inches(3.6), Inches(8.1)]

for r, (f, b, d) in enumerate(rows):
    y = sy + r * rh
    if r == 0:
        bg = RGBColor(0x1A, 0x1A, 0x40)
        colors = [WHITE, ACCENT_GREEN, ACCENT_PURPLE]
        bld, fsize = True, 15
    else:
        bg = CARD_BG if r % 2 == 0 else RGBColor(0x16, 0x16, 0x30)
        colors = [LIGHT_GRAY, LIGHT_GRAY, LIGHT_GRAY]
        bld, fsize = False, 13
    for c, (txt, col, w, l) in enumerate(zip([f, b, d], colors, cw, cx)):
        cell = add_shape(sl, l, Inches(y), w, Inches(rh - 0.02), bg, CARD_BORDER if r == 0 else None)
        set_text(cell, txt, fs=fsize, color=col, bold=bld, align=PP_ALIGN.CENTER)

ins = add_shape(sl, Inches(0.6), Inches(6.2), Inches(12.0), Inches(0.7), RGBColor(0x0A, 0x2A, 0x1A), ACCENT_GREEN, Pt(1))
tf = ins.text_frame; tf.word_wrap = True
p = tf.paragraphs[0]; p.text = "Both BFS & DFS are graph traversal techniques. They serve as building blocks for advanced algorithms like Bellman-Ford and Ford-Fulkerson."
p.font.size = Pt(14); p.font.color.rgb = ACCENT_GREEN; p.font.name = "Calibri"; p.alignment = PP_ALIGN.CENTER


# =================================================================
# SLIDE 7 — BELLMAN-FORD CONCEPT
# =================================================================
sl = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(sl, DARK_BG)
add_bar(sl, Inches(0), Inches(0), SW, Inches(0.06), ACCENT_ORANGE)

tb = sl.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(10), Inches(0.8))
set_text(tb, "Bellman-Ford Algorithm", fs=36, color=WHITE, bold=True)
add_bar(sl, Inches(0.8), Inches(1.25), Inches(2.5), Inches(0.04), ACCENT_ORANGE)

card = add_shape(sl, Inches(0.8), Inches(1.7), Inches(6.0), Inches(5.2), CARD_BG, CARD_BORDER, Pt(1))
tf = card.text_frame; tf.word_wrap = True
p = tf.paragraphs[0]; p.text = "Purpose: Shortest Path"; p.font.size = Pt(22); p.font.color.rgb = ACCENT_ORANGE; p.font.bold = True; p.font.name = "Calibri"

bullet(tf, "Finds the shortest path from a SINGLE SOURCE to all other vertices", color=WHITE, bold=True)
bullet(tf, "Works on weighted directed graphs")
bullet(tf, "Handles NEGATIVE edge weights (unlike Dijkstra)")
bullet(tf, "Can detect negative-weight cycles")
bullet(tf, "")
add_para(tf, "Core Idea -- Edge Relaxation:", fs=18, color=ACCENT_BLUE, bold=True)
bullet(tf, "1. Initialize: dist[source] = 0, all others = infinity")
bullet(tf, "2. Repeat (V-1) times:")
bullet(tf, "    For each edge (u, v, weight):", level=1)
bullet(tf, "       if dist[u] + weight < dist[v]:", level=1)
bullet(tf, "          dist[v] = dist[u] + weight", level=1)
bullet(tf, '3. One more pass to detect negative cycles')

card2 = add_shape(sl, Inches(7.2), Inches(1.7), Inches(5.3), Inches(2.4), CARD_BG, CARD_BORDER, Pt(1))
tf2 = card2.text_frame; tf2.word_wrap = True
p = tf2.paragraphs[0]; p.text = "Key Properties"; p.font.size = Pt(20); p.font.color.rgb = ACCENT_ORANGE; p.font.bold = True; p.font.name = "Calibri"
bullet(tf2, "Problem: Single-source shortest path")
bullet(tf2, "Time Complexity: O(V x E)")
bullet(tf2, "Space Complexity: O(V)")
bullet(tf2, "Negative weights: YES")
bullet(tf2, "Negative cycle detection: YES")

card3 = add_shape(sl, Inches(7.2), Inches(4.35), Inches(5.3), Inches(2.55), CARD_BG, ACCENT_ORANGE, Pt(2))
tf3 = card3.text_frame; tf3.word_wrap = True
p = tf3.paragraphs[0]; p.text = "Relaxation Formula"; p.font.size = Pt(20); p.font.color.rgb = ACCENT_ORANGE; p.font.bold = True; p.font.name = "Calibri"
add_para(tf3, "For edge (u -> v) with weight w:", fs=15, color=LIGHT_GRAY)
add_para(tf3, "", fs=6, color=DARK_BG)
add_para(tf3, "if dist[u] + w  <  dist[v]:", fs=17, color=ACCENT_BLUE, bold=True, font="Consolas")
add_para(tf3, "    dist[v] = dist[u] + w", fs=17, color=ACCENT_GREEN, bold=True, font="Consolas")
add_para(tf3, "", fs=6, color=DARK_BG)
add_para(tf3, 'Relax = update distance if a shorter path is found', fs=14, color=LIGHT_GRAY)


# =================================================================
# SLIDE 8 — BELLMAN-FORD WORKED EXAMPLE
# =================================================================
sl = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(sl, DARK_BG)
add_bar(sl, Inches(0), Inches(0), SW, Inches(0.06), ACCENT_ORANGE)

tb = sl.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(10), Inches(0.8))
set_text(tb, "Bellman-Ford -- Worked Example", fs=36, color=WHITE, bold=True)
add_bar(sl, Inches(0.8), Inches(1.25), Inches(2.5), Inches(0.04), ACCENT_ORANGE)

# Graph
card = add_shape(sl, Inches(0.5), Inches(1.6), Inches(5.5), Inches(3.0), CARD_BG, CARD_BORDER, Pt(1))
tf = card.text_frame; tf.word_wrap = True
p = tf.paragraphs[0]; p.text = "Weighted Directed Graph (Source = A)"; p.font.size = Pt(19); p.font.color.rgb = ACCENT_ORANGE; p.font.bold = True; p.font.name = "Calibri"
add_para(tf, "", fs=4, color=DARK_BG)
add_para(tf, "Edges:", fs=17, color=ACCENT_BLUE, bold=True)
bullet(tf, "A --( 6 )--> B", fs=15)
bullet(tf, "A --( 7 )--> C", fs=15)
bullet(tf, "B --( 5 )--> C", fs=15)
bullet(tf, "B --(-4 )--> D     (negative!)", fs=15, color=ACCENT_PINK)
bullet(tf, "C --(-3 )--> D     (negative!)", fs=15, color=ACCENT_PINK)
bullet(tf, "D --( 9 )--> B", fs=15)

# Iterations
card2 = add_shape(sl, Inches(6.3), Inches(1.6), Inches(6.5), Inches(3.0), CARD_BG, CARD_BORDER, Pt(1))
tf2 = card2.text_frame; tf2.word_wrap = True
p = tf2.paragraphs[0]; p.text = "Relaxation Iterations"; p.font.size = Pt(19); p.font.color.rgb = ACCENT_GREEN; p.font.bold = True; p.font.name = "Calibri"
add_para(tf2, "", fs=4, color=DARK_BG)
add_para(tf2, "             A       B       C       D", fs=15, color=WHITE, bold=True, font="Consolas")
add_para(tf2, "Init:        0       inf     inf     inf", fs=14, color=LIGHT_GRAY, font="Consolas")
add_para(tf2, "Iter 1:      0       6       7       2", fs=14, color=ACCENT_BLUE, font="Consolas")
add_para(tf2, "Iter 2:      0       6       7       2", fs=14, color=ACCENT_GREEN, font="Consolas")
add_para(tf2, "Iter 3:      0       6       7       2", fs=14, color=ACCENT_PURPLE, font="Consolas")
add_para(tf2, "", fs=4, color=DARK_BG)
add_para(tf2, "Shortest path A->D = 2  (via A->B->D : 6+(-4))", fs=15, color=ACCENT_GREEN, bold=True)

# Explanation
card3 = add_shape(sl, Inches(0.5), Inches(4.85), Inches(12.3), Inches(2.3), CARD_BG, ACCENT_PINK, Pt(2))
tf3 = card3.text_frame; tf3.word_wrap = True
p = tf3.paragraphs[0]; p.text = "Step-by-Step Explanation"; p.font.size = Pt(20); p.font.color.rgb = ACCENT_PINK; p.font.bold = True; p.font.name = "Calibri"
bullet(tf3, "Iteration 1: Process all edges. A->B gives dist[B]=6. A->C gives dist[C]=7. B->D gives dist[D]=6+(-4)=2. C->D: 7+(-3)=4 > 2, no update.")
bullet(tf3, "Iteration 2: No distances change -- algorithm can stop early (optimization).")
bullet(tf3, "Negative cycle check: Process all edges once more. No distance decreases -- NO negative cycle exists.")
bullet(tf3, "Result: Shortest paths from A: B=6, C=7, D=2. The negative edge B->D gave us a shortcut!", color=WHITE, bold=True)


# =================================================================
# SLIDE 9 — FORD-FULKERSON CONCEPT
# =================================================================
sl = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(sl, DARK_BG)
add_bar(sl, Inches(0), Inches(0), SW, Inches(0.06), ACCENT_BLUE)

tb = sl.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(10), Inches(0.8))
set_text(tb, "Ford-Fulkerson Algorithm", fs=36, color=WHITE, bold=True)
add_bar(sl, Inches(0.8), Inches(1.25), Inches(2.5), Inches(0.04), ACCENT_BLUE)

card = add_shape(sl, Inches(0.8), Inches(1.7), Inches(6.0), Inches(5.2), CARD_BG, CARD_BORDER, Pt(1))
tf = card.text_frame; tf.word_wrap = True
p = tf.paragraphs[0]; p.text = "Purpose: Maximum Flow"; p.font.size = Pt(22); p.font.color.rgb = ACCENT_BLUE; p.font.bold = True; p.font.name = "Calibri"

bullet(tf, "Finds the MAXIMUM FLOW from source (S) to sink (T)", color=WHITE, bold=True)
bullet(tf, "Works on flow networks (directed + capacities)")
bullet(tf, "Uses augmenting paths via BFS or DFS")
bullet(tf, "Based on the Max-Flow Min-Cut theorem")
bullet(tf, "")
add_para(tf, "Core Idea -- Augmenting Paths:", fs=18, color=ACCENT_GREEN, bold=True)
bullet(tf, "1. Start with zero flow on all edges")
bullet(tf, "2. Find a path from Source to Sink with available capacity")
bullet(tf, "3. Push maximum possible flow through that path")
bullet(tf, "4. Update the residual graph (forward - backward edges)")
bullet(tf, "5. Repeat until no augmenting path exists")
bullet(tf, "6. Total flow pushed = Maximum Flow")

card2 = add_shape(sl, Inches(7.2), Inches(1.7), Inches(5.3), Inches(2.4), CARD_BG, CARD_BORDER, Pt(1))
tf2 = card2.text_frame; tf2.word_wrap = True
p = tf2.paragraphs[0]; p.text = "Key Properties"; p.font.size = Pt(20); p.font.color.rgb = ACCENT_BLUE; p.font.bold = True; p.font.name = "Calibri"
bullet(tf2, "Problem: Maximum network flow")
bullet(tf2, "Time: O(E x max_flow)  [DFS version]")
bullet(tf2, "Time: O(V x E^2)  [BFS / Edmonds-Karp]")
bullet(tf2, "Space Complexity: O(V + E)")
bullet(tf2, "Relies on: Residual graphs")

card3 = add_shape(sl, Inches(7.2), Inches(4.35), Inches(5.3), Inches(2.55), CARD_BG, ACCENT_BLUE, Pt(2))
tf3 = card3.text_frame; tf3.word_wrap = True
p = tf3.paragraphs[0]; p.text = "Residual Graph Concept"; p.font.size = Pt(20); p.font.color.rgb = ACCENT_BLUE; p.font.bold = True; p.font.name = "Calibri"
add_para(tf3, "For each edge with capacity C and flow F:", fs=15, color=LIGHT_GRAY)
add_para(tf3, "", fs=6, color=DARK_BG)
add_para(tf3, "Forward edge:  remaining = C - F", fs=16, color=ACCENT_GREEN, bold=True, font="Consolas")
add_para(tf3, "Backward edge: remaining = F", fs=16, color=ACCENT_ORANGE, bold=True, font="Consolas")
add_para(tf3, "", fs=6, color=DARK_BG)
add_para(tf3, "Backward edges allow the algorithm", fs=14, color=LIGHT_GRAY)
add_para(tf3, 'to "undo" bad flow decisions.', fs=14, color=LIGHT_GRAY)


# =================================================================
# SLIDE 10 — FORD-FULKERSON WORKED EXAMPLE
# =================================================================
sl = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(sl, DARK_BG)
add_bar(sl, Inches(0), Inches(0), SW, Inches(0.06), ACCENT_BLUE)

tb = sl.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(10), Inches(0.8))
set_text(tb, "Ford-Fulkerson -- Worked Example", fs=36, color=WHITE, bold=True)
add_bar(sl, Inches(0.8), Inches(1.25), Inches(2.5), Inches(0.04), ACCENT_BLUE)

# Graph
card = add_shape(sl, Inches(0.5), Inches(1.6), Inches(5.5), Inches(2.7), CARD_BG, CARD_BORDER, Pt(1))
tf = card.text_frame; tf.word_wrap = True
p = tf.paragraphs[0]; p.text = "Flow Network (S=source, T=sink)"; p.font.size = Pt(19); p.font.color.rgb = ACCENT_BLUE; p.font.bold = True; p.font.name = "Calibri"
add_para(tf, "", fs=4, color=DARK_BG)
add_para(tf, "Edges (with capacity):", fs=17, color=ACCENT_GREEN, bold=True)
bullet(tf, "S --[10]--> A", fs=15)
bullet(tf, "S --[ 8]--> B", fs=15)
bullet(tf, "A --[ 5]--> B", fs=15)
bullet(tf, "A --[ 7]--> T", fs=15)
bullet(tf, "B --[10]--> T", fs=15)

# Iterations
card2 = add_shape(sl, Inches(6.3), Inches(1.6), Inches(6.5), Inches(2.7), CARD_BG, CARD_BORDER, Pt(1))
tf2 = card2.text_frame; tf2.word_wrap = True
p = tf2.paragraphs[0]; p.text = "Finding Augmenting Paths"; p.font.size = Pt(19); p.font.color.rgb = ACCENT_GREEN; p.font.bold = True; p.font.name = "Calibri"
add_para(tf2, "", fs=4, color=DARK_BG)
add_para(tf2, "Path 1: S -> A -> T", fs=16, color=ACCENT_BLUE, bold=True)
add_para(tf2, "  Bottleneck = min(10, 7) = 7. Push flow = 7", fs=14, color=LIGHT_GRAY)
add_para(tf2, "Path 2: S -> B -> T", fs=16, color=ACCENT_PURPLE, bold=True)
add_para(tf2, "  Bottleneck = min(8, 10) = 8. Push flow = 8", fs=14, color=LIGHT_GRAY)
add_para(tf2, "Path 3: S -> A -> B -> T", fs=16, color=ACCENT_ORANGE, bold=True)
add_para(tf2, "  Bottleneck = min(3, 5, 2) = 2. Push flow = 2", fs=14, color=LIGHT_GRAY)
add_para(tf2, "No more paths! Max Flow = 7 + 8 + 2 = 17", fs=15, color=ACCENT_GREEN, bold=True)

# Explanation
card3 = add_shape(sl, Inches(0.5), Inches(4.55), Inches(12.3), Inches(2.65), CARD_BG, ACCENT_GREEN, Pt(2))
tf3 = card3.text_frame; tf3.word_wrap = True
p = tf3.paragraphs[0]; p.text = "Step-by-Step Explanation"; p.font.size = Pt(20); p.font.color.rgb = ACCENT_GREEN; p.font.bold = True; p.font.name = "Calibri"
bullet(tf3, "Step 1: Find path S->A->T using BFS/DFS. The bottleneck (smallest capacity along path) = min(10, 7) = 7. Send 7 units of flow.")
bullet(tf3, "Step 2: Update residual graph. S->A now has 3 remaining. A->T has 0 remaining (fully used). Create backward edges.")
bullet(tf3, "Step 3: Find next path S->B->T. Bottleneck = min(8, 10) = 8. Send 8 units. Update residual graph.")
bullet(tf3, "Step 4: Find next path S->A->B->T. S->A has 3 left, A->B has 5, B->T has 2 left. Bottleneck = min(3, 5, 2) = 2. Send 2 units.")
bullet(tf3, "Step 5: No more augmenting paths from S to T exist. MAXIMUM FLOW = 7 + 8 + 2 = 17 units.", color=WHITE, bold=True)


# =================================================================
# SLIDE 11 — BELLMAN-FORD vs FORD-FULKERSON HEAD TO HEAD
# =================================================================
sl = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(sl, DARK_BG)
add_bar(sl, Inches(0), Inches(0), SW, Inches(0.06), ACCENT_PINK)

tb = sl.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(11), Inches(0.8))
set_text(tb, "Bellman-Ford vs Ford-Fulkerson -- Head to Head", fs=34, color=WHITE, bold=True)
add_bar(sl, Inches(0.8), Inches(1.25), Inches(2.5), Inches(0.04), ACCENT_PINK)

rows2 = [
    ("Aspect",             "Bellman-Ford",                           "Ford-Fulkerson"),
    ("Problem Solved",     "Shortest Path (single source)",          "Maximum Flow (source to sink)"),
    ("Graph Type",         "Weighted directed graph",                "Flow network (directed + capacities)"),
    ("Edge Weights",       "Can be negative",                        "Non-negative capacities only"),
    ("Core Technique",     "Edge Relaxation (V-1 iterations)",       "Augmenting Paths + Residual Graph"),
    ("Uses BFS/DFS?",      "No (iterates over all edges)",           "Yes (BFS or DFS to find paths)"),
    ("Output",             "Shortest distances from source",         "Maximum flow value"),
    ("Negative Cycles",    "Detects them",                           "Not applicable"),
    ("Time Complexity",    "O(V x E)",                               "O(E x max_flow) or O(V x E^2)"),
    ("Space Complexity",   "O(V)",                                   "O(V + E)"),
]

rh = 0.5
sy = 1.55
cw = [Inches(2.8), Inches(4.6), Inches(4.6)]
cx = [Inches(0.5), Inches(3.3), Inches(7.9)]

for r, (f, b, d) in enumerate(rows2):
    y = sy + r * rh
    if r == 0:
        bg = RGBColor(0x1A, 0x1A, 0x40)
        colors = [WHITE, ACCENT_ORANGE, ACCENT_BLUE]
        bld, fsize = True, 14
    else:
        bg = CARD_BG if r % 2 == 0 else RGBColor(0x16, 0x16, 0x30)
        colors = [LIGHT_GRAY, LIGHT_GRAY, LIGHT_GRAY]
        bld, fsize = False, 12
    for c, (txt, col, w, l) in enumerate(zip([f, b, d], colors, cw, cx)):
        cell = add_shape(sl, l, Inches(y), w, Inches(rh - 0.02), bg, CARD_BORDER if r == 0 else None)
        set_text(cell, txt, fs=fsize, color=col, bold=bld, align=PP_ALIGN.CENTER)

ins = add_shape(sl, Inches(0.5), Inches(6.6), Inches(12.2), Inches(0.55), RGBColor(0x1A, 0x0A, 0x2A), ACCENT_PINK, Pt(1))
set_text(ins, "These algorithms solve COMPLETELY DIFFERENT problems. Bellman-Ford = shortest distance. Ford-Fulkerson = maximum throughput.",
         fs=14, color=ACCENT_PINK, align=PP_ALIGN.CENTER)


# =================================================================
# SLIDE 12 — WHAT IF WE SWAP THEM?
# =================================================================
sl = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(sl, DARK_BG)
add_bar(sl, Inches(0), Inches(0), SW, Inches(0.06), ACCENT_RED)

tb = sl.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(11), Inches(0.8))
set_text(tb, "What If We Swap Them?", fs=36, color=WHITE, bold=True)
add_bar(sl, Inches(0.8), Inches(1.25), Inches(2.5), Inches(0.04), ACCENT_RED)

# Scenario 1 — Bellman-Ford for max flow
card1 = add_shape(sl, Inches(0.4), Inches(1.65), Inches(6.1), Inches(5.2), CARD_BG, ACCENT_ORANGE, Pt(2))
tf1 = card1.text_frame; tf1.word_wrap = True
p = tf1.paragraphs[0]; p.text = "Using Bellman-Ford for Max Flow?"; p.font.size = Pt(22); p.font.color.rgb = ACCENT_ORANGE; p.font.bold = True; p.font.name = "Calibri"

add_para(tf1, '', fs=4, color=DARK_BG)
add_para(tf1, "WILL NOT WORK!", fs=22, color=ACCENT_RED, bold=True, align=PP_ALIGN.CENTER)
add_para(tf1, '', fs=6, color=DARK_BG)
bullet(tf1, "Bellman-Ford finds shortest DISTANCE, not maximum FLOW")
bullet(tf1, "It doesn't understand capacity constraints on edges")
bullet(tf1, "It has no concept of residual graphs or augmenting paths")
bullet(tf1, "It doesn't track flow on edges, only cumulative distance")
bullet(tf1, "")
add_para(tf1, "However... Bellman-Ford CAN help inside", fs=15, color=ACCENT_GREEN)
add_para(tf1, "Ford-Fulkerson as a subroutine!", fs=15, color=ACCENT_GREEN)
bullet(tf1, "In the Min-Cost Max-Flow variant, Bellman-Ford")
bullet(tf1, "finds the cheapest augmenting path instead of")
bullet(tf1, "BFS/DFS finding any path. This optimizes COST,", level=0)
bullet(tf1, "not just maximizing flow.", level=0)

# Scenario 2 — Ford-Fulkerson for shortest path
card2 = add_shape(sl, Inches(6.85), Inches(1.65), Inches(6.1), Inches(5.2), CARD_BG, ACCENT_BLUE, Pt(2))
tf2 = card2.text_frame; tf2.word_wrap = True
p = tf2.paragraphs[0]; p.text = "Using Ford-Fulkerson for Shortest Path?"; p.font.size = Pt(22); p.font.color.rgb = ACCENT_BLUE; p.font.bold = True; p.font.name = "Calibri"

add_para(tf2, '', fs=4, color=DARK_BG)
add_para(tf2, "WILL NOT WORK!", fs=22, color=ACCENT_RED, bold=True, align=PP_ALIGN.CENTER)
add_para(tf2, '', fs=6, color=DARK_BG)
bullet(tf2, "Ford-Fulkerson maximizes THROUGHPUT, not minimizes DISTANCE")
bullet(tf2, "It treats edge values as capacities, not costs/weights")
bullet(tf2, "It can't handle negative edge weights at all")
bullet(tf2, "It finds amount of flow, not a path with minimum cost")
bullet(tf2, "")
add_para(tf2, "Which is more optimized overall?", fs=18, color=ACCENT_GREEN, bold=True)
bullet(tf2, "This is like comparing a hammer and a screwdriver")
bullet(tf2, "They solve DIFFERENT problems!")
bullet(tf2, "Bellman-Ford: O(V x E) -- for shortest path, works great")
bullet(tf2, "Ford-Fulkerson: O(V x E^2) -- for max flow, works great")
bullet(tf2, "Neither can replace the other. Choose based on")
bullet(tf2, "your PROBLEM, not the algorithm's speed.")


# =================================================================
# SLIDE 13 — COMPLEXITY COMPARISON
# =================================================================
sl = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(sl, DARK_BG)
add_bar(sl, Inches(0), Inches(0), SW, Inches(0.06), ACCENT_GREEN)

tb = sl.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(10), Inches(0.8))
set_text(tb, "Time & Space Complexity", fs=36, color=WHITE, bold=True)
add_bar(sl, Inches(0.8), Inches(1.25), Inches(2.5), Inches(0.04), ACCENT_GREEN)

algos = [
    ("BFS", ACCENT_GREEN, [("Time", "O(V + E)"), ("Space", "O(V)"), ("Best For", "Unweighted shortest path"), ("Used In", "Ford-Fulkerson (Edmonds-Karp)")]),
    ("DFS", ACCENT_PURPLE, [("Time", "O(V + E)"), ("Space", "O(h)"), ("Best For", "Exploration, backtracking"), ("Used In", "Ford-Fulkerson (original)")]),
    ("Bellman-Ford", ACCENT_ORANGE, [("Time", "O(V x E)"), ("Space", "O(V)"), ("Best For", "Shortest path + neg. weights"), ("Unique", "Detects negative cycles")]),
    ("Ford-Fulkerson", ACCENT_BLUE, [("Time", "O(E x max_flow)"), ("Space", "O(V + E)"), ("Best For", "Maximum network flow"), ("Variant", "Edmonds-Karp: O(V x E^2)")]),
]

for i, (name, color, metrics) in enumerate(algos):
    left = 0.35 + i * 3.2
    card = add_shape(sl, Inches(left), Inches(1.65), Inches(3.05), Inches(4.8), CARD_BG, color, Pt(2))
    tf = card.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]; p.text = name; p.font.size = Pt(22); p.font.color.rgb = color; p.font.bold = True; p.font.name = "Calibri"; p.alignment = PP_ALIGN.CENTER
    for label, value in metrics:
        add_para(tf, "", fs=4, color=DARK_BG)
        add_para(tf, label, fs=13, color=LIGHT_GRAY)
        add_para(tf, value, fs=17, color=WHITE, bold=True, align=PP_ALIGN.CENTER)

note = add_shape(sl, Inches(0.35), Inches(6.65), Inches(12.6), Inches(0.55), CARD_BG, CARD_BORDER, Pt(1))
set_text(note, "V = Vertices  |  E = Edges  |  h = Max depth  |  Bellman-Ford is slower than Dijkstra but handles negative weights",
         fs=13, color=LIGHT_GRAY, align=PP_ALIGN.CENTER)


# =================================================================
# SLIDE 14 — REAL WORLD APPLICATIONS
# =================================================================
sl = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(sl, DARK_BG)
add_bar(sl, Inches(0), Inches(0), SW, Inches(0.06), ACCENT_PURPLE)

tb = sl.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(10), Inches(0.8))
set_text(tb, "Real-World Applications", fs=36, color=WHITE, bold=True)
add_bar(sl, Inches(0.8), Inches(1.25), Inches(2.5), Inches(0.04), ACCENT_PURPLE)

apps = [
    ("Bellman-Ford Applications", ACCENT_ORANGE, [
        "Network routing -- RIP protocol",
        "Currency exchange -- detect arbitrage",
        "  (negative cycles = profit loop!)",
        "GPS navigation with toll roads",
        "Financial modeling with losses",
        "Detecting economic fraud cycles",
    ]),
    ("Ford-Fulkerson Applications", ACCENT_BLUE, [
        "Network bandwidth optimization",
        "Water/oil pipeline flow planning",
        "Airline scheduling & seat allocation",
        "Bipartite matching (job assignment)",
        "Image segmentation in computer vision",
        "Baseball elimination problem",
    ]),
]

for i, (title, color, items) in enumerate(apps):
    left = 0.5 + i * 6.3
    card = add_shape(sl, Inches(left), Inches(1.65), Inches(5.8), Inches(5.2), CARD_BG, color, Pt(2))
    tf = card.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]; p.text = title; p.font.size = Pt(22); p.font.color.rgb = color; p.font.bold = True; p.font.name = "Calibri"
    for item in items:
        add_para(tf, "", fs=4, color=DARK_BG)
        bullet(tf, item, fs=16)


# =================================================================
# SLIDE 15 — PSEUDOCODE COMPARISON
# =================================================================
sl = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(sl, DARK_BG)
add_bar(sl, Inches(0), Inches(0), SW, Inches(0.06), ACCENT_BLUE)

tb = sl.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(10), Inches(0.8))
set_text(tb, "Pseudocode -- Side by Side", fs=36, color=WHITE, bold=True)
add_bar(sl, Inches(0.8), Inches(1.25), Inches(2.5), Inches(0.04), ACCENT_BLUE)

# Bellman-Ford
card1 = add_shape(sl, Inches(0.5), Inches(1.6), Inches(6.0), Inches(5.4), RGBColor(0x1A, 0x15, 0x0D), ACCENT_ORANGE, Pt(1.5))
tf1 = card1.text_frame; tf1.word_wrap = True
p = tf1.paragraphs[0]; p.text = "Bellman-Ford"; p.font.size = Pt(20); p.font.color.rgb = ACCENT_ORANGE; p.font.bold = True; p.font.name = "Consolas"
code_bf = [
    "BellmanFord(graph, source):",
    "  dist = {v: INF for all v}",
    "  dist[source] = 0",
    "",
    "  for i = 1 to V-1:",
    "    for each edge (u, v, w):",
    "      if dist[u] + w < dist[v]:",
    "        dist[v] = dist[u] + w",
    "",
    "  // Negative cycle detection",
    "  for each edge (u, v, w):",
    "    if dist[u] + w < dist[v]:",
    "      REPORT negative cycle!",
    "",
    "  return dist[]",
]
for line in code_bf:
    add_para(tf1, line, fs=12, color=LIGHT_GRAY, font="Consolas")

# Ford-Fulkerson
card2 = add_shape(sl, Inches(6.8), Inches(1.6), Inches(6.0), Inches(5.4), RGBColor(0x0D, 0x15, 0x1A), ACCENT_BLUE, Pt(1.5))
tf2 = card2.text_frame; tf2.word_wrap = True
p = tf2.paragraphs[0]; p.text = "Ford-Fulkerson"; p.font.size = Pt(20); p.font.color.rgb = ACCENT_BLUE; p.font.bold = True; p.font.name = "Consolas"
code_ff = [
    "FordFulkerson(graph, S, T):",
    "  max_flow = 0",
    "  residual = copy(graph)",
    "",
    "  while path = BFS(residual, S, T):",
    "    // Find bottleneck capacity",
    "    bottleneck = min capacity on path",
    "",
    "    // Update residual graph",
    "    for each edge (u,v) in path:",
    "      residual[u][v] -= bottleneck",
    "      residual[v][u] += bottleneck",
    "",
    "    max_flow += bottleneck",
    "",
    "  return max_flow",
]
for line in code_ff:
    add_para(tf2, line, fs=12, color=LIGHT_GRAY, font="Consolas")


# =================================================================
# SLIDE 16 — WHEN TO USE WHICH
# =================================================================
sl = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(sl, DARK_BG)
add_bar(sl, Inches(0), Inches(0), SW, Inches(0.06), ACCENT_PINK)

tb = sl.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(11), Inches(0.8))
set_text(tb, "Decision Guide -- Which Algorithm to Use?", fs=34, color=WHITE, bold=True)
add_bar(sl, Inches(0.8), Inches(1.25), Inches(2.5), Inches(0.04), ACCENT_PINK)

decisions = [
    ("What is your problem?", ACCENT_BLUE, 1.7,
     "Finding shortest distance?", ACCENT_ORANGE,
     "Maximizing flow / throughput?", ACCENT_BLUE),
    ("Shortest path details:", ACCENT_ORANGE, 2.8,
     "Negative weights? -> Bellman-Ford", ACCENT_ORANGE,
     "No negatives? -> Dijkstra (faster)", ACCENT_GREEN),
    ("Max flow details:", ACCENT_BLUE, 3.9,
     "Want guaranteed poly runtime? -> Edmonds-Karp (BFS)", ACCENT_BLUE,
     "Integer capacities? -> Ford-Fulkerson (DFS) is fine", ACCENT_PURPLE),
    ("Need BOTH cost + flow?", ACCENT_PINK, 5.0,
     "Min-Cost Max-Flow: use Bellman-Ford INSIDE Ford-Fulkerson!", ACCENT_GREEN,
     "This combines both algorithms together", ACCENT_GREEN),
]

for question, qcolor, y, ans_l, lcolor, ans_r, rcolor in decisions:
    qbox = add_shape(sl, Inches(0.4), Inches(y), Inches(3.5), Inches(0.85), CARD_BG, qcolor, Pt(2))
    set_text(qbox, question, fs=15, color=qcolor, bold=True, align=PP_ALIGN.CENTER)
    a1 = add_shape(sl, Inches(4.1), Inches(y), Inches(4.3), Inches(0.85), CARD_BG, CARD_BORDER, Pt(1))
    set_text(a1, ans_l, fs=13, color=lcolor, align=PP_ALIGN.CENTER)
    a2 = add_shape(sl, Inches(8.6), Inches(y), Inches(4.3), Inches(0.85), CARD_BG, CARD_BORDER, Pt(1))
    set_text(a2, ans_r, fs=13, color=rcolor, align=PP_ALIGN.CENTER)

summary = add_shape(sl, Inches(0.4), Inches(6.1), Inches(12.5), Inches(1.0), RGBColor(0x0A, 0x1A, 0x2A), ACCENT_GREEN, Pt(1))
tf = summary.text_frame; tf.word_wrap = True
p = tf.paragraphs[0]; p.text = "Bottom Line"; p.font.size = Pt(18); p.font.color.rgb = ACCENT_GREEN; p.font.bold = True; p.font.name = "Calibri"; p.alignment = PP_ALIGN.CENTER
add_para(tf, "Bellman-Ford = shortest path (even with negative weights)  |  Ford-Fulkerson = maximum flow  |  They are NOT interchangeable!",
         fs=15, color=WHITE, align=PP_ALIGN.CENTER)


# =================================================================
# SLIDE 17 — SUMMARY & KEY TAKEAWAYS
# =================================================================
sl = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(sl, DARK_BG)
add_bar(sl, Inches(0), Inches(0), SW, Inches(0.06), ACCENT_GREEN)

tb = sl.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(10), Inches(0.8))
set_text(tb, "Summary & Key Takeaways", fs=36, color=WHITE, bold=True)
add_bar(sl, Inches(0.8), Inches(1.25), Inches(2.5), Inches(0.04), ACCENT_GREEN)

takeaways = [
    ("1", "BFS (Queue) and DFS (Stack) are fundamental graph traversal algorithms -- building blocks for everything", ACCENT_GREEN),
    ("2", "Bellman-Ford solves the SHORTEST PATH problem using edge relaxation (V-1 iterations)", ACCENT_ORANGE),
    ("3", "Ford-Fulkerson solves the MAXIMUM FLOW problem using augmenting paths + residual graphs", ACCENT_BLUE),
    ("4", "Bellman-Ford handles negative edge weights and detects negative cycles -- Dijkstra cannot", ACCENT_ORANGE),
    ("5", "Ford-Fulkerson uses BFS (Edmonds-Karp) or DFS internally to find augmenting paths", ACCENT_BLUE),
    ("6", "They solve DIFFERENT problems -- you CANNOT replace one with the other", ACCENT_RED),
    ("7", "However, they CAN work together in Min-Cost Max-Flow (Bellman-Ford inside Ford-Fulkerson)", ACCENT_GREEN),
    ("8", "Choose based on your PROBLEM: distance minimization -> Bellman-Ford; flow maximization -> Ford-Fulkerson", ACCENT_PINK),
]

for i, (num, text, color) in enumerate(takeaways):
    y = 1.55 + i * 0.64
    c = add_circle(sl, Inches(0.7), Inches(y + 0.05), Inches(0.38), color)
    set_text(c, num, fs=13, color=WHITE, bold=True, align=PP_ALIGN.CENTER)
    tb = sl.shapes.add_textbox(Inches(1.3), Inches(y + 0.05), Inches(11.5), Inches(0.5))
    set_text(tb, text, fs=15, color=WHITE)


# =================================================================
# SLIDE 18 — THANK YOU
# =================================================================
sl = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(sl, DARK_BG)
add_bar(sl, Inches(0), Inches(0), SW, Inches(0.06), ACCENT_BLUE)

add_circle(sl, Inches(1.0), Inches(1.5), Inches(3.0), ACCENT_PURPLE)
add_circle(sl, Inches(9.5), Inches(4.0), Inches(2.5), ACCENT_BLUE)
add_circle(sl, Inches(0.5), Inches(5.0), Inches(1.5), ACCENT_ORANGE)

tb = sl.shapes.add_textbox(Inches(2), Inches(2.5), Inches(9), Inches(1.5))
tf = tb.text_frame; tf.word_wrap = True
p = tf.paragraphs[0]; p.text = "Thank You!"; p.font.size = Pt(56); p.font.color.rgb = WHITE; p.font.bold = True; p.font.name = "Calibri"; p.alignment = PP_ALIGN.CENTER

add_bar(sl, Inches(5), Inches(4.1), Inches(3.3), Inches(0.05), ACCENT_BLUE)

tb = sl.shapes.add_textbox(Inches(2), Inches(4.4), Inches(9), Inches(0.8))
tf = tb.text_frame; tf.word_wrap = True
p = tf.paragraphs[0]; p.text = "Bellman-Ford  vs  Ford-Fulkerson"; p.font.size = Pt(22); p.font.color.rgb = ACCENT_BLUE; p.font.name = "Calibri"; p.alignment = PP_ALIGN.CENTER

tb = sl.shapes.add_textbox(Inches(2), Inches(5.5), Inches(9), Inches(0.8))
tf = tb.text_frame; tf.word_wrap = True
p = tf.paragraphs[0]; p.text = "Presented by: Mihir & Ahana"; p.font.size = Pt(16); p.font.color.rgb = LIGHT_GRAY; p.font.name = "Calibri"; p.alignment = PP_ALIGN.CENTER
add_para(tf, "Questions? Let's discuss!", fs=14, color=LIGHT_GRAY, align=PP_ALIGN.CENTER)


# ─── SAVE ────────────────────────────────────────────────────────────
output = r"d:\MedicalChatbot\Graph_Algorithms_BellmanFord_vs_FordFulkerson.pptx"
prs.save(output)
print("Presentation saved to:", output)
print("Total slides:", len(prs.slides))
