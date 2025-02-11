# -*- coding: utf-8 -*-
import logging
from logging import StreamHandler
from logging.handlers import RotatingFileHandler
from datetime import datetime
from os import makedirs


class LoggerConfig:

    FMT = logging.Formatter('[%(asctime)s][%(levelname)s] | %(message)s')
    SIZE = 15

    def __init__(self):

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.logger.handlers = [
            self.set_file_handler(), self.set_stream_handler()]

    def set_stream_handler(self):

        stream_handler = StreamHandler()
        stream_handler.setFormatter(self.FMT)
        stream_handler.setLevel(logging.INFO)
        return stream_handler

    def set_file_handler(self, folder="./logs"):

        makedirs(folder, exist_ok=True)
        today = datetime.now().today().strftime('%Y%m%d')
        filename = f"{folder}/log{today}.log"
        file_handler = RotatingFileHandler(filename,
                                           maxBytes=1024*1024*self.SIZE)

        file_handler.setFormatter(self.FMT)
        file_handler.setLevel(logging.DEBUG)
        return file_handler

    def info(self, message):
        self.logger.info(message)

    def critical(self, message):
        self.logger.critical(message)

    def error(self, message):
        self.logger.error(message)

    def debug(self, message):
        self.logger.debug(message)


if __name__ == '__main__':

    # Levels
    # CRITICAL 50
    # ERROR 40
    # WARNING 30
    # INFO 20
    # DEBUG 10
    # NOTSET 0

    instance_log = LoggerConfig()
