### Design Choices

I've used a recursive approach to this problem. The base case checks wether a user is in the current group. If the user
is not in the current group the method gets called recursively for every group existing in the parent group.

### Time complexity

The time complexity is O(n), where n is the number of users and groups.

### Space complexity

The space complexity is O(n), where n is the number of groups and users