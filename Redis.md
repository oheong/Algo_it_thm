# Redis

##### Redis란 무엇일까?

캐시 시스템으로, 모든 데이터를 메모리에 저장하고 조회한다.

인메모리 DB임.

NoSQL. Key-value 형태로 데이터가 저장된다.



특징

```text
- 영속성을 지원하는 인메모리 데이터 저장소
- 읽기 성능 증대를 위한 서버 측 복제를 지원
- 쓰기 성능 증대를 위한 클라이언트 측 샤딩(Sharding) 지원
- 다양한 서비스에서 사용되며 검증된 기술
- 문자열, 리스트, 해시, 셋, 정렬된 셋과 같은 다양한 데이터형을 지원.
- 메모리 저장소임에도 불구하고 많은 데이터형을 지원하므로 다양한 기능을 구현
```



##### Redis 영속성

지속성을 보장하기위해 데이터를 disk에도 저장할 수 있다.

서버가 내려가더라도 disk에 저장된 데이터를 읽어 메모리에 로딩한다.

- 데이터를 disk에 저장하는 방식
  1. RDB(Snapshotting) 방식
     순간적으로 메모리에 있는 내용 전체를 디스크에 옮겨담음
  2. AOF(Append On File) 방식
     레디스의 모든 write/update 연산 자체를 모두 log 파일에 기록



##### 흔히 사용하는 Map의 구조와 비슷하다고 생각하면 된다.



DBMS를 이용한다면 DB에 데이터를 저장하고, 저장된 데이터를 정렬하여 읽어오는 과정에서 디스크에 직접 접근을 해야하기 때문에시간이 더 걸린다. 이 때, In-Memory DB인 Redis를 이용하고 레디스를 제공하는 Sorted-Set이라는 자료구조를 사용하면 더 빠르고 간단하게 데이터를 정렬할 수 있음.







이거 읽어보면 좋을듯
[몽고db, redis](https://meetup.toast.com/posts/274)