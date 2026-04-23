class Process:
    """
    Representa un proceso del sistema operativo con un PID y un tiempo de ejecucion virtual (vruntime).
    vruntime es la clave que usa CFS para determinar el orden de planificacion.
    """

    def __init__(self, pid: int, vruntime: float):
        self.pid = pid
        self.vruntime = vruntime

    def __repr__(self) -> str:
        return f"Process(pid={self.pid}, vruntime={self.vruntime:.4f})"