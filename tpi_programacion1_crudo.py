"Auxiliar"
def filtrar_por_continente(dic_paises):
    continentes_disponibles = []
    for pais in dic_paises:
        continente_actual = pais.get("continente")
        if continente_actual not in continentes_disponibles:
            continentes_disponibles.append(continente_actual)
