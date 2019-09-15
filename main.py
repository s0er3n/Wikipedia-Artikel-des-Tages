from bs4 import BeautifulSoup
import requests
import webbrowser
wiki = requests.get("https://de.wikipedia.org/wiki/Wikipedia:Hauptseite")

soup = BeautifulSoup(wiki.text, "lxml").find("div", title="Artikel des Tages").p.b.a["href"]

print()
webbrowser.open("https://de.wikipedia.org" +soup)
