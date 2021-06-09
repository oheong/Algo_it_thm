# ETL

- Extract, Transform, Load (추출, 변환, 적재)

- 데이터 웨어하우스(DW, Data Warehouse) 구축 시 데이터를 운영 시스템에서 추출(Data Lake)하여 가공한 후 데이터 웨어하우스에 적재하는 모든 과정

- ##### 한 곳에 저장된 데이터를 필요에 의해 다른 곳으로 이동하는 것

<img src="https://user-images.githubusercontent.com/24339310/121107024-23442f80-c842-11eb-9970-e182624e18d6.PNG">

###### data warehouse : raw data(가공 되지 않은 데이터)를 통한 분석자료를 제공하여 조직내 의사결정을 지원하는 정보관리 시스템

- ##### E/Extract(추출) : 원본 데이터베이스 또는 데이터 소스에서 데이터를 가져오는 것을 말한다. ETL을 사용하면 데이터가 임시 스테이징 영역을 들어가고, ELT를 사용하면 즉시 데이터가 Lake 스토리지 시스템으로 이동한다.

- ##### T/Transform(변환) : 데이터의 구조를 변경하는 프로세스를 의미한다. 용도에 맞는 필터링, 정제 등의 단계를 통해 필요한 형태로 변환한다.

- ##### L/Load(적재) : 데이터를 스토리지에 저장하는 프로세스를 의미한다.

<hr>

ETL Tools

- Air-flow
- Luigi
- SSIS
- embulk
- [기타등등](https://ichi.pro/ko/etlilan-mueos-imyeo-etleul-sayonghaneun-iyu-83573115998652)

<hr>

##### ETL vs ELT

|                    |                             ETL                              |                             ELT                              |
| :----------------- | :----------------------------------------------------------: | :----------------------------------------------------------: |
| 프로세스           |      staging 서버에서 데이터를 변형하고 DW의 DB에 옮김       |                   DW의 DB에 데이터가 남음                    |
| 코드사용           |                       적은 양의 데이터                       |                        대용량 데이터                         |
| 변형               |               ETL 서버나 staging 영역에서 완료               |                    target system에서 실행                    |
| 적재 시간          | 데이터가 staging에 먼저 적재되고 나중에 target system에 적재됨. 시간에 민감함 |             target system에 한번만 로드됨. 빠름              |
| 변형 시간          | 데이터의 변형이 완료될 때 까지 기다려야함 데이터 사이즈가 커질수록 변형에 들어가는 시간 증가 |               데이터 사이즈와 시간은 관계 없음               |
| 유지보수 시간      | 높은 수준의 유지보수가 요구되고, 적재하고 변형할 데이터를 선택해야함 | 낮은 수준의 유지보수가 요구되며, 데이터는 모두 사용할 수 있음 |
| 구현 복잡도        |                 초기 영역에서는 구현이 쉬움                  | 프로세스를 구현하기 위해서는 이에 대한 숙련된 기술과 툴에 대한 깊은 이해가 요구됨 |
| DW를 위한지원      |      온프라미스 환경에 관계형이고 정형 데이터에 사용됨       | 확장가능한 클라우드 환경에서 사용되며 정형 데이터와 비정형 데이터를 지원 |
| Data Lake 지원     |                              x                               |        데이터레이크가 비정형 데이터를 사용하게 해 줌         |
| 복잡도             |          설계를 하는 시점에 중요한 데이터들만 적재           |      output backward와 관련있는 데이터의 개발에만 관련       |
| 비용               |         작은 규모와 중간 규모의 비지니스에 높은 비용         | 온라인 소프트웨어를 서비스 플랫폼으로 사용하여 진입 비용 절감 |
| 검색               |  staging 영역에 facts와 dimensions이 활성화 되어 있어야 함   | 모든 데이터가 활성화되어 있어야 함. 한개의 액션에서 추출과 적재가 일어나기 때문 |
| Aggregation        |       데이터셋에 추가되는 데이터 단위마다 복잡도 증가        |     타겟 플랫폼의 힘으로 중요 단위 데이터를 빠르게 처리      |
| 계산               | 기존 컬럼을 덮어쓰거나 데이터셋을 추가하고 타겟 플랫폼에 푸시 |          존재하는 테이블에 계산된 컬럼을 쉽게 추가           |
| 성숙도             |                     20년 이상 사용되었음                     |                  새로운 컨셉과 복잡한 구현                   |
| 하드웨어           |       대부분의 툴이 유니크한 HW를 요구하고 가격이 비쌈       |             Saas 형태의 HW로 가격은 이슈가 안됨              |
| 비정형 데이터 지원 |                 대부분의 관계형 데이터 지원                  |                  비정형 데이터를 즉시 지원                   |
| 장점               |    정교한 데이터 변환을 수행할 수 있음<br/>보안성이 높음     |   필요한 데이터만 변환하여 유연성 향상<br />보안성이 낮음    |

![img](https://blog.kakaocdn.net/dn/b90h8K/btq3yw9ta7Y/qrqLMzHKQn3qWbaRSnC6lK/img.webp)

[출처](https://www.xplenty.com/blog/etl-vs-elt/)




<hr>


gcp etl using python

https://towardsdatascience.com/building-a-simple-etl-pipeline-with-python-and-google-cloud-platform-6fde1fc683d5



https://towardsdatascience.com/part-2-building-a-simple-etl-pipeline-with-python-and-google-cloud-functions-mysql-to-bigquery-4e1987f9f89b



ETL

https://datafloq.com/read/what-is-etl/6948



