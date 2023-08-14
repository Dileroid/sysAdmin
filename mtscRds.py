import os
from time import sleep
from sys import exit

def sessionsParsing(pcName):
    qwinsta = 'cmd /c qwinsta /server:' + (pcName)
    os.system(qwinsta)
pcName = input('Введите имя ПК:')
sessionsParsing(pcName)
def rdsConnect (userId,togglecontrol):
    if togglecontrol in ('y' , 'ye' , 'yes'):
        mstsc = 'cmd /c mstsc /v:' + (pcName) + ' /admin' + ' /shadow:' + (userId) + ' /control' + ' /noConsentPrompt'
    elif togglecontrol in ('n' , 'no'):
        mstsc = 'cmd /c mstsc /v:' + (pcName) + ' /admin' + ' /shadow:' + (userId) + ' /noConsentPrompt'
    else:
        print('Ошибка выбора на предыдущем шаге')
        print("Выход...")
        sleep(1)
        exit(0)
    return(mstsc)
userId = input('Введите ID пользователя:')
togglecontrol = input('Перехватить контроль?(y/n)')
os.system(rdsConnect(userId,togglecontrol))