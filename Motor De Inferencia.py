def get_input():
    clausulas = []
    print("Introduce las cláusulas de la base de conocimiento (escribe 'fin' para terminar):")
    while True:
        entrada = input("Clausula: ")
        if entrada.lower() == 'fin':
            break
        clausulas.append(frozenset(entrada.replace('∨', '').split()))

    consulta = input("Introduce la consulta: ")
    query = frozenset([consulta])
    return clausulas, query

def resolver(ci, cj):
    resolventes = set()
    for x in ci:
        for y in cj:
            if x.startswith('~'):
                literal_negado = x[1:]
            else:
                literal_negado = '~' + x
            if literal_negado in cj:
                resolvente = (ci - {x}) | (cj - {literal_negado})
                if not resolvente:
                    return {frozenset()}  # Cláusula vacía encontrada
                resolventes.add(frozenset(resolvente))
    return resolventes

def resolucion(clausulas, query):
    clausulas.append(frozenset(['~' + list(query)[0]]))  # Negamos la consulta y la agregamos a las cláusulas
    nuevas = set()

    while True:
        n = len(clausulas)
        pares = [(clausulas[i], clausulas[j])
                 for i in range(n) for j in range(i+1, n)]
        
        for (ci, cj) in pares:
            resolventes = resolver(ci, cj)
            if frozenset() in resolventes:
                print("Contradicción encontrada: ", resolventes)
                return True
            nuevas.update(resolventes)
        
        if nuevas.issubset(clausulas):
            return False
        clausulas.update(nuevas)

# Obtener la entrada del usuario
clausulas, query = get_input()
print("¿Es la consulta una consecuencia lógica?", resolucion(clausulas, query))
