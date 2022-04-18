# Service Mesh

##### Service Mesh란?

마이크로 서비스 간의 통신을 담당하는 요소.

Service Mesh는 통신 및 네트워크 기능을 비즈니스 로직과 분리한 네트워크 통신 인프라이다. 모든 서비스의 인프라 레이어로써 서비스들 간의 통신을 처리하며, 위의 기능을 포함하고 있다. 아키텍처 내부에서 요청이 어떤 지점으로 갈지 전달되는 방식을 추상화 하며 이는 실질적인 서버로 존재하는 거싱 아니고 어떤 하나의 추상적인 개념을 뜻하는 것이다.

마이크로 서비스 구성 요소 간 상호 통신을 위해서 필요한 것

1. Service Discovery

2. Service Routing

3. Failure Recovery

4. Load Balancing(트래픽 관리)

5. 보안

6. 등등

❗API Gateway와는 다른 기능을 함❗

##### API Gateway

 : Service Discovery, 라우팅, 트래픽 관리와 같은 비슷한 기능 담당.

#### Service Mesh vs API Gateway.

1. 무엇이 다를까?
- 적용되는 위치
  API Gateway는 마이크로서비스 그룹의 외부 경계에 위치하여 역할을 수행하지만, Service Mesh는 경계 내부에서 그 역할을 수행함.

- 주요 목적
  API Gateway는 네트워크 외부의 트래픽을 수락하고 내부적으로 배포하지만, Service Mesh는 네트워크 내부에서 트래픽을 라우팅하고 관리하는 것.

- 아키텍처 형태
  API Gateway가 중앙집중형 아키텍쳐여서 SPOF(Single Point of Failure)을 생성한다면, Service Mesh는 분산형 아키텍쳐를 취하기 때문에 SPOF를 생성하지 않고 확장이 용이하다.

- 패턴
  API Gateway는 일반적으로 Gateway proxy pattern을 사용해서 수행된다.
  
  Consumer(호출자)은 구현 내용을 알 필요 없이 Gateway를 호출하는 방법만 알면 게이트웨이가 알아서 수행해주는 방식.
  
  반면에 Service Mesh는 일반적으로 Sidecar proxy pattern을 사용한다.
  
  Consumer(호출자)의 코드에는 Provider(공급자)의 주소를 찾는 방법, failover과 관련된 코드 등의 내용이 들어가게 된다. 다만, 호출자의 코드는 어플리케이션 코드(비즈니스 로직)에 내장되느넋이 아니아 sidecar 형태로 별개로 관리된다.

|           | API Management                                                                  | Service Mesh                                                  |
| --------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| 라우팅 주체    | 서버                                                                              | 요청하는 서비스                                                      |
| 라우팅 구성 요소 | 별도의 네트워크를 도입하는 독립적인 API Gateway 구성 요소                                           | 서비스 내 sidecar로 Local network스택의 일부가 됨                         |
| 로드 밸런싱    | 단일 엔드포인트 제공<br/>API Gateway 내 로드밸런싱을 담당하는 구성 요소에 요청을 redirection 하여 해당 구성요소가 처리 | Service Registry에서 서비스 목록 수신<br/>sidecar에서 로드 밸런싱 알고리즘을 통해 수행 |
| 네트워크      | 외부 인터넷과 내부 서비스 네트워크 사이에 위치                                                      | 내부 서비스 네트워크 사이에 위치하며 응용 프로그램의 네트워크 경계 내에서만 통신 가능              |
| 분석        | API 에 대한 사용자 및 공급자에 대한 모든 호출에 대해 수집되고 분석됨                                       | Mesh 내 모든 마이크로 서비스 구성 요소에 대해 분석가능                             |

2. 그러면 둘 다 필요할까?
   
   Service Mesh와 API Gateway는 함께 작동하여 외부 트래픽을 효율적으로 수락 한 다음 해당 트래픽이 네트워크에 있으면 효과적으로 라우팅 할 수 있습니다. API 게이트웨이와 서비스 베시가 있는 배포에서 클러스터 외부에서 들어오는 트래픽은 먼저 API Gateway를 통해 라우팅 된 다음 메시로 라우팅 됩니다. 
   
   ##### API Gateway는 인증, 엣지 라우팅 및 기타 엣지 기능을 처리할 수 있으며 서비스 메시는 아키텍처에 대해 세밀한 관찰 및 제어를 제공할 수 있다.

#### LB(Load Balancer)

여러 대의 서버에 트래픽을 골고루 분산하기 위해 배분해주는 기술이다.

