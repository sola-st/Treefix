# Extracted from https://stackoverflow.com/questions/13733552/logger-configuration-to-log-to-file-and-print-to-stdout
import logging
logging.getLogger().addHandler(logging.StreamHandler())

import sys
# ...
logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))

import logging
logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
rootLogger = logging.getLogger()

fileHandler = logging.FileHandler("{0}/{1}.log".format(logPath, fileName))
fileHandler.setFormatter(logFormatter)
rootLogger.addHandler(fileHandler)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
rootLogger.addHandler(consoleHandler)

2012-12-05 16:58:26,618 [MainThread  ] [INFO ]  my message

