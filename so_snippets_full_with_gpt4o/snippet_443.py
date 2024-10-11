# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/14058453/making-python-loggers-output-all-messages-to-stdout-in-addition-to-log-file
from l3.Runtime import _l_
try:
    import logging
    _l_(12598)

except ImportError:
    pass

logging.basicConfig(filename="logfile.txt")
_l_(12599)
stderrLogger=logging.StreamHandler()
_l_(12600)
stderrLogger.setFormatter(logging.Formatter(logging.BASIC_FORMAT))
_l_(12601)
logging.getLogger().addHandler(stderrLogger)
_l_(12602)

