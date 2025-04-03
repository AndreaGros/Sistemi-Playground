import threading
import time
import random

players = [f"C{i}" for i in range(10)]
points = {c: 0 for c in players}
lock = threading.Lock()
semaphore_7 = threading.Semaphore(7)
semaphore_3 = threading.Semaphore(3)

def prima_prova():
    concorrenti_in_gara = random.sample(players, 7)
    risultati = []
    
    def gara(concorrente):
        #with equivale ad using in linguaggio c#,teoricamente mi permette di non non dover fare manualmente lock.release() ma non sono pienamente certo che funzioni così (trovato su uno stack overflow)
        with semaphore_7:
            with lock:
                print(f"{threading.current_thread().name} - Concorrente {concorrente} attende di iniziare la prima prova")
            time.sleep(random.uniform(0.5, 1.5))
            with lock:
                print(f"{threading.current_thread().name} - Concorrente {concorrente} inizia la prima prova")
            tempo = random.uniform(1, 3)
            time.sleep(tempo)
            with lock:
                print(f"{threading.current_thread().name} - Concorrente {concorrente} termina la prima prova con tempo {tempo:.2f}s")
            risultati.append((concorrente, tempo))
    
    thread_list = []
    for c in concorrenti_in_gara:
        t = threading.Thread(target=gara, args=(c,))
        thread_list.append(t)
        t.start()
    
    for t in thread_list:
        t.join()
    
    risultati.sort(key=lambda x: x[1])
    for i, (concorrente, _) in enumerate(risultati):
        points[concorrente] += len(concorrenti_in_gara) - i

def seconda_prova():
    concorrenti_in_gara = random.sample(players, 3)
    
    def gara(concorrente):
        with semaphore_3:
            with lock:
                print(f"{threading.current_thread().name} - Concorrente {concorrente} attende di iniziare la seconda prova")
            time.sleep(random.uniform(0.5, 1.5))
            with lock:
                print(f"{threading.current_thread().name} - Concorrente {concorrente} inizia la seconda prova")
            time.sleep(random.uniform(2, 4))
            punti = random.randint(1, 10)
            points[concorrente] += punti
            with lock:
                print(f"{threading.current_thread().name} - Concorrente {concorrente} termina la seconda prova con {punti} punti")
    
    thread_list = []
    for c in concorrenti_in_gara:
        t = threading.Thread(target=gara, args=(c,))
        thread_list.append(t)
        t.start()
    
    for t in thread_list:
        t.join()

def premiazione():
    for concorrente in players:
        with lock:
            print(f"Concorrente {concorrente} termina la gara con totale {points[concorrente]} punti")
        time.sleep(1)
        
t1 = threading.Thread(target=prima_prova)
t2 = threading.Thread(target=seconda_prova)

t1.start()
t1.join()
t2.start()
t2.join()
premiazione()