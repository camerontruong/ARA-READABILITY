from selenium import webdriver
URL= "https://www.empireonline.com/movies/features/best-movies-2/"
diver_path = "C:/temp/Development/chromedriver"
driver = webdriver.Chrome(executable_path=diver_path)

driver.get(URL)

search = driver.find_elements_by_css_selector(".listicle-item h3")
movies = [item.text for item in search]
movies = movies[::-1]
with open("movies.txt", "w") as file:
    for movie in movies:
        file.write(f"{movie.encode('utf-8')}\n")
driver.quit()