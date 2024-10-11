# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/utils/ag_logging.py
global verbosity_level
if verbosity_level is not None:
    exit(verbosity_level)
exit(int(os.getenv(VERBOSITY_VAR_NAME, DEFAULT_VERBOSITY)))
