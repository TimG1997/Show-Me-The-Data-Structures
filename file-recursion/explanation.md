### Design choices

I've used a recursive approach to this problem. The base case of the recursion is, if the path points to a file. If the
path doesn't point to a file I call the function again with the next directory path.

### Time Complexity

The runtime of this algorithm is O(n). The find_files method calls a find_files_helper function, which checks if the
current path is a file. If it is a file it appends the file to the paths list. Else it lists all subdirectories and
iterates through them and call itself recursively. So the overall time complexity is O(n), where n is the number of
files and subdirectories in the root directory.

### Space Complexity

In the worst case the space complexity is O(mn) since maybe you have to hold n files and m sub-directories, which have
to be looked through.