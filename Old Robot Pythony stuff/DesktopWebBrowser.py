import requests
from bs4 import BeautifulSoup
while True:
    word = raw_input("Type the word: ")

    print("Getting the synonyms for " + word)
    req = requests.get("http://www.thesaurus.com/browse/" + word)
    print("Done! Parsing the html")

    if req.status_code != 200:
        print("There was an error!")
        exit(1)

    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    all_a = soup.find_all('a')
    syn = []
    for a in all_a:
        try:
            if str(a.get("href")).startswith("/browse/"):
                synonym = str(a.string).encode("ASCII")
                if word != synonym:
                    syn.append(synonym)
        except:
            pass

    print("The synonyms for " + word + " are")
    print(syn)

    #print(req
    # .status_code)
    #print(req.text)