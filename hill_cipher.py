from matrices import *

def hill_cipher(message: str, key: list[list[float]]) -> str:

if __name__ == '__main__':
    key: list[list[float]] = [[2, 3], [4, 5]]
    message = 'ATTACKATDAWN'
    print(hill_cipher(message, key))