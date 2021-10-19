import time
import random
import sys
from multiprocessing import Process



def process_run(tiempo):
    nap = random.randint(1,tiempo)
    time.sleep(nap)
    print('(H) Tiempo en espera --> ' + str(nap) + ' segundos')

def num_aleatorios():
    cont2 = 0
    while cont2 < 10:
        numero = random.random()
        print(numero)
        cont2 = cont2 + 1


if __name__ == '__main__':

    cont = 0

    num = int(sys.argv[1])
    aux =  sys.argv[2]
    tiempo = int(sys.argv[3])

    while (cont < num):
        print('(P) Hola soy el proceso principal, y voy a crear un subproceso')
        my_process = Process(target=process_run(tiempo))
        my_process.start()
        time.sleep(1)

        if(aux == 's'):
            my_process.join()

        print('(P) Lista -->' + num_aleatorios())
        cont = cont + 1

