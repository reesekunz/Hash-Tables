import time
import hashlib
import bcrypt


class DynamicArray:
    def __init__(self, capacity=8):  # default capacity is defined at 8
        self.capacity = capacity
        self.count = 0
        # creates an array of [None, None, None, None, None, None, None, None]
        self.storage = [None] * capacity

    def insert(self, index, value):
        # check to see if array is full before inserting
        if self.count == self.capacity:
            self.double_size()
        self.storage[index] = value  # go to an index and put a value there
        # Start at None, count backwards by 1 until we get to the index we selected (2), shift everything over by 1.
        for index in range(self.count, index, -1):
            # index -1 because we want to set the index at what is before it since shifting each one over.
            self.storage[index] = selfstorage[index - 1]
        # insert value at index
        self.storage[index] = value
        self.count += 1

# Append is 0(1) - sometimes O(n) if we call double size, but we amortize (call it O(1) b/c more often than not thats what it is)
    def append(self, value):
        # Check is array is full
        if self.count == self.capacity:
            self.double_size()
        # If array isnt full, insert value at end of array(find end using self.count)
        self.storage[self.count] = value
        self.count += 1

# Double size is O(n)
    def double_size(self):
        self.capacity = self.capacity * 2  # double our capacity
        # create a new empty array with that doubled capacity
        new_array = [None] * self.capacity
        # copy everything over from the old array
        for index in range(self.count):
            new_array[index] = self.storage[index]
        self.storage = new_array


# Time complexity = O(n^2)
def add_to_front(n):
    x = []
    for index in range(0, n):  # O(n)
        x.insert(index, n-1)  # O(n)
    return x

# Time complexity = O(n). May need to resize


def add_to_back(n):
    x = []
       for index in range(0, n):  # O(n)
            x.append(index)  # O(1)
        return x

# Its like adding to back, but never need to resize so should be faster.
def pre_allocate(n):
    x = None * n # make array as big as we need it to be
    for index in range(0,n):
        x[index] = index
    return x



n = 100000000
start_time = time.time()
add_to_front(n) # O(n^2)
end_time = time.time()

print("Time to add to front", end_time - start_time) #2.09

n = 5000
start_time = time.time()
add_to_back(n) # O(n)
end_time = time.time()

print("Time to add to back", end_time - start_time) # 0.9

n = 5000
start_time = time.time()
pre_allocate(n) # O(n)
end_time = time.time()

print("Time to add to back with preallocated space", end_time - start_time) # 0.6
# Still O(n) but faster cause we dont have to create new space sometimes 




# HASHES
hash("myname") # returns "ofjdalkfjdaljkfds". what you get back is the hash.

# What is a hash function? Needs to meet these characteristics.

# Deterministic: For a given input, the output will always be the same.
# Defined output range: For a hash table of size 16, all keys must hash to a value 0-15. For smaller values, this is usually accomplished using the modulo % operation.
# Predictable Speed: Hash functions for hash tables should be lightning fast while cryptographic hashes (like bcrypt) should be very slow.
# Non-invertible: You should not be able to reconstruct the input value from the output. This trait is important in cryptographic hashes but not necessary for general hash tables.

def myFakeHash(word):
    return len(word)

myFakeHash("Reese") # will return 5. Non invertible - we know it returns 5, but cant guess what went into it even though we know what we got out of it. 
myFakeHash("fivee") # --> 5
# Avoid collisions. We dont want these things to return the same thing.


# Hash table - combines an array and a hash function

# Arrays are indexed by numbers. You cant get a value by a given key. 
# Hash function can take a key and give us an index for that key. Then we can go to that index from the key.
# Both are constant time. Can now store strings in constant time. 



# Array = [(key, value), (key, value), None]
# HashFunction = f(key)

# scramble the key and come up with very different values to avoid collisons
def djb2(key):
    # start from a large prime number
    hash_value = 5381

# bit shifting
    # 0b 100010101011001111001
    # 0b 000101010110011110010 # bit shift - delete from front, add to end . This is what we are doing 5 times from hash_value << 5.
    # 0b 001010101100111100100 # bit shift - delete from front, add to end 

    # randomly scramble it using bit shifting
    for char in key:
        hash_value = hash_value + (hash_value << 5) + char

    return hash_value

"I like turtles"
hashlib.sha256() ---> jroeipfpji39009ihgnre

# cryptographic hashes should be slow bc scrambles a lot. want it to be slow to prevent brute forcing.


key = b"mypassword"

n = 10000

start_time = time.time()
for i in range(0, n):
    djb2(key)
end_time = time.time()

print("djb2 run time = ", end_time - start_time)

start_time = time.time()
for i in range(0, n):
    haslib..sha256(n)
end_time = time.time()

print("sha256 run time = ", end_time - start_time)
