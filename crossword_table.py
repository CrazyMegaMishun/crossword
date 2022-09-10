"""отрисовать матрицу 5х5 с координатами в каждой клетке
    потом наполнить словами"""

from tabulate import tabulate
from сell import Cell


class CrosswordTable:
    def __init__(self):
        self.table = self.create_table()

    def create_table(self):
        table = []
        for x in range(1, 6):
            for y in range(1, 6):
                table.append(Cell(x, y, '_'))
        return table

    def visualize_table(self, table):
        

    def word_fill(self):
        pass


if __name__ == '__main__':
    t = CrosswordTable()
    print(t.visualize_table(t.table))
