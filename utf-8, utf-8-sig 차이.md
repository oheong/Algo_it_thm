# utf-8, utf-8-sig 차이



python에서 csv 파일로 내보내는데 한글 오류가 나서 찾아봄

```python
# csv 파일 헤더 행 추가
col_name=['이름', '메일', '비밀번호', '생년월일']

# 리스트 데이터프레임에 저장
df = pd.DataFrame(list, columns = col_name)

# 파일 저장 이름, 인덱스 없음, 인코딩
df.to_csv('result.csv', index = False, encoding = "utf-8-sig")
```



utf-8-sig에서 sig는 'signature'의 약자이다.

utf-8-sig를 사용하면 스트링(문자열)로 처리하는게 아니라, Byte Order Mark(BOM)으로 취급한다.