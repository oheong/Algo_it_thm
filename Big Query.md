# Google Big Query

1. 빅쿼리 테이블을 만들기 위해서는 데이터셋을 만들고 시작해야한다 (이거몰라서 두시간 헤맴)

   > 데이터세트는 특정 [프로젝트](https://cloud.google.com/docs/overview?hl=ko#projects)에 포함됩니다. 데이터세트는 [테이블](https://cloud.google.com/bigquery/docs/tables?hl=ko)과 [뷰](https://cloud.google.com/bigquery/docs/views?hl=ko)에 대한 액세스를 구성 및 제어하는 데 사용되는 최상위 컨테이너입니다. 테이블이나 뷰는 반드시 데이터세트에 속해야 하므로, 개발자는 최소한 한 개 이상의 데이터세트를 만든 후에 [데이터를 BigQuery로 로드](https://cloud.google.com/bigquery/loading-data-into-bigquery?hl=ko)해야 합니다.
   >
   > ​																																									[출처](https://cloud.google.com/bigquery/docs/datasets-intro?hl=ko)

2. 빅쿼리는 주키가 없다(주임님 아니었으면 몰랐음)

3. 빅쿼리는 auto-increase가 없음 뭐 이런?ㅎㅎ

4. 빅쿼리는 쿼리 성능을 최적화하여 셔플한다.

   > 성능 최적화 평가 요소
   >
   > 1. 입력 데이터 및 데이터소스(I/O) : 쿼리에서 읽는 바이트 수
   > 2. 노드 간 통신(셔플) : 쿼리에서 다음 단계로 전달하는 바이트 수, 쿼리에서 각 슬롯에 전달하는 바이트 수
   > 3. 계산 : 쿼리에 필요한 cpu 작업량
   > 4. 출력(구체화) : 쿼리에서 쓰는 바이트 수
   > 5. 쿼리 안티패턴 : 쿼리의 SQL 권장사항 준수 여부

5. 빅쿼리에는 암호화하는 함수가 있음,,,ㅋㅎㅠ
