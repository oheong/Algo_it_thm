import pandas as pd
import Connect
"""
DB to CSV
"""

list = Connect.rows

for i in list:
    print(i)
print("=====================================")
print(str(len(list))+"개의 데이터 조회 완료")
print("=====================================")

col_name=['이름', '메일', '비밀번호', '생년월일']

df = pd.DataFrame(list, columns=col_name)

df.to_csv('result.csv', index = False, encoding="utf-8-sig")
print("&&&&&&&&csv 생성 완료&&&&&&&&")


