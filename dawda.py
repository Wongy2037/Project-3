from flask import Flask, render_template,request
import json
import pandas as pd
import pymysql
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
@app.route('/get_data/nn',methods=['GET','POST'])
def get_data():
    testInfo={}
    testInfo['name'] = 'xiaoming'
    testInfo['age'] = '28'
    data = pd.read_csv(r'confirmed.csv', sep=',', header='infer', usecols=[0,1,2,3])
    testInfo = data.iloc[:,0:4].to_json(orient='index',date_format='epoch',force_ascii=False)
    print(testInfo)
    return testInfo
@app.route('/get_data/confirm',methods=['GET','POST'])
def confirm_data():
    json_data = json.loads(request.get_data())
    country = json_data.get('country')
    province =   json_data.get('province')
    confirm = pd.read_csv(r'confirmed.csv', sep=',', header='infer')
    if province=="block":
        confirm = confirm[
            confirm["Country/Region"] == country].iloc[:,4:]
    elif country=="block":
        confirm = confirm[
            confirm["Province/State"] == province].iloc[:,4:]
    else:
        confirm = confirm[
            (confirm["Country/Region"] == country) & (confirm[
                                                          "Province/State"] == province)].iloc[:,4:]
    result = confirm.to_json(orient='records', date_format='epoch', force_ascii=False)
    print("confirm",type(result),result)


    return result[1:-1]
@app.route('/get_data/recovered',methods=['GET','POST'])
def recovered_data():

    json_data = json.loads(request.get_data())
    country = json_data.get('country')
    province = json_data.get('province')
    recovered = pd.read_csv(r'recovered.csv', sep=',', header='infer')
    if province == "block":
        recovered = recovered[
                      recovered["Country/Region"] == country].iloc[:, 4:]
    elif country == "block":
        recovered = recovered[
                      recovered["Province/State"] == province].iloc[:, 4:]
    else:
        recovered = recovered[
                      (recovered["Country/Region"] == country) & (recovered[
                                                                    "Province/State"] == province)].iloc[:, 4:]

    result = recovered.to_json(orient='records', date_format='epoch', force_ascii=False)
    print("recovered", type(result), result)

    return result[1:-1]
@app.route('/get_data/deaths',methods=['GET','POST'])
def deaths_data():
    json_data = json.loads(request.get_data())
    country = json_data.get('country')
    province = json_data.get('province')
    deaths = pd.read_csv(r'deaths.csv', sep=',', header='infer')
    if province == "block":
        deaths = deaths[
                        deaths["Country/Region"] == country].iloc[:, 4:]
    elif country == "block":
        deaths = deaths[
                        deaths["Province/State"] == province].iloc[:, 4:]
    else:
        deaths = deaths[
                        (deaths["Country/Region"] == country) & (deaths[
                                                                        "Province/State"] == province)].iloc[:, 4:]
    result = deaths.to_json(orient='records', date_format='epoch', force_ascii=False)
    print("deaths", type(result), result)

    return result[1:-1]


# deaths = pd.read_csv(r'deaths.csv', sep=',', header='infer')
# deaths = deaths.iloc[1, 4:].to_json(orient='index', date_format='epoch', force_ascii=False)

if __name__ == '__main__':
    app.debug=True
    app.run(debug=True)
