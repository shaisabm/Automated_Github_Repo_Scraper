from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import urljoin


# Gather all the repos based on the search keyword
def scrap(url):
    html = urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    anchor_tags = soup.find_all('a')

    href_links_lists = []
    for i in anchor_tags:
        href = i.get("href")
        href_links_lists.append(href)
    for j in href_links_lists:
            link_join = urljoin(url,j)
            filter_1.append(link_join)



def html_filter(filter_1):
        for i in filter_1:
            slash = 0
            for j in i:
                if j == "/":
                    slash = slash + 1
            if (slash == 4) and (i not in filter_2):
                filter_2.append(i)
            else:
                continue


def class_check(filter_2):
    for i in filter_2:
        html = urlopen(i).read()
        soup = BeautifulSoup(html, 'html.parser')
        Class = soup.find(class_="repository-content")
        if Class != None:
            file = open("repo.txt", "a")
            file.write(i)
            file.write('\n')
        else:
            pass
    file.close()



search_word = input("Enetr the search word (use + as+space): ")
page = 1
while True:
    target_search = f'https://www.github.com/search?q={search_word}&type=repositories&p={page}'
    html = urlopen(target_search)
    soup = BeautifulSoup(html, 'html.parser')
    print(f"Working on page {page}")
    joined_links = []
    filter_1 = []
    filter_2 = []

    if 'Your search did not match any repositories' in soup.get_text():
        print("page end reached")
        break
    else:
        scrap(target_search)
        print("scrap done")
        html_filter(filter_1)
        print("html_filter done")
        class_check(filter_2)
        print("class_check done")
        page = page + 1



















