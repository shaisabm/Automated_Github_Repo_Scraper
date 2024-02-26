from bs4 import BeautifulSoup
from urllib.parse import urljoin
from selenium import webdriver

# Gather all the files from individual repo from repo.txt

def auto(repo_base):
    browser = webdriver.Firefox()
    folders = open("all_folders.txt",'r')
    all_files = open('all_files.txt','a')
    links = folders.readlines()

    for link in links:
        browser.get(link)
        soup = BeautifulSoup(browser.page_source, 'html.parser')

        all_links = set(soup.find_all(class_='react-directory-truncate'))

        for link in all_links:
            anchor_tag = link.find('a')
            href = anchor_tag.get('href')
            if "(Directory)" in str(link):
                links.append(urljoin(repo_base, href))
            else:
                all_files.write(urljoin(repo_base, href) + "\n")
    browser.close()
    folders.close()
    all_files.close()




def directory(repo):
    browser = webdriver.Firefox()
    browser.get(repo)
    soup = BeautifulSoup(browser.page_source,'html.parser')
    all_links =set(soup.find_all(class_='react-directory-truncate'))

    all_files = open('all_files.txt', 'a')
    all_folders = open('all_folders.txt', 'a')
    for link in all_links:
        anchor_tag = link.find('a')
        href = anchor_tag.get('href')
        if "(Directory)" in str(link):
            all_folders.write(urljoin(repo, href)+'\n')
        else: all_files.write(urljoin(repo,href)+"\n")
    browser.close()
    all_files.close()
    all_folders.close()



def main(repo):

    directory(repo)
    auto(repo_base='https://github.com/')



with open('repo.txt','r') as repo_file:
    scap_repo = input("Enter the number of repo to be scrap (enter * to scap all repo): ")
    repos= repo_file.read().split()
    if scap_repo == '*': scap_repo = len(repos)
    repo_file.close()
    count = 0
    while count < int(scap_repo):
        main(repos[count])
        print(repos[count])
        count += 1







