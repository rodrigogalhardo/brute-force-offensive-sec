"""
Brute Force de Directory
Versão - 1.0   
By Rodrigo Galhardo | CISO, Ethical Hacking, Offensive Sec
"""

import requests
arq = open('directory.2.0.txt')
linhas = arq.readlines()
url = 'https://www.globo.com/'
try:
    for linha in linhas:
        res = requests.get(url + linha)
        codigo = res.status_code
        if codigo != 404 and linha[0] != '#' and codigo != 403:
            print(url + linha, codigo)
        elif codigo == 403 and codigo == 404:
            print('STATUS HTTP -> ERRO')
except Exception as err:
    pass
finally:
    print('=======FIM======')
