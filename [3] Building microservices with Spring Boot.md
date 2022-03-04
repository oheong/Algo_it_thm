# [3] Building microservices with Spring Boot

##### 서비스 나누는 기준 : 명사 | API: 동사

우리 msa가 curd만 하고있다. 그러면 안된다. 비즈니스 로직이 들어가야 한다.

crud만 하고있다면 msa를 너무 잘게 나눈 것이다. (이거 내 문제였음)

- REST 기본 철학을 지켜야 한다.

- URI를 intent해서 사용해라.



~ 못들음,,,ㅎ

 

##### 개발자라면 이거는 이해 해야 한다!

- HATEOAS => iptv랑 컨셉이 잘 맞음(컨텐츠를 주고 컨텐츠가 어디있는지를 리턴하기 때문에)

- HTTP/HTTPS를 기본 프로토콜로 써라

- 기본 동사를 사용해서 레스트풀하게 써라 POST, GET, PUT, DELETE

- JSON을 써라!

- ★에러, 인증 처리를 HTTP에 맞춰서 써라!!!
  ex) 200으로 리턴하고 바디에 결과를 넣는것은 절대 안됨!!!!!! 
  HTTP response code는 좀 익혀둬야 함. 100% 알 필요는 없지만, 대중적인 코드는 알아둬야 함

##### API 버저닝은 꼭 필요함!!!

와 이건 몰랐넴,,,,,, ex) /v1/어쩌구~~~~

왜? api는 한번 나가면 바꿀 수가 없어서 버전 관리는 꼭 해줘야 함!

[httpie.io](https://httpie.io/)

실행은 다음주 부터 해볼까?

다음주는 우리가 없는데요!!!!!ㅠ0ㅠ!!!

##### end point naming은 중요하다.

##### 버전정보 제공도 중요하다.

##### devops

- msa는 셀프 컨테인드 될 수 있도록 해야 함

- 컨피규러블 하게 만들어야 함

- 마이크로서비스 인스턴스는 위치가 어디든지 상관 없어야 함 

- 마이크로서비스 상태정보를 항상 체크할 수 있도록
1. Assembly
   결과물은 하나의 JAR 파일만 나와야 함

2. Bootstrapping

3. Discovery
   multiple service instance가 있어야 하며, discovery agent가 나누어서 제공

4. Monitoring
   
   /actuator/health를 통해서 상태 정보를 확인할 수 있어야 함.







도커 이미지 하나 정도만 받아보고 와라
