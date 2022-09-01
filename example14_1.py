import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:

    def __init__(self,text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence %s ' % reprlib.repr(self.text)


t = 'g'
sen = Sentence(f'{t} o i n ma igot go!')
for s in sen:
    print(s)

t = iter(sen)
print(t)

while True:
    elem = next(t)
    print(elem)