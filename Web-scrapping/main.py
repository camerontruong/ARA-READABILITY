from bs4 import BeautifulSoup
import lxml
import requests

URL ="https://www.rottentomatoes.com/top/bestofrt/top_100_kids__family_movies/"

response = requests.get(URL)
web = response.text
soup = BeautifulSoup(web, "html.parser")

movies = soup.find_all(name="a", class_="unstyled articleLink")
# print(movies)
text = [m.getText() for m in movies]
t = text[43:-2]
ts = [it.split("\n",1)[1] for it in t]
print(ts)

x = 1
with open("children_movies.text", 'w') as file:
    for m in ts:
        file.write(f"{x}. {m}\n")
        x += 1

# URL = "https://www.timeout.com/newyork/movies/best-movies-of-all-time"
# response = requests.get(URL)
# web = response.text
# soup = BeautifulSoup(web, "html.parser")
#
# # print(soup.prettify())
# movies = soup.find_all(name="h3" , class_="_h3_cuogz_1")
# print(movies)
# names = [t.getText().split("\xa0",1) for t in soup.find_all(name="h3" , class_="_h3_cuogz_1")]
# names = names[:-1]
# # movies_names = [item[0] for item in names]
# movies_names = [item[1] for item in names]
#
# move = movies_names[::-1]
# x = 1
# with open("movies.text", 'w') as file:
#     for m in move:
#         file.write(f"{x}. {m}\n")
#         x += 1

# response = requests.get(URL)
# web = response.text
# soup = BeautifulSoup(web, "html.parser")

# response = requests.get("https://news.ycombinator.com/news")
# web = response.text
# https://www.timeout.com/newyork/movies/best-movies-of-all-time
# soup = BeautifulSoup(web, "html.parser")
#
#<h3 class="jsx-4245974604">99) Raging Bull</h3>
#
# texts = [t.getText() for t in soup.find_all(name="a", class_="storylink")]
# links = [t.get("href") for t in soup.find_all(name="a", class_="storylink")]
# points = [int(s.getText().split()[0]) for s in soup.find_all(name='span', class_="score")]
#
#
# # print(texts)
#
# max_index = points.index(max(points))
# print(texts[max_index])
# print(links[max_index])
# print(points[max_index])
# with open("website.html", encoding="utf8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
#
# # print(soup.title)
# # print(soup.title.string)
# # print(soup.prettify())
#
# # print(soup.p)
# anchor = soup.find_all(name="a")
#
# for tag in anchor:
#     print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading.getText())
#
# section = soup.find(name='h3', class_='heading')
# print(section.getText())
#
# company_url = soup.select_one(selector="#name")
# print(company_url)
#
# headings = soup.select(".heading")
# print(headings)