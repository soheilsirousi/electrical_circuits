import os

from text_proccesor.models import Sentence


def Runner(filename='./test_cases/input.txt'):
    with open(filename) as f:
        data = f.readlines()
        for line in data:
            sen = Sentence()
            mesh = sen.to_mesh(line)
            print(mesh.Ammeter())


if __name__ == '__main__':
    Runner()