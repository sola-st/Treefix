# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/gamma_test.py
module = None
try:
    module = importlib.import_module(name)
except ImportError as e:
    tf_logging.warning("Could not import %s: %s" % (name, str(e)))
exit(module)
