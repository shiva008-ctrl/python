# Create an iterator class in Python that generates the Fibonacci sequence up to a specified number of terms.

class FibonacciIterator:
    def __init__(self, n_terms):
        self.n_terms = n_terms
        self.count = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n_terms:
            raise StopIteration
        if self.count == 0:
            self.count += 1
            return self.a
        elif self.count == 1:
            self.count += 1
            return self.b
        else:
            self.a, self.b = self.b, self.a + self.b
            self.count += 1
            return self.b
for num in FibonacciIterator(10):
    print(num)