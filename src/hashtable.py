# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

# 2 parts of a hash table - array and hash function
# hash function - turn a string into a number.
# hash table - uses hash function ^ to get an index in our storage array
# no longer have to iterate to find values! Can use hash function to look up where we stored something
# Collisions - hash function puts out same value for 2 different strings


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.count = 0

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''

        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity
    # Given a key, the algorithm computes an index that suggests where the entry can be found:

    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''

        # find index of given key with hash_mod function above
        index = self._hash_mod(key)

        # check in storage to see if someting is at that index already
        if self.storage[index] is not None:
            print("WARNING you are overriding stuff ")

            # insert (key, value) pair at that index
            self.storage[index] = (key, value)

            self.count += 1

        else:
             # insert (key, value) pair at that index
            self.storage[index] = (key, value)

    def remove(self, key):
        '''
            Remove the value stored with the given key.

            Print a warning if the key is not found.

            Fill this in.
            '''
        # find index of given key with hash_mod function above
        index = self._hash_mod(key)
        # set value at that index to None
        self.storage[index] = None

        self.count -= 1

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # find index of given key with hash_mod function above
        index = self._hash_mod(key)
        # return value at that given index
        return self.storage[index]

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity = self.capacity * 2  # double capacity
        new_storage = [None] * self.capactiy
        # We dont know what index stuff will be stored at like we did with the dynamic array, so need to iterate through entire array
        # ex: [None, (key, value), None, None, (key, value) ]
        # copy stuff into new array
        for index in (len(self.storage)):
            new_storage[index] = old_storage[index]


if __name__ == "__main__":
    ht = HashTable(2)

print(ht.insert("line_1", "Tiny hash table"))
ht.insert("line_2", "Filled beyond capacity")
ht.insert("line_3", "Linked list saves the day!")

print("")

# Test storing beyond capacity
print(ht.retrieve("line_1"))
print(ht.retrieve("line_2"))
print(ht.retrieve("line_3"))

# Test resizing
old_capacity = len(ht.storage)
ht.resize()
new_capacity = len(ht.storage)

print(f"\nResized from {old_capacity} to {new_capacity}.\n")

# Test if data intact after resizing
print(ht.retrieve("line_1"))
print(ht.retrieve("line_2"))
print(ht.retrieve("line_3"))

print("")
