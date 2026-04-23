from process import Process


class BSTNode:
    """Nodo de un arbol binario de busqueda."""

    def __init__(self, process: Process):
        self.process: Process = process
        self.left: BSTNode | None = None
        self.right: BSTNode | None = None

    def __repr__(self) -> str:
        return f"BSTNode({self.process})"