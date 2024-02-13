import threading
import time

# Define a function that will be executed by the thread
def print_numbers():
    for i in range(5):
        print(i)
        time.sleep(1)

# Create a thread
thread = threading.Thread(target=print_numbers)

# Start the thread
thread.start()

# Main thread continues executing for 3 seconds
time.sleep(9)

# Wait for the thread to finish (optional)
thread.join()

print("Thread execution is complete.")

