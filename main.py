class Human:
    def __init__(
            self,
            eyes: str = "blue",
            mouses: int = 5,
    ):
        self.eyes = eyes
        self.mouses = mouses
yuka = Human(eyes = "brown",mouses = 1)
print(yuka.mouses)  # Output: blue
