from typing import Any

class Queue(object):

  def __init__(self) -> None:
    self.queue = []

  def enqueue(self, data: Any) -> None:
    self.queue.append(data)

  def dequeue(self) -> None:
    if self.queue:
      return self.queue.pop(0)

if __name__ == '__main__':
  q = Queue()
  print(q.queue)
  q.enqueue(1)
  q.enqueue(2)
  print(q.queue)
  q.dequeue()
  print(q.queue)