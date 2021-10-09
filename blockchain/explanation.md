### Design Choices

For the blockchain I've implemented an append method, which appends a block with the data passed to the method.
The data gets hashed with SHA-256.

### Time Complexity

The appending of a block is O(1), because I have a reference to the last block in the blockchain. So I don't have to iterate
through the whole blockchain to find the previous_hash for the new block.

### Space Complexity

The space complexity is O(n) since all blocks have to be stored (n is the number of blocks).