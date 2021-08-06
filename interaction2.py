from selenium import webdriver
URL= "https://en.wikipedia.org/wiki/Main_Page"
diver_path = "C:/temp/Development/chromedriver"
driver = webdriver.Chrome(executable_path=diver_path)

driver.get(URL)

# article = driver.find_element_by_css_selector("#articlecount a")
# article.click()

all_portals = driver.find_element_by_link_text("All portals")
all_portals.click()