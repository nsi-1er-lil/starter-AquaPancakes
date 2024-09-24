import random

c = random.randint(1,4)
P = c * 4
A = c ** 2
b = A > 5

print("On prend", c, "comme la longueur d'un cote")
print("Le perimetre du carre est de", c)
print("L'air du carre est", A)
print("L'air du carre est superieur a 5 ?", b)

x = random.randint(1,4)
def perimetre(x):
    return x * 4
def surface(x):
    return x ** 2

print("Le perimetre du carre d'apres le calcule est de", perimetre(x), "la long")
print("L'air du carre d'apres le calcule est de", surface(x))
# hello Prof, je ne veux plus de jeux video en cours
# Promis ok