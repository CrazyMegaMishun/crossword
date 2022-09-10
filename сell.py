class Cell:
    def __init__(self, x_coordinate, y_coordinate, letter):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.letter = letter

    def __str__(self):
        return f'{self.x_coordinate, self.y_coordinate}'

    def __repr__(self):
        return self.__str__()
