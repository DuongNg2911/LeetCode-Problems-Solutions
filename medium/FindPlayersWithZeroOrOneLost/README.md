# Solution Explained

## Approach
- Created a hash table to count the number of lost matches among each player
- Divided the hash keys into 2 different subsets. The first subset contains keys with a 0 value while the other holds keys with a 1 value
- Sorted these two subsets using quicksort
- Remember to delete the hash table for better memory usage

## Complexity
- Time Complexity: O(nlogn)
- Space Complexity: O(n)

## Result


