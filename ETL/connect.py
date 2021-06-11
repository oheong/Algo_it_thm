import psycopg2

try:
    print("*************Connected*************")
    # DB 연동
    db = psycopg2.connect(host='localhost',
                        dbname='ABC-test',
                        user='postgres',
                        password='oheong',
                        port=5432)

    # 명령 처리할때 사용
    cursor = db.cursor()

    cursor.execute("select * from member order by no;")
    rows=cursor.fetchall()

    for i in rows:
        print(i)

    # print(execute())

except psycopg2.DatabaseError as db_err:
    print("==========Not Connected!==========")
    print(db_err)
