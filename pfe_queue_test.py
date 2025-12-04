import unittest


class Queue:

    
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)
    
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.items[0]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)


class Queue_Test(unittest.TestCase):
    
    def setUp(self):
        self.queue = Queue()
    
    def test_enqueue(self):
        self.queue.enqueue(10)
        self.assertEqual(self.queue.size(), 1)
        self.queue.enqueue(20)
        self.queue.enqueue(30)
        self.assertEqual(self.queue.size(), 3)
        self.queue.enqueue(None)
        self.assertEqual(self.queue.size(), 4)
    
    def test_dequeue(self):
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        result = self.queue.dequeue()
        self.assertEqual(result, 10)
        self.assertEqual(self.queue.size(), 1)
        self.queue.dequeue()  
        with self.assertRaises(IndexError):
            self.queue.dequeue()
    
    def test_peek(self):
        self.queue.enqueue(5)
        self.queue.enqueue(15)
        result = self.queue.peek()
        self.assertEqual(result, 5)
        self.assertEqual(self.queue.size(), 2)  
        empty_queue = Queue()
        with self.assertRaises(IndexError):
            empty_queue.peek()
    
    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue(100)
        self.assertFalse(self.queue.is_empty())
        self.queue.dequeue()
        self.assertTrue(self.queue.is_empty())
    
    def test_size(self):
        self.assertEqual(self.queue.size(), 0)
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.assertEqual(self.queue.size(), 3)
        self.queue.dequeue()
        self.queue.dequeue()
        self.assertEqual(self.queue.size(), 1)
        self.queue.dequeue()
        self.assertEqual(self.queue.size(), 0)
    
    def test_fifo_order(self):
        items = [10, 20, 30, 40, 50]
        for item in items:
            self.queue.enqueue(item)
        
        dequeued_items = []
        while not self.queue.is_empty():
            dequeued_items.append(self.queue.dequeue())
        
        self.assertEqual(items, dequeued_items)
        
        self.queue.enqueue(99)
        self.assertEqual(self.queue.dequeue(), 99)


if __name__ == '__main__':
    unittest.main()