class NoElementsInQueue(Exception):
    pass


class Queue:
    
    def __init__(self, max_size=50):

        self.elements = [None] * max_size
        self.front_index = 0
        self.back_index = 0
    
    def enqueue(self, new_element):

        self.elements[self.back_index] = new_element
        self.back_index += 1
    
    def front(self):
       
        return self.elements[self.front_index]
    
    def dequeue(self):
        
        if self.front_index == self.back_index:
            raise NoElementsInQueue("Cannot dequeue from an empty queue")
        
        element = self.elements[self.front_index]
        self.elements[self.front_index] = None
        self.front_index += 1
        return element
    
    def __repr__(self):
        queue_elements = []
        for i in range(self.front_index, self.back_index):
            queue_elements.append(str(self.elements[i]))
        return ' '.join(queue_elements)



if __name__ == '__main__':
    queue = Queue()
    queue.enqueue('AAA')
    queue.enqueue('BBB')
    print(f'After initial enqueue: {queue}') 
    print(f'{queue.front() = }')
    print(f'{queue.dequeue() = }')
    print(f'After initial dequeue: {queue}')
    queue.enqueue('YYY')
    queue.enqueue('ZZZ')
    print(f'After second enqueue: {queue}')
    print(f'{queue.dequeue() = }')
    print(f'After second dequeue: {queue}')
    print(f'{queue.front() = }')
    print(f'{queue.dequeue() = }')
    print(f'{queue.dequeue() = }')
    try:
        print(f'{queue.dequeue() = }')
    except NoElementsInQueue as error:
        print('Cannot dequeue from an empty queue')
