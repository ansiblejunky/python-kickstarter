'''
Customized logging functionality

CRITICAL    (50)    Calls critical() function and sys.exit(1)
ERROR       (40)    Prints error message using date/time
WARNING     (30)    Prints warning message using date/time
INFO        (20)    Prints info message (no date/time, just plain message)
TASK        (15)    CUSTOM LABEL - Prints a task header message (using asterisks)
DEBUG       (10)    Prints debug message (using date/time)
FILE        (5)     CUSTOM LABEL - Prints only to file handler (using date/time)
'''
import logging
import sys

class LOG_LEVEL_TASK():
    level = 15
    label = "TASK"

class LOG_LEVEL_FILE():
    level = 5
    label = "FILE"

def initialize_logger(application_name):
    '''
    Initialize custom logging levels, handlers, and so on. Call this method
    from your application's main start point.
        filename = the name for the log file
    '''
    # check if already initialized with custom class
    if logging.getLoggerClass() == CustomLogger:
       return
    # set custom class
    logging.setLoggerClass(CustomLogger)
    # set custom labels
    logging.addLevelName(LOG_LEVEL_TASK.level, LOG_LEVEL_TASK.label)
    logging.addLevelName(LOG_LEVEL_FILE.level, LOG_LEVEL_FILE.label)
    # enable raising exceptions
    logging.raiseExceptions = True
    # get root logger
    logger = logging.getLogger(application_name)
    # propagate
    logger.propagate = False
    # set default logging level
    logger.setLevel(LOG_LEVEL_FILE.level)

    # create console handler
    handler = logging.StreamHandler()
    formatter = CustomFormatter("%(message)s")
    handler.setFormatter(formatter)
    # logging level set to INFO (do not display DEBUG level logging)
    handler.setLevel(logging.DEBUG)
    logger.addHandler(handler)

    # create file handler
    handler = logging.FileHandler(application_name + ".log", "w")
    formatter = CustomFormatter("%(message)s")
    handler.setFormatter(formatter)
    handler.setLevel(LOG_LEVEL_FILE.level)
    logger.addHandler(handler)


class CustomLogger(logging.Logger, object):
    """
    Customized Logger class

    Python 2.6 workaround - logging.Formatter class does not use new-style class
        and causes 'TypeError: super() argument 1 must be type, not classobj' so
        we use multiple inheritance to get around the problem.
    """
    def task(self, msg, *args, **kwargs):
        super(CustomLogger, self).log(LOG_LEVEL_TASK.level, msg, *args, **kwargs)

    def file(self, msg, *args, **kwargs):
        super(CustomLogger, self).log(LOG_LEVEL_FILE.level, msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        super(CustomLogger, self).critical(msg, *args, **kwargs)
        sys.exit(1)

    def debug(self, msg, *args, **kwargs):
        super(CustomLogger, self).debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        super(CustomLogger, self).info(msg, *args, **kwargs)

class CustomFormatter(logging.Formatter, object):
    """
    Custom formatter to handle different logging formats based on logging level

    Python 2.6 workaround - logging.Formatter class does not use new-style class
        and causes 'TypeError: super() argument 1 must be type, not classobj' so
        we use multiple inheritance to get around the problem.
    """
    def format(self, record):
        if record.levelno == LOG_LEVEL_TASK.level:
            temp = '*' * (90 - len(record.msg) - 25)
            self._fmt = "\n\n[%(asctime)s] %(levelname)s - [%(message)s] " + temp + "\n\n"
            self.datefmt = "%m/%d/%Y %H:%M:%S"
        elif record.levelno in [logging.INFO, LOG_LEVEL_FILE.level]:
            self._fmt = "%(message)s"
            self.datefmt = ""
        elif record.levelno in [logging.WARNING]:
            self._fmt = "%(levelname)s - %(message)s"
            self.datefmt = ""
        else:
            self._fmt = "[%(asctime)s] %(levelname)s - %(message)s"
            self.datefmt = "%m/%d/%Y %H:%M:%S"

        return super(CustomFormatter, self).format(record)