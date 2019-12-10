import generator
import data_gen
import consts
import argparse
import csv

parser = argparse.ArgumentParser()
parser.add_argument('--num_strings', required=False)
parser.add_argument('--dataset', required=False)

args = parser.parse_args()

dataset = args.dataset

if (not dataset is None and type(dataset == str)):
    if args.dataset.find(".txt") > 0:
        dataset = open(args.dataset, 'r')
        dataset = dataset.read()

else:
    dataset = open('wordgen/test.txt', 'r')
    dataset = dataset.read()

matrix = data_gen.fill_matrix(dataset)

with open("out.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(matrix)

if (args.num_strings):
    generator.generate(matrix, int(args.num_strings))
else:
    generator.generate(matrix)
