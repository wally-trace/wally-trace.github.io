---
title: "Review 12/25"
date: 2025-12-25T11:40:30-05:00
# 현재 생성되는 폴더의 부모 폴더 이름을 자동으로 가져와서 series에 넣습니다.
series: ["coding-interview"]
series_order: 2
draft: false
---

> Find 3 easy problems involving arrays.
> 1. Do **not** write code immediately.
> 2. Identify the *Pattern* (Two pointer? Hash Map?).
> 3. Create a Trace Table for an edge case on paper.
> 4. Write the solution trying to use the *fewest lines possible*.

* **LeeCode ID**: [#283 Move Zeroes](https://leetcode.com/problems/move-zeroes/description/?envType=study-plan-v2&envId=leetcode-75) (Programming language: C)
    1. 아직 two pointers 방식을 편하게 사용하는 것이 서툰 것 같다. (Classic pattern에 대한 연습 필요: Sliding Window, Slow/Fast Pointer, Two-Pointer)
        * 프로그래밍의 logic은 맞지만, 복잡(multiple if statements)하다.
        * Google Standard: Engineers look for **standard patterns**. This problem is a classic **"Slow & Fast Pointer"** pattern (or Partition pattern).
            * Golden Logic: "Iterate through the array. If I see a non-zero, move it to the 'slow' pointer position and advance the 'slow' pointer.
        * TODO
            * Stop tring to solve every movement logically. Start categorizing problems.
                * Is this a Sliding Window?
                * Is this a Slow/Fast Pointer?
                * Is this a Two-Pointer from ends? Why? Using a standard pattern reduces liens of code by 50% and eliminates bugs like the "consecutive zero" error you had.

    2. 손으로 테스트케이스를 돌려보는 작업을 해야 한다.
        * The Google Standard: You must catch the bug **before** you write a single line of code.
        * TODO
            * Draw a **Trace Table** on your paper:
                * Write the array: `[1, 0, 0, 2]`
                * Manually move your mental pointers.
                * Only when your manual logic works on the edge case do you start coding

    3. English
        | Instead of saying ... | Say this (Google standard) |
        |---|---|
        |I'd like to find the leftmost... | I will scan for the leftmost...|
        |The array size affect the execution time... | The complexity is linear with respect to the input size N.|
        |Can I write the edge cases? | I will list out the edge cases to ensure coverage|

    4. Clean Code
        * No checking fo -1. No complex `if` conditions. Just "if non-zero, move it to the front"
        * My code:
        ```C
            void moveZeroes (int * nums, int numsSize) {
              if (numsSize == 1) { return ; }
              int zero = -1 ;
              int nonZero = -1 ;
            
              for (int i = 0; i < numsSize; i++) {
                if (zero == -1 && nums[i] == 0) {
                  zero = i ;
                }
                if (nums[i] != 0) {
                  nonZero = i ;
                }
            
                if (zero != -1 && zero < nonZero) {
                  swap(nums, zero, nonZero) ;
                  zero++ ;
                }
              }
            }
        ```
        * Clean Code (pattern):
        ```C
            void moveZeroes(int* nums, int numsSize) {
                int lastNonZeroFoundAt = 0;
                for (int i = 0; i < numsSize; i++) {
                    if (nums[i] != 0) {
                        // Swap current non-zero with the element at the write pointer
                        int temp = nums[lastNonZeroFoundAt];
                        nums[lastNonZeroFoundAt++] = nums[i];
                        nums[i] = temp;
                    }
                }
            }
        ```
