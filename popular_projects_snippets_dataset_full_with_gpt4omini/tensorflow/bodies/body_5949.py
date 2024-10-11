# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/combinations_test.py
original_argv = list(sys.argv)
sys.argv.clear()
importlib.reload(combinations)
sys.argv = original_argv
