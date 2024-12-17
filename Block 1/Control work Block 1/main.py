
first=0
result='Ошибка: вы еще не выполнили не одну операцию с числами!'
numberone=0
numbertwo=0
summary=0
def plus(numone,numtwo):
    result=numone+numtwo


def minus(numone,numtwo):
    result=numone-numtwo


def umn(numone,numtwo):
    result=numone*numtwo


def razd(numone,numtwo):
    result=numone/numtwo


numberone=int(input('Введите первое число: '))
numbertwo=int(input('Введите второе число: '))
while True:
    choice=input('Введите требуемое действие: ').lower
    if choice == 'результат' or 'ответ':
        print('Ответ:',result)


    elif choice == 'сложение':
        if first == 0:
            plus(numberone,numbertwo)
            first=1
        elif first == 1:
            plus(result,numbertwo)


    elif choice == 'вычитание':
        if first == 0:
            minus(numberone,numbertwo)
            first=1
        elif first == 1:
            minus(result,numbertwo)


    elif choice == 'умножение':
        if first == 0:
            umn(numberone,numbertwo)
            first=1
        elif first == 1:
            umn(result,numbertwo)


    elif choice == 'деление':
        if first == 0:
            razd(numberone,numbertwo)
            first=1
        elif first == 1:
            razd(result,numbertwo)
