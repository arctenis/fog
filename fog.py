import sys


class Fog:
    def __init__(self):
        if len(sys.argv) > 2:
            raise Exception("Usage: pylox [script]")
        elif len(sys.argv) == 2:
            self.__run_file(sys.argv[1])
        else:
            self.__run_prompt()
        self.had_error = False

    def __run_file(self, lox_file):
        with open(lox_file, "r") as f:
            lines = f.readlines()
            for line in lines:
                self.__run(line)

    def __run_prompt(self):
        while True:
            line = input("lox> ")
            if line == None:
                break
            self.__run(line)

    def __run(self, line):
        tokens = self.scan_tokens(line)
        for token in tokens:
            print(token)
        if self.had_error:
            sys.exit()
        self.had_error = False

    def scan_tokens(self, line):
        return line.split(" ")

    @classmethod
    def error(cls, line_nb, msg):
        cls.__report(line_nb, "", msg="")

    def __report(self, line_nb, where, msg):
        raise Exception(f"Line {line_nb} Error {where}: {msg}")


fog = Fog()
