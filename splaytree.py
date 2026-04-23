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

    def insert(self, process: Process) -> None:
        """Inserta un proceso. La implementacion completa se agregara en la siguiente fase."""
        raise NotImplementedError("SplayTree.insert() se implementara despues.")

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