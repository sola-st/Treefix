# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/googletest.py
try:
    file_io.delete_recursively(dirname)
except errors.OpError as e:
    logging.error('Error removing %s: %s', dirname, e)
