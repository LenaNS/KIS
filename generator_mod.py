import random
import oms_mod

class Generator_name():
    
    def __init__(self) -> None:

        self.list_fio = []
        self.list_oms = []

    def create_list_names(self):
        with open("names.txt", encoding="utf_8") as file:
            data = file.read()
        names_list = data.split()
        print(names_list)
        return names_list
    
    def create_list_surname(self):
        with open("surname.txt", encoding="utf_8") as file:
            data = file.read()
        surname_list = data.split()
        return surname_list

    def create_list_patronymic(self):
        with open("patronymic.txt", encoding="utf_8") as file:
            data = file.read()
        patronymic_list = data.split()
        return patronymic_list

    def create_fio(self):
        for i in range(len(self.create_list_surname())):
            for j in range(len(self.create_list_names())):
                for g in range(len(self.create_list_patronymic())):
                    string_fio = self.create_list_surname()[i] + " " + self.create_list_names()[j] + " " + self.create_list_patronymic()[g]
                    self.list_oms.append(oms_mod.Oms_Policy().form_namber())                  
                    self.list_fio.append(string_fio)
        print(self.list_oms)
        #print(self.list_fio)
        return self.list_fio, self.list_oms

    def get_fio(self):
        for i in range(len(self.create_list_surname())):
            for j in range(len(self.create_list_names())):
                for g in range(len(self.create_list_patronymic())):
                    string_fio = self.create_list_surname()[i] + " " + self.create_list_names()[j] + " " + self.create_list_patronymic()[g]
                    self.list_oms.append(oms_mod.Oms_Policy().form_namber())                  
                    self.list_fio.append([])
        return self.list_fio

       
