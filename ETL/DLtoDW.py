from google.oauth2 import service_account
from google.cloud import bigquery

"""
7. DataLake to DataWarehouse
"""


# API 요청에 필요한 구성
key_path = "C:\hstest-316104-7a2efb3e9c0e.json"
credentials = service_account.Credentials.from_service_account_file(
    key_path,
    scopes=["https://www.googleapis.com/auth/cloud-platform"],
)

try :
    client = bigquery.Client(project = 'hstest-316104', credentials = credentials)

    query = """
        select *
        from dataset.memberDL
        where birth between '1991-01-01' and '1999-12-31'
    """

    result = client.query(query = query)

    print("----------Connect----------")
    # 결과 잘 나옴!
    for row in result:
        print("{},{},{},{}".format(row["name"], row["mail"], row["password"], row["birth"]))

except : 
    print("----------Error----------")




"""
이 데이터들을 어떻게 구워삶아볼까나
"""