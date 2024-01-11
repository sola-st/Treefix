import logging


logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')

logger = logging.getLogger("L3 logger")
logger.setLevel(logging.INFO)

logger.info("Logging starts")