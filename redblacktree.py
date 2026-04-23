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
        # Centinela NIL: hoja negra compartida usada en lugar de None.
        self.NIL: RBNode = RBNode(process=None, color=BLACK)
        self.root: RBNode = self.NIL
 
    def insert(self, process: Process) -> None:
        """Inserta un proceso. La implementacion completa con ajuste se agregara en la siguiente fase."""
        raise NotImplementedError(
            "RedBlackTree.insert() con rotaciones se implementara despues."
        )
 
    def search(self, vruntime: float) -> tuple[RBNode | None, int]:
        """
        Busca un proceso por PID.
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