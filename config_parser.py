import configparser
import os
import errno


class ConfigParser():

    def __init__(self, path="./discord.env"):
        if not os.path.exists(path):
            raise FileNotFoundError(errno.ENOENT, os.strerror(
                errno.ENOENT), path)
        self.path = path
        self.parser = configparser.ConfigParser()

    def load(self):
        self.parser.read(self.path, encoding='utf-8')
        return self.parser


if __name__ == "__main__":
    parser = ConfigParser()
    config = parser.load()
