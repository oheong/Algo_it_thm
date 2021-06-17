from google.oauth2 import service_account
from google.cloud import bigquery
import base64
from Crypto import Random
from Crypto.Cipher import AES
import pandas as pd


"""
7. DataLake(BQ) to DataWarehouse(BQ)
    => BQ to BQ는 조회해서 적재하면 됨
"""
"""
create DW table query : 

create table dataset.memberDW(
    name string not null,
    mail string not null,
    password string not null,
    birth date
)
"""

def aes(pwd):
    password = pwd
    raw = pad(password).encode('utf-8')
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CFB, iv) 
    password = base64.b64encode(iv + cipher.encrypt(raw))
    return password.decode('utf-8') # 장난하나 왜안되노🤛

    

# API 요청에 필요한 구성
table_id = "hstest-316104.dataset.memberDW"
key_path = "C:\hstest-316104-7a2efb3e9c0e.json"
credentials = service_account.Credentials.from_service_account_file(
    key_path,
    scopes=["https://www.googleapis.com/auth/cloud-platform"],
)

key = 'eongisGoodGirlzz'.encode('utf-8')
try :
    client = bigquery.Client(project = 'hstest-316104', credentials = credentials)

    query = """
        select name,
               mail,
               password,
               birth
        from dataset.memberDL
        where birth between '1991-01-01' and '1999-12-31'
    """
    result = client.query(query = query).to_dataframe()
    print("----------DL에서 조회 성공----------")

    # 블럭 사이즈 패딩 로직
    BS = 16
    pad = lambda s : s + (BS - len(s) % BS) * chr(BS - len(s) % BS)

    # result.loc['password'] = aes(result['password'])

    # print(result)

    # result.replace("", aes(result['password']))
    # result.loc['password'] = aes(result['password'])

    # password에 암호화 알고리즘 적용
    for i in result.password:
        result.password = aes(i)

    # for row in result:
        # password = row['password']
        # raw = pad(password).encode('utf-8')
        # iv = Random.new().read(AES.block_size)
        # cipher = AES.new(key, AES.MODE_CFB, iv) 
        # password = base64.b64encode(iv + cipher.encrypt(raw))
        # row["password"].replace(row["password"], password.decode('utf-8')) # 장난하나 왜안되노🤛


    print(result)


    # print("----------DW적재 시작----------")
      
    # job_config = bigquery.LoadJobConfig(
    #     schema=[
    #         # 순서가 필요가 없는게 빅쿼리에서 쿼리속도를 최척화하여 셔플함
    #         bigquery.SchemaField("name", "STRING", mode='required'),
    #         bigquery.SchemaField("mail", "STRING", mode='required'),
    #         bigquery.SchemaField("password", "STRING", mode='required'),
    #         bigquery.SchemaField("birth", "Date", mode='nullable'),
    #     ],
    #     write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE, # 테이블 대체
    #     source_format = bigquery.SourceFormat.CSV,
    # )
    # uri = "gs://oheong-test-bucket/result.csv"

    # load_job = client.load_table_from_uri(
    #     uri, table_id, job_config = job_config
    # ) 

    # load_job.result()

    # destination_table = client.get_table(table_id)  
    
    # print("========BigQuery Connect && Load!========")
    
    # # 왜 중복?ㅠ 해결~~ 걍 덮어버리기(WRITE_TRUNCATE),,
    # print("Loaded {} rows.".format(destination_table.num_rows)) 

except Exception as e : 
    print("----------Error----------")
    print(e)


