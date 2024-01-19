# Solution Explained

## Approach
- Used Bottom-up approach
- Started from the second row of the matrix, for each element [r, c], modified it with the minimum number between ([r,c] + [r-1, c], [r,c] +
[r, c], [r, c] + [r-1, c+1]) 

## Complexity
- Time Complexity: O(n^2)
- Space Complexity: O(1)

## Result
<p align="center">
  <img width="701" alt="Screenshot 2024-01-19 at 9 27 47 AM" src="https://github.com/DuongNg2911/LeetCode-Problems-Solutions/assets/127082369/fc1bf8fe-a089-4822-8c60-ab43f7a26e13">
</p>

