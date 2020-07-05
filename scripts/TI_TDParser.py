class Parser:
    # this represents the rule
    # S -> aSa | bSb | cSc | x
    def S(self):

        current = self.next()
        if current in ['a', 'b', 'c']:
            return self.match(current) and self.S() and self.match(current)
        else:
            # its an x 
            return self.match(current)

    def parse(self, s):
        self.pos = 0
        self.input = s + '#'
        return self.S() and self.match('#')
        
    def next(self):
        return self.input[self.pos]

    def match(self, c):
        if self.next() == c:
            self.pos += 1
            return True
        else:
            return False

    def __init__(self):
        pass


parser = Parser()
print(parser.parse("abcbxbcba"))

