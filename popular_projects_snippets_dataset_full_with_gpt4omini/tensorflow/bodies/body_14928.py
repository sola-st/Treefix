# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/raw_ops_test.py
data = ["123456"]
data_splits = [0, 1]
separator = "a" * 15
ngram_widths = []
pad_width = -5
left_pad = right_pad = ""
with self.assertRaisesRegex(errors.InvalidArgumentError,
                            "Pad width should be >= 0"):
    self.evaluate(gen_string_ops.string_n_grams(
        data=data,
        data_splits=data_splits,
        separator=separator,
        ngram_widths=ngram_widths,
        left_pad=left_pad,
        right_pad=right_pad,
        pad_width=pad_width,
        preserve_short_sequences=True))
with self.assertRaisesRegex(errors.InvalidArgumentError,
                            "Pad width could lead to integer overflow"):
    self.evaluate(
        gen_string_ops.string_n_grams(
            data=["000.0", "000.0"],
            data_splits=[0, 2],
            separator="",
            ngram_widths=[2**30, 2**30],
            left_pad=" ",
            right_pad=" ",
            pad_width=-2**30,
            preserve_short_sequences=False))
