class Chip:
    def __init__(self, type) -> None:
        self.type = type

    def __repr__(self) -> str:
        if self.type == 'skull':
            return '💀'
        elif self.type == 'flower':
            return '🌸'
        else:
            return ValueError("No chip type with name given")