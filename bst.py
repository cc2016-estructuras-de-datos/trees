from process import Process
from bstnode import BSTNode

class BST:
    """
    Arbol binario de busqueda indexado por vruntime.
    search() retorna (node, iterations) para permitir mediciones de rendimiento.
    La logica completa de insercion se agregara en una fase posterior.
    """
 
    def __init__(self):
        self.root: BSTNode | None = None
 
    def insert(self, process: Process) -> None:
        """Inserta un proceso en el árbol basado en su vruntime."""
        new_node = BSTNode(process)
        if self.root is None:
            self.root = new_node
            return
        current = self.root
        while True:
            if process.vruntime < current.process.vruntime:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right
 
    def search(self, vruntime: float) -> tuple[BSTNode | None, int]:
        """
        Busca un proceso por vruntime.
        Retorna (node, iterations) — iterations cuenta las comparaciones desde la raiz.
        La implementacion completa se agregara en una fase posterior.
        """
        iterations = 0
        current = self.root
 
        while current is not None:
            iterations += 1
            if vruntime == current.process.vruntime:
                return current, iterations
            elif vruntime < current.process.vruntime:
                current = current.left
            else:
                current = current.right
 
        return None, iterations