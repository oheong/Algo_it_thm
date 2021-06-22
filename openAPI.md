# open API

- 오픈 API (Open Application Programming Interface)
- 누구나 사용할 수 있도록 공개된 API
- 활용하기 위해서는 '서비스 키'를 발급받아야 한다.

![img](https://www.incheon.go.kr/humanframe/theme/data/assets/image/data02/diagram-open-api.png)

[출처](https://www.incheon.go.kr/data/DATA020302)

<hr>

##### API란?

- Application programmin Interface
- 어떠한 응용 프로그램에서 데이터를 주고 받기 위한 방법
- 특정 사이트에서 특정 데이터를 공유 할 경우 어떠한 방식으로 정보를 요청하고 받을수 있는지에 대한 규격

###### API의 역할별 분류

- Open API(Public API) : 외부에서 제약없이 호출할 수 있도록 공개된 API. 오픈 플랫폼에서 기본적으로 제공되어야 할 API 형태이다.
- Partner API : 제휴 API로써 핀테크기업 등 제휴업체와 사전 협의 후 제작하여 제공하며 이용 라이선스, 권한 등이 별도로 필요하다.
- Internal API(Private API) : 기업 내부 시스템에서만 사용될 수 있으며, ESB 시스템이나 내부용 API Gateway에 등록되어 호출되거나, API 서버에 직접 등록되어 Client에서 호출 될 수 있다.
- Composite API : 복수의 API를 한번에 동기적으로 호출하는 방식으로 처리 속도를 높일수 있으며, 개별 API의 성공 및 실패를 하나의 Response에 Composite Subrequest로 구별하여 되돌려준다.

<hr>

> interface란?
>
> ​	기계 혹은 장치 끼리 정보를 교환하기 위한 수단이나 방법



kakao, naver, 통계청, 기상청 등의 사이트에서 프로그래밍에 사용할 수 있도록 open API를 제공하고있다.

특정 값을 넣으면 해당 값에 대한 결과값을 json, xml 등의 포맷으로 리턴받을 수 있으며, 받은 값을 가지고 프로그래밍에 활용할 수 있다.



#### API 호출

- 요청 URL(request URL) : 오픈 API를 호출하기 위한 API의 웹 주소(url)
- 요청 변수(request parameter) : 오픈 API를 호출할 때 함께 서버로 전송해야 하는 값. API 레퍼런스를 보며 요청 변수의 이름이 틀리거나 필요 요청 변수가 누락되지 않도록 조심해야 함.

#### API 코드

- 200 : 성공
- 400 : 파라미터 오류
- 403 : 허가되지 않은 요청
- 404 : 리소스 없음
- 500 : 서버 오류

