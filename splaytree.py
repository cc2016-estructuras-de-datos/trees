from process import Process
from splaynode import SplayNode

class SplayTree:
    """
    Arbol Splay basado en vruntime.
    En cada acceso, el nodo accedido se rota hasta la raiz (operacion splay).
    Esto da un costo amortizado de O(1) para accesos repetidos al mismo nodo,
    lo que es directamente relevante para el Escenario C (proceso con E/S frecuente).

    search() retorna (node, iterations) para permitir mediciones de rendimiento.
    La logica completa del splay se agregara en una fase posterior.
    """

    def __init__(self):
        self.root: SplayNode | None = None
 
    def _rotate_right(self, node: SplayNode) -> None:
        left_child = node.left
        if left_child is None:
            return
        node.left = left_child.right
        if left_child.right is not None:
            left_child.right.parent = node
        left_child.parent = node.parent
        if node.parent is None:
            self.root = left_child
        elif node is node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child
        left_child.right = node
        node.parent = left_child
 
    def _rotate_left(self, node: SplayNode) -> None:
        right_child = node.right
        if right_child is None:
            return
        node.right = right_child.left
        if right_child.left is not None:
            right_child.left.parent = node
        right_child.parent = node.parent
        if node.parent is None:
            self.root = right_child
        elif node is node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child
        right_child.left = node
        node.parent = right_child
 
    def _splay(self, node: SplayNode) -> None:
        """Sube el nodo a la raíz mediante los casos zig, zig-zig y zig-zag."""
        while node.parent is not None:
            parent = node.parent
            grandparent = parent.parent
            if grandparent is None:
                if node is parent.left:
                    self._rotate_right(parent)
                else:
                    self._rotate_left(parent)
            elif node is parent.left and parent is grandparent.left:
                self._rotate_right(grandparent)
                self._rotate_right(parent)
            elif node is parent.right and parent is grandparent.right:
                self._rotate_left(grandparent)
                self._rotate_left(parent)
            elif node is parent.right and parent is grandparent.left:
                self._rotate_left(parent)
                self._rotate_right(grandparent)
            else:
                self._rotate_right(parent)
                self._rotate_left(grandparent)
 
    def insert(self, process: Process) -> None:
        """Inserta como BST por vruntime y luego sube el nodo nuevo a la raíz."""
        new_node = SplayNode(process)
        if self.root is None:
            self.root = new_node
            return
        current = self.root
        while True:
            if process.vruntime < current.process.vruntime:
                if current.left is None:
                    current.left = new_node
                    new_node.parent = current
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    new_node.parent = current
                    break
                current = current.right
        self._splay(new_node)

    def search(self, vruntime: float) -> tuple[SplayNode | None, int]:
        """
        Busca un proceso por vruntime.
        Retorna (node, iterations) — iterations cuenta las comparaciones desde la raiz.
        Despues de una busqueda exitosa, el nodo se sube a la raiz con splay.
        La implementacion completa se agregara en una fase posterior.
        """
        iterations = 0
        current = self.root
        found_node: SplayNode | None = None
 
        while current is not None:
            iterations += 1
            if vruntime == current.process.vruntime:
                found_node = current
                break
            elif vruntime < current.process.vruntime:
                current = current.left
            else:
                current = current.right
 
        if found_node is not None:
            self._splay(found_node)
 
        return found_node, iterations