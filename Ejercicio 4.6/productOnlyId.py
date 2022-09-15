class ProductOnlyId():
    _id: int
    _nombre: str = ""
    _precio: float = 0
    _stock: int = 0

    def __init__(self, id: int) -> None:
        self._id = id
