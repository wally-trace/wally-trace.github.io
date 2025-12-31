+++
title = 'Smart Pointer'
date = 2025-12-23T17:09:46-05:00
series = ['c++']
series_order = 1
+++

C++에서는 기본적으로 `new`로 객체를 생성하고 `delete`로 해제해야 한다.
하지만, 이 작업을 사람이 직접 관리하다 보면 메모리 누수(memory leak), 이중 해제(double free), dangling pointer같은 문제가 발생하게 된다.

그래서 C++에서는 스마트 포인터(smart pointer)를 사용함으로써 메모리를 안전하게 자동 관리하도록 한다.
* 객체의 소유권을 명확히 하고, 소유권이 끝나면 자동으로 메모리를 정리한다.

**Smart pointer**
* Smart pointer는 객체가 범위(scope)를 벗어날 때 destructor가 자동으로 메모리를 해제한다.
* C에서는 할당된 메모리에 대해서 개발자가 `free()`를 해줘야 하는 반면에, C++에서는 compiler가 삽입한 destructor가 자동으로 해제한다.

**Move Constructor**
* 객체가 가지고 있는 자원(메모리 등)을 복사하지 않고, '그대로 전달(transfer)'하는 생성자이다.
    - 메모리 주소를 복사하고, 기존 객체의 포인터는 `nullptr`로 만든다.

**std::unique_ptr**
* 특정 자원을 '단 한명'만 가질 수 있도록 설계된 smart pointer다(즉, 복사가 불가능).
    - 사용하는 스코프가 끝나면 바로 해제한다.
    - 복사는 안되지만 `std::move`를 통해서 다른 `unique_ptr`에게 넘겨줄 수는 있다.
    - C 라이브러리 리소스 관리를 위해 custom deleter를 함께 사용하여 효과적으로 메모리를 관리한다.
        ```C++
        void uniquePtrExpertExample() {
        auto fileDeleter = [](FILE* f) {
          if (f) {
            std::cout << "Closing file automatically...\n";
            fclose(f);
          }
        };

        // unique_ptr<자원타입, 삭제자타입>
        std::unique_ptr<FILE, decltype(fileDeleter)> myFile(fopen("test.txt", "w"), fileDeleter);

        // 여기서 함수가 종료되면(즉, scope을 벗어나면) fclose가 자동으로 실행됩니다. (RAII)
        }
        ```

**std::shared_ptr**
* 특정 자원을 공동 소유 할 수 있다.
    - 해당 자원을 참조하고 있는 reference count가 0이 되면 해제한다.
    - 복사가 가능하며, 복사할 경우 reference count가 증가한다.
