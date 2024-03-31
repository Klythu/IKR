from pack_animal import pack_animal

class horse(pack_animal):
    def __init__(self,name,birth_date,comands):
        super().__init__(name,birth_date,comands)
    
    def info(self):
        comands=''
        for comand in self.comands:
            comands+=comand
            if comand!=self.comands[-1]:
                comands+=','
        print(f' Кличка {self.get_name()}\n Животное - лошади\n Дата рождения {self.get_birth()}\n Выученные команды {comands}') 

