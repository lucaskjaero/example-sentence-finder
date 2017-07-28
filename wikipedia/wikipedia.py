from xml.etree.cElementTree import iterparse
import codecs

from bs4 import BeautifulSoup

PATH = "zhwiki-20170701-pages-meta-current.xml"


def process_page(xml):
    soup = BeautifulSoup(xml, "lxml-xml")
    title = soup.title.string
    text = soup.get_text()

    if "talk" not in title and "User" not in title and "Talk" not in title and "Wikipedia" not in title and "Help" not in title:
        print(title)
        print()
        print(text)
        print("+" * 40)


def get_wikipedia_pages(path=PATH):
    # Used tipes from http://enginerds.craftsy.com/blog/2014/04/parsing-large-xml-files-in-python-without-a-billion-gigs-of-ram.html
    inputbuffer = ""
    count = 0
    with codecs.open(path, "r", "utf-8") as source:
        append = False
        for line in source:
            if "<page>" in line:
                inputbuffer = line
                append = True
            elif "</page>" in line:
                inputbuffer += line
                append = False
                process_page(inputbuffer)
                inputbuffer = None

                # Let's develop with a reasonable number of articles first
                count = count + 1
                if count > 5:
                    break
            elif append:
                inputbuffer += line


def main():
    get_wikipedia_pages()


if __name__ == '__main__':
    main()
