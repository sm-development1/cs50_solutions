class Jar:
    def __init__(self, capacity=12):
        # Set capacity, ensuring it's not negative
        if capacity < 0:
            raise ValueError("Capacity must be non-negative")
        self._capacity = capacity
        self._size = 0  # Start with an empty jar

    def __str__(self):
        # Return a cookie emoji repeated by number of cookies
        return "🍪" * self._size

    def deposit(self, n):
        # Add cookies if there's space
        if self._size + n > self.capacity:
            raise ValueError("Too many cookies")
        self._size += n

    def withdraw(self, n):
        # Remove cookies if enough available
        if self._size - n < 0:
            raise ValueError("Not enough cookies")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
