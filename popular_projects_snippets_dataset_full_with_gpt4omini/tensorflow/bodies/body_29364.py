# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/options_test.py
with self.assertRaisesRegex(ValueError,
                            "At least one options should be provided"):
    options.merge_options()
