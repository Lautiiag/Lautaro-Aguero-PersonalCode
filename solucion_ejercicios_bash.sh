!/bin/bash
# Script de solución para los ejercicios de Bash Scripting.
# Ejecutar con: bash solucion_ejercicios_bash.sh

# =================================================================
# GRUPO 1: Creación de scripts y comandos básicos
# =================================================================

echo "========================================="
echo "GRUPO 1: Comandos Básicos"
echo "========================================="

# Ejercicio 1.1: Crear un script llamado saludo.sh que muestre en pantalla el mensaje "Y si, es nuestro primer programa".
echo "--- Ejercicio 1.1: Saludo ---"
echo "Y si, es nuestro primer programa"

# Ejercicio 1.2: Escribir un script que liste todos los archivos y directorios del directorio actual en formato largo.
echo "--- Ejercicio 1.2: Listado Largo ---"
ls -l

# Ejercicio 1.3: Crear un script que cree un directorio llamado backup y copie en él todos los archivos.txt del directorio actual.
echo "--- Ejercicio 1.3: Backup (.txt) ---"
mkdir -p backup # Crea el directorio backup si no existe
# Creamos archivos.txt de prueba para asegurar que el ejercicio funcione
touch archivo1.txt archivo2.txt otro_archivo.log
cp *.txt backup/
echo "Archivos *.txt copiados a la carpeta 'backup'."
echo "Contenido de 'backup':"
ls backup/

# Limpieza de prueba
rm -f archivo1.txt archivo2.txt otro_archivo.log
rm -rf backup

# =================================================================
# GRUPO 2: Variables y operadores aritméticos
# =================================================================

echo ""
echo "========================================="
echo "GRUPO 2: Variables y Operadores Aritméticos"
echo "========================================="

# Ejercicio 2.1: Crea un script que defina dos variables numéricas y muestre la suma, resta, multiplicación y división entre ellas.
echo "--- Ejercicio 2.1: Operaciones Aritméticas ---"
NUM1=20
NUM2=5

SUMA=$((NUM1 + NUM2))
RESTA=$((NUM1 - NUM2))
MULTIPLICACION=$((NUM1 * NUM2))
DIVISION=$((NUM1 / NUM2)) # División entera

echo "Número 1: $NUM1"
echo "Número 2: $NUM2"
echo "Suma: $SUMA"
echo "Resta: $RESTA"
echo "Multiplicación: $MULTIPLICACION"
echo "División (entera): $DIVISION"

# Ejercicio 2.2: Escribe un script que calcule el área de un rectángulo a partir de dos variables (base y altura).
echo "--- Ejercicio 2.2: Área del Rectángulo ---"
BASE=15
ALTURA=8
AREA=$((BASE * ALTURA))

echo "Base: $BASE, Altura: $ALTURA"
echo "El área del rectángulo es: $AREA"

# Ejercicio 2.3: Define tres variables: nombre, edad y ciudad, y luego imprime un mensaje con esos datos concatenados en una oración.
echo "--- Ejercicio 2.3: Concatenación ---"
NOMBRE="Juan"
EDAD=25
CIUDAD="Mendoza"

echo "$NOMBRE tiene $EDAD años y vive en $CIUDAD."


# =================================================================
# GRUPO 3: Condicionales
# =================================================================

echo ""
echo "========================================="
echo "GRUPO 3: Condicionales"
echo "========================================="

# Ejercicio 3.1: Escribir un script que pida al usuario ingresar su edad y muestre si es mayor o menor de edad.
echo "--- Ejercicio 3.1: Mayor/Menor de Edad ---"
read -p "Por favor, ingresa tu edad: " EDAD_USUARIO

if [[ $EDAD_USUARIO -ge 18 ]]; then
    echo "Tienes $EDAD_USUARIO años. Eres mayor de edad."
else
    echo "Tienes $EDAD_USUARIO años. Eres menor de edad."
fi


# =================================================================
# GRUPO 4: Bucles
# =================================================================

echo ""
echo "========================================="
echo "GRUPO 4: Bucles"
echo "========================================="

# Ejercicio 4.1: Crear un script que imprima los números del 1 al 10 usando un bucle for.
echo "--- Ejercicio 4.1: Bucle for (1 al 10) ---"
echo "Números del 1 al 10:"
for i in {1..10}; do
    echo "$i"
done

