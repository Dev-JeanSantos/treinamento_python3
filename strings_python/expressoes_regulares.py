import re
###################### EXPRESSÕES REGULARES ####################

endereco = "RUA MANOEL NOVIS, 201 CENTRO TANGUA-RJ 24890000"

padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]")

busca_cep = padrao.search(endereco)
if busca_cep:
    cep = busca_cep.group()
    print(cep)