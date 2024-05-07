import threading
import time

recurso_compartilhado1 = 0
recurso_compartilhado2 = 0

# Criação dos semáforos
semaforo1 = threading.Semaphore()
semaforo2 = threading.Semaphore()

# Função
def calculo(id):
    global recurso_compartilhado1
    global recurso_compartilhado2
    
    for i in range(1):
        
        print(f"Thread {id}: Tentando adquirir o semáforo1")
        semaforo1.acquire()
        print(f"Thread {id}: Semáforo1 adquirido.")
        recurso_compartilhado1 += 1
        print(f"Thread {id}: recurso_compartilhado1 = {recurso_compartilhado1}")
        semaforo1.release()
        print(f"Thread {id}: Semáforo1 liberado.")
        print(f"Thread {id}: Tentando adquirir o semáforo2")
        semaforo2.acquire()
        print(f"Thread {id}: Semáforo2 adquirido.")
        recurso_compartilhado2 += 2
        print(f"Thread {id}: recurso_compartilhado2 = {recurso_compartilhado2}")
        semaforo2.release()
        print(f"Thread {id}: Semáforo2 liberado.")
        

        # So para ver o for rodando
        time.sleep(20)

# Geração de 5 threads
for i in range(1, 6):
    thread = threading.Thread(target=calculo, args=(i,))
    thread.start()
