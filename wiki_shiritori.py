import requests
from bs4 import BeautifulSoup
import re

def get_wikipedia_links(topic):
    url = f"https://en.wikipedia.org/wiki/{topic}"
    response = requests.get(url)
    if response.status_code != 200:
        return None

    soup = BeautifulSoup(response.content, 'html.parser')
    content = soup.find(id="bodyContent")
    links = content.find_all('a', href=True)
    
    valid_links = []
    for link in links:
        href = link['href']
        # Check if the link is a valid Wikipedia article link
        if href.startswith("/wiki/") and not href.startswith("/wiki/Special:") and not ':' in href:
            valid_links.append(href[6:])
    return valid_links

def get_last_char(word):
    word = re.sub(r'\W+', '', word)  # Remove non-alphanumeric characters
    if not word:
        return None
    return word[-1]

def find_next_word(words):
    last_char = get_last_char(words[-1])
    if not last_char:
        return None
    
    links = get_wikipedia_links(words[-1])
    if not links:
        return None
    
    for link in links:
        if link[0].lower() == last_char:
            return link
    return None

def wiki_shiritori(start_word):
    words = [start_word]
    while True:
        next_word = find_next_word(words)
        if not next_word or next_word in words:
            break
        words.append(next_word)
        print(f"Next word: {next_word}")
    return words

if __name__ == "__main__":
    start_word = input("Enter a starting word: ")
    words = wiki_shiritori(start_word)
    print("Wiki Shiritori Sequence:")
    for word in words:
        print(word)
