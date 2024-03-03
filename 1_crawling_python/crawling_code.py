# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 22:49:44 2024

@author: Admin
"""

#크롬 드라이버를 자동으로 설치하는 코드
#구글 크롬 드라이버의 자동 설치를 위한 라이브러리를 불러옵니다.
from webdriver_manager.chrome import ChromeDriverManager

#크롬 드라이버의 제어를 위해  selenium 라이브러리를 불러옵니다.
from selenium import webdriver

#크롬드라이버를 시작합니다. 프로그램이 설치되지 않았다면 프로그램을 자동으로 설치합니다
#버전이 업데이트 되면서  Chrome() 내부에  ChromeDriverManager().install() 이 필요없어짐. 
driver=webdriver.Chrome()


#구글이미지 검색 사이트로 이동합니다.
URL='https://www.google.co.kr/imghp'
driver.get(url=URL)

#사이트로 이동할 때까지 최대 10초동안 기다립니다. 
driver.implicitly_wait(time_to_wait=10)

#구글 상에서 이미지 크롤링하는 코드
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# #APjFqb는 검색창의 class의 값. 구글창에서 f12 누른 뒤 해당 코드 셀렉터를 클릭후 
#검색창을 선택하면 해당 태그 전체를 확인할 수 있음. 
elem=driver.find_element(By.CSS_SELECTOR,"#APjFqb") 
elem.send_keys("cute") ##찾을 키워드 넣기 --> 나중에는 인풋값을 집어넣을 수 있도록 하자. 
elem.send_keys(Keys.RETURN)


import time
# 태그<body> 부분에서 페이지 다운키를 200회 진행
elem= driver.find_element(By.TAG_NAME,"body")
for i in range(200):# 60회에서 200회로 늘림
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)#1에서 5로 수정. 

#중간에 결과 더보기 버튼이 있다면 눌러서 계속 사진이 보이도록 함
try:
    driver.find_element(By.CSS_SELECTOR,'#islmp > div > div > div >div.gBPM8>div.qvfT1>div.YstHxe > input').click()
    
#결과 더보기 버튼이 눌린 후 페이지 다운 키를 눌러 사진이 계속 보이도록 한다. 
    for i in range(200):#200회 늘림 
        elem.send_keys(Keys.PAGE_DOWN)
        # time.sleep(0.1)
        time.sleep(0.5) #밀리초 늘림
except Exception:
    pass

links=[]
images=driver.find_elements(By.CSS_SELECTOR,"#islrg > div.islrc > div> div> a.FRuiCf.islib.nfEiy > div.fR600b.islir > img")
##islrg > div.islrc > div > a.wXeWr.islib.nfEiy>div.bRMDJf.islir>img  <--책에는 이렇게 나왔으나 실제로 검색해서 처리 하였음.

#이미지에 링크가 있으면 links 리스트에 추가시키고 linke길이를 구한다. 
for image in images:

    if image.get_attribute('src') is not None:
        links.append(image.get_attribute('src'))
        
print('찾은 이미지 개수:',len(links))


import urllib.request

# 경로는 절대 경로로 했으며 \\을 쓴 이유는 파이썬에서 문자열 안에 \만 쓰면 이스케이프 문자로 해석하여 원하는 코딩이 나오지 않는다.
for i,k in enumerate(links):
    
    url=k
    urllib.request.urlretrieve(url,"C:\\py_crawling\\photo\\"+ str(i)+".jpg")
print('다운로드를 완료하였습니다.')
    
    





