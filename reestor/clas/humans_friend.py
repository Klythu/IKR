from abc import ABC,abstractmethod

class human_friend(ABC):
    def __init__(self,name,birth_date,comands):
        self.name=name
        self.birth=birth_date
        self.comands=list()
        for com in comands.split(','):
            self.comands.append(com)
    

    def get_name(self):
        return (str(self.name))
    def get_birth(self):
        return (str(self.birth))
    def get_comands(self):
        tmp=''
        for com in self.comands:
            tmp = tmp + com +', '
        return (tmp)
    def learn(self,comands):
        for com in comands.split(','):
            self.comands.append(com)

    @abstractmethod
    def info(self):pass


