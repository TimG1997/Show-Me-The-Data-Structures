### Design Choices
I used a dict to store the frequencies of every letter.
I've also used a priority queue to have the frequencies in the right order (ascending from the element with the lowest frequency).
Then I've built a custom Node class to be able to represent the Huffman tree.

### Time Complexity
The time complexity is O(n) since you run through the unencoded/encoded data character by character for determening frequences,
building the queue (creating the huffman dict is < O(n)), creating the encoded string and creating the decoded string.

### Space Complexity
The space complexity is O(n) due to storing the encoded data, the priority queue and the frequencies.
The storing of the rest of the data is O(1)