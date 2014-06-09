from threading import Thread
import time


class TestThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.thread_stop = False

    def run(self):
        while not self.thread_stop:
            print 'running'
            time.sleep(1)

    def stop(self):
        self.thread_stop = True

def main():
    print 'main'
    test_thread = TestThread()
    test_thread.start()


if __name__ == '__main__':
    main()
