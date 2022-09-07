for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()