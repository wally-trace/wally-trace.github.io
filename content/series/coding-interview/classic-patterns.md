---
title: "Classic Patterns"
date: 2025-12-25T12:36:56-05:00
# 현재 생성되는 폴더의 부모 폴더 이름을 자동으로 가져와서 series에 넣습니다.
series: ["coding-interview"]
series_order: 3
math: true
draft: false
---

### 1. Array/String
$O(N^2) \rightarrow O(N)$를 요구하는 문제에서 자주 등장함.
* **Two Pointer**: 두 개의 포인터를 양 끝이나 특정 위치에서 시작하여 서로 조작하며 조건을 만족하는 값을 찾는다.
    * 사용 시기: 정렬된 배열에서 쌍(pari) 찾기, 문자열 뒤집기, Palindrome 확인
* **Sliding Window**: 고정되거나 가변적인 크기의 창(windows)을 데이터 위에서 이동시키며 부분 배열/문자열의 특성을 계산한다. (3Sum, Container w/ most water, Trapping rain water)
    * 사용 시기: 연속된 부분 배열(subarray)의 최대/최소 합, 가장 긴 부분 문자열(substring) 문제 (Longest substring w/o repeating characters, Minimun window substring)

### 2. Graphs & Search
* **BFS**: Queue를 사용하여 가까운 노드부터 탐색한다.
    * 사용 시기: 가중치가 없는 그래프에서 최단 거리(shortest path), 레벨(level) 단위 탐색 (Word ladder, Rotting oranges)
* **DFS**: Stack이나 재귀를 사용하여 갈 수 있는 만큼 깊게 탐색한다.
    * 사용 시기: 미로 찾기, 연결된 구성요소(Connected Components) 찾기, 사이클 탐지 (Number of islands, Max area of island)
* **Backtracking**: DFS의 일종으로, 가능한 모든 경우의 수를 탐색하되 조건에 맞지 않으면 되돌아가서(pruning) 다시 탐색한다.
    * 사용 시기: 순열(permutation), 조합(combination), 부분 집합(subsets), 스도쿠/N-Queen 문제. (Generate parentheses, Subsets)
* **Topological Sort**: 방향성 있는 비순호나 그래프(DAG)에서 순서를 거스르지 않고 나열하는 알고리즘. (주로 Indegree방식 사용)
    * 사용 시기: 선수과목(prerequisite), 빌드 순서(build order), 의존성 해결 문제 (Courser schedule, Alien dictionary)
* **Union-Find / Disjoint Set)**: 여러 노드가 서로 같은 집합에 속해 있는지 빠르게 확인하고 합치는 알고리즘.
    * 사용 시기: 그래프의 연결성 확인, 무방향 그래프 사이클 탐지, 네트워크 연결 (Number of connected components, Redundant connection)
