import threading

def daemon_task():
    while True:
        print("Daemon thread is running...")

daemon_thread = threading.Thread(target=daemon_task)
daemon_thread.daemon = True  # Set as daemon thread
daemon_thread.start()

daemon_thread.isDaemon()
