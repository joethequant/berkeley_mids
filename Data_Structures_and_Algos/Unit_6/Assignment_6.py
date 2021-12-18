class MyTable:

    class _item:
        ### Over kill for this but why not but why not.  It makes it more correct and pretty.
        def __init__(self, k, v) -> None:
            self._key = k
            self._value = v

        def __str__(self):
            return f'{self._value}'
        
        def __repr__(self) -> str:
            return f'{self._key}: {self._value}'

        def __eq__(self, other):
            return self._key == other._key

        def __ne__(self, other):
            return not (self == other)

        def __lt__(self, other):
            return self._key < other._key

    def __init__(self, size):

        self._table_length = size
        self._table = [None]*size
        self.keys = [None]*size
        self.values = [None]*size

    def __str__(self):
            return f'{self._table}'
        
    def __repr__(self) -> str:
        return f'{self._table}'

    def __setitem__(self, key, value):

        found_hash = self._hash_find(key)
        if found_hash:
            self._table[found_hash] = self._item(key, value)
            self.keys[found_hash] = key
            self.values[found_hash] = value
        else:
            hash_key = self._hash_next_empty(key)
            if self.keys[hash_key] is None:
                self._table[hash_key] = self._item(key, value)
                self.keys[hash_key] = key
                self.values[hash_key] = value

    def __getitem__(self, key):

        hashed_key = self._hash_find(key)

        if hashed_key is None:
            return 'Key not in table.' 
        else: 
            return self._table[hashed_key]

    def __delitem__(self, key):
        hashed_key = self._hash_find(key)

        if hashed_key is None:
            return 'Key not in table.' 
        else: 
            self._table[hashed_key] = self._item('deleted', 'deleted')
            self.keys[hashed_key] = 'deleted'
            self.values[hashed_key] = 'deleted'

    def _is_empty(self, hash_key):
        return (self.keys[hash_key] is None) or (self.keys[hash_key] == 'deleted') 

    def _hash_next_empty(self, key):
        initial_hash_key = ord(key) % self._table_length

        is_empty = self._is_empty(initial_hash_key)

        while not is_empty:
            initial_hash_key += 1
            is_empty = self._is_empty(initial_hash_key)

        return initial_hash_key

    def _hash_find(self, key):
        hash_key = ord(key) % self._table_length

        # is_empty = self._is_empty(hash_key)
        found_key = self.keys[hash_key]

        while (found_key is not key) and (found_key is not None):
                hash_key = (hash_key + 1) % self._table_length
                found_key = self.keys[hash_key]
                # is_empty = self._is_empty(hash_key)

        if self.keys[hash_key] == key:
            return hash_key
        else:
            return None
            