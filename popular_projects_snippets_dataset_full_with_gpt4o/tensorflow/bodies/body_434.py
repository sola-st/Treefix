# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_test.py
_, report, unused_errors, unused_new_text = self._upgrade(
    "import tensorflow as tf\na + \n")
self.assertNotEqual(report.find("Failed to parse"), -1)
