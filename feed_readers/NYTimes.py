from urllib.request import urlopen

import feedparser

from bs4 import BeautifulSoup

from feed_reader_base import FeedReader

NY_TIMES_URL = "https://cn.nytimes.com/rss.html"

class NYTimes(FeedReader):
    def get_articles(self):
        articles = []
        for title, link in download_feed_data():
            article = get_article_text(link)
            output_dict = {
                'title': title,
                'link': link,
                'article': article
            }
            articles.append(output_dict)

        return articles


def download_feed_data():
    feed = feedparser.parse(NY_TIMES_URL)
    data = [[article.title, article.link] for article in feed['entries']]
    return data


def get_article_text(link):
    html = urlopen(link).read()
    page = BeautifulSoup(html, "html5lib")

    content_div = page.find(id="content")
    sentences = [paragraph.string for paragraph in content_div.find_all('p', attrs={'class':'paragraph'}) if paragraph.string is not None]
    article = "".join(sentences)

    return article


def write_feed_information(file_name="article_headers.csv"):
    with open(file_name, "a") as output:
        for title, link in download_feed_data():
            output_line = '"%s","%s"\n' % (title, link)
            output.write(output_line)


def main():
    write_feed_information()
    for title, link in download_feed_data():
        file_name = title + ".txt"
        with open(file_name, "w") as output:
            output.write(get_article_text(link))


if __name__ == '__main__':
    main()
