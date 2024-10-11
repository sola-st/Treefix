# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_test.py
text = "(foo + bar)[a].word()"
_ = self._upgrade(text)
