# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = "self.est.export_savedmodel(path)"
_, report, unused_errors, unused_new_text = self._upgrade(text)
self.assertIn(
    "rename the method export_savedmodel() to export_saved_model()",
    report)
