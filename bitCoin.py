from flask import Flask, render_template, request
import requests
app = Flask(__name__)

@app.route('/')
def price():
    info = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    r_json = info.json()
    Time = r_json['time']['updated']
    Des = r_json['disclaimer']
    USD_des = r_json['bpi']['USD']['description']
    USD_rate = r_json['bpi']['USD']['rate_float'] 
    GBP_des = r_json['bpi']['GBP']['description']
    GBP_rate = r_json['bpi']['GBP']['rate_float']
    EUR_des = r_json['bpi']['EUR']['description']
    EUR_rate = r_json['bpi']['EUR']['rate_float']

    return render_template("coin.html", coinTime = Time, coinDes = Des ,
    coinUSD_des= USD_des, coinUSD_rate = USD_rate ,coinGBP_des = GBP_des , 
    coinGBP_rate = GBP_rate , coinEUR_des = EUR_des , coinEUR_rate = EUR_rate)
    



if __name__ == '__main__':
    app.run(debug=True)
    

