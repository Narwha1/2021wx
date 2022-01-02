import pymysql
import re

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='qazwsx12',
    db='wx',
    charset='utf8mb4',
    port=3306)

cur = conn.cursor()

with open(r"/Users/zhangjingyi/Downloads/聊天记录/Narwhal/倍倍.txt", encoding='utf-8') as f:
    lines = f.readlines()
    filter_lines = []
    reg = "^.+[\u4E00-\u9FFF]\s"

    for line in lines:
        # 去除转发的聊天记录 简单过滤
        if (line.startswith('倍倍💖') or line.startswith('Narwhal')) and re.match(reg, line):
            filter_lines.append(line.strip())
    # print(filter_lines)


for line in filter_lines:
    s1 = line.find(" ")
    s2 = line.find("):")
    name = line[:s1]
    time = line[s1 + 2:s2]
    content = line[s2 + 2:]
    # print(line)
    insert_sql = f"insert into log(user,datetime,content) values ('{name}','{time}' ,'{content}')"
    print(insert_sql)
    # cur.execute(insert_sql)
conn.commit()
