import random


class Oms_Policy():
    def __init__(self):
        self.namber = []
        self.string_namber = ""

    def random_namber(self):
        for i in range(4):
            self.part_namber = random.randint(1000,9999)
            self.namber.append(self.part_namber)
        return self.namber

    def form_namber(self):
        for item in self.random_namber():
            self.string_namber += str(item) + " "
        return self.string_namber
