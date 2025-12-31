---
title: "Map"
date: 2025-12-31T10:15:03-05:00
series: ["c++"]
#series_order: 1
draft: false
---

C++로 LeetCode에서 HashMap을 사용하려면 **`std::unordered_map`**을 사용해야 합니다.

C++ 문법이 낯설더라도 알고리즘 문제 풀이에 필요한 핵심 패턴은 정해져 있습니다. 가장 자주 쓰이는 문법과 대표적인 예제인 **Two Sum** 문제를 통해 설명해 드리겠습니다.

---

### 1. C++ HashMap 핵심 문법 (`std::unordered_map`)

C++에서는 `map`이 아닌 `unordered_map`이 해시맵(Hash Table)입니다. (`map`은 정렬된 트리 구조라 속도가 다릅니다.)

#### 1) 선언 및 라이브러리 추가

```cpp
#include <unordered_map> // 필수 헤더
#include <iostream>

using namespace std; // std:: 생략 가능

// 선언: unordered_map<Key타입, Value타입> 변수명;
unordered_map<string, int> myMap;

```

#### 2) 데이터 추가 (Insert)

```cpp
myMap["apple"] = 10;        // 가장 직관적인 방법 (추천)
myMap.insert({"banana", 20});

```

#### 3) 데이터 검색 (Find) - **가장 중요!**

LeetCode에서 "이 키가 존재하는가?"를 확인할 때 `find()` 메서드를 사용합니다.

```cpp
// "apple"이라는 키가 있는지 확인
if (myMap.find("apple") != myMap.end()) {
    // 찾는 키가 맵의 끝(end)이 아니라면 존재한다는 뜻
    cout << "Found! Value: " << myMap["apple"] << endl;
} else {
    cout << "Not Found" << endl;
}

```

> **주의:** C++에서는 Python의 `if key in dict:` 처럼 간단하지 않고, **이터레이터(Iterator)가 끝(`end()`)에 도달했는지**로 존재 여부를 판단합니다.  
> * `auto k = myMap["apple"]`처럼 대괄호를 사용해서 값을 찾으면, 맵에 키가 없을 경우 자동으로 **새로운 요소를 삽입(Default insertion)**을 하는 부작용이 있을 수 있다.

#### 4) 순회 (Loop)

```cpp
// auto 키워드를 쓰면 타입 추론이 되어 편리합니다.
for (auto const& [key, val] : myMap) {
    cout << key << ": " << val << endl;
}

```

---

### 2. 실전 적용: LeetCode #1 Two Sum

이 문제는 "배열에서 두 수를 더해 Target이 되는 두 인덱스를 찾아라"는 문제입니다.

**전략:**

1. 숫자를 하나씩 확인합니다.
2. `Target - 현재숫자` (필요한 짝꿍 숫자)가 이미 해시맵에 있는지 확인합니다.
3. 있으면 정답을 반환하고, 없으면 `현재숫자`와 `인덱스`를 해시맵에 저장합니다.

#### C++ 솔루션 코드

```cpp
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // Key: 숫자 값, Value: 그 숫자의 인덱스
        unordered_map<int, int> map;

        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i]; // 찾아야 하는 짝꿍 숫자

            // 1. 맵에서 짝꿍 숫자가 있는지 확인 (find)
            if (map.find(complement) != map.end()) {
                // 찾았다면 {짝꿍의 인덱스, 현재 인덱스} 반환
                return {map[complement], i};
            }

            // 2. 못 찾았다면 현재 숫자와 인덱스를 맵에 저장
            map[nums[i]] = i;
        }

        return {}; // 정답이 없는 경우 (문제 조건상 도달 안 함)
    }
};

```

---

### 3. C++ 문제 풀이 팁 (Cheat Sheet)

* **`auto` 키워드 활용:** 변수 타입을 일일이 쓰기 귀찮거나 모를 때 `auto`를 쓰면 컴파일러가 알아서 맞춰줍니다.
* 예: `auto it = map.find(key);`


* **대괄호 `[]` 주의:** `val = map[key]`를 할 때, 만약 `key`가 맵에 없으면 C++은 **자동으로 키를 생성하고 값을 0으로 초기화**해버립니다. 단순히 있는지 확인할 때는 반드시 `find()`를 쓰세요.
* **헤더 파일:** LeetCode 에디터는 대부분 헤더가 포함되어 있지만, 로컬에서 연습할 때는 `#include <unordered_map>`, `#include <vector>`, `#include <string>` 등을 꼭 넣어주세요.

---

### 4. `map` vs `unordered_map` 차이점

두 컨테이너 모두 `key-value` 쌍을 저장하지만, **내부 구현 방식**과 **성능**에서 결정적인 차이가 있습니다. LeetCode 같은 알고리즘 테스트에서는 **속도** 때문에 90% 이상 `unordered_map`을 사용합니다.

