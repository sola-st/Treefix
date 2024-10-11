# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
for contrib_alias in ["tf.contrib.", "contrib_"]:
    api_symbols = [
        "make_early_stopping_hook", "stop_if_higher_hook",
        "stop_if_lower_hook",
        "stop_if_no_decrease_hook", "stop_if_no_increase_hook"
    ]
    for symbol in api_symbols:
        text = contrib_alias + "estimator." + symbol
        expected_text = "tf.estimator.experimental." + symbol
        _, _, _, new_text = self._upgrade(text)
        self.assertEqual(expected_text, new_text)
