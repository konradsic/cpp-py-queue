"""
Class implementing deque in Python
Same functionality dequeue liblary
With usage example
Version: v1.16
Consists:
	a) Program template
    b) mQueue (my queue) with functions
    c) Usage example
Author: Konrad S. (konradsic)
Project created on OKI 2022 (https://oki.org.pl)
"""
class QueueIndexOutOfRange(Exception): pass
class QueueIsEmpty(Exception): pass
class QueueExtenderIsNotIterable(Exception): pass
class QueueIsAlreadyEmpty(Exception): pass
class QueueExecutorFailed(Exception): pass

class mQueue:
    # setting first and last to None - after push they will update
    def __init__(self):
        self._queue = []
        self.first = None
        self.last = None

    #functions
    def is_empty(self):
        return not self._queue

    def size(self):
        return len(self._queue)

    def items(self):
        if self.is_empty():
            raise QueueIsEmpty
        return self._queue

    def get(self):
        return self.items()

    def copy(self):
        return self._queue

    def push(self, item):
        first = False
        if self.is_empty(): 
            first = True
        self._queue.append(item)
        if first: 
            self.first = self._queue[0]
        self.last = self._queue[-1]

    def pushleft(self, item):
        self._queue = [item].extend(self._queue)
        self.first = item
        self.last = self._queue[-1]
    
    def extend(self, l):
        if not list(l):
            raise QueueExtenderIsNotIterable(f"Element {l} is not iterable. Try using a list() type")
        first = False
        if self.is_empty: 
            first = True
        self._queue.extend(l)
        if first: 
            self.first = self._queue[0]
        self.last = self._queue[-1]

    def rotate(self, r):
        if self.is_empty():
            raise QueueIsEmpty
        if r >= self.size():
            raise QueueIndexOutOfRange(f"Rotation index {r} is out of range")
        before = self._queue
        self._queue = list(before[r:])+ list(before[:(self.size()-r)])
        self.first = self._queue[0]
        self.last = self._queue[-1]

    def empty(self):
        if self.is_empty():
            raise QueueExtenderIsNotIterable("Queue is already empty, why you are trying to empty an empty queue?")
        self._queue = []
        self.first = None
        self.last = None

    def delete(self, index): 
        if self.is_empty():
            raise QueueIsEmpty
        if index >= self.size():
            raise QueueIndexOutOfRange(f"Index {index} is out of range")
        del self._queue[index]
        if index == 0:
            self.first = self._queue[0]
        if index == -1 or index == len(self._queue)-1:
            self.last = self._queue[-1]

    def pop(self): 
        if self.is_empty():
            raise QueueIsEmpty
        first = self.first
        self._queue.pop(0)
        self.first = self._queue[0]
        return first

    def popleft(self): 
        last = self.last
        if self.is_empty():
            raise QueueIsEmpty
        self._queue.pop(-1)
        return last

    def dequeue(self, executor):
        if self.is_empty():
            raise QueueIsEmpty
        try:
            execute = executor(self.first)
            self.pop()
            return execute
        except:
            raise QueueExecutorFailed(f"\"{executor}\" is not a method or executing a function \"{executor}\" failed")
        

#usage example
import random

MAX_PAYOUT = 30
MAX_PAYMENT = 1000

payments = mQueue()

people = 8
for x in range(people):
    payments.push(random.randint(-1*MAX_PAYOUT,MAX_PAYMENT))

print(payments.items())
payments.pop()
payments.popleft()
print(payments.items())
payments.rotate(3)
print(payments.items())
payments.extend([-1,2,4])
#uncomment next line if you want to know what will happen
#payments.empty()

def helper(integer):
    print(f"Person has been served ({integer})")

class something:
    def __init__(self): pass

for value in payments.items():
    payments.dequeue(something)
