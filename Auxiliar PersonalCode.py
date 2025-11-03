"Auxiliar"
def validaciones_fundamentales(linea, num_linea):
    if linea is None:
        return None

    texto = linea.strip()
    if texto == "":
        return None

    partes = [p.strip() for p in texto.split(",")]
    if len(partes) != 3:
        print(f"Línea {num_linea} descartada. Formato incorrecto (se esperaban 3 campos): {texto}")
        return None

    id_str, nombre, precio_str = partes

    if nombre == "":
        print(f"Línea {num_linea} descartada. Nombre vacío.")
        return None
    try:
        producto_id = int(id_str)
    except ValueError:
        print(f"Línea {num_linea} descartada. ID no numérico: {id_str!r}")
        return None

    if producto_id <= 0:
        print(f"Línea {num_linea} descartada. ID no positivo: {producto_id}")
        return None

    try:
        producto_precio = float(precio_str)
    except ValueError:
        print(f"Línea {num_linea} descartada. Precio no numérico: {precio_str!r}")
        return None

    if producto_precio < 0:
        print(f"Línea {num_linea} descartada. Precio negativo: {producto_precio}")
        return None

    return {"id": producto_id, "nombre": nombre, "precio": producto_precio}
