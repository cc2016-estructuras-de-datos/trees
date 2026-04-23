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

    def search(self, pid: int) -> tuple[SplayNode | None, int]:
        """
        Busca un proceso por PID.
        Retorna (node, iterations) — iterations cuenta las comparaciones desde la raiz.
        Despues de una busqueda exitosa, el nodo se sube a la raiz con splay.
        La implementacion completa se agregara en una fase posterior.
        """
        raise NotImplementedError("SplayTree.search() se implementara despues.")