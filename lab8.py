from abc import ABC


class Count(ABC):
    def __init__(self, address):
        self.adress = address

    def calculateFreq(self):
        pass


class ListCount(Count):
    def __init__(self, address):
        super().__init__(address)

    def calculateFreq(self):  # make constructor and super.
        file1 = open(address, "r")
        str1 = file1.read()
        list1 = str1.split()
        unique = set(list1)

        print("List Count\n")
        for words in unique:
            print("frequency of ", words, " is ", list1.count(words))

        file1.close()


class DictCount(Count):

    def __init__(self, address):
        super().__init__(address)

    def calculateFreq(self):
        file2 = open(address, "r")
        str2 = file2.read()
        dict1 = {}
        print("\nDict Count\n")
        for words in str2.split():
            dict1[words] = dict1.get(words, 0)+1
        for unique in dict1:
            print("frequency of ", unique, " is ", dict1[unique])


address = "strange.txt"  # file is in the project directory
file = open(address, "r")
obj = ListCount
str = file
obj.calculateFreq(str)

obj2 = DictCount
str2 = file
obj2.calculateFreq(str2)
