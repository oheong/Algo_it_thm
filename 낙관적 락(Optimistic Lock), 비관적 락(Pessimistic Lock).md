# 낙관적 락(Optimistic Lock), 비관적 락(Pessimistic Lock)





#### DB 충돌 상황을 개선할 수 있는 방법?

1. 테이블의 row에 접근 시 Lock을 걸고 다른 Lock이 걸려 있지 않은 경우에만 수정이 가능하게 한다.

2. 수정할 때 내가 먼저 이 값을 수정했다고 명시하여 다른 사람이 동일한 조건으로 값을 수정할 수 없게 한다.



#### 비관적 락(Pessimistic Lock)

Reeatable Read || Serializable 정도의 격리성 수준에서 가능하다.

##### 트랜잭션이 시작될 때 Shared Lock || Exclusive Lock을 걸고 시작하는 방법.

Shared Lock을 걸게되면 write를 하기 위해서 Exclusive Lock을 얻어야 하는데, Shared Lock이 다른 트랜잭션에 의해 걸려있으면 해당 Lock을 얻지 못해서 업데이트를 할 수 없다.

수정을 하기위해서는 해당 트랜잭션을 제외한 모든 트랜잭션이 종료(commit)되어 있어야 함.

##### Transaction을 이용하여 충돌을 예방하는 것이 비관적 락(Pessimistic Lock)이다.



#### 낙관적 락(Optimistic Lock)

특정 트랜잭션이 먼저 값을 수정했다고 명시하여 다른 트랜잭션이 동일한 조건으로 값을 수정할 수 없게 하는 것.

##### DB에서 제공해주는 특징을 이용하는 것이 아닌 Application Level에서 잡아주는 Lock이다.

ex) 같은 row에 각기 다른 두 개의 수정 요청이 있었지만, 하나가 업데이트 됨에 따라 version이 변경되었기때문에 뒤의 수정요청을 반영되지 않음.

##### version과 같은 별도의 컬럼을 추가하여 충돌적인 업데이트를 막음. version 뿐만 아니라, hashcode, timestamp를 이용하기도 한다.


