import nltk
from nltk.corpus import stopwords
import enchant

d = enchant.Dict("en_US")
stop_words = set(stopwords.words("english"))


def check_if_english_word(word):
    if d.check(word):
        return True
    return False


def process_text(input_string):
    text = nltk.word_tokenize(input_string)
    word_with_tag = nltk.pos_tag(text)
    return word_with_tag


def is_proper_noun(input_string):
    word_with_tag = process_text(input_string)
    parts_of_speech = word_with_tag[0][1]
    if parts_of_speech == "NNP" or parts_of_speech == "NN" or parts_of_speech == "NNS":
        return True
    return False


def is_conjunction(input_string):
    word_with_tag = process_text(input_string)
    if word_with_tag[0][1] == "CC":
        return True
    return False


def get_river_name(sentence):
    words = sentence.split(" ")
    river = ""
    for i in range(len(words) - 1):
        try:
            if(words[i] == "river" or words[i] == "River") and is_proper_noun(words[i + 1]) and i+1 == len(words) - 1:
                river = words[i+1]
            elif (words[i] == "rivers" or words[i] == "Rivers" or words[i] == "river" or words[i] == "River") and is_proper_noun(words[i + 1]) and is_conjunction(words[i+2]):
                river = words[i+1] + " and " + words[i+3]
            elif (words[i] == "river" or words[i] == "River") and is_proper_noun(words[i + 1]):
                river = words[i+1]
            elif (words[i] == "river" or words[i] == "River") and is_proper_noun(words[i-1]):
                river = words[i-1]
        except:
            river = ""
    # nltk classifies even Bank as a noun! hence, this check is needed.
    if len(river) != 0 and check_if_english_word(river.lower()):
        river = ""
    return river

""" scraping module below"""
# socket.getaddrinfo('localhost', 8080)
# # get URL
# page = requests.get("https://en.wikipedia.org/wiki/List_of_rivers_of_Assam")
#
#
# # scrape webpage
# soup = BeautifulSoup(page.content, 'html.parser')
#
#
# list(soup.children)
#
# k = soup.find_all('a')
#
# rivers_list = []
# response_list = []
# for i in k:
#     print(i.get('title'))
#     response_list.append(i.get('title'))
#     # if( type(i.get('title')) != None and "River" in i.get('title')):
#     #     rivers_list.append(i.get('title'))
# res = list(filter(None, response_list))
# rivers_of_assam = list()
# #print(res)
# for element in res:
#     content_with_river_name = str(element)
#     if content_with_river_name.endswith(" River") or content_with_river_name.endswith("(page does not exist)"):
#         river_name = content_with_river_name.replace("River", "").replace("(page does not exist)", "")
#         rivers_of_assam.append(river_name)
#
# print(rivers_of_assam)
# print(len(rivers_of_assam))
