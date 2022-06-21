import re

def word_frequencies(filename):
    list = []
    dict = {}
    with open (filename, 'r') as f:
        for line in f:
            line=line.strip("""!"#$%&'()*,-./:;?@[]_""")
            for word in re.findall(r"([a-zA-Z]+)", line, re.IGNORECASE):
                list.append(word)
            #list.append(i for i in re.findall(r"([a-zA-Z]+)", line)) creates generstor objects
        for i in set(list):
            dict[i] = list.count(i)
    print(dict)
    return dict

def main():
        filename = input("TEST CASE:\nPlease write the path of the file that you want to get word frequencies:")
        word_frequencies(filename)

if __name__ == "__main__":
    main()
