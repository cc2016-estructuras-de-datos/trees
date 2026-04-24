from process import Process
from rbnode import RBNode, RED, BLACK

class RedBlackTree:
    """
        Arbol rojo-negro indexado por vruntime.
        Esta es la estructura de datos usada por el planificador CFS de Linux (rb_root).
 
        Garantiza O(log n) en el peor caso para insercion y busqueda mediante
        invariantes estrictas de balanceo basadas en colores:
            1. Todo nodo es ROJO o NEGRO.
            2. La raiz es NEGRA.
            3. Las hojas NIL son NEGRAS.
            4. Los nodos ROJOS solo tienen hijos NEGROS.
            5. Todos los caminos desde un nodo hasta sus descendientes NIL tienen la misma profundidad NEGRA.
 
        search() retorna (node, iterations) para permitir mediciones de rendimiento.
        La logica completa de rotaciones y ajuste se agregara en una fase posterior.
    """
 
    def __init__(self):
        self.NIL: RBNode = RBNode(process=None, color=BLACK)
        self.root: RBNode = self.NIL
 
    def _rotate_left(self, node: RBNode) -> None:
        right_child = node.right
        node.right = right_child.left
        if right_child.left is not self.NIL:
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
 
    def _rotate_right(self, node: RBNode) -> None:
        left_child = node.left
        node.left = left_child.right
        if left_child.right is not self.NIL:
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
 
    def _insert_fixup(self, node: RBNode) -> None:
        """Restaura las invariantes del árbol rojo-negro después de la inserción."""
        while node.parent is not None and node.parent.color == RED:
            parent = node.parent
            grandparent = parent.parent
            if grandparent is None:
                break
            if parent is grandparent.left:
                uncle = grandparent.right
                if uncle.color == RED:
                    parent.color = BLACK
                    uncle.color = BLACK
                    grandparent.color = RED
                    node = grandparent
                else:
                    if node is parent.right:
                        node = parent
                        self._rotate_left(node)
                        parent = node.parent
                        grandparent = parent.parent
                    parent.color = BLACK
                    grandparent.color = RED
                    self._rotate_right(grandparent)
            else:
                uncle = grandparent.left
                if uncle.color == RED:
                    parent.color = BLACK
                    uncle.color = BLACK
                    grandparent.color = RED
                    node = grandparent
                else:
                    if node is parent.left:
                        node = parent
                        self._rotate_right(node)
                        parent = node.parent
                        grandparent = parent.parent
                    parent.color = BLACK
                    grandparent.color = RED
                    self._rotate_left(grandparent)
        self.root.color = BLACK
 
    def insert(self, process: Process) -> None:
        """Inserta un proceso en el árbol basado en su vruntime, manteniendo las propiedades"""
        new_node = RBNode(process, color=RED)
        new_node.left = self.NIL
        new_node.right = self.NIL
 
        parent: RBNode | None = None
        current = self.root
 
        while current is not self.NIL:
            parent = current
            if process.vruntime < current.process.vruntime:
                current = current.left
            else:
                current = current.right
 
        new_node.parent = parent
 
        if parent is None:
            self.root = new_node
        elif process.vruntime < parent.process.vruntime:
            parent.left = new_node
        else:
            parent.right = new_node
 
        if new_node.parent is None:
            new_node.color = BLACK
            return
        if new_node.parent.parent is None:
            return
 
        self._insert_fixup(new_node)
 
    def search(self, vruntime: float) -> tuple[RBNode | None, int]:
        """
        Busca un proceso por vruntime.
        Retorna (node, iterations) — iterations cuenta las comparaciones desde la raiz.
        La implementacion completa se agregara en una fase posterior.
        """
        iterations = 0
        current = self.root
 
        while current is not self.NIL and current is not None:
            iterations += 1
            if vruntime == current.process.vruntime:
                return current, iterations
            elif vruntime < current.process.vruntime:
                current = current.left
            else:
                current = current.right
 
        return None, iterations