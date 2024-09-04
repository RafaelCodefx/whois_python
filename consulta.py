import whois

dominio = input('Digite o Dominio: ' )
consulta = whois.whois(dominio)
print(consulta)