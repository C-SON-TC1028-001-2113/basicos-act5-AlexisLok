import math
def main():
    #escribe tu código abajo de esta línea
    altura = abs(float(input("Altura de la casa: ")))
    angulo = abs(int(input("Angulo en grados: ")))

    seno = math.sin(math.radians(angulo))
    largo = round(altura/seno)

    print(f"Largo de la escalera: {largo}")    
if __name__ == '__main__':
    main()