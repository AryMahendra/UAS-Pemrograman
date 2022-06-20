numberTree = [1, 2, 3, [4, 5], [6, [7, 8, 9]]]


def showNumber(tree):
    if isinstance(tree, list):
        for angka in tree:
            showNumber(angka)

    else:
        print("angka",tree)


showNumber(numberTree)