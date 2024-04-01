from bs4 import BeautifulSoup
import requests

def scrapBlogs():
    pageToScrape = requests.get("https://www.tapaway.com.au/blog")
    soup = BeautifulSoup(pageToScrape.text, "html.parser")
    titles = soup.findAll('p',attrs={'class':'bD0vt9'})
    views = soup.findAll('span',attrs={'class':'eYQJQu'})
    contents = soup.findAll('div',attrs={'class':'BOlnTh'})
    likes = soup.findAll('span', attrs={'class':'FYRNvd'})

    for title, view, like in zip(titles, views, likes):
        print(title.text + "  _view: " + view.text + "  _likes: " + like.text)



scrapBlogs()

# def crapWeb():
