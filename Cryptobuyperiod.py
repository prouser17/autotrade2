import pyupbit
import schedule
import time


access = ""
secret = ""
upbit = pyupbit.Upbit(access, secret)



# step2.실행할 함수 선언
def message1():
    from datetime import datetime
    now = datetime.now()
    print("Current Time is",now)

KRW = upbit.get_balance("KRW")         # 보유 현금 조회
print(KRW)

def periodic_buy():
    print(KRW)
    if KRW > 5000:
                    upbit.buy_market_order("KRW-BTC", 5000)       
            #         upbit.buy_limit_order("KRW-BTC", 56000000, 0.0001)
                    KRW = upbit.get_balance("KRW")         # 보유 현금 조회
                    print(KRW)
                    print("purchase complete")
    else: print("not enough money to buy")
           
# step3.실행 주기 설정

schedule.every().day.at("00:00").do(periodic_buy)
schedule.every().day.at("01:00").do(periodic_buy)
schedule.every().day.at("02:00").do(periodic_buy)
schedule.every().day.at("03:00").do(periodic_buy)
schedule.every().day.at("04:00").do(periodic_buy)
schedule.every().day.at("05:00").do(periodic_buy)
schedule.every().day.at("06:00").do(periodic_buy)
schedule.every().day.at("07:00").do(periodic_buy)
schedule.every().day.at("08:00").do(periodic_buy)
schedule.every().day.at("09:00").do(periodic_buy)
schedule.every().day.at("10:00").do(periodic_buy)
schedule.every().day.at("11:00").do(periodic_buy)
schedule.every().day.at("12:00").do(periodic_buy)
schedule.every().day.at("13:00").do(periodic_buy)
schedule.every().day.at("14:00").do(periodic_buy)
schedule.every().day.at("15:00").do(periodic_buy)
schedule.every().day.at("16:00").do(periodic_buy)
schedule.every().day.at("17:00").do(periodic_buy)
schedule.every().day.at("18:00").do(periodic_buy)
schedule.every().day.at("19:00").do(periodic_buy)
schedule.every().day.at("20:00").do(periodic_buy)
schedule.every().day.at("21:00").do(periodic_buy)
schedule.every().day.at("22:00").do(periodic_buy)
schedule.every().day.at("23:00").do(periodic_buy)


#schedule.every(5).seconds.do(message1)

# step4.스캐쥴 시작
while True:
    schedule.run_pending()
    time.sleep(1)

#schedule.every().day.at("15:26:00").do(periodic_buy("KRW-BTC"))