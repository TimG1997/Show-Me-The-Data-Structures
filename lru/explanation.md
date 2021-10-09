### Design Choices

The task was to implement a Cache, which uses LRU (Least Recently Used)
as eviction strategy. If the full capacity of the cache is reached the least recently used element should be evicted (deleted).

I used a OrderedDict, which keeps track of the insertion order of elements. 

### Time complexity

The OrderedDict also allows removing elements at an arbitrary position in O(1), because it uses a doubly-linked-list as underlying data structure.

So everytime, when an element is retrieved from the cache it gets deleted and inserted again, which ensures, that the last used element is at the end of the OrderedDict and the least recently used one is at the front.

If the capacity is full and a new element is inserted the first element in the OrderedDict (= the least recently used one) will get removed to make space for the new element.