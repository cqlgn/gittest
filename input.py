#coding=utf-8

from selenium import webdriver
from time import sleep
import requests
import re
#获取元素
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
url = 'https://jinshuju.net/f/EwZkQr'
res = requests.get(url, headers=headers).text
#print(res)
print (type(res))
regular= re.findall(r'"apiCode":"(field_\d)',res)
for filed in regular:
    print(filed)

browser = webdriver.Chrome(executable_path ="/Users/张三/Desktop/chromedriver")#驱动保存路径\驱动名

browser.get("url链接 ")#jinshuju链接

sleep(1)

# browser.set_window_size(1400,800)#调窗口大小

name=browser.find_element_by_name(regular[0]).send_keys("姓名")

student_type=browser.find_element_by_name(regular[1]).click()


student_mingzu=browser.find_element_by_name(regular[2]).send_keys("民族");

student_date=browser.find_element_by_xpath("/html/body/div[1]/div[1]/div/form/div[3]/div[1]/div[7]/div/div/div[2]/div[1]/div/span/div/span/input").send_keys("2022-04-25");

student_number=browser.find_element_by_name(regular[4]).send_keys("13920375335009");


student_phone=browser.find_element_by_name(regular[5]).send_keys("电话");


student_address=browser.find_element_by_name(regular[6]).send_keys("住址");

browser.find_element_by_css_selector('.ant-btn').click()

# student_sub=browser.find_element_by_xpath("/html/body/div[1]/div[1]/div/form/div[5]/div[1]/button");
#
# student_sub.click();
