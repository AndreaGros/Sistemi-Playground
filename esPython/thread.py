import threading
import random
import time


def thread1():
    for x in range(20):
        print(f"Thread1:{x}")
        time.sleep(random.randint(0, 10)/10)


def thread2():
    for x in range(20):
        print(f"Thread2:{x}")
        time.sleep(random.randint(0, 3)/10)


my_thread1 = threading.Thread(target=thread1)
my_thread2 = threading.Thread(target=thread2)
my_thread1.start()
my_thread2.start()
my_thread2.join()
print("FINITO, Buonanotte")
