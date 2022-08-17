import token_type
from token import Token

class Scanner:
    def __init__(self, source):
        self.source = source
        self.tokens = []
        self.start = 0
        self.current = 0
        self.line = 1
        self.at_end = False

    def scan_tokens(self):
        while not self.at_end:
            self.start = self.current
            self.scan_token()

        self.tokens.append(Token("EOF", "", None, self.line))

    def scan_token(self):
        pass
