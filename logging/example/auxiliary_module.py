import logging

class Auxiliary:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.info('creating an instance of Auxiliary')

    def do_something(self):
        self.logger.info('doing something')
        a = 1 + 1
        self.logger.info('done doing something')

def some_function():
    logger = logging.getLogger(__name__)
    print "auxiliary __name__="+ __name__
    print "auxiliary logger __class__=" + logger.__class__.__name__

    logger.debug("debug - output should only go to the filehandler")
    logger.info('received a call to "some_function"')