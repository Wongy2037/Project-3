import pandas as pd
import pymysql
conn = pymysql.connect(
    host='bj-cynosdbmysql-grp-bzwfkr20.sql.tencentcdb.com',  # Host IP Address 127.0.0.1
    user='covid',  # Username
    passwd='Aa123456789',  # Password
    port=23079,  # Port 23079
    db='covid',  # db_name
    # charset='utf8' 
)
# death
cur = conn.cursor()
confirm = pd.read_csv(r'confirmed.csv', sep=',', header='infer')
confirm = pd.read_csv(r'deaths.csv', sep=',', header='infer')
confirm = pd.read_csv(r'recovered.csv', sep=',', header='infer')

confirm = confirm.groupby(by='Country/Region').sum()

insertDatas = []
for index in  confirm.index:
    insertDatas.append((index,(','.join([str(int(data)) for data in confirm.loc[index][2:]]))))


sql = "INSERT INTO `coviddata_sum` (`country`, `data`) VALUES (%s, %s);"
sql = "INSERT INTO `coviddata_death_sum` (`country`, `data`) VALUES (%s, %s);"
sql = "INSERT INTO `coviddata_recovered_sum` (`country`, `data`) VALUES (%s, %s);"
cur = conn.cursor()
cur.executemany(sql,insertDatas)
conn.commit()
# print(confirm['China'])
# print(confirm[confirm['Country/Region']=='China'])