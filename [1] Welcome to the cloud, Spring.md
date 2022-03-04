# [1] Welcome to the cloud, Spring

1. msa 이해

2. 왜 회사에서 msa를 쓰는지?

3. spring boot, spring cloud

N-tire아키 | msa

| n-tire                               | msa    |
| ------------------------------------ | ------ |
| 여러 팀이 하나의 코드 베이스 안에서 빌드.<br/>하나의 jar | war 파일 |

msa는 json을 사용하고 각 서비스들이 구현되는 기술들에 종속되어있지 않다. (언어, DB 다 달라도 됨) => 하지만 같은걸 쓰는게 좋긴 함.

가용성을 유지하기위해 힘 씀

전체장애를 피하기위해 유연성, 회복탄력성, 확장성을 유지해야 함

##### Small, Simple, and Decoupled Services = Scalable, Resilience4j, and Flexible Applications

★조직구조로 인해서 아키텍처의 형태가 결정되면 안됨. (조직 개편 시 망함)★

Spring boot가 MSA에는 더 맞다.

## 차이점

Spring Boot는 Spring framework와 몇 가지면에서 차이가 있다.

- Embed Tomcat을 사용하기 때문에, (Spring Boot 내부에 Tomcat이 포함되어있다.) 따로 Tomcat을 설치하거나 매번 버전을 관리해 주어야 하는 수고로움을 덜어준다.

- starter을 통한 dependency 자동화 :  
  아마 Spring 유저들이 가장 열광한 기능이 아닐까 싶다. 과거 Spring framework에서는 각각의 dependency들의 호환되는 버전을 일일이 맞추어 주어야 했고, 때문에 하나의 버전을 올리고자 하면 다른 dependeny에 까지 영향을 미쳐 version관리에 어려움이 많았다. 하지만, 이제 starter가 대부분의 dependency를 관리해주기 때문에 이러한 걱정을 많이 덜게 되었다.

- XML설정을 하지 않아도 된다.

- jar file을 이용해 자바 옵션만으로 손쉽게 배포가 가능하다.  
  Spring Actuaor를 이용한 애플리케이션의 모니터링과 관리를 제공한다.

옛날에는 tomcat 서버에 war 파일을 사용해서 따로 배포해야 했음.

문제점 : 서버와 로컬 사이에 차이가 나는 경우가 있음

현재는 embeded web server를 사용하여 소스파일과 서버정보가 하나의 jar파일로 만들어짐

##### configuration

spring eureka : 분산환경에서의 discovery 찾아줌

spring cloud : 서비스 게이트웨이

keycloak server : 보안

organization db : 

Redis : 인메모리 서비스

Resilience4j : 

Kafka : 

distributed tracing : 

docker container : 로깅과 모니터링

Actuator : 

좋은 방법 : 모놀리식->모듈화->msa

[스프링 보기 좋은 책]([Spring Start Here](https://www.manning.com/books/spring-start-here))

Spring 동작 방식

1. Route mapping

2. Parameter destruction

3. JSON => Java object mappig (Deserializable)

4. Business logic execution

5. Java =>JSON object mapping (Serializable)

[@Controller, @RestContoller 차이]([[Spring] @Controller와 @RestController 차이 - MangKyu's Diary](https://mangkyu.tistory.com/49))

##### @RequestParam, @PathVariable 차이 알아오기

[1]([스프링 controller에서 파라미터를 받는 다양한 방법 ( @RequestParam, @RequestBody, @PathVariable)](https://takeknowledge.tistory.com/39))

지금은 gradle로 하는게 나음!!!! 왜지? 이것도 설명해야겠다

Java vs Groovy

Maven vs Gradle

| Maven            | Gradle |
| ---------------- | ------ |
| xml 기반이라 유지보수 힘듦 | ?      |

post맨으로 함 떄려서 결과 보여주기

IaaS : AWS(EC2), 인프라 제공. 컴퓨팅 제공

CaaS : 컨테이너를 서비스함 (ECS)

PaaS : 앱엔진

FaaS : AWS 람다

SaaS : 

<적절하게 사용하는것이 중요함>

##### MSA 가이드라인

- Right-sized : MSA 도메인마다 적절한 사이즈가 중요함

- Location transparent : 

- Resilient : 탄력회복성 (fail fast? 실패 시 빠르게 복구하여 다른 부분에 피해 없도록)

- Repeatable :

- Scalable :  

새로운 서비스를 배포할 때 마다 이전 서비스는 삭제하고 새로 배포해야했음.

##### MS routing patterns in Spring

- Service discoverty - service mesh. (etcd, Consul, Apache Zookeeper)

- Service routing - API Gateway

[넷플릭스 테크 블로그 ](https://netflixtechblog.com/?gi=c9bca0cec0b1)

##### MS client resiliency (죽어도 혼자 죽는법)

- **Client-side load balancing**

- Circuit breaker pattern (회로차단기. 두꺼비집)

- Fallback pattern : 개인 추천 서버가 삐리하면 일반적인 추천 내용으로 추천서비스 내보내는 것. 해당 서비스가 제대로 동작하지 않을 때 대체로 동작하는 서비스.

- Bulkhead pattern : 서버가 한번에 다운되지 않도록 문제를 분리하는 기능 (Thread Pool. 세마포어 방식)

##### 인증

- Autherntication : 인증

- Authorization : 권한부여

- Credential management and propagation : 서비스별로 로그인하지 않고, 하나의 토큰을 가지고 모든 서비스에 접근할 수 있도록

- 2fa (2단계 인증)

API Gateway에서 모든 트래픽을 받으니까 얘가 죽으면 다 죽음,,,,,,(JONNA 중요함)

여러 서비스에 공통으로 걸쳐있는 일을 하는 곳이 API Gateway

ex) 삐리한 토큰이 들어오면 쳐내기, 서버에 과다 리퀘스트나

토큰 validation을 각 서버에서 하는 방법이 있음

##### logging and tacing patterns

- Log correlation : 한 트랜잭션을 처리했는지 볼려면 로그를 중앙 서비스에서 볼 수 있도록 해야 함. correlation ID. 

- Log aggregation : 개발자는 이거 없으면 안됨

- Microservice tracing 

- 로그만 모으는 db가 또 있음

로깅과 모니터링은 다른 것이다!!

##### 매트릭스 서비스

매트릭스 서비스는 한 시점에서 시계열로 다 보여줘야 됨. 어디서 발생했는지 원인을 찾을 수 있음.

##### build/deployment patterns

- Build and deployment pipelines

- Infrastructure as code : 인프라도 코드로 다 만듦. 유지 가능한 구조로 만들어야 함

- Immutable servers : 불변서버. 서버가 배포되고나서 재배포 될 때 까지 절대로 건들면 안됨. 이미지로 생성되어 배포되고 생성 후 절대 변경되면 안됨

- Phoenix server : 불사조 서버.

dev - 개발

test - 이미지 생성

prod - 테스트에서 생성된 이미지를 그대로 받아와야 함.

[The Twelve-Factor App (한국어)](https://12factor.net/ko/)

트랜잭션이 빨라야하는 부분에서는 rest보다는 다른 프로토콜을 쓰는 경우가 있다.

restAPI를 만들고 문서화 하는 스킬은 기본으로 돼어있어야 한다. ex) swagger

내가 만든 api가 클라이언트에 전달된다하면, 정형화 되어있어야 하고 public으로 나가도 될 정도로 해야 한다. 컨벤션이 아주 중요함.

변수명 잘못 정하면 확장할때 어려워짐

##### 
