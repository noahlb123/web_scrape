import requests

site = 'https://dining.uconn.edu/spring-valley-farm/housing-2/'
print('\nthe website:\n' + site + '\nis', end=' ')

class Works():
    def __init__(self):
        self.page = requests.get(site)
        self.pageT = self.page.text

        self.pre = open("Previous.txt","r")
        self.preT = self.pre.read()
        self.c1 = 0
        self.c2 = 0

    def this_ok(self, a, b, c):
        return ord(self.pageT[self.c2]) == a and ord(self.pageT[self.c2 + 1]) == b and ord(self.preT[self.c1]) == c

    def skip_comment(self):
        k1 = self.c1
        k2 = self.c2
        while self.preT[k1:k1+3] != '-->' and self.preT[k1:k1+2] != ']>':
            k1 += 1
        while self.pageT[k2:k2+3] != '-->' and self.pageT[k2:k2+2] != ']>':
            k2 += 1
        return k1, k2
    
    def magic(self):
        max = len(self.pageT)
        while True:
            try:
                if self.preT[self.c1:self.c1+4] == '<!--' or self.pageT[self.c2:self.c2+4] == '<!--':
                    self.c1, self.c2 = self.skip_comment()
                    continue
                elif self.preT[self.c1] != self.pageT[self.c2]:
                    if self.this_ok(13, 10, 10):
                        self.c2 += 1
                        continue
                    else:
                        print('DIFFERENT\n')
                        print(ord(self.pageT[self.c2]), ord(self.pageT[self.c2+1]))
                        print(ord(self.preT[self.c1]), ord(self.preT[self.c1+1]))
                        print(self.pageT[self.c2-5:self.c2+5])
                        print(self.preT[self.c1-5:self.c1+5],'\n')
                        break
                self.c1 += 1
                self.c2 += 1
            except IndexError:
                print('same\n')
                break
w = Works()
w.magic()
