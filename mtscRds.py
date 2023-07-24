import os

pcName = input('Введите имя ПК:')
qwinsta = 'cmd /c qwinsta /server:' + (pcName)
os.system(qwinsta)
userId = input('Введите ID пользователя:')
mstsc = 'cmd /k mstsc /shadow:' + (userId) + '/v:' + (pcName) + '/control /noConsentPrompt'
os.system(mstsc)
