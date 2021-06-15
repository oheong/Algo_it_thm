# SQL MERGE문

```sql
MERGE INTO
```

java단에서 복잡하게 짰던 로직을 좀 더 쉽게 만들어 줌!



##### merge 

- 충돌나지 않게 합친다
- table에 있는 데이터는 변경만 하고, 없는 데이터는 삽입을 하여 적절하게 통합



##### 즉,  <span style="color:red">데이터가 이미 존재하면 UPDATE</span> !!!! <span style="color:red">존재하지 않으면 INSERT</span> !!!!

```sql
merge into [1. 테이블 명] -- update||insert 할 테이블 명
using [2. 조회 서브 쿼리] -- merge into 절과 동일한 테이블이라면 dual 사용
on [1과 2의 조인 조건] -- update, insert로 나뉠 조건
when matched then -- on절 조건이랑 일치하는 경우
update set
[컬럼] = [값], ... -- on절에 사용한 컬럼은 update 불가!
when not matched then -- on절 조건이랑 일치 안하는경우
insert into [테이블 이름](컬럼, ...)
values (값, ...)
```

=> update만 가능한게 아니라 상황에 따라서는 delete도 가능함

