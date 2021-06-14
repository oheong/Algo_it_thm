import Extract

# 두 자리 이하의 숫자로 구성된 리스트를 받아서
# 1자리일 경우 앞에 0을 붙여 반환
def num_list_to_double_digit(list):
    print("=============중간 변환 시작=============")
    temp_list = [str(data) for data in list]

    for i, data in enumerate(list):
        temp_list[i] = data if len(data) == 2 else '0' + data

    print("=============중간 변화 완료=============")
    return temp_list


hour = num_list_to_double_digit(Extract.hour)
min = num_list_to_double_digit(Extract.min)

# 데이터 변환 중간 확인
# print(hour)
# print(min)

#데이터 변환
hm = [hour[i] + ":" + min[i] for i in range(len(hour))]

print(str(len(hm))+"개의 데이터 변환 완료")
#데이터 변환 확인
# print(hm)
