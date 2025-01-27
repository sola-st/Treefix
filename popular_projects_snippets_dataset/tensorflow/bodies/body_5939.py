# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/combinations_test.py
# There's no perfect way to check if the test runs in a subprocess. We
# approximate by checking the presence of TF_CONFIG, which is normally not
# set to the main process.
self.assertNotEqual(os.getenv("TF_CONFIG"), "")
