
from selenium import webdriver
URL = "https://www.amazon.com/LG-32QN600-B-32-Inch-Monitor-FreeSync/dp/B088YN9LBK/ref=sxin_11_ac_d_rm?ac_md=0-0-Y29tcHV0ZXIgbW9uaXRvciAzMiBpbmNo-ac_d_rm_rm_rm&crid=1QY186FCHGPHE&cv_ct_cx=computer+monitor+32+inch&dchild=1&keywords=computer+monitor+32+inch&pd_rd_i=B088YN9LBK&pd_rd_r=01ef8f0b-3fde-445e-87d1-d8653158da58&pd_rd_w=iqrAy&pd_rd_wg=ptY9n&pf_rd_p=bdf723b2-f1c3-4d1c-967e-60197e162550&pf_rd_r=RJFW5D2D2EG3WE0CJ5EJ&psc=1&qid=1628211947&sprefix=computer+monitor+32%2Caps%2C383&sr=1-1-12d4272d-8adb-4121-8624-135149aa9081"

diver_path = "C:/temp/Development/chromedriver"
driver = webdriver.Chrome(executable_path=diver_path)

driver.get("https://www.python.org")
# price = driver.find_element_by_id("priceblock_ourprice")
# search_bar = driver.find_element_by_name("q")
# driver.close()
# driver.quit()
# logo = driver.find_element_by_class_name("python-logo")
# link = driver.find_element_by_css_selector(".documentation-widget a")
# link = driver.find_element_by_xpath('//*[@id="__next"]/main/article/div[5]/div[2]/div[2]/h3')

event_time = driver.find_elements_by_css_selector(".event-widget time")

event_name = driver.find_elements_by_css_selector(".event-widget li a")

text =[t.text for t in event_time]
print(text)

names =[t.text for t in event_name]
print(names)

events = {}
# x = 0
# for i in text:
#     dict = {}
#     dict['time'] = text[x]
#     dict['name'] = names[x]
#     events[x] = dict
#     x += 1
#
# print(events)

for n in range(len(text)):
    events[n] = {
        "time": event_time[n].text,
        "name": event_name[n].text,
    }
print(events)
driver.quit()