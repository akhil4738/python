import threading
import queue 

def producer(queue):
    for i in range(5):
        queue.put(i)
        print("Produced", i)

def consumer(queue):
    while True:
        item = queue.get()
        if item is None:
            break
        print("Consumed", item)

q = queue.Queue()  # Using Queue directly
producer_thread = threading.Thread(target=producer, args=(q,))
consumer_thread = threading.Thread(target=consumer, args=(q,))

producer_thread.start()
consumer_thread.start()

producer_thread.join()
q.put(None)  # signal the consumer thread to exit
consumer_thread.join()
