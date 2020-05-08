from core.common import logger
from useme import examples
from core.common import application_post_end
from core.common import application_pre_start


def main():

    logger.log_message("initializing application")
    application_pre_start.initialize()

    logger.log_message("generating html")
    examples.digraph_example()
    examples.table_example()

    logger.log_message("shutting down application")
    application_post_end.finalize()


if __name__ == '__main__':
    main()
