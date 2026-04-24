"""
Paso 4 - Escenario A: Llegada Aleatoria
- Inserta 1000 procesos con vruntime aleatorio en BST, SplayTree y RedBlackTree
- Visualiza los primeros VIZ_DEPTH niveles de cada árbol con Graphviz
- Busca 100 procesos al azar (garantizados en el árbol) por vruntime
- Grafica iteraciones por búsqueda y promedio para los 3 árboles
"""

import random
import math
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

SEED       = 42
N          = 1000
N_SEARCH   = 100
VIZ_DEPTH  = 5
OUTPUT_DIR = "escenario_a"

random.seed(SEED)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# -----------------------------------------------------------------------
# 1. Generar 1000 procesos con vruntime aleatorio
# -----------------------------------------------------------------------
processes = [
    Process(pid=i, vruntime=round(random.uniform(0, 10_000.0), 4))
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

print(f"Insertados {N} procesos en los 3 árboles.")

# -----------------------------------------------------------------------
# 3. Seleccionar 100 procesos aleatorios garantizados en los árboles
# -----------------------------------------------------------------------
search_sample = random.sample(processes, N_SEARCH)

# -----------------------------------------------------------------------
# 4. Buscar por vruntime y registrar iteraciones
# -----------------------------------------------------------------------
bst_iters, splay_iters, rbt_iters = [], [], []

for p in search_sample:
    _, b = bst.search(p.vruntime)
    _, s = splay.search(p.vruntime)
    _, r = rbt.search(p.vruntime)
    bst_iters.append(b)
    splay_iters.append(s)
    rbt_iters.append(r)

avg_bst   = sum(bst_iters)   / N_SEARCH
avg_splay = sum(splay_iters) / N_SEARCH
avg_rbt   = sum(rbt_iters)   / N_SEARCH
log_n     = math.log2(N)

print(f"\nEscenario A — Promedio de iteraciones ({N_SEARCH} búsquedas):")
print(f"  BST          : {avg_bst:.2f}")
print(f"  Splay Tree   : {avg_splay:.2f}")
print(f"  Red-Black    : {avg_rbt:.2f}")
print(f"  O(log₂ 1000) : {log_n:.2f}  (referencia teórica)")

# -----------------------------------------------------------------------
# 5. Gráfica de barras - iteraciones por búsqueda
# -----------------------------------------------------------------------
x      = list(range(1, N_SEARCH + 1))
colors = ['#4C72B0', '#DD8452', '#55A868']
names  = ['BST', 'Splay Tree', 'Red-Black Tree']
iters  = [bst_iters, splay_iters, rbt_iters]
avgs   = [avg_bst, avg_splay, avg_rbt]

fig, axes = plt.subplots(3, 1, figsize=(14, 11), sharex=True)
fig.suptitle(
    "Escenario A — Iteraciones por búsqueda (100 procesos aleatorios, N=1000)",
    fontsize=13, fontweight='bold'
)

for ax, color, name, data, avg in zip(axes, colors, names, iters, avgs):
    ax.bar(x, data, color=color, alpha=0.75, width=0.8)
    ax.axhline(avg,   color='black',   linewidth=1.5, linestyle='--',
               label=f'Promedio: {avg:.1f}')
    ax.axhline(log_n, color='crimson', linewidth=1.2, linestyle=':',
               label=f'O(log₂n) ≈ {log_n:.1f}')
    ax.set_ylabel("Iteraciones", fontsize=9)
    ax.set_title(name, fontsize=10, fontweight='bold')
    ax.legend(fontsize=8, loc='upper right')
    ax.set_ylim(0, max(data) * 1.2)
    ax.grid(axis='y', alpha=0.3)

axes[-1].set_xlabel("Búsqueda #", fontsize=10)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "escenario_a_iteraciones.png"), dpi=150, bbox_inches='tight')
plt.close()
print(f"\nGráfica guardada: {os.path.join(OUTPUT_DIR, 'escenario_a_iteraciones.png')}")

# -----------------------------------------------------------------------
# 6. Graphviz - primeros VIZ_DEPTH niveles de cada árbol
# -----------------------------------------------------------------------

def viz_bst(tree: BST, depth_limit: int, filename: str) -> None:
    dot = Digraph()
    dot.attr(rankdir='TB')
    dot.attr('node', shape='circle', style='filled', fillcolor='#AED6F1',
             fontsize='10')

    def add(node, depth):
        if node is None or depth > depth_limit:
            return
        label = f"p{node.process.pid}"
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
    dot.attr('node', shape='circle', style='filled', fillcolor='#A9DFBF',
             fontsize='10')

    def add(node, depth):
        if node is None or depth > depth_limit:
            return
        label = f"p{node.process.pid}"
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
        label = f"p{node.process.pid}"
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


viz_bst(bst,     VIZ_DEPTH, "tree_bst_a")
viz_splay(splay, VIZ_DEPTH, "tree_splay_a")
viz_rbt(rbt,     VIZ_DEPTH, "tree_rbt_a")