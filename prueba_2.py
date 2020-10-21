#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Prueba-2 Python3
    Franco Friz Rodriguez
"""
import threading

class myThread (threading.Thread):
   def __init__(self, name, message):
      threading.Thread.__init__(self)
      self.name = name
      self.message = message
   def run(self):
      # Get lock to synchronize threads
      threadLock.acquire()
      print_message(self.message)
      # Free lock to release next thread
      threadLock.release()

def print_message(message):
    #print message without line breaks 
    print(message, end = '')

def concurrency_with_coffee():
    """The function should display the phrase "- I'm tired, Bob!" and then create 5 threads, 
    which will display words without line breaks.Finally the program will wait for the completion 
    of these threads and print the phrase"- You're right!"
    """
    print("- I'm tired, Bob!", end = '')

    global threadLock
    threadLock = threading.Lock()
    threads = []

    # Create new threads
    thread1 = myThread("Thread-1"," are made of coffee?")
    thread2 = myThread("Thread-2"," Do you know")
    thread3 = myThread("Thread-3"," it!")
    thread4 = myThread("Thread-4"," that our bodies")
    thread5 = myThread("Thread-5"," -Try drinking")

    # Start new Threads
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()

    # Add threads to thread list
    threads.append(thread1)
    threads.append(thread2)
    threads.append(thread3)
    threads.append(thread4)
    threads.append(thread5)

    # Wait for all threads to complete
    for t in threads:
        t.join()
    print("- You’re right!")

def main():
    concurrency_with_coffee()

if __name__ == "__main__":
    main()

