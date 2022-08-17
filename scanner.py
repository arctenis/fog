from token_type import T
from token import Token

class Scanner:
    def __init__(self, source):
        self.source = source
        self.tokens = []
        self.start = 0
        self.current = 0
        self.line = 1

    def scan_tokens(self):
        while not self.at_end():
            self.start = self.current
            self.scan_token()

        self.tokens.append(Token("EOF", "", None, self.line))

    def scan_token(self):
        c = self.advance()
        match c:
            case "(": 
                self.add_token(T.LEFT_PAREN)
            case ")": 
                self.add_token(T.RIGHT_PAREN)
            case "{": 
                self.add_token(T.LEFT_BRACE)
            case "}": 
                self.add_token(T.RIGHT_BRACE)
            case ",": 
                self.add_token(T.COMMA)
            case ".": 
                self.add_token(T.DOT)
            case "-": 
                self.add_token(T.MINUS)
            case "+": 
                self.add_token(T.PLUS)
            case ";": 
                self.add_token(T.SEMICOLON)
            case "*": 
                self.add_token(T.STAR)

    def at_end(self):
        return self.current >= len(self.source)

    def advance(self):
        return self.source[self.current+1]

    def add_token(self, token_type, literal=None):
        text = self.source[self.start:self.current]
        self.tokens.append(Token(token_type, text, literal, self.line))
