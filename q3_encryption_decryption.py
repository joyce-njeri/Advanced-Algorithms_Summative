from prettytable import PrettyTable
import pprint

# encryption algorithm that will organize text in a matrix guided by the key-value 
# such that data can be re-written in columns to produce encrypted data
def encryptor(msg, key):
    print('\n\tENCRYPT')
    print('\tOriginal message:', msg)
    print('\tKey:', str(key))
    # The key specifies the number of rows
    rows = key
    # The text length specifies the number of columns
    cols = len(msg) 
    # initialize matrix
    key_values = [['' for i in range(cols)] for j in range(rows)] 

    # generate encryption table
    for i in range(cols):
        row = i % key
        col = i
        key_values[row][col] = msg[i]

    # print table as pretty table
    x = PrettyTable()
    x.field_names = [i+1 for i in range(cols)]
    for i in range(rows):
        x.add_row(key_values[i])
    print(x)

    # print table with pprint
    # pprint.pprint(key_values)

    # get encrypted message
    encrypted=''
    for i in range(rows):
        for j in range(cols):
            encrypted+=key_values[i][j]
    
    return encrypted

def decryptor(encrypted,key):
    print('\tDECRYPT')
    print('\tEncrypted message:', encrypted)
    print('\tKey:', str(key))
    rows = key
    cols = len(encrypted) 
    key_values = [['' for i in range(cols)] for j in range(rows)] 

    # generate decryption table
    i = 0
    row = 0
    col = 0
    while i < cols:
        # reset indexes
        if col >= cols:
            col = row + 1
            row += 1
        key_values[row][col] = encrypted[i]
        i += 1
        col += key

    # print table
    x = PrettyTable()
    x.field_names = [i+1 for i in range(cols)]
    for i in range(rows):
        x.add_row(key_values[i])
    print(x)

    # print table with pprint
    # pprint.pprint(key_values)

    # get decrypted message
    decrypted=''
    for i in range(cols):
        col = i
        row = i % key
        decrypted+=key_values[row][col]
    
    return decrypted

encrytped_message = encryptor('Plain text',3)
print('\tEncrypted message:',encrytped_message,)
print('\n')

decrytped_message = decryptor(encrytped_message,3)
print('\tDecrypted message:',decrytped_message)