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
<p align="center">
  <img width="685" alt="Screenshot 2024-01-15 at 8 54 17 AM" src="https://github.com/DuongNg2911/LeetCode-Problems-Solutions/assets/127082369/0b9cb562-4461-4fb7-93f0-6b5589c60cf6">
</p>
