from token_type import T
from token import Token
from fog import Fog
from fog import Fog


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
            case "!":
                self.add_token(T.BANG_EQUAL if self.match("=") else T.BANG)
            case "=":
                self.add_token(T.EQUAL_EQUAL if self.match("=") else T.EQUAL)
            case "<":
                self.add_token(T.LESS_EQUAL if self.match("=") else T.LESS)
            case ">":
                self.add_token(T.GREATER_EQUAL if self.match("=") else T.GREATER)
            case "/":
                if self.match("/"):
                    while self.peek() != "\n" and not self.at_end():
                        self.advance()
                else:
                    self.add_token(T.SLASH)
            case " " | "\r" | "\t":
                pass
            case "\n":
                self.line += 1
            case '"':
                self.string()
            case _:
                if c.isnumeric():
                    self.number()
                elif is_alpha(c):
                    self.identifier()
                else:
                    Fog.error(self.line, "Unexpected character.")

    def add_token(self, token_type, literal=None):
        text = self.source[self.start : self.current]
        self.tokens.append(Token(token_type, text, literal, self.line))

    def match(self, expected):
        if self.at_end():
            return False
        if self.source[self.current] != expected:
            return False
        self.current += 1
        return True

    def peek(self):
        if self.at_end():
            return "\0"
        return self.source[self.current]

    def at_end(self):
        return self.current >= len(self.source)

    def advance(self):
        return self.source[self.current + 1]

    def string(self):
        while self.peek() != '"' and not self.at_end():
            if self.peek() == "\n":
                self.line += 1
            self.advance()

        if self.at_end():
            Fog.error(self.line, "Unterminated string.")
            return None
        self.advance()
        value = self.source[self.start + 1 : self.current - 1]
        self.add_token(T.STRING, value)

    def number(self):
        while self.peek().isdigit():
            self.advance()

        if self.peek() == "." and self.peek_next().isdigit():
            self.advance()
            while self.peek().isdigit():
                self.advance()
        self.add_token(T.NUMBER, float(self.source[self.start : self.current]))

    def peek_next(self):
        if self.current + 1 >= len(self.source):
            return "\0"
        return self.source[self.current + 1]

    def is_alpha(self, c):
        return (c >= "a" and c <= "z") or (c >= "A" and c <= "Z") or c == "_"

    def identifier(self):
        while self.peek().isalnum():
            self.advance()
        self.add_token(T.IDENTIFIER)

    """
    TODO
    Remplacer isdigit() par une fonction maison is_digit()
    Remplacer isalnum() par une fonction maison is_alphanumeric()
    """
