import threading
import time

def worker(event):
    print("Worker waiting for event")
    event.wait()
    print("Worker finished waiting")

event = threading.Event()
thread = threading.Thread(target=worker, args=(event,))
thread.start()

print("Main thread sleeping")

time.sleep(10)
print("Main thread setting event")
event.set()
thread.join()