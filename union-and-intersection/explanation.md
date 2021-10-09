### Design Choices

I've implemented a to_set() method in the LinkedList class, so a LinkedList can be converted to a set quite easily.
Then I used the built in methods to handle the union and intersection between two sets.

### Time Complexity

The time complexity is O(n) for converting the LinkedList to a Set. The Set operations are in general faster and in the worst case 
they are O(n) (if hash collisions occur).

### Space Complexity

The space complexity is O(n + m), where n is the number of elements in the first list and m is the number of 
elements in the second list.