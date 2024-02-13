import threading
import time

def producer(cv):
    with cv:
        print("Producing...")
        time.sleep(2)
        print("Produced")
        cv.notify()

def consumer(cv):
    with cv:
        print("Consumer waiting...")
        cv.wait(5)
        print("Consumed")

cv = threading.Condition()
producer_thread = threading.Thread(target=producer, args=(cv,))
consumer_thread = threading.Thread(target=consumer, args=(cv,))

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()
