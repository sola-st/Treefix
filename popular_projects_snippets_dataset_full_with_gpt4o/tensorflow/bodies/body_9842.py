# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli_test.py
super(SavedModelCLITestCase, self).setUp()
if platform.system() == 'Windows':
    self.skipTest('Skipping failing tests on Windows.')