# Ejercicio 4.2: Escribir un script que sume todos los números del 1 al 100 utilizando un bucle while.
echo "--- Ejercicio 4.2: Suma con Bucle while (1 al 100) ---"
CONTADOR=1
SUMA_TOTAL=0

while [[ $CONTADOR -le 100 ]]; do
    SUMA_TOTAL=$((SUMA_TOTAL + CONTADOR))
    CONTADOR=$((CONTADOR + 1))
done

echo "La suma de los números del 1 al 100 es: $SUMA_TOTAL"

# Ejercicio 4.3: Crear un script que pida al usuario ingresar contraseñas hasta que escriba "secreto", usando un bucle until.
echo "--- Ejercicio 4.3: Bucle until (Contraseña) ---"
CLAVE_INGRESADA=""

until [[ "$CLAVE_INGRESADA" == "secreto" ]]; do
    read -p "Ingresa la contraseña para salir: " CLAVE_INGRESADA
done

echo "¡Contraseña correcta! El bucle ha finalizado."


# =================================================================
# GRUPO 5: Entrada del usuario
# =================================================================

echo ""
echo "========================================="
echo "GRUPO 5: Entrada del usuario"
echo "========================================="

# Ejercicio 5.1: Crear un script interactivo que solicite nombre y apellido
echo "--- Ejercicio 5.1: Solicitud de Nombre y Apellido ---"
read -p "Ingresa tu Nombre: " NOMBRE_USR
read -p "Ingresa tu Apellido: " APELLIDO_USR

echo "Hola, $NOMBRE_USR $APELLIDO_USR. ¡Bienvenido!"

# Ejercicio 5.2: Crear un script que solicite al usuario una contraseña oculta con "read -s" y luego confirme su ingreso con un mensaje
echo "--- Ejercicio 5.2: Contraseña Oculta (read -s) ---"
read -s -p "Ingresa una contraseña oculta: " CLAVE_OCULTA
echo "" # Salto de línea para la salida
echo "Contraseña ingresada y confirmada."


# =================================================================
# GRUPO 6: Scripts combinando conceptos
# =================================================================

echo ""
echo "========================================="
echo "GRUPO 6: Scripts combinando conceptos"
echo "========================================="

# Ejercicio 7.1: Escribir un script que solicite al usuario su nombre y edad, y luego le diga si puede votar (mayor de 16).
echo "--- Ejercicio 7.1: Votación (Condicional) ---"
read -p "Ingresa tu Nombre: " V_NOMBRE
read -p "Ingresa tu Edad: " V_EDAD

if [[ $V_EDAD -ge 16 ]]; then
    echo "$V_NOMBRE, con $V_EDAD años, SÍ puedes votar en Argentina."
else
    echo "$V_NOMBRE, con $V_EDAD años, aún NO puedes votar."
fi


# Ejercicio 7.2: Crear un script que lea una lista de nombres desde un archivo de texto (nombres.txt) e imprima un saludo personalizado para cada uno.
echo "--- Ejercicio 7.2: Lectura de Archivo (while read) ---"

# Creación del archivo de prueba
echo "Ana" > nombres.txt
echo "Beto" >> nombres.txt
echo "Carlos" >> nombres.txt

echo "Saludos personalizados:"
while read -r NOMBRE_LISTA; do
    echo "¡Hola $NOMBRE_LISTA! Espero que tengas un buen día."
done < nombres.txt

# Limpieza de prueba
rm nombres.txt


# Ejercicio 7.3: Generar codigo bash para calcular el promedio entre 5 números utilizando el bucle for.
echo "--- Ejercicio 7.3: Promedio con Bucle for ---"
SUMA_PROMEDIO=0
CANTIDAD=5

echo "Ingresa 5 números:"
for (( i=1; i<=$CANTIDAD; i++ )); do
    read -p "Número $i: " NUMERO_ACTUAL
    SUMA_PROMEDIO=$((SUMA_PROMEDIO + NUMERO_ACTUAL))
done

# Usamos 'bc' para obtener un resultado con precisión decimal para el promedio.
PROMEDIO=$(echo "scale=2; $SUMA_PROMEDIO / $CANTIDAD" | bc)

echo "La suma total es: $SUMA_PROMEDIO"
echo "El promedio de los $CANTIDAD números es: $PROMEDIO"

echo "========================================="
echo "Fin de la ejecución de ejercicios."
echo "========================================="
