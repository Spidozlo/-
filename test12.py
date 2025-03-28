from abc import ABC, abstractmethod
import random


class Character(ABC):
    def __init__(self, name, lvl):
        self.name = name
        self.lvl = lvl
        self.hp = 100 * lvl

    @abstractmethod
    def damage(self, aim):
        pass

    def info(self):
        print(f'{self.name} is {self.lvl} and have {self.hp} hp')


class Elf(Character):
    def __init__(self, name, lvl):
        super().__init__(name, lvl)

    def damage(self, aim):
        if aim.lvl < self.lvl:
            damage = self.lvl * 10
        else:
            damage = self.lvl * 9
        return damage


class Ogre(Character):
    def __init__(self, name, lvl):
        super().__init__(name, lvl)
        self.hp = 110 * lvl

    def damage(self, aim):
        if aim.lvl < self.lvl:
            damage = self.lvl * 8
        else:
            damage = self.lvl * 7
        return damage


def fight(char1, char2):
    round = 1
    char1_damage = char1.damage(char2)
    char2_damage = char2.damage(char1)
    while char1.hp > 0 and char2.hp > 0:
        print(f'{round} раунд: ')
        if random.randint(1, 2) == 1 and round == 1:
            char1, char2 = char2, char1
            round += 1
            print(f'Первым атакует {char1.name}')
        round += 1
        char2.hp -= char1_damage
        if char2.hp <= 0:
            return print(f'{char1.name} ПОБЕДИЛ ПОЗДРАВЛЕМ')
        print(f'{char1.name} give {char1_damage} damage to {char2.name} he left {char2.hp}')
        char1.hp -= char2_damage
        if char1.hp <= 0:
            return print(f'{char2.name} ПОБЕДИЛ ПОЗДРАВЛЕМ')
        print(f'{char2.name} give {char2_damage} damage to {char1.name} he left {char1.hp}')


ogre1 = Ogre('Огр Володя', 100)
elf1 = Elf('Эльф Григорий', 100)


print(fight(ogre1, elf1))
