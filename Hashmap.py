class hashmap:
    def __init__(self, size = 10):
        self.size = size
        self.hashlist = [None] * self.size
    
    def getHash(self, key):
        return hash(key) % self.size

    def __setitem__(self, key, value):
        index = self.getHash(key)
        if not self.hashlist[index]:
            self.hashlist[index] = [[key, value]]
        else:
            sublist = self.hashlist[index]
            for pair in sublist:
                if pair[0] == key:
                    pair[1] = value
                    return
            self.hashlist[index].append([key,value])

    def __getitem__(self, key):
        index = self.getHash(key)
        if self.hashlist[index]:
            sublist = self.hashlist[index]
            for pair in sublist:
                if pair[0] == key:
                    return pair[1]
        return "Key Not Found"
    
    def __delitem__(self, key):
        index = self.getHash(key)
        if self.hashlist[index]:
            sublist = self.hashlist[index]
            for i,pair in enumerate(sublist):
                if pair[0] == key:
                    del sublist[i]
                    return
        return "Key Not Found"


hashmap = hashmap()
hashmap["Name"] = "Asqar"
hashmap["Age"] = 19
hashmap["DOB"] = "26-08-2008"
print(hashmap["Name"])
del hashmap["Name"]
print(hashmap["Name"])