# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/unicode_script_op_test.py
inputs = [
    ord("a"),
    0x0411,  # CYRILLIC CAPITAL LETTER BE
    0x82b8,  # CJK UNIFIED IDEOGRAPH-82B8
    ord(",")
]
with self.cached_session():
    input_vector = constant_op.constant(inputs, dtypes.int32)
    outputs = string_ops.unicode_script(input_vector).eval()
    self.assertAllEqual(
        outputs,
        [
            25,  # USCRIPT_LATIN (LATN)
            8,  # USCRIPT_CYRILLIC (CYRL)
            17,  # USCRIPT_HAN (HANI)
            0  # USCRIPT_COMMON (ZYYY)
        ])
