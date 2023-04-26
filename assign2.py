"""
Assignment -2

Title:
Implement all the functions of a dictionary (ADT) using hashing.
Data: Set of (key, value) pairs, Keys are mapped to values, Keys must be comparable, Keys must be unique
Standard Operations: Insert (key, value), Find(key), Delete(key)

"""

class Dictionary:
    def __init__(self, size=10):
        self.size = size
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def custom_hash(self, key):
        p = 31  # a prime number
        hash_val = 0

        for i in range(len(key)):
            hash_val = (hash_val * p + ord(key[i])) % self.size

        return hash_val

    def rehash(self, old_hash):
        return (old_hash + 1) % self.size

    def insert(self, key, value):
        hash_val = self.custom_hash(key)

        while self.keys[hash_val] is not None:
            if self.keys[hash_val] == key:
                self.values[hash_val] = value
                return
            hash_val = self.rehash(hash_val)

        self.keys[hash_val] = key
        self.values[hash_val] = value

    def find(self, key):
        hash_val = self.custom_hash(key)

        while self.keys[hash_val] is not None:
            if self.keys[hash_val] == key:
                return self.values[hash_val]
            hash_val = self.rehash(hash_val)

        return None

    def delete(self, key):
        hash_val = self.custom_hash(key)

        while self.keys[hash_val] is not None:
            if self.keys[hash_val] == key:
                self.keys[hash_val] = None
                self.values[hash_val] = None
                return
            hash_val = self.rehash(hash_val)

    def display(self):
        for i in range(self.size):
            if self.keys[i] is not None:
                print(self.keys[i], ":", self.values[i])

d = Dictionary()

# Insert some key-value pairs
d.insert("apple", 1)
d.insert("banana", 2)
d.insert("cherry", 3)

# Find a value by key
print(d.find("banana"))  # Output: 2

# Delete a key-value pair
d.delete("banana")

# Display all key-value pairs
d.display()

print("Code by Pranav Mehendale")