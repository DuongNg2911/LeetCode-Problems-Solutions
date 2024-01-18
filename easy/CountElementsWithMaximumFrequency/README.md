# Solution Explained

## Approach
- Created a hash table to count the frequencies among all elements of the input array
- Iterated over all keys inside the hash table and checked if the value of each key whether was greater than or equal to the current max
- If the value was greater than the current max, set the value of the current max and final result to that value
- If the value was equal to the current max, then add that value to the final result
  
## Complexity
- Time Complexity: O(n)
- Space Complexity: O(n)

## Result
<p align="center">
  <img width="659" alt="Screenshot 2024-01-18 at 8 22 13 AM" src="https://github.com/DuongNg2911/LeetCode-Problems-Solutions/assets/127082369/fceb0876-bb55-438f-b88c-504aa507c45b">
</p>
