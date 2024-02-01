# Solution Explained

## Approach
- Sort the input array
- At each subarray of size 3, check the difference between the last and the first element, whether it is less than or equal to k, then append the subarray to the result and return [] otherwise.

## Complexity
- Time Complexity: O(nlogn)
- Space Complexity: O(n)
## Result
<p align="center">
  <img width="662" alt="Screenshot 2024-02-01 at 10 01 44 PM" src="https://github.com/DuongNg2911/LeetCode-Problems-Solutions/assets/127082369/b34a09b2-0041-4781-9cb9-50e5630d56df">
</p>
