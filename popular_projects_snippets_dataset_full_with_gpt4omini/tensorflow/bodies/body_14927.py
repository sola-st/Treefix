# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/raw_ops_test.py
data = ["aa", "bb", "cc", "dd", "ee", "ff"]
with self.assertRaisesRegex(
    errors.InvalidArgumentError,
    r"Invalid split value|First split value must be 0"):
    self.evaluate(
        gen_string_ops.string_n_grams(
            data=data,
            data_splits=splits,
            separator="",
            ngram_widths=[2],
            left_pad="",
            right_pad="",
            pad_width=0,
            preserve_short_sequences=False))
