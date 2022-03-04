# [2] Exploring the microservices sorle with Spring Cloud

##### 니가 뭘 좋아할지 몰라서 다 준비했어

##### 

##### Cloud Native components

- Microservices

- DevOps

- Continuous delivery

- Containers : ec2 사용 시 보다 비용 효율 30% 좋음

##### 

##### [The Twelve-Factor App (한국어)](https://12factor.net/ko/)

여기의 내용들은 꼭 지켜야 함!!!!

1. Codebase

2. Dependencies

3. Config
   .M2 local repository를 권장함
   환경 변수들이 들어가야 하는 부분임

4. Backing services

5. Build, release, run
   depOps에서 잘 (꼭)지켜줘야 할 내용임

6. Processes
   서비스 하나를 가축처럼 있다 없을 수도 있다.는 것을 생각해야 함.(?)
   application 상태를 로컬로 갖고있으면 절대 안됨

7. Port binding

8. Concurrency
   Scale up < Scale out

9. Disposability

10. Dev/prod parity
    staging이 dev랑 똑같다고 하면 prod에서 에러날 확률이 적음
    보통 dev랑 pord랑은 환경이 다름. 그렇기 때문에 많은 테스트를 해야 함
    환경 자체를 똑같이 만들어주는 코드를 만들어야 함. (Cloud Native)

11. Logs
    Event stream
    
    각 로그파일들을 묶어서 Logstash -> Elastic-search->Kibana

12. Admin apocesses
    스크립트를 통해서 실행하도록
    임의로 명령을 쳐서는 안된다.

올바른 프로세스를 가지고 정착시켜야 한다! 이거 안하면 문제가 된다.

알고있느냐 모르느냐의 차이는 있으니까~






























































