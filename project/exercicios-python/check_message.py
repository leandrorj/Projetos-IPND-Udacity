import urllib

def read_text():
    quotes = open("C:\arquivo.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_message(contents_of_file)

def check_message(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
    output = connection.read()
    print(output)
    connection.close()


read_text()
