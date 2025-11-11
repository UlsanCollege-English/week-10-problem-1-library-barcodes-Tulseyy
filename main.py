"""
HW01 — Library Barcodes → Book Titles (Chaining)

Implement a tiny hash table with chaining.
Do not add type hints. Use only the standard library.
"""

def make_table(m):
    """Return a new table with m empty buckets (lists)."""
    # TODO Step 4: build the data structure (list of lists)
    return [[] for _ in range(m)]

def hash_basic(s):
    """Return a simple integer hash for string s.
    Hint: sum ordinals of characters.
    """
    # TODO Step 5→6: compute a stable integer from s
    return sum(ord(c) for c in s)

def put(t, key, value):
    """Insert or overwrite (key, value) in table t using chaining."""
    # TODO Steps 4–6: compute index, scan bucket, overwrite or append
    index = hash_basic(key) % len(t)
    bucket = t[index]
    
    # Scan for existing key and overwrite if found
    for i, (k, v) in enumerate(bucket):
        if k == key:
            bucket[i] = (key, value)
            return
    
    # If not found, append new pair
    bucket.append((key, value))

def get(t, key):
    """Return value for key or None if not present."""
    # TODO Steps 4–6: compute index, scan bucket, return value or None
    index = hash_basic(key) % len(t)
    bucket = t[index]
    
    for k, v in bucket:
        if k == key:
            return v
    
    return None

def has_key(t, key):
    """Return True if key exists in table t; else False."""
    # TODO Steps 4–6: scan the correct bucket
    return get(t, key) is not None

def size(t):
    """Return total number of stored pairs across all buckets."""
    # TODO Step 4: count all pairs
    return sum(len(bucket) for bucket in t)

if __name__ == "__main__":
    # Optional manual check (not graded)
    # TODO Step 7: try a tiny run by yourself
    pass
