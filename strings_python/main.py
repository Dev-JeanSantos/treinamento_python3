from gettext import find


url = "http://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"


#fatiando a string (base) baseado na posição do caracter
base_url = url[:26]
url_parametros = url[27:]

print(url)
print(f'Utilizando posição do caracter: {base_url}')
print(f'Utilizando posição do caracter: {url_parametros}')

#fatiando a string (base) dinamicamente utilizando a função find()
url2 = "http://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
indice_de_fateamento = url2.find('?')
base2 = url2[:indice_de_fateamento] #pode omitir o indice so inicio e ou fim da string
url_paramteros2 = url2[indice_de_fateamento + 1:]


print(f'Utilizando o metodo find: {base2}')
print(f'Utilizando o metodo find: {url_paramteros2}')

#fatiando a string (base) dinamicamente utilizando a função find() mas o len()
url3 = "http://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"

#Separa a base do parametros
indice_interrogacao_3 = url3.find('?')
url_base_3 = url3[:indice_interrogacao_3]
url_parametros_3 = url3[indice_interrogacao_3 + 1:]
print(f'URL 3 parametros: {url_parametros_3}')

#Busca o valor de um parametro
parametro_busca = 'quantidade'
indice_parametro_3 = url_parametros_3.find(parametro_busca)
indice_valor = indice_parametro_3 + len(parametro_busca) + 1
indice_e_comercial = url_parametros_3.find('&', indice_valor)
if indice_e_comercial == -1:
    valor = url_parametros_3[indice_valor:]
else:
    valor = url_parametros_3[indice_valor:indice_e_comercial]
print(f'O valor: {valor}')