##### LB는 어떻게 트래픽을 특정 서버에 연결할 수 있을까?

LB는 MSA의 각 모듈에 대한 연결 정보(ip, port, hostname)를 알고있다. 우리는 각 모듈의 연결 정보를 LB에 등록해야 한다.

###### CI/CD를 수행하며 각 모듈은 계속하여 업그레이드 된다. 그 과정을 통하면서 연결 정보가 바뀌게 된다. 그럼 그 때 마다 LB에 새롭게 등록해야하는데 너무 번거롭다! 그래서 Eureka라는 기술이 등장했다.

#### Eureka란?

넷플릭스에서 제공한 MSA를 위한 클라우드 오픈 소스이다.🥫🥫

LB와 Middle-tire server 사이의 에러 대응을 위한 Rest 기반 서비스이다.



MSA에서 각 서비스별로 application이 나뉘어져 있다. 각 application들은 서로간의 통신을 위해, 서로 연결 정보(ip, hostname, port)를 알아야 한다. 그럼 이 연결정보를 Load Balancer에 저장하게된다.



msa 구조를 클라우드에 구축하게되면, 각 서비스 어플리케이션 연결정보는 계속해서 바뀌게 된다. 이 때 마다 로드밸런서에 구성된 설정을 바꿔야하는 이상한 상황이 발생한다.



클라우드 환경에서의 연결정보(ip, hostname, port)의 Registering(등록)과 De-registering(해지)를 바로바로 할 수 있도록 해 주는 것이 eureka이다.



###### Eureka에 존재하는 단어

> ###### Discovery
> 
>     다른 서비스의 연결 정보를 찾는 것
> 
> ###### Registry
> 
>     서비스의 연결 정보를 등록하는 것

###### Eureka 구성

> ###### Eureka Server
> 
>     Eureka Client를 관리하는 서버
> 
> - Eureka Server는 Eureka Client의 정보를 Registry에 등록한다
> 
> - Eureka Server는 Eureka Client의 Heartbeat를 수신하여 해당 Client가 수행 중임을 안다.
> 
> - heartbeat가 오지 않는 경우, eureka server는 client가 죽었다고 판단하여 해당 client정보를 registry에서 삭제한다.
> 
> - 이렇게 유지된 registry 정보를 server는 client들에게 전달한다.
> 
> - 등록되는 정보는 ID와 URL이 포함되는데, 마이크로서비스는 유레카 클라이언트를 이용해서 정보를 유레카 서버에 등록한다.
> 
> ###### Eureka Client
> 
>     각각의 서비스에 해당하는 모듈
> 
> - 등록된 마이크로 서비스를 호출해서 사용할 때 유레카 클라이언트를 이용해서 필요한 서비스를 발견한다.
> 
> - 유레카 서버는 유레카 서버인 동시에 서로의 상태를 동기화 하기도 한다. 그렇기 때문에 서로를 바라보는 유레카 클라이언트이기도 한다. (= 다른 유레카 서버와 상태를 동기화 함. 아니어도되긴함)

##### 

#### Service Mesh가 왜 필요한가❓❗

그니까 말이ㅑㅇ,,, 왜필요한가 그것을 알아보자.

MSA 환경에서 가장 중요한 점은 각각의 마이크로 서비스간의 통신이 원활하게 이루어져야 한다는 것이다.

만약 마이크로 서비스가 2~3개라면 서로간의 통신을 마이크로 서비스 내부에 직접 구축해도 큰 어려움이 없겠지만, 수십 수백개가 넘어가고 사용자의 증가로 인해 더 늘어난다면 그때는 서비스 내부의 통신 로직을 개발자가 모두 구현할 수 없을 것이다.

서비스 메쉬에서는 요청이 프록시를 통해 msa간에 라우팅된다. 서비스 메쉬를 구성하는 개발 프록시는 msa 내부 실행이 아닌 따로 실행이 되므로 Sidecar라고 부르기도 한다.

아니 그래서 url 불러올때는 어떻게써야되냐고,,,,ㅋ 아 진짜 불친절하냄1`!~!~~!~!!~!~

### Service(Eureka-Client) : 실제 로직이 실행되는 서비스

### Eureka-Server : 서비스들의 정보를 관리하는 Eureka Server

### Zuul(Eureka-Client) : 실제 서비스로 Routing 하는 Edge서비스

내가 찾던게 Zuul이었음!!!!!!!!!!!!!!!!!!이걸로 url 설정해서 라우팅하기 이제시작 궈궈 가보작오!~!~~~