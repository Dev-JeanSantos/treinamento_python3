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
url3 = "http://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar"

parametro_inicio = 'moedaDestino'
indice_de_inicio_fateamento = url3.find(parametro_inicio)
print(indice_de_inicio_fateamento)
print(len(parametro_inicio))

indices_do_valor_buscado = (indice_de_fateamento + len(parametro_inicio) + 1)
print(indices_do_valor_buscado)


indice_e_comercial = url3.find('&', indices_do_valor_buscado)
print(indice_e_comercial)

if indice_e_comercial == -1:
    valor_buscado = url3[indices_do_valor_buscado:]
 
    # else:
    #  valor_buscado = url3[indice_do_valor_buscado:indice_e_comercial]
#print(f'Utilizando o metodo find() + len() Valor Buscado: {valor_buscado}')
