"""
Paso 5 - Escenario B: Llegada Secuencial (El peor caso)
- Inserta 1000 procesos con vruntime secuencial (1, 2, ..., 1000)
- Busca el último proceso insertado (el 1000) en las tres estructuras
- Compara la cantidad de iteraciones
- Visualiza los primeros niveles de los árboles para notar la degeneración estructural
"""

import sys
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from graphviz import Digraph

sys.path.insert(0, '.')
from process import Process
from bst import BST
from splaytree import SplayTree
from redblacktree import RedBlackTree

# Aumentamos el límite de recursión por si los métodos de tu BST están implementados 
# de forma recursiva, ya que en este escenario el árbol alcanzará una profundidad de 1000.
sys.setrecursionlimit(2500)

N          = 1000
VIZ_DEPTH  = 5
OUTPUT_DIR = "escenario_b"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# -----------------------------------------------------------------------
# 1. Generar 1000 procesos con vruntime secuencial (1 al 1000)
# -----------------------------------------------------------------------
processes = [
    Process(pid=i, vruntime=float(i))
    for i in range(1, N + 1)
]

# -----------------------------------------------------------------------
# 2. Insertar en los tres árboles
# -----------------------------------------------------------------------
bst   = BST()
splay = SplayTree()
rbt   = RedBlackTree()

for p in processes:
    bst.insert(p)
    splay.insert(p)
    rbt.insert(p)

print(f"Insertados {N} procesos secuenciales en los 3 árboles.")

# -----------------------------------------------------------------------
# 3. Buscar el proceso número 1000 (el peor caso)
# -----------------------------------------------------------------------
vruntime_to_search = 1000.0

_, bst_iters   = bst.search(vruntime_to_search)
_, splay_iters = splay.search(vruntime_to_search)
_, rbt_iters   = rbt.search(vruntime_to_search)

print("\nEscenario B — Iteraciones para encontrar el último proceso (1000):")
print(f"  BST          : {bst_iters}")
print(f"  Splay Tree   : {splay_iters}")
print(f"  Red-Black    : {rbt_iters}")

# -----------------------------------------------------------------------
# 4. Gráfica de barras comparativa
# -----------------------------------------------------------------------
names  = ['BST', 'Splay Tree', 'Red-Black Tree']
iters  = [bst_iters, splay_iters, rbt_iters]
colors = ['#4C72B0', '#DD8452', '#55A868']

plt.figure(figsize=(8, 6))
plt.bar(names, iters, color=colors, alpha=0.8, width=0.5)
plt.title(f"Escenario B: Iteraciones buscando el último proceso (N={N})", fontweight='bold')
plt.ylabel("Iteraciones")
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Agregar el valor de iteraciones encima de cada barra
for i, v in enumerate(iters):
    plt.text(i, v + (max(iters) * 0.02), str(v), ha='center', fontweight='bold', fontsize=10)

plt.tight_layout()
chart_path = os.path.join(OUTPUT_DIR, "escenario_b_iteraciones.png")
plt.savefig(chart_path, dpi=150)
plt.close()
print(f"\nGráfica guardada: {chart_path}")

# -----------------------------------------------------------------------
# 5. Graphviz - primeros VIZ_DEPTH niveles de cada árbol
# -----------------------------------------------------------------------

def viz_bst(tree: BST, depth_limit: int, filename: str) -> None:
    dot = Digraph()
    dot.attr(rankdir='TB')
    dot.attr('node', shape='circle', style='filled', fillcolor='#AED6F1', fontsize='10')

    def add(node, depth):
        if node is None or depth > depth_limit:
            return
        label = f"p{node.process.pid}\n({int(node.process.vruntime)})"
        dot.node(str(id(node)), label=label)
        if node.left and depth < depth_limit:
            dot.edge(str(id(node)), str(id(node.left)))
            add(node.left, depth + 1)
        if node.right and depth < depth_limit:
            dot.edge(str(id(node)), str(id(node.right)))
            add(node.right, depth + 1)

    add(tree.root, 1)
    dot.render(filename, directory=OUTPUT_DIR, format='png', cleanup=True)
    print(f"Árbol guardado: {os.path.join(OUTPUT_DIR, filename)}.png")

def viz_splay(tree: SplayTree, depth_limit: int, filename: str) -> None:
    dot = Digraph()
    dot.attr(rankdir='TB')
    dot.attr('node', shape='circle', style='filled', fillcolor='#A9DFBF', fontsize='10')

    def add(node, depth):
        if node is None or depth > depth_limit:
            return
        label = f"p{node.process.pid}\n({int(node.process.vruntime)})"
        dot.node(str(id(node)), label=label)
        if node.left and depth < depth_limit:
            dot.edge(str(id(node)), str(id(node.left)))
            add(node.left, depth + 1)
        if node.right and depth < depth_limit:
            dot.edge(str(id(node)), str(id(node.right)))
            add(node.right, depth + 1)

    add(tree.root, 1)
    dot.render(filename, directory=OUTPUT_DIR, format='png', cleanup=True)
    print(f"Árbol guardado: {os.path.join(OUTPUT_DIR, filename)}.png")

def viz_rbt(tree: RedBlackTree, depth_limit: int, filename: str) -> None:
    dot = Digraph()
    dot.attr(rankdir='TB')

    def add(node, depth):
        if node is None or node is tree.NIL or depth > depth_limit:
            return
        fill  = '#F1948A' if node.color == "RED" else '#85929E'
        label = f"p{node.process.pid}\n({int(node.process.vruntime)})"
        dot.node(str(id(node)), label=label, style='filled',
                 fillcolor=fill, fontcolor='white', shape='circle',
                 fontsize='10')
        if node.left and node.left is not tree.NIL and depth < depth_limit:
            dot.edge(str(id(node)), str(id(node.left)))
            add(node.left, depth + 1)
        if node.right and node.right is not tree.NIL and depth < depth_limit:
            dot.edge(str(id(node)), str(id(node.right)))
            add(node.right, depth + 1)

    add(tree.root, 1)
    dot.render(filename, directory=OUTPUT_DIR, format='png', cleanup=True)
    print(f"Árbol guardado: {os.path.join(OUTPUT_DIR, filename)}.png")

viz_bst(bst,     VIZ_DEPTH, "tree_bst_b")
viz_splay(splay, VIZ_DEPTH, "tree_splay_b")
viz_rbt(rbt,     VIZ_DEPTH, "tree_rbt_b")