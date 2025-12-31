---
title: "Sliding Window"
date: 2025-12-31T14:31:49-05:00
# 현재 생성되는 폴더의 부모 폴더 이름을 자동으로 가져와서 series에 넣습니다.
series: ["coding-pattern"]
#series_order: 1
draft: false
---

* Sliding Window는 array나 string에서 특정 조건을 만족하는 연속된 elements를 찾기 위해서 사용하는 패턴으로써, 핵심은 **중복된 연산을 제거**하는 것이다.
    * Brute Force: 구간을 이동할 때마다 구간 내의 모든 값을 다시 계산한다.
	* Sliding Window: 윈도우가 한 칸 이동할 때마다 새로 들어오는 값은 더하고, 뒤로 빠지는 값은 빼는 방식으로 연산량을 줄인다.
* 해당 패턴을 떠올려야 하는 키워드:
    * 연속된(Continuous / Contiguous) 데이터
	* Subarray, Substring
	* 최대 합, 최소 길이, 모든 아나그램 찾기

---
* LeetCode ID:[643. Maximum Average Subarray 1](https://leetcode.com/problems/maximum-average-subarray-i/description/?envType=study-plan-v2&envId=leetcode-75)
    * `i = k`에서 시작하는 이유를 고민하기
	* `i - k`는 out-of-bound를 예방하기 위함
	* `max_sum`을 사용하면 왜 효과적인가?
    ```C++
    #include <vector>
    #include <algorithm>
    #include <iostream>
    
    class Solution {
    public:
        double findMaxAverage(std::vector<int>& nums, int k) {
            // Use double to prevent precision loss during large additions
            double current_sum = 0;
    
            // Phase 1: Sum the first window (indices 0 to k-1)
            for (int i = 0; i < k; i++) {
                current_sum += nums[i];
            }
    
            // Initialize max_sum with the sum of the very first window
            double max_sum = current_sum;
    
            // Phase 2: Slide the window (start lead pointer at index k)
            // nums[i] is the element entering, nums[i - k] is the element leaving
            for (int i = k; i < nums.size(); i++) {
                current_sum += nums[i] - nums[i - k];
    			max_sum = std::max(max_sum, current_sum) ;
            }
    
            // Final Step: Perform division only once for maximum accuracy
            return max_sum / k;
        }
    };
    ```
