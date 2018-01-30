import logging


def initialize_logger(filename):
    # set custom class
    logging.setLoggerClass(CustomLogger)
    # get root logger
    logger = logging.getLogger()
    # set default logging level
    logger.setLevel(logging.DEBUG)
    # create console handler
    handler = logging.StreamHandler()
    formatter = CustomFormatter("%(message)s")
    handler.setFormatter(formatter)
    # logging level set to INFO (do not display DEBUG level logging)
    handler.setLevel(logging.INFO)
    logger.addHandler(handler)
    # create file handler
    handler = logging.FileHandler(filename, "w")
    formatter = CustomFormatter("%(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    # propagate
    logger.propagate = True

class CustomLogger(logging.Logger):
    
    def task(self, msg, *args, **kwargs):
        temp = '*' * (90 - len(msg) - 9)
        msg_current = msg
        msg = "TASK: [%s] %s\n" % (msg_current, temp)
        super(CustomLogger, self).info(msg, *args, **kwargs)
        msg = msg_current

class CustomFormatter(logging.Formatter):
    """
    Custom formatter for different logging levels
    """

    def format(self, record):
        if record.levelno == logging.INFO or record.levelno == logging.DEBUG:
            self._fmt = "%(message)s"
            self.datefmt = ""
        else:
            self._fmt = "[%(asctime)s] %(levelname)s - %(message)s"
            self.datefmt = '%m/%d/%Y %I:%M:%S %p'

        return super(CustomFormatter, self).format(record)