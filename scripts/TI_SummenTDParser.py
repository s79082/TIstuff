# S -> S + S | x | y | z hat linksrekursion
# deshalb:
# S -> xS' | yS' | zS' 
# S' -> +S | epsilon

class Parser:
    def S(self):
        current = self.next()
        print("S       : pos: " + str(self.pos) + " current: " + current)


        if current in ['x', 'y', 'z']:
            return self.match(current) and self.S_strich()
        else:
            return False

    
    def S_strich(self):
        print("S_strich: pos: " + str(self.pos) + " current: " + self.next())   


        if self.next() == '+':
            return self.match('+') and self.S()

        elif self.next() == '#':        # epsilon
            return self.match('#')
        else:                           # etwas anderes
            return False
        
    def parse(self, s):
        self.pos = 0
        self.input = s + '#'
        return self.S()
        
    def next(self):
        return self.input[self.pos]

    def match(self, c):
        if self.next() == c:
            self.pos += 1
            return True
        else:
            return False

parser = Parser()
print(parser.parse("x+y+z"))