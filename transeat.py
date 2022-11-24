import requests
from urllib.parse import urlparse, parse_qsl, urlencode, urlunparse
from bs4 import BeautifulSoup as bs
from korail2 import *
print("전화번호, 비밀번호 순으로 입력하세요.")
phone_number = str(input())
password = str(input())
korail = Korail(phone_number, password)
korail.login()

parts = urlparse("https://www.letskorail.com/ebizprd/EbizPrdTicketPr11131_i1.do?txtRunDt=20221123&txtDptDt=20221123&txtTrnNo=01005&txtTrnGpCd=101")

print("출발역, 도착역 순으로 입력하세요.")
dep=str(input())
arr=str(input())
print("출발일, 도착일, 기차번호, 기차종류, 날짜 순으로 입력하세요.")
txtRunDt=str(input())#'20221127'
txtDptDt=str(input())#'20221127'
txtTrnNo=str(input())#'00171'
txtTrnGpCd=str(input())#'100'
date=str(input())#'20221127'

def find_station(parts, txtRunDt,txtDptDt,txtTrnNo,txtTrnGpCd):
    qs = dict(parse_qsl(parts.query))
    qs['txtRunDt'] = txtRunDt
    parts = parts._replace(query=urlencode(qs))

    qs = dict(parse_qsl(parts.query))
    qs['txtDptDt'] = txtDptDt
    parts = parts._replace(query=urlencode(qs))

    qs = dict(parse_qsl(parts.query))
    qs['txtTrnNo'] = txtTrnNo
    parts = parts._replace(query=urlencode(qs))

    qs = dict(parse_qsl(parts.query))
    qs['txtTrnGpCd'] = txtTrnGpCd
    parts = parts._replace(query=urlencode(qs))
    new_url = urlunparse(parts)

    return new_url

def check_seat_part(a,dep_index,arr_index,date,time):
    phone_number = "01024884113"
    password = "gustj486!!"
    dep='%s'%a[dep_index]
    arr='%s'%a[arr_index]
    trains1 = korail.search_train(dep, arr, date, time)
    trains2 = korail.search_train(dep, arr, date, time, include_no_seats=True)
    if trains1==[]:
        return 0
    else:
        x = trains1[0].dep_time
        y = trains2[0].dep_time


        if x == y:
            print(dep, arr)
            print(trains2[0])
            return 1
        else:
            return 0

'''def find_seat(a: list,dep,arr,phone_number,passward):
    korail = Korail(phone_number, passward, want_feedback=True)
    tickets = korail.tickets()
    print(tickets)'''


def check_seat(a,b,dep,arr,date,phone_number,passward):
    seat_set=[]
    dep_index=0
    arr_index=0
    n=len(a)
    for i in range(0,n):
        if dep==a[i]:
            dep_index=i
        if arr==a[i]:
            arr_index=i
    dep_shadow_index=dep_index
    arr_shadow_index=arr_index
    if dep_index<arr_index:
        while dep_shadow_index<arr_shadow_index:
            if check_seat_part(a,dep_shadow_index,arr_shadow_index,date,b[dep_shadow_index])==0: #check_seat_part:해당 구간에 좌석이 있으면 1을 리턴, 없으면 0을 리턴
                arr_shadow_index-=1
                continue
            else:
                #seat_set.append(find_seat(a,dep_shadow_index,i,phone_number,password)) #find_seat:해당 구간의 특정 좌석을 리턴
                print(a[arr_shadow_index])
                dep_shadow_index=arr_shadow_index
                arr_shadow_index=arr_index




new_url = find_station(parts,txtRunDt,txtDptDt,txtTrnNo,txtTrnGpCd)


print(new_url) # https://velog.io/tags?sort=name&keyword=new
res = requests.get(new_url)
station_list=[]
dep_time=[]
n=0 #해당 열차의 정차역 갯수를 셀 변수
soup = bs(res.text, 'html.parser')
for p in soup.select('tr'):
    n+=1
n-=2
print(n)

if res.status_code == 200:
    html = res.text
    soup = bs(html, 'html.parser')
    for i in range(1,n+1):
        title = soup.select_one('body > div > div.cont > div > table > tbody > tr:nth-child(%d) > td:nth-child(1)'%i)
        station_list.append(title.get_text().strip())
        title = soup.select_one('body > div > div.cont > div > table > tbody > tr:nth-child(%d) > td:nth-child(3)' %i)
        dep_t=title.get_text().strip()
        dep_t=dep_t.replace(':','')
        dep_t+='00'
        dep_time.append(dep_t)
else:
    print(res.status_code)
print(station_list)
print(dep_time)
check_seat(station_list,dep_time,dep,arr,date,phone_number,password)
