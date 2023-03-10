# Importando as Bibliotecas:
import requests
from bs4 import BeautifulSoup

# Definindo o site do Mercado Livre para Scraping
requests=requests.get('https://www.mercadolivre.com.br/ofertas#DEAL_ID=MLB15920&S=landingHubdia-do-consumidor-2023&V=29&T=CarouselDynamic-normal&L=VER-MAIS&deal_print_id=55a7be80-be93-11ed-bbf9-3b8ca5d9adc4&c_id=carouseldynamic-normal&c_element_order=undefined&c_campaign=VER-MAIS&c_uid=55a7be80-be93-11ed-bbf9-3b8ca5d9adc4')

# Retorna as informações da página
print('Status',requests)
print('↓↓ Headers below ↓↓')
print("="*30)
print(requests.headers)
print("="*30)

# Retorna o código HTML da página:
print(requests.content)

# Atribui uma variável ao código e adiciona o BeautifulSoup ao código:
content = requests.content
sites = BeautifulSoup(content,'html.parser')

# Retorna um código HTML mais organizado:
print(sites.prettify())

# Determina o valor do produto:
preco = sites.find('span', attrs = {'class': 'andes-money-amount__fraction'})
print('R${}'.format(preco.text))

# Determina o nome do produto:
nomeProduto = sites.find('p', attrs = {'class':'promotion-item__title'})
print(f'{nomeProduto.text} custa R${preco.text},00')

# Aplicando o FindAll e juntando o nome com o preço:
siteBody = sites.findAll('li', attrs = {'class': 'promotion-item default'})
listaItems = []
for site in siteBody:
    preco = site.find('span', attrs = {'class':'andes-money-amount__fraction'})
    nomeProduto = site.find('p', attrs = {'class':'promotion-item__title'})
    for i in listaItems:
        if nomeProduto in listaItems:
            continue
    listaItems.extend([nomeProduto])
    print(f'\033[31m → \033[m{nomeProduto.text} custa\033[35m R${preco.text},00\033[m')
    print("="*50)
print(f'\033[34mExistem {len(listaItems)} itens no total')

# Analisando a lista de nomes criada:
for i in range(len(listaItems)):
    print(f'\033[4;32m→\033[m {listaItems[i].text} \033[4;32m←\033[m')
print(len(listaItems))
