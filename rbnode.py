from process import Process

RED = "RED"
BLACK = "BLACK"

class RBNode:
    """
    Nodo de un arbol rojo-negro.
    Incluye puntero al padre y color, que son necesarios para el balanceo.
    Los nodos NIL se representan con process = None y color negro.
    """

    def __init__(self, process: Process | None = None, color: str = RED):
        self.process: Process | None = process
        self.left: RBNode | None = None
        self.right: RBNode | None = None
        self.parent: RBNode | None = None
        self.color: str = color

    @property
    def is_nil(self) -> bool:
        """Indica si el nodo es un centinela NIL."""
        return self.process is None

    def __repr__(self) -> str:
        if self.is_nil:
            return "RBNode(NIL, BLACK)"
        return f"RBNode({self.process}, {self.color})"
