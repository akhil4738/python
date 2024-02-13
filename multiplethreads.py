import threading
import time

# Define a function that will be executed by the thread
def print_numbers():
    for i in range(5):
        print(f"Thread 1: {i}")
        time.sleep(4)
                   
def print_letters():
    for char in 'ABCDE':
        print(f"Thread 2: {char}")
        time.sleep(4)

# Create threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Start threads
thread1.start()
thread2.start()

# Wait for threads to finish (optional)
thread1.join()
thread2.join()

print("All threads have finished.")
