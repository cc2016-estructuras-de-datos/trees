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
        """Inserta un proceso. La implementacion completa se agregara en la siguiente fase."""
        raise NotImplementedError("BST.insert() se implementara despues.")
 
    def search(self, pid: int) -> tuple[BSTNode | None, int]:
        """
        Busca un proceso por PID.
        Retorna (node, iterations) — iterations cuenta las comparaciones desde la raiz.
        La implementacion completa se agregara en una fase posterior.
        """
        raise NotImplementedError("BST.search() se implementara despues.")