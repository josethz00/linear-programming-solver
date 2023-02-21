from matrices import *

substitutions = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26
}

def hill_cipher_encrypt(message: str, key: list[list[float]]) -> str:
    three_chunk_blocks: list[str] = []
    three_chunk_accumulator = 0
    current_block = ''

    message = message.replace(' ', '').lower() # remove spaces and convert to lowercase

    for index in range(len(message)): # split message into blocks of 3 and convert to the corresponding alphabet number
        three_chunk_accumulator +=1
        current_block = current_block + ',' + str(substitutions[message[index]]) if current_block != '' else str(substitutions[message[index]])
        # add to current block and prevent adding a comma to the first character

        if three_chunk_accumulator == 3:
            three_chunk_blocks.append(current_block)
            three_chunk_accumulator = 0
            current_block = ''
        elif len(message) - index < 3 and three_chunk_accumulator <= 1:
            current_block = current_block + ',' + current_block + ',' + current_block
            three_chunk_blocks.append(current_block)
            current_block = ''
            
    print(three_chunk_blocks)
    
    return 'aaa'

def hill_cipher_decrypt(message: str, key: list[list[float]]) -> str:
    pass

if __name__ == '__main__':
    print('Hill Cipher')
    print('===========')
    print('1. Encrypt')
    print('2. Decrypt')

    choice = input('Enter your choice: ')
    message = input('Enter the message: ')

    print('Enter the key matrix: ')

    if choice == '1':
        key = get_matrix(3, 3)
        print(hill_cipher_encrypt(message, key))

    elif choice == '2':
        key = get_matrix(3, 3)
        print(hill_cipher_decrypt(message, key))
    else:
        print('Invalid choice')

    