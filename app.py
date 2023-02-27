from flask import Flask, render_template, request
import json
import logging
import pymysql
import pandas as pd
from pymysql.cursors import DictCursor

app = Flask(__name__)
conn = pymysql.connect(
    host='bj-cynosdbmysql-grp-bzwfkr20.sql.tencentcdb.com',  # Host IP Address 127.0.0.1
    user='covid',  # Username
    passwd='Aa123456789',  # Password
    port=23079,  # Port 23079
    db='covid',  # db_name
    # charset='utf8'
)


@app.route('/')
def hello_world():  # put application's code here
    return render_template("new.html")


@app.route('/get_data/nn', methods=['GET', 'POST']) 
def get_data():
    data = pd.read_csv(r'confirmed.csv', sep=',', header='infer', usecols=[0,1,2,3])
    testInfo = data.iloc[:,0:4].to_json(orient='index',date_format='epoch',force_ascii=False)
    curDict = conn.cursor(DictCursor)
    sql = 'SELECT `province`, `country`, `lat`, `long`, `id` ,`data` FROM `coviddata`'
    curDict.execute(sql)
    results = curDict.fetchall()
    count = 1
    dictData = {}
    for result in results:
        dictData[str(count)] = result
        count += 1
    # print(testInfo)
    return dictData
# ====================================================================
# A separate state data of each province
# ====================================================================
@app.route('/get_data/confirm', methods=['GET', 'POST'])
def confirm_data():
    json_data = json.loads(request.get_data())
    cou = json_data.get('country')
    pro = json_data.get('province')
    curDict1 = conn.cursor(DictCursor)
    sql = f"SELECT `data` FROM `coviddata` WHERE `province` = '{pro}' AND `country` = '{cou}'   "

    curDict1.execute(sql)
    results = curDict1.fetchall()
    curDict1.close()
    print(results)

    return results[0]


@app.route('/get_data/recovered', methods=['GET', 'POST'])
def recovered_data():
    json_data = json.loads(request.get_data())
    cou = json_data.get('country')
    pro = json_data.get('province')
    curDict2 = conn.cursor(DictCursor)
    sql = f"SELECT `data` FROM `coviddata_recovered` WHERE `province` = '{pro}' AND `country` = '{cou}'   "
    curDict2.execute(sql)
    results = curDict2.fetchall()

    temp = results[0]['data'].split(',')
    maxtemp = max(temp)
    index = temp.index(maxtemp)
    # recover max
    for i in range(index, len(temp)):
        temp[i] = maxtemp
    return {'data': ",".join(temp)}


@app.route('/get_data/deaths', methods=['GET', 'POST'])
def deaths_data():
    json_data = json.loads(request.get_data())
    cou = json_data.get('country')
    pro = json_data.get('province')
    curDict3 = conn.cursor(DictCursor)
    sql = f"SELECT `data` FROM `coviddata_death` WHERE `province` = '{pro}' AND `country` = '{cou}' "
    curDict3.execute(sql)
    results = curDict3.fetchall()
    curDict3.close()
    # print(results)
    return results[0]


@app.route('/get_data/information', methods=['GET', 'POST'])
def information():
    curDict4 = conn.cursor(DictCursor)
    sqldate = 'select value from `other` where name="information"'
    curDict4.execute(sqldate)
    results = curDict4.fetchall()
    curDict4.close()
    # print(results)
    return results[0]


@app.route('/get_data/pie', methods=['GET', 'POST'])
def pieData():
    json_data = json.loads(request.get_data())
    cou = json_data.get('country')
    pro = json_data.get('province')
    curDict6 = conn.cursor(DictCursor)
    sql = f"SELECT `data` FROM `coviddata` WHERE `province` = '{pro}' AND `country` = '{cou}' "
    curDict6.execute(sql)
    results = curDict6.fetchall()
    results = results[0]['data'].split(',')
    resultDict = {"1": int(results[89]) - int(results[0]),
                  "2": int(results[179]) - int(results[89]),
                  "3": int(results[269]) - int(results[179]),
                  "4": int(results[359]) - int(results[269]),
                  "5": int(results[449]) - int(results[359]),
                  "6": int(results[539]) - int(results[449]),
                  "7": int(results[629]) - int(results[539]),
                  "8": int(results[719]) - int(results[629]),
                  "9": int(results[809]) - int(results[719]),
                  "10": int(results[899]) - int(results[809]),
                  "11": int(results[989]) - int(results[899]),
                  "12": int(results[-1]) - int(results[989]),
                  }

    return resultDict


@app.route('/get_data/id', methods=['GET', 'POST'])
def countrySelect():
    json_data = json.loads(request.get_data())
    id = json_data.get('id')
    curDict5 = conn.cursor(DictCursor)
    sqldate = f'select `province`, `country`  FROM `coviddata` WHERE `id`={id}'
    curDict5.execute(sqldate)
    results = curDict5.fetchall()
    # print(results)
    return results[0]


# =========================================================================================
# ■
# =========================================================================================
# ====================================================================
# sum
# ====================================================================
@app.route('/get_data/sum/confirm', methods=['GET', 'POST'])
def confirm_sum_data():
    json_data = json.loads(request.get_data())
    cou = json_data.get('country')
    curDict1 = conn.cursor(DictCursor)
    sql = f"SELECT `data` FROM `coviddata_sum` WHERE `country` = '{cou}'   "
    curDict1.execute(sql)
    results = curDict1.fetchall()
    curDict1.close()
    print(results)

    return results[0]


@app.route('/get_data/sum/recovered', methods=['GET', 'POST'])
def recovered_sum_data():
    json_data = json.loads(request.get_data())
    cou = json_data.get('country')
    curDict2 = conn.cursor(DictCursor)
    sql = f"SELECT `data` FROM `coviddata_recovered_sum` WHERE `country` = '{cou}'   "
    curDict2.execute(sql)
    results = curDict2.fetchall()

    temp = results[0]['data'].split(',')
    maxtemp = max(temp)
    index = temp.index(maxtemp)
    # recover max
    for i in range(index, len(temp)):
        temp[i] = maxtemp
    return {'data': ",".join(temp)}


@app.route('/get_data/sum/deaths', methods=['GET', 'POST'])
def deaths_sum_data():
    json_data = json.loads(request.get_data())
    cou = json_data.get('country')
    curDict3 = conn.cursor(DictCursor)
    sql = f"SELECT `data` FROM `coviddata_death_sum` WHERE  `country` = '{cou}' "
    curDict3.execute(sql)
    results = curDict3.fetchall()
    curDict3.close()

    return results[0]

@app.route('/get_data/sum/pie', methods=['GET', 'POST'])
def pieSumData():
    json_data = json.loads(request.get_data())
    cou = json_data.get('country')

    curDict6 = conn.cursor(DictCursor)
    sql = f"SELECT `data` FROM `coviddata` WHERE `country` = '{cou}' "
    curDict6.execute(sql)
    results = curDict6.fetchall()
    results = results[0]['data'].split(',')
    resultDict = {"1": int(results[89]) - int(results[0]),
                  "2": int(results[179]) - int(results[89]),
                  "3": int(results[269]) - int(results[179]),
                  "4": int(results[359]) - int(results[269]),
                  "5": int(results[449]) - int(results[359]),
                  "6": int(results[539]) - int(results[449]),
                  "7": int(results[629]) - int(results[539]),
                  "8": int(results[719]) - int(results[629]),
                  "9": int(results[809]) - int(results[719]),
                  "10": int(results[899]) - int(results[809]),
                  "11": int(results[989]) - int(results[899]),
                  "12": int(results[-1]) - int(results[989]),
                  }

    return resultDict

import sys

if __name__ == '__main__':
    sys.stdout.flush()

    # achieve the data with date order

    app.debug = True
    app.run(debug=True)
