# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/utils/ag_logging.py
print(msg % args)
if kwargs.get('exc_info', False):
    traceback.print_exc()
