strings = ["My", "World", "Apple", "Pear"]

def add_s(string):
    return string + "s"


def maior_que_4(string):
    return len(string) > 4


# =--=-=-=-=-=---=-=---=-=--=-==-=-=--=--=
tamanhos = map(add_s, strings)
print(list(tamanhos))

filtrado = filter(maior_que_4, strings)
print(list(filtrado))
