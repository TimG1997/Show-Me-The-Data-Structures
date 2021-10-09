# Explanation Problem 2 File Recursion

The runtime of this algorithm is O(n). The find_files method calls a find_files_helper function, which checks if the current
path is a file. If it is a file it appends the file to the paths list. 
Else it lists all subdirectories and iterates through them and call itself recursively.
So the overall time complexity is O(n), where n is the number of files and subdirectories in the root directory.

