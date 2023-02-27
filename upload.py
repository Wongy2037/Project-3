import pandas as pd
import pymysql
import math
conn = pymysql.connect(
    host='bj-cynosdbmysql-grp-bzwfkr20.sql.tencentcdb.com',  # Host IP Address 127.0.0.1
    user='covid',  # Username
    passwd='Aa123456789',  # Password
    port=23079,  # Port 23079
    db='covid',  # db_name
    # charset='utf8',  
)
# death
cur = conn.cursor()
# confirm = pd.read_csv(r'confirmed.csv', sep=',', header='infer')
# confirm = pd.read_csv(r'deaths.csv', sep=',', header='infer')
confirm = pd.read_csv(r'recovered.csv', sep=',', header='infer')

listarrays =[]
for row in confirm.iterrows():
    sentence = row[1].values
    print(
        sentence
    )
    listArray = []
    for i in sentence[:4]:
        if type(i)==float:
            if math.isnan(i):
                listArray.append("0")
                continue
            else:
                listArray.append(i)
        else:
            listArray.append(i)
    # for i in sentence[2:4]:
    #     listArray.append(str(i))

    listArray.append(",".join([str(s) for s in sentence[4:]]))
    print(listArray)
    listarrays.append(tuple(listArray))
print(listarrays)
# sql = "INSERT INTO `coviddata` (`province`, `country`, `lat`, `long`, `data`) VALUES (%s, %s, %s, %s, %s);"
# sql = "INSERT INTO `coviddata_death` (`province`, `country`, `lat`, `long`, `data`) VALUES (%s, %s, %s, %s, %s);"
sql = "INSERT INTO `coviddata_recovered` (`province`, `country`, `lat`, `long`, `data`) VALUES (%s, %s, %s, %s, %s);"
insert = cur.executemany(sql,listarrays)
conn.commit()