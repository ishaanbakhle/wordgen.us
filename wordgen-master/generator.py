import numpy as np
from consts import rang, get_ord, get_char


def generate(matrix, num_strings=10):
    np.seterr(divide='ignore', invalid='ignore')
    if num_strings == None:
        num_strings = 10
    while (num_strings > 0):
        firstlet = np.random.randint(low=0, high=len(list(rang))-1)

        next_let = [0 for i in rang]

        next_let[firstlet] = 1

        generated = get_char(firstlet)

        nli = firstlet

        while ((len(generated) < 3 or get_char(nli) != '') and len(generated) < 11):
            next_let = np.matmul(matrix, next_let)
            next_let /= next_let.sum()
            nli = np.random.choice(list(rang), p=next_let)
            next_let = [0 for i in rang]
            next_let[nli] = 1
            generated += get_char(nli)

        print(generated)
        num_strings -= 1
