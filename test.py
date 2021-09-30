import urllib.request
import os

def match(text, alphabet=set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')):
        return not alphabet.isdisjoint(text.lower())

pathToFile = os.getcwd() + '\\onTest.txt'
file = open(pathToFile)
arr = []
for line in file:
        try:
                print(line)
                answer = urllib.request.urlopen(urllib.request.Request(line, headers={'User-Agent': 'Mozilla/5.0'}), timeout=3);
                answer_charset = answer.headers.get_content_charset()
                if(answer_charset==None):
                        answer_charset='UTF-8'
                answer_body = answer.read()
                f=''
                try:
                        f = answer_body.decode(answer_charset)
                except:
                        f = answer_body.decode('cp1251', errors='ignore')
                if(match(f)):
                        arr.append(line[:-1] + ' - СНГ')
                else:
                        arr.append(line[:-1] + ' - ENG')
        except:
                arr.append(line[:-1] + ' - error')
file = open(pathToFile, 'w')
file.write("\n".join(arr))
file.close()


