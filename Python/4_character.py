# Escribir una clase que permita representar al personaje de un videojuego. Un personaje
# tiene un nombre (o nickname), un porcentaje de vida (o salud), un poder (su nombre,
# por ejemplo, “patada giratoria”), y una medida de daño (número entero entre 0 y 100).
# 1. Implementar un método que permite atacar a otro personaje (que se recibe cómo
#    parámetro). El ataque del personaje (p1) le quita vida al personaje que es atacado
#    (p2), utilizando la siguiente función:
#    nueva_vida(p2) = vida_actual(p2) - medida_de_daño(p1)
# 2. Implementar un método que indica (devolviendo True) si un personaje está con vida
#    (salud > 0)
# 3. Crear 3 personajes llamados pj1, pj2 y pj3 (con el porcentaje de salud y poder que
#    ustedes desee), pj1 debe atacar a pj2 y pj3

class Character:
    '''Clase Character'''
    def __init__(self, nickname, life, damage, power):
        self.nickname = nickname
        self.life = life
        self.damage = damage
        self.power = power

    def attack(self, elotro):
        elotro.life = elotro.life - self.damage

    def health(self):
        return self.life > 0

# Programa principal
p1 = Character("La momia", 100, 70, "Abrazo mortal")
p2 = Character("La viuda negra", 100, 75, "Mordida venenosa")
p3 = Character("El cazador", 100, 65, "Hachazo")

print(p1.nickname, " salud:", p1.health())
print(p2.nickname, " salud:", p2.health())
print()
print("El personaje {} ataca al personaje {}".format(
    p1.nickname,
    p2.nickname
))

p1.attack(p2)

print()
print(p1.nickname, " salud:", p1.health())
print(p2.nickname, " salud:", p2.health())
print()
print("El personaje {} ataca al personaje {}".format(
    p1.nickname,
    p3.nickname
))

p1.attack(p3)

print()
print(p1.nickname, " salud:", p1.health())
print(p2.nickname, " salud:", p2.health())
print(p3.nickname, " salud:", p3.health())
print()
