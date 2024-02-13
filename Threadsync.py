import threading
import time

# Shared resource
shared_resource = 0

# Define a lock
lock = threading.Lock()

# Function to increment the shared resource
def increment():
    global shared_resource
    for _ in range(2000000):
        # Acquire the lock
        lock.acquire()
        shared_resource += 1
        # Release the lock
        lock.release()

# Create two threads to increment the shared resource
thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=increment)

# Start the threads
thread1.start()
thread2.start()

# Wait for the threads to finish
thread1.join()
thread2.join()

print("Final value of shared_resource:", shared_resource)

