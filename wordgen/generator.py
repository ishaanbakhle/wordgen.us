import numpy as np
from wordgen import consts


def generate(matrix, num_strings=10):
    np.seterr(divide='ignore', invalid='ignore')
    if num_strings == None:
        num_strings = 10
    while (num_strings > 0):
        firstlet = np.random.randint(low=0, high=len(list(consts.rang))-1)

        next_let = [0 for i in consts.rang]

        next_let[firstlet] = 1

        generated = consts.get_char(firstlet)

        nli = firstlet

        while ((len(generated) < 3 or consts.get_char(nli) != '') and len(generated) < 11):
            next_let = np.matmul(matrix, next_let)
            if len(generated) > 1 and generated[:-1] == generated[:-2] and generated[:-1] != 'o':
                next_let[consts.get_ord(generated[:-1])] = 0
            next_let /= next_let.sum()
            nli = np.random.choice(list(consts.rang), p=next_let)
            next_let = [0 for i in consts.rang]
            next_let[nli] = 1
            generated += consts.get_char(nli)

        num_strings -= 1
    return(generated)
