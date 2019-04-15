import re

# answer: 

class SimpleBars(list):

    def __str__(self):
        return "".join(self)

    def __len__(self):
       return len(self.__str__())
    
    def next(self):
        before = self
        after = before

        for i in range(len(self.__str__()) - 1):
            if 'iTi' == before[i:3]:
                after[i + 1] = 'i'
            elif 'T' == before[i]:
                after[i] = "i"
            elif 'i ' == before[i:1]:
                after[i + 1] = "i"
            elif ' i' == before[i:1]:
                after[i] = "i"
            elif 'i' == before[i]:
                after[i] = "T"
            

        # if re.search('iTi', before):
        #     after = re.sub('iTi', ' i ', before)
        # if re.search(' iT ', before):
        #     after = re.sub(' iT ', '    ', before)
        # if re.search(' Ti ', before):
        #     after = re.sub(' Ti ', '    ', before)
        # for rep in re.findall('T'):
        #     after = re.sub(' T ', ' i ', before)
        
        # if re.search('i i', before):
        #     after = re.sub('i i', '   ', before)
        # if re.search('i ', before):
        #     after = re.sub(' i', '  ', before)
        # if re.search(' i', before):
        #     after = re.sub('i ', '  ', before)
        # if re.search(' ', before):
        #     after = re.sub(' ', ' ', before)
        
        # if re.search('i', before):
        #     after = re.sub('i', 'T', before)
        
        # aaa
        # if self.__str__() == 'Ti  ':
        #     self.insert(0, self.pop())
        #     return self.__str__()
        # elif self.__str__() == ' Ti ':
        #     self.insert(0, self.pop())
        #     return self.__str__()
        # elif self.__str__() == '  Ti':
        #     self.insert(0, self.pop())
        #     return self.__str__()
        # elif self.__str__() == 'i  T':
        #     self.insert(0, self.pop())
        #     return self.__str__()
        # bbb
        # elif self.__str__() == '  iT':
        #     self.append(self.pop(0))
        #     return self.__str__()
        # elif self.__str__() == ' iT ':
        #     self.append(self.pop(0))
        #     return self.__str__()
        # elif self.__str__() == 'iT  ':
        #     self.append(self.pop(0))
        #     return self.__str__()
        # elif self.__str__() == 'T  i':
        #     self.append(self.pop(0))
        #     return self.__str__()
        
        self.clear()
        self.append('i'*24)