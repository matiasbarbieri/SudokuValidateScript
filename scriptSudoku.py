"""
This script determinate if a 9 x 9 Sudoku board is valid or not.

"""


#ejemplo de tablero
board = [
 ["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]
]

class Solution:
    def __init__(self, board):
        self.board = board
        self.lista = list()

    def chequeo_general(self):
        assert len(self.board) == 9, "El tablero no tiene 9 filas" # Chequeo que el tablero tenga 9 filas
        for fila in self.board:
            assert len(fila) == 9, "La fila no tiene 9 columnas" # Chequeo que cada fila tenga 9 columnas
            for columna in fila:
                assert columna in "123456789.", "La columna no es un numero entre 1 y 9" # Chequeo que cada columna sea un numero entre 1 y 9

    def chequeo_filas(self):
        for fila in self.board:
            for elemento in fila:
                if elemento != ".":
                    assert fila.count(elemento) == 1, "Hay un numero repetido en la fila" # Chequeo que no haya numeros repetidos en las filas
    
    def chequeo_columnas(self):
        for columna in range(9):
            lista = list()
            for fila in self.board:
                lista.append(fila[columna])
            for elemento in lista:
                if elemento != ".":
                    assert lista.count(elemento) == 1, "Hay un numero repetido en la columna"

    def chequeo_cuadros(self):
        for fila in range(0, 9, 3):
            for columna in range(0, 9, 3):
                lista = list()
                for i in range(3):
                    for j in range(3):
                        lista.append(self.board[fila+i][columna+j])
                for elemento in lista:
                    if elemento != ".":
                        assert lista.count(elemento) == 1, "Hay un numero repetido en el cuadro"

if __name__ == "__main__":
    sudoku = Solution(board)
    sudoku.chequeo_general()
    sudoku.chequeo_filas()
    sudoku.chequeo_columnas()
    sudoku.chequeo_cuadros()
    print("Is Valid")