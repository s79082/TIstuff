class Parser:

    values = {
        'x': 1,
        'y': 2,
        'z': 3
    }

    operations = {
        '+': lambda x,y : x+y,
        '-': lambda x,y : x-y,
        '*': lambda x,y : x*y,
        '/': lambda x,y : x/y
    }

    def E(self):
        res = self.T()
        curr = self.next()
        while curr in ['+', '-']:
            self.match(curr)
            res = self.operations[curr](res, self.T())
            curr = self.next()
        return res

    def T(self):
        res = self.F()
        curr = self.next()
        while curr in ['*', '/']:
            self.match(curr)
            res = self.operations[curr](res, self.F())
            curr = self.next()
        return res

    def F(self):
        res = 0
        if self.next() == '(':
            self.match('(')
            res += self.E()
            self.match(')')
            return res
        #elif self.next() in ['x', 'y', 'z']:
        #build a list of int chars
        numbers = []
        for i in range(10):
            numbers.append(str(i))
        #if self.next() in ['x', 'y', 'z']:
        if self.next() in numbers:
            tmp = self.next()
            self.match(tmp)
            print(tmp)
            #coverted = int(tmp)
            #return self.values[tmp]
            return int(tmp)
    

    def parse(self, s):
        self.numbers = list(map(str, range(10)))
        print(self.numbers[0].__class__)
        print("parse " + s)
        self.pos = 0
        self.input = s + '#'
        return self.E()
        
    def next(self):
        return self.input[self.pos]

    def match(self, c):
        if self.next() == c:
            self.pos += 1
            print(self.pos)
            print(self.next())
            return True
        else:
            return False

parser = Parser()
while True:
    print(parser.parse(input()))