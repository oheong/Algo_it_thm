# JPA랑 친해지는중,,,,,,



##### VO(Value Object)

- 객체 그 자체
- 로직 있을 수 있음

##### Entity

- DB테이블과 맵핑
- RDBMS에서 Table을 객체화 시킨 것으로 생각하면 됨
- id로 각각의 Entity 구분
- 로직 있을 수 있음

##### DTO(Data Transfer Object)

- 계층간 데이터 교환을 위해 사용.
- getter, setter만 있음 (로직x)

``` text
Client

↕️[DTO]

Controller

↕️[DTO]

Service

↕️[DTO]

Dao (=Repository)

↕️[Entity]

DB
```



##### Entity 구성 요소

- @Entity : Entity 클래스임을 명시함

- @Table(name="테이블명") : 매핑할 테이블명 지정

- @Getter @Setter : 게터세터 메소드 자동 생성 (Lombok)
  ❗️Entity에서는 Setter금지❗️❗️❗️❗️❗️❗️

- @NoArgsConstructor @AllArgsConstructor : 기본생성자, 필드값을 모두 포함한 생성자 자동 생성(Lombok)

- @Id : 기본 키. 모든 Entity 클래스는 @Id설정 필요. (복합키 : @Embeddedid)

- @GeneratedBalue(stratege = GenerationType.IDENTITY) : JPA가 기본키 생성하도록

- @Column : Entity 클래스의 모든 필드는 DB 컬럼과 매핑되어있어서 따로 명시하지 않아도 됨. 하지만 매핑될 컬럼 명이 다르거나, 디폴트 값이 다른 경우에 사용한다. (default : 카멜->소문자 스네이크, length = 225, nullable = true)

- ##### @Builder 

```markdown
@builder를 사용할 때 장점
1. 인자가 많을 경우 쉽고 안전하게 객체 생성 가능
ex) 인자 많을때 보기 어려움
	NutritionFacts cocaCola = new NutritionFacts(240, 8, 100, 3, 35, 27);
	NutritionFacts mountainDew = new NutritionFacts(230, 10);
2. 인자의 순서와 상관 없이 객체 생성 가능
3. 적절한 책임을 이름에 부여하여 가독성 향상
4. setter 메소드가 없기 때문에 변경 불가능 객체를 만들 수 있다.
5. 한번에 객체를 생성하므로 객체 일관성이 깨지지 않는다.

Service단에서 builder를 사용해 객체를 생성한다
```





##### Repository (@Repository)

> 스프링 부트에서는 기본적인 CRUD가 가능하도록 JpaRepository 인터페이스 제공 => JpaRepository 인터페이스를 상속하기만 하면 @Repository어노테이션 추가할 필요 없음



<기본기능>

| method    | 기능                                    |
| --------- | --------------------------------------- |
| save()    | 레코드 저장(insert, update)             |
| findOne() | primary key로 레코드 하나 찾기          |
| findAll() | 전체 레코드 불러오기. 정렬, 페이징 가능 |
| count()   | 레코드 갯수                             |
| delete()  | 레코드 삭제                             |
❗️MICHIN❗️ JPA는 update만을 위한 메소드는 없음❗️❗️❗️❗️

대신 save()가 update의 기능도 수행하기 때문에, 데이터 변경 뒤 save()하면 됨❗️



기본 기능 외 조회 기능 추가 하고싶으면 규칙에 맞는 메소드를 추가 해야 함

| method         | 설명                                                         |
| -------------- | ------------------------------------------------------------ |
| findBy로 시작  | 쿼리를 요청하는 메소드임을 알림<br />반환형이 Entity이면 하나의 결과만을 전달<br />List면 쿼리에 해당하는 모든 객체 전달 |
| countBy로 시작 | 쿼리 결과 레코드 수를 요청하는 메소드임을 알림               |



쿼리 메소드에 포함할 수 있는 키워드

| 키워드           | 예시                                              | 설명                               |
| ---------------- | ------------------------------------------------- | ---------------------------------- |
| And              | findByEmailAndUserId(String email, String userId) | 여러 필드를 and로 검색             |
| Or               | findByEmailOrUserId(String email, String userId)  | 여러 필드를 or로 검색              |
| Between          | findByBirthdayBetween(Date fromDate, Date toDate) | 필드의 두 값 사이에 있는 항목 검색 |
| LessThan         | findByAgeLessThan(int age)                        | 작은 항목 검색                     |
| GreaterThanEqual | findByAgeGreaterThanEqual(int age)                | 크거나 같은 항목 검색              |
| Like             | findByNameLike(String name)                       | like 검색                          |
| IsNull           | findByHobbyIsNull(String hobby)                   | null인 항목 검색                   |
| In               |                                                   | 여러 값 중에 하나인 항목 검색      |
| OrderBy          | findByEmailOrderByNameAsc(String email)           | 검색 결과를 정렬하여 전달          |

[JPA 레퍼런스]( http://docs.spring.io/spring-data/jpa/docs/1.10.1.RELEASE/reference/html/#jpa.sample-app.finders.strategies)



