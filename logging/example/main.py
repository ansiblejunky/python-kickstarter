import logging
import xlogging
import auxiliary_module

def main():
    xlogging.initialize_logger("main")
    # get module level logger (inherits from root logger)
    logger = logging.getLogger(__name__)

    try:
        logger.info("test info")
        logger.error("test error")
        logger.debug("test debug")
        logger.fatal("test fatal")
        logger.warning("test warning")

        while True:
            question = "Username: "
            username = raw_input(question)
            logger.debug(question + username)
            if username == "test":
                break

        logger.task('creating an instance of auxiliary_module.Auxiliary')
        a = auxiliary_module.Auxiliary()
        logger.info('created an instance of auxiliary_module.Auxiliary')
        logger.info('calling auxiliary_module.Auxiliary.do_something')
        a.do_something()
        logger.info('finished auxiliary_module.Auxiliary.do_something')
        logger.info('calling auxiliary_module.some_function()')
        auxiliary_module.some_function()
        logger.info('done with auxiliary_module.some_function()')
    except (SystemExit, KeyboardInterrupt):
        raise
    except Exception, e:
        # exc_info parameter outputs extra stack trace information
        logger.error('Something failed', exc_info=True)

if __name__ == "__main__":
    main()
