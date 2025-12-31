+++
title = 'Review 12/23'
date = 2025-12-23T16:11:36-05:00
series = ['coding-interview']
showSeries = false
series_order = 1
+++

* **LeeCode ID**: [#345 Reverse Vowels of a String](https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=leetcode-75) (Programming language: C)
    1. String을 C로 처리하는데 시간이 많이 걸렸다.
        - C의 string 관련 함수는 모두 null character('\0')를 포함하지 않기 때문에 개발자가 직접 넣어줘야 함 (`strncpy`)
        - Edge case를 code로 표현하는데 서툴렀다.
        - pointer offset을 debugging 하느라 hieh-level logic에 대한 생각을 많이 하지 못했다.
    2. 주어진 test case에 대해서 올바르게 동작하는지 확인을 잘 못했다.
    3. Interviewer가 제공해준 hint를 catch하고 코드로 작업하는 과정을 잘하지 못했고, 나의 fixing 과정을 설명하지 않았다. (큰 문제임)

* **LeetCode ID**: [#334 Increasing Triplet Subsequence](https://leetcode.com/problems/increasing-triplet-subsequence/description/?envType=study-plan-v2&envId=leetcode-75) (Programming language: C)
    1. Patching Mentality (땜질하듯이 주먹구구 식으로 문제를 해결하려는 방식)
        - 사례: When I challenged you on the INT_MAX boundary case, your immediate instinct was to write an extra if statement to "catch" it (if (first == INT_MAX) return false).
        - L4 Assessment: Senior engineers trust their core logic. _They **trace** the main loop to see if it handles the edge case naturally before adding special checks_. Adding special if clauses for edge cases often signals that the candidate is "patching" holes rather than designing a robust system.


* **LeetCode ID**: [#238 Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=leetcode-75) (Programming language: C)
    1. Algorithmic Pattern Recognition
        - Standard patterns (**Prefix Sums** or **Two-Pass Traversal**)를 잘 모르고 있다. 인터뷰에서는 처음 2-3분 이내에 어떤 유형인지 파악하는 것을 요구한다.
            - LeetCode에서 유형별로 코드를 풀면서 패턴을 익히는 것이 필요함.
    2. Micro-Optimization vs. Code Cleanliness
        - 작은 최적화를 위해서 `break`와 같은 statement는 logical bug가 될 수 있으니, 기본 logic에서 handle할 수 있는 경우라면, 코드를 복잡하게 만들지 않는다.
    3. Manual Dry-Running (Tracing)
        - Test case에 대해서 코드가 올바르게 동작하는지 스스로 확인하는 부분이 약하다.
