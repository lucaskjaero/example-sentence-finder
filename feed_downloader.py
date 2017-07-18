import feedparser

NY_TIMES_URL = "https://cn.nytimes.com/rss.html"


def download_data():
    feed = feedparser.parse(NY_TIMES_URL)
    data = [[article.title, article.link] for article in feed['entries']]
    return data


def main():
    with open("article_headers.csv", "a") as output:
        for title, link in download_data():
            output_line = '"%s","%s"\n' % (title, link)
            output.write(output_line)


if __name__ == '__main__':
    main()
