class Simpledb:
    def __init__(self, filename):
        self.filename = filename

    # def insert(self,key,value):
    # f=open(self.filename,'a')
    # f.write(key+'\t'+value+'\n')
    # f.close()
    def add(self, key, value):
        f = open(self.filename, 'a')
        f.write(key + '\t' + value + '\n')
        f.close()

    def find(self, key):
        f = open(self.filename, 'r')
        found = False
        for row in f:
            (k, v) = row.split('\t', 1)
            if k == key:
                value = v
                print(value)
                found = True
                break
        if found == False:
            print('That is not in this database.')
        f.close

    def delete(self, key):
        f = open(self.filename, 'r')
        result = open('result.txt', 'w')
        for (row) in f:
            (k, v) = row.split('\t', 1)
            if k != key:
                result.write(row)
        if len(self.filename) == len('result.txt'):
            print('That is not in this database')
        f.close()
        result.close()
        import os
        os.replace('result.txt', self.filename)

    def update(self, key, value):
        f = open(self.filename, 'r')
        result = open('result.txt', 'w')
        for (row) in f:
            (k, v) = row.split('\t', 1)
        if k == key:
            result.write(key + '\t' + value + '\n')
        else:
            result.write(row)
        f.close()
        result.close()
        import os
        os.replace('result.txt', self.filename)

    def __repr__(self):
        return ('<' + self.__class__.__name__ + 'file=' + self.filename)

    def quit():
        exit()






