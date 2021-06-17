from google.cloud import storage
from google.cloud.storage import blob
from google.oauth2 import service_account

"""
5. GCP(CSV to BigQuery)
"""

# API 요청에 필요한 구성
key_path = "C:\hstest-316104-7a2efb3e9c0e.json"

credentials = service_account.Credentials.from_service_account_file(
    key_path,
    scopes=["https://www.googleapis.com/auth/cloud-platform"],
)
storage_client = storage.Client(credentials=credentials)

# Google Cloud Console을 통해 생성된 버킷 이름
bucket = storage_client.get_bucket('oheong-test-bucket')

csv_file = 'result.csv'

# csv 업로드
try :
    # gcs에 저장 될 파일 이름
    blob = bucket.blob(csv_file)
    # blob = bucket.blob("다른_이름으로_들어가니") # yes 들어감

    # open() 없이 로컬 파일 업로드
    blob.upload_from_filename(csv_file)

    print("@@@@@@@@@@@@@@@gcs에 csv 업로드 성공@@@@@@@@@@@@@@@")

except :
    print("@@@@@@@@@@@@@@@gcs에 csv 업로드 실패@@@@@@@@@@@@@@@")