from selenium import webdriver
URL= "https://www.coronavirus.vic.gov.au/exposure-sites"
diver_path = "C:/temp/Development/chromedriver"
driver = webdriver.Chrome(executable_path=diver_path)

driver.get(URL)

# search = driver.find_elements_by_css_selector(".ch-exposure-sites__search-results span")
# search = driver.find_elements_by_class_name("rpl-search-results-table__value")
search = driver.find_elements_by_css_selector("td[data-tid='col-suburb']  span")
search_text1 = [item.text for item in search]
print(search_text1)
# # with open("movies.txt", "w") as file:
# #     for movie in movies:
# #         file.write(f"{movie.encode('utf-8')}\n")
# myset = list(set(search_text))
# print(myset[1:])
click2 = driver.find_element_by_xpath('//*[@id="rpl-main-content"]/div/div/div/div/div[6]/div/div/div/div[3]/div[3]/div/nav/ol/li[2]/button')
click2.click()
search2 = driver.find_elements_by_css_selector("td[data-tid='col-suburb']  span")
search_text2 = [item.text for item in search2]
print(search_text2)

click3 = driver.find_element_by_xpath('//*[@id="rpl-main-content"]/div/div/div/div/div[6]/div/div/div/div[3]/div[3]/div/nav/ol/li[3]/button')
click3.click()
search3 = driver.find_elements_by_css_selector("td[data-tid='col-suburb']  span")
search_text3 = [item.text for item in search3]
print(search_text3)

all = search_text1+search_text2+search_text3
myset = sorted(list(set(all)))
print(myset[1:])

x = 1
with open("covid_site.txt", "w") as file:

    for sub in myset[1:]:
        file.write(f"{x}. {sub}\n")
        x += 1

driver.quit()
#

