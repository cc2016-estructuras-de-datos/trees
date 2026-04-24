# Hoja de Trabajo 8: Árboles y Sistemas Operativos

## Integrantes

- Weslly Cabrera — 25771
- Brian Bolaños — 24846

## Propósito

Este proyecto simula y compara el comportamiento de tres estructuras de datos de árboles de búsqueda, BST, Splay Tree y Red-Black Tree, en el contexto de la gestión de procesos de un sistema operativo. Se modela el concepto de vruntime utilizado por el Completely Fair Scheduler de Linux para analizar empíricamente cómo cada árbol responde ante diferentes patrones de carga: inserción aleatoria, inserción secuencial y acceso repetido al mismo proceso.

## Estructura del proyecto

```
├── process.py     # Clase Process (pid, vruntime)
├── bst_node.py    # Nodo del BST
├── splay_node.py  # Nodo del Splay Tree
├── rb_node.py     # Nodo del Red-Black Tree
├── bst.py         # Binary Search Tree
├── splay_tree.py  # Splay Tree
|── red_black_tree.py  # Red-Black Tree
├── escenario_a.py          # Escenario A: 1000 procesos con vruntime aleatorio
├── escenario_b.py          # Escenario B: 1000 procesos con vruntime secuencial (peor caso del BST)
├── escenario_c.py          # Escenario C: búsqueda repetida del mismo proceso
├── escenario_a/           # Imágenes y gráficas generadas del Escenario A
├── escenario_b/           # Imágenes y gráficas generadas del Escenario B
|── escenario_c/           # Gráficas generadas del Escenario C
├── README.md
```

## Requisitos

- Python 3.10 o superior
- graphviz (sistema): `sudo apt install graphviz` o `brew install graphviz`

Instalar dependencias de Python:

```bash
pip install graphviz matplotlib
```

## Cómo ejecutar

Desde la raíz del proyecto:

```bash
# Escenario A: inserción aleatoria, visualización y benchmarking
python scenario_a.py

# Escenario B: inserción secuencial, peor caso del BST
python scenario_b.py

# Escenario C: proceso frecuente de I/O, búsqueda repetida
python scenario_c.py
```

Cada script genera automáticamente sus imágenes y gráficas dentro de su carpeta correspondiente.

## Referencia

Documentación oficial del kernel de Linux sobre el CFS Scheduler:
https://www.kernel.org/doc/html/latest/scheduler/sched-design-CFS.html
