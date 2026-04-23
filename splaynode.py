from process import Process

class SplayNode:
    """
    Nodo de un arbol Splay.
    Incluye un puntero al padre, que es necesario para las rotaciones splay.
    """

    def __init__(self, process: Process):
        self.process: Process = process
        self.left: SplayNode | None = None
        self.right: SplayNode | None = None
        self.parent: SplayNode | None = None

    def __repr__(self) -> str:
        return f"SplayNode({self.process})"