| 비교 항목 | `std::map` | `std::unordered_map` |
| --- | --- | --- |
| **내부 구조** | **Red-Black Tree** (이진 탐색 트리) | **Hash Table** (해시 테이블) |
| **정렬 여부** | Key를 기준으로 **자동 정렬됨** (오름차순) | **정렬되지 않음** (입력 순서와 무관하게 뒤섞임) |
| **탐색 시간** |  - 데이터가 많아지면 조금 느려짐 | **** - 데이터 양과 상관없이 즉시 찾음 (평균) |
| **사용 시점** | 순서가 중요하거나 범위 검색(Range Search)이 필요할 때 | **단순히 데이터 존재 여부나 값을 빨리 찾을 때** |

**요약:**

* 문제에서 "순서대로 출력하라"는 말이 없으면 무조건 **`unordered_map`**이 빠릅니다.
* `map`은 데이터를 넣을 때마다 정렬 비용이 발생하여  시간이 걸리지만, `unordered_map`은 $O(1)$입니다.

---

### 5. `for` 문에서 `const`와 `&`를 사용하는 이유

```cpp
// 예시 코드
for (auto const& [key, val] : myMap) { ... }

```

이 구문은 효율성과 안전성을 위해 사용하는 C++의 표준적인 관용구(Idiom)입니다. `&`와 `const`를 나눠서 설명해 드릴게요.

#### 1) `&` (Reference, 참조)를 쓰는 이유: "복사 비용 방지"

C++은 기본적으로 변수를 대입하면 **값을 복사(Copy)**합니다.

* `&` 없이 `for (auto item : myMap)`을 쓰면, 맵에 있는 데이터를 매 반복마다 **새로운 메모리 공간에 복사**해서 `item` 변수를 만듭니다.
* 데이터가 단순 `int`라면 상관없지만, 문자열(`string`)이나 거대한 객체라면 복사하는 데 시간이 오래 걸리고 메모리 낭비가 심합니다.
* `&`를 붙이면 "복사하지 말고, 맵에 있는 **원본 데이터 자체를 가리켜라(참조해라)**"는 뜻이 되어 속도가 훨씬 빨라집니다.
* 하지만, Primitive type (`int`, `char`, `float`, `double`, `bool`)과 같이 크기가 작고 복사가 저렴한 경우에는 `&` 대신 값을 바로 복사하는 것이 더 저렴하다.
    * 보통 `int`는 4 바이트이기 때문에 한번에 8바이트를 처리하는 64비트(8바이트)시스템에서 `int`를 복사하는 것이 더 권장된다. 메모리 주소(8바이트 포인터)를 참조(dereference)하는 추가 단계가 없기 때문임.

#### 2) `const` (Constant, 상수)를 쓰는 이유: "수정 방지(안전)"

* `&`를 써서 원본을 참조하고 있는데, 실수로 반복문 안에서 `key`나 `val` 값을 바꿔버리면 **원본 데이터가 망가집니다.**
* `const`를 붙이면 "원본을 보기는 하되, **절대 수정하지 않겠다(Read-only)**"라고 선언하는 것입니다. 컴파일러가 수정 시도를 에러로 잡아줍니다.

**결론:** Primitive type이 아닌 데이터를 단순히 읽기만 할 때는 **`const &` (읽기 전용 참조)**가 국룰(Best Practice)입니다.

---

### 6. `return { }` 의 의미

`return {}`은 C++11부터 도입된 **유니폼 초기화(Uniform Initialization)** 문법입니다. 함수의 **반환 타입(Return Type)**에 맞춰서 "알아서 적절한 객체를 만들어 반환하라"는 뜻입니다.

#### 상황 1: 정답을 못 찾았을 때 (빈 객체 반환)

```cpp
vector<int> twoSum(...) {
    // ... 로직 ...
    return {}; // "빈 vector<int>를 만들어서 반환해"
}

```

* 함수의 반환 타입이 `vector<int>`이므로, `return vector<int>();`와 똑같은 의미입니다. 즉, 비어있는 벡터 `[]`를 반환합니다.

#### 상황 2: 정답을 찾았을 때 (값 채워서 반환)

```cpp
// 1. {값1, 값2} 형태로 리턴하면
return {map[complement], i}; 

// 2. 컴파일러가 "아, 반환 타입이 vector<int>니까"라고 인식하고
// 3. 자동으로 아래와 같이 변환해서 처리합니다.
vector<int> temp = {map[complement], i};
return temp;

```

* 과거 C++(C++98)에서는 `vector`를 만들고 `push_back`을 한 뒤 리턴해야 했지만, 이제는 중괄호 `{ }` 만으로 즉석에서 객체를 생성해 반환할 수 있어 코드가 훨씬 간결해졌습니다.

