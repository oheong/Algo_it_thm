# ETL

- Extract, Transform, Load (추출, 변환, 적재)

- 데이터 웨어하우스(DW, Data Warehouse) 구축 시 데이터를 운영 시스템에서 추출(Data Lake)하여 가공한 후 데이터 웨어하우스에 적재하는 모든 과정

- ##### 한 곳에 저장된 데이터를 필요에 의해 다른 곳으로 이동하는 것

<img src="https://user-images.githubusercontent.com/24339310/121107024-23442f80-c842-11eb-9970-e182624e18d6.PNG">

###### data warehouse : raw data(가공 되지 않은 데이터)를 통한 분석자료를 제공하여 조직내 의사결정을 지원하는 정보관리 시스템



#### 1. 기존 테이블의 데이터를 추출

​	SQL의 select를 통해 데이터를 가져온다. 

#### 2. 추출한 데이터를 변환

​	고객의 요구에 맞게 데이터에 변화를 준다.

#### 3. 추출 및 변환한 데이터의 적재

​	가공한 데이터를 새로 만든 테이블에 적재(insert)한다.



<hr>

JAVA 오픈소스 ETL 도구

SSIS, 



