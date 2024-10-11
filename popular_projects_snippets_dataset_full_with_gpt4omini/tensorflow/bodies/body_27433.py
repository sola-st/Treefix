# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/make_csv_dataset_test.py
"""Tests making a CSV dataset with an encoding except for utf-8."""
record_defaults = [
    constant_op.constant([], dtypes.string),
    constant_op.constant([], dtypes.string)
]

column_names = ["col%d" % i for i in range(2)]
inputs = [[",".join(x for x in column_names), "さる,猿", "とり,鳥"],
          [",".join(x for x in column_names), "いぬ,犬", "ねこ,猫"]]
expected_output = [["さる".encode("shift-jis"), "猿".encode("shift-jis")],
                   ["とり".encode("shift-jis"), "鳥".encode("shift-jis")],
                   ["いぬ".encode("shift-jis"), "犬".encode("shift-jis")],
                   ["ねこ".encode("shift-jis"), "猫".encode("shift-jis")]]
label = "col0"

self._test_dataset(
    inputs,
    expected_output=expected_output,
    expected_keys=column_names,
    column_names=column_names,
    label_name=label,
    batch_size=1,
    num_epochs=1,
    shuffle=False,
    header=True,
    column_defaults=record_defaults,
    encoding="shift-jis",
)
