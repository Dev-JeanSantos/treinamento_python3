import re
###################### EXPRESSÕES REGULARES ####################

endereco = "RUA MANOEL NOVIS, 201 CENTRO TANGUA-RJ 24890-000"

#Utilizando Quantificadores e Intervalos
padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")

busca_cep = padrao.search(endereco)
if busca_cep:
    cep = busca_cep.group()
    print(cep)