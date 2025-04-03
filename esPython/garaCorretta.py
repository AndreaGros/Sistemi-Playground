import time
import random
import threading

semaphore_prova1 = threading.Semaphore(7)
semaphore_prova2 = threading.Semaphore(3)
lock = threading.Lock()

classifica_prova1 = []

def gara1():
    semaphore_prova1.acquire()
    
    lock.acquire()
    print(f"{current_thread} attende di iniziare la prima prova")
    lock.release()
    
    current_thread = threading.current_thread().name
    
    lock.acquire()
    print(f"{current_thread} inizia la prima prova")
    lock.release()
    
    time.sleep(random.randint(1, 3))
    
    lock.acquire()
    print(f"{current_thread} termina la prima prova")
    lock.release()
    
    lock.acquire()
    classifica_prova1.append(current_thread)
    lock.release()
    
    semaphore_prova1.release()

def gara2():
    semaphore_prova2.acquire()
    
    current_thread = threading.current_thread().name
    
    lock.acquire()
    print(f"{current_thread} attende di iniziare la seconda prova")
    lock.release()
    
    lock.acquire()
    print(f"{current_thread} inizia la seconda prova")
    lock.release()
    
    time.sleep(random.randint(2, 4))
    
    punti = random.randint(1, 10)
    punteggi[current_thread] += punti
    
    lock.acquire()
    print(f"{current_thread} termina la seconda prova con {punti} punti")
    lock.release()
    
    semaphore_prova2.release()

def premiazione():
    current_thread = threading.current_thread().name
    lock.acquire()
    print(f"{current_thread} termina la gara con totale {punteggi[current_thread]} punti")
    lock.release()

concorrenti = [f"C{x}" for x in range(10)]
punteggi = {concorrente: 0 for concorrente in concorrenti}

my_thread = []
for c in concorrenti:
    single_thread = threading.Thread(target=gara1)
    single_thread.name = c
    my_thread.append(single_thread)

print(concorrenti)

for th in my_thread:
    th.start()
for th in my_thread:
    th.join()

N = len(concorrenti)
for i, concorrente in enumerate(classifica_prova1):
    punteggi[concorrente] += N - i

my_thread = []
for c in concorrenti:
    single_thread = threading.Thread(target=gara2)
    single_thread.name = c
    my_thread.append(single_thread)

for th in my_thread:
    th.start()
for th in my_thread:
    th.join()

my_thread = []
for c in concorrenti:
    single_thread = threading.Thread(target=premiazione)
    single_thread.name = c
    my_thread.append(single_thread)

for th in my_thread:
    th.start()
for th in my_thread:
    th.join()