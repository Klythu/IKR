from humans_friend import human_friend
from pet import pet
from pack_animal import pack_animal
from camel import camel
from cat import cat
from dog import dog
from donkey import donkey
from horse import horse
from humster import humster
from mule import mule

humans_friend_list=[]
while True:
    instruction=input(f'Введите инструкцию, усли вы забыли инструкции просмотрите их [С]писок\n')
    if instruction =='С':
        print(f' C - просмотр списка инсдрукций\n А - добавить новое животное\n [кличка],К - просмотр команд выученых животным\n [кличка],О - добавление новой выученной команды или нескольких\n М - меню всех животных')
    if instruction =='А':
        type=input(f'Выбирите вид животного\n[К]от\n[С]обака\n[Г]рызун\n[Л]ошадь\n[В]ерблюд\n[О]сёл\n[М]ул\n')
        if type=='К':
            humans_friend_list.append(cat(input('Введите кличку '),input('Введите дату рождения в фотмате ДД-ММ-ГГГГ '),input('Введите команды которым обучено животное через запитую ')))
        if type=='С':
            humans_friend_list.append(dog(input('Введите кличку '),input('Введите дату рождения в фотмате ДД-ММ-ГГГГ '),input('Введите команды которым обучено животное через запитую ')))
        if type=='Г':
            humans_friend_list.append(humster(input('Введите кличку '),input('Введите дату рождения в фотмате ДД-ММ-ГГГГ '),input('Введите команды которым обучено животное через запитую ')))
        if type=='Л':
            humans_friend_list.append(horse(input('Введите кличку '),input('Введите дату рождения в фотмате ДД-ММ-ГГГГ '),input('Введите команды которым обучено животное через запитую ')))
        if type=='М':
            humans_friend_list.append(mule(input('Введите кличку '),input('Введите дату рождения в фотмате ДД-ММ-ГГГГ '),input('Введите команды которым обучено животное через запитую ')))
        if type=='О':
            humans_friend_list.append(donkey(input('Введите кличку '),input('Введите дату рождения в фотмате ДД-ММ-ГГГГ '),input('Введите команды которым обучено животное через запитую ')))
        if type=='В':
            humans_friend_list.append(camel(input('Введите кличку '),input('Введите дату рождения в фотмате ДД-ММ-ГГГГ '),input('Введите команды которым обучено животное через запитую ')))
    if instruction=='М':
        for animal in humans_friend_list:
            print(animal.get_name())
    if ',' in instruction:    
        if instruction.split(',')[1]=='К':
            for search in humans_friend_list:
                if instruction.split(',')[0]==search.get_name():
                    flag=1
                    index=humans_friend_list.index(search)
                else:
                    flag=0
            if flag==1:
                tmp=humans_friend_list[index]
                print(f'Выученные команды животного :')
                print(tmp.get_comands())
        if instruction.split(',')[1]=='С':
            for search in humans_friend_list:
                if instruction.split(',')[0]==search.get_name():
                    flag=1
                    index=humans_friend_list.index(search)
                else:
                    flag=0
            if flag==1:
                humans_friend_list[index].learn(input('Введите команды через запитую'))