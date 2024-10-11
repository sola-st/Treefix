# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/config_test.py
os.environ.pop(config._DT_JOBS, [])
super().tearDown()
