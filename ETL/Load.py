from google.cloud import bigquery
from google.oauth2 import service_account
"""
6. GCP(CSV in gcs to BigQuery)
https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-csv#python
"""

"""
사전 작업 : gcp에 데이터셋, 테이블 만들기

create table query : 

create table dataset.member(
    name string not null,
    mail string not null,
    password string not null,
    birth date
)

"""

schema_field = []
table_id = "hstest-316104.dataset.member"
key_path = "C:\hstest-316104-7a2efb3e9c0e.json"

credentials = service_account.Credentials.from_service_account_file(
    key_path,
    scopes=["https://www.googleapis.com/auth/cloud-platform"],
)

try:
    conn = bigquery.Client(credentials=credentials)

    job_config = bigquery.LoadJobConfig(
        schema=[
            bigquery.SchemaField("name", "STRING", mode='required'),
            bigquery.SchemaField("mail", "STRING", mode='required'),
            bigquery.SchemaField("password", "STRING", mode='required'),
            bigquery.SchemaField("birth", "Date", mode='nullable'),
        ],
        skip_leading_rows=1,
        # The source format defaults to CSV, so the line below is optional.
        source_format=bigquery.SourceFormat.CSV,
    )
    uri = "gs://oheong-test-bucket/result.csv"

    load_job = conn.load_table_from_uri(
        uri, table_id, job_config = job_config
    ) 

    load_job.result()  # Waits for the job to complete.

    destination_table = conn.get_table(table_id)  
    
    print("========BigQuery Connect!========")
    print("Loaded {} rows.".format(destination_table.num_rows))
    

except Exception as e : 
    print("========BigQuery Connect Error!========")
    print(e)

