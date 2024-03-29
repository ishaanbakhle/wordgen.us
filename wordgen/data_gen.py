from wordgen import consts
import numpy as np
from sklearn import preprocessing


def fill_matrix(dataset):

    assert type(dataset) == str
    assert len(dataset) > 0, print("Dataset must be > 0")

    matrix = []

    for i in consts.rang:
        matrix.append([])
        for o in consts.rang:
            matrix[i].append(0)

    dataset = dataset.lower()

    accepted = list("abcdefghijklmnopqrstuvqwxyz") + ['\n']
    for i in range(len(dataset)-1):
        # if (dataset[i+1] in accepted and dataset[i] in accepted):
        if dataset[i] in accepted:
            val2 = i+1
            while (val2 < len(dataset) and not (dataset[val2] in accepted)):
                val2 += 1
            ind1 = consts.get_ord(dataset[i])
            ind2 = consts.get_ord(dataset[val2])
            matrix[ind2][ind1] += 1

    matrix = preprocessing.normalize(matrix, norm='l1')

    return matrix


if __name__ == '__main__':
    print(fill_matrix("james as"))
