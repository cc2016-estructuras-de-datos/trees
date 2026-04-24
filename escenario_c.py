"""
Paso 6 - Escenario C: Proceso Frecuente de I/O
- Inserta 1000 procesos con vruntime aleatorio en SplayTree y RedBlackTree
- Busca el mismo proceso 50 veces seguidas en ambos árboles
- Registra iteraciones por búsqueda y grafica la comparación
"""

import random
import sys
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

sys.path.insert(0, '.')
from process import Process
from splaytree import SplayTree
from redblacktree import RedBlackTree

SEED       = 42
N          = 1000
N_SEARCHES = 50
OUTPUT_DIR = "escenario_c"

random.seed(SEED)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# -----------------------------------------------------------------------
# 1. Generar 1000 procesos con vruntime aleatorio (mismo seed que Escenario A)
# -----------------------------------------------------------------------
processes = [
    Process(pid=i, vruntime=round(random.uniform(0, 10_000.0), 4))
    for i in range(1, N + 1)
]

# -----------------------------------------------------------------------
# 2. Insertar en Splay Tree y Red-Black Tree
# -----------------------------------------------------------------------
splay = SplayTree()
rbt   = RedBlackTree()

for p in processes:
    splay.insert(p)
    rbt.insert(p)

print(f"Insertados {N} procesos en Splay Tree y Red-Black Tree.")

# -----------------------------------------------------------------------
# 3. Elegir un proceso frecuente (simula proceso de I/O que regresa
#    constantemente a ready). Usamos el proceso 500 como ejemplo central.
# -----------------------------------------------------------------------
frequent_process = processes[499]  # pid=500
print(f"\nProceso frecuente: pid={frequent_process.pid}, vruntime={frequent_process.vruntime}")

# -----------------------------------------------------------------------
# 4. Buscar el mismo proceso 50 veces seguidas en ambos árboles
# -----------------------------------------------------------------------
splay_iters = []
rbt_iters   = []

for i in range(N_SEARCHES):
    _, s = splay.search(frequent_process.vruntime)
    _, r = rbt.search(frequent_process.vruntime)
    splay_iters.append(s)
    rbt_iters.append(r)

avg_splay = sum(splay_iters) / N_SEARCHES
avg_rbt   = sum(rbt_iters)   / N_SEARCHES

print(f"\nEscenario C — Iteraciones promedio ({N_SEARCHES} búsquedas del mismo proceso):")
print(f"  Splay Tree     : {avg_splay:.2f}")
print(f"  Red-Black Tree : {avg_rbt:.2f}")
print(f"\nDetalle por búsqueda:")
print(f"  Splay  — búsqueda 1: {splay_iters[0]}, búsqueda 2: {splay_iters[1]}, resto: {splay_iters[2]}")
print(f"  RBT    — búsqueda 1: {rbt_iters[0]}, búsqueda 2: {rbt_iters[1]}, búsqueda 50: {rbt_iters[49]}")

# -----------------------------------------------------------------------
# 5. Gráfica comparativa
# -----------------------------------------------------------------------
x = list(range(1, N_SEARCHES + 1))

fig, axes = plt.subplots(2, 1, figsize=(12, 8), sharex=True)
fig.suptitle(
    "Escenario C — Búsqueda repetida del mismo proceso (50 veces, N=1000)",
    fontsize=13, fontweight='bold'
)

# Splay Tree
axes[0].bar(x, splay_iters, color='#DD8452', alpha=0.8, width=0.7)
axes[0].axhline(avg_splay, color='black', linewidth=1.5, linestyle='--',
                label=f'Promedio: {avg_splay:.2f}')
axes[0].set_title('Splay Tree', fontsize=11, fontweight='bold')
axes[0].set_ylabel('Iteraciones', fontsize=9)
axes[0].legend(fontsize=9)
axes[0].set_ylim(0, max(splay_iters) * 1.3)
axes[0].grid(axis='y', alpha=0.3)
# Annotate first bar
axes[0].annotate(f'{splay_iters[0]}',
                 xy=(1, splay_iters[0]), xytext=(4, splay_iters[0] * 0.85),
                 fontsize=9, color='darkred', fontweight='bold',
                 arrowprops=dict(arrowstyle='->', color='darkred'))

# Red-Black Tree
axes[1].bar(x, rbt_iters, color='#55A868', alpha=0.8, width=0.7)
axes[1].axhline(avg_rbt, color='black', linewidth=1.5, linestyle='--',
                label=f'Promedio: {avg_rbt:.2f}')
axes[1].set_title('Red-Black Tree', fontsize=11, fontweight='bold')
axes[1].set_ylabel('Iteraciones', fontsize=9)
axes[1].set_xlabel('Búsqueda #', fontsize=10)
axes[1].legend(fontsize=9)
axes[1].set_ylim(0, max(rbt_iters) * 1.3)
axes[1].grid(axis='y', alpha=0.3)

plt.tight_layout()
chart_path = os.path.join(OUTPUT_DIR, "escenario_c_iteraciones.png")
plt.savefig(chart_path, dpi=150, bbox_inches='tight')
plt.close()
print(f"\nGráfica guardada: {chart_path}")