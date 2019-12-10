import numpy as np
from wordgen import consts as ct

def generate(matrix, num_strings=1): 
    np.seterr(divide='ignore', invalid='ignore')
    if num_strings == None:
        num_strings = 10
    while (num_strings > 0):
        firstlet = np.random.randint(low=0, high=len(list(ct.rang))-1)

        next_let = [0 for i in ct.rang]

        next_let[firstlet] = 1

        generated = ct.get_char(firstlet)

        nli = firstlet

        while ((len(generated) < 3 or ct.get_char(nli) != '') and len(generated) < 11):
            next_let = np.matmul(matrix, next_let)
            next_let /= next_let.sum()
            nli = np.random.choice(list(ct.rang), p=next_let)
            next_let = [0 for i in ct.rang]
            next_let[nli] = 1
            generated += ct.get_char(nli)

        print(generated)
        num_strings -= 1
