# 데이터 불러옴
filename = 'data.txt'
with open(filename) as file_object:
    contents = file_object.read()
# print(contents)

# 각 결과 값을 담을 리스트
year = []
month = []
day = []
hour = []
min = []

# 데이터 값 분리
temp = contents.split()

num = len(temp)

# 쿼리 결과를 리스트에 추가
for i in range(0, num):
    n = i % 6
    if n == 0:
        year.append(temp[i])
    elif n == 1:
        month.append(temp[i])
    elif n == 2:
        day.append(temp[i])
    elif n == 3:
        hour.append(temp[i])
    elif n == 4:
        min.append(temp[i])

# 잘 추가되었는지 확인
# print(year)
# print(month)
# print(day)
# print(hour)
# print(min)
print("총 "+str(len(year)) + "개의 데이터 추출")