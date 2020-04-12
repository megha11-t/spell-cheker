from textblob import TextBlob
from nltk.tokenize import word_tokenize
from string import punctuation
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
dictionary = set()
def read_dictionary_file():
    global dictionary
    if dictionary:
        return

    with open("words.txt", "r") as f:
        contents = f.read()

    dictionary = set(
        word.lower()
        for word in contents.splitlines()

    )
def is_spelled_correctly(word):
    word = word.lower()
    read_dictionary_file()
    return word in dictionary

def check(values):
    value = values.split()
    for val in value:
        if not is_spelled_correctly(val):
            print("NOT SPELLED CORRECTLY: " + val)
            answer = None
            while answer not in ("yes", "no"):
                answer = input("You spelled incorrectly,do you want to correct it ?,say yes or no. ")
                if answer == "yes":
                    print(values.correct())
                elif answer == "no":
                    print(values)
                else:
                    print("Please enter yes or no.")
def meaning(values):
    te =values.lower()
    te = word_tokenize(te)
    without_p = [w for w in te if w not in punctuation]
    sw = stopwords.words('english')
    without_sw = [w for w in without_p if w not in sw]
    print(without_sw)
    for w in without_sw:
        de = wn.synsets(w)[0]
        print(de.name(), ' - ', de.definition(), '.')
def question_word():
    answer = None
    while answer not in ("yes", "no"):
        answer = input("Do you want to know meaning of any word say yes or no")
        if answer == "yes":
            tex = input("enter the word , to display the meaning: ")
            meaning(tex)
        elif answer == "no":
            continue
        else:
            print("Please enter yes or no.")
def text_to_user():
    answer = None
    while answer not in ("yes", "no"):
        answer = input("Do you want to continue to write a sentence, say yes or no")
        if answer == "yes":
            while True:
                values = TextBlob(input("enter sentence or paragraph:"))
                check(values)
        elif answer == "no":
            continue
        else:
            print("Please enter yes or no.")
question_word()
text_to_user()












