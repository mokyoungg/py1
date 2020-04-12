#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests                       #웹 페이지의 HTML을 가져오는 모듈
from bs4 import BeautifulSoup         #HTML을 파싱하는 모듈

#웹 페이지를 가져온 뒤 BeautifulSoup 객체로 만듦
response = requests.get('https://www.koreabaseball.com/Record/Player/HitterBasic/Basic1.aspx')
soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('table', { 'class': 'tData01 tt' })  #<table class ="tData01 tt">을 찾음

data = []                            #데이터를 저장할 리스트 생성
for tr in table.find_all('tr'):     #모든 <tr> 태그를 찾아서 반복( 각 지점의 데이터를 가져옴)
    tds = list(tr.find_all('td'))   # 모든 <td> 태그를 찾아서 리스트로 만듦
                                    #(각 세부 기록을 리스트로 만듦)
    for td in tds:                 #<td> 태그 리스트 반복(각 세부 기록을 가져옴)
        if td.find('a'):       #<a> 태그 안에서 선수이름을 가져옴
            player = td.find('a').text       #<a> 태그 안에서 선수 이름을 가져옴
            bat_average = tds[3].text        #<td> 태그 리스트의 '네 번째'(인덱스 3)에서 타율을 가지고 온다.
            hit = tds[8].text                #<td> 태그 리스트의 '아홉번째'(인덱스 8)에서 안타를 가져온다.
            homerun = tds[11].text           #<td> 태그 리스트의 '열두번째'(인덱스 11)에서 홈런을 가져온다.
            RBI = tds[13].text               #<td> 태그 리스트의 '열네번째'(인덱스 13)에서 타점을 가져온다.
            data.append([player, bat_average, hit, homerun, RBI])   #dat 리스트에 선수, 타율, 안타를 추가

data  # data 표시.


# In[2]:


with open('2019KBObatter.csv', 'w') as file:         # 2019KBObatter.csv. 파일을 쓰기 모드로 열기
    file.write('player,bat_average,hit,homerun,RBI\n')            # 컬럼 이름 추가
    for i in data:                                   # data를 반복하면서
        file.write('{0},{1},{2},{3},{4}\n'.format(i[0], i[1], i[2], i[3],i[4]))  #선수이름,타율,안타수를 줄 단위로 저장


# In[3]:


#%matplotlib inline을 설정하면 matplotlib.pyplot의 show 함수를 호출하지 않아도
#주피터 노트북 안에서 그래프가 표시됨
get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd          # 데이터를 저장하고 처리하는 패키지
import matplotlib as mpl     # 그래프를 그리는 패키지
import matplotlib.pyplot as plt   # 그래프를 그리는 패키지

# csv 파일을 읽어 DataFrame 객체로 만듦. 인덱스 컬럼은 player로 설정
df = pd.read_csv('2019KBObatter.csv', index_col='player', encoding='euc-kr')
df            # df 표시


# In[4]:


# 상위 10명만 모아서 DataFrame 객체로 만듦
topb_df = df.loc[['양의지', '페르난데스', '박민우', '이정후', '강백호', '고종욱', '로하스', '박건우', '유한준', '채은성']]
topb_df   # topb_df 표시

