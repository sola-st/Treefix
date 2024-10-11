# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/decode_csv_op_test.py
if expected_err_re is None:
    decode = parsing_ops.decode_csv(**args)
    out = self.evaluate(decode)

    for i, field in enumerate(out):
        if field.dtype == np.float32 or field.dtype == np.float64:
            self.assertAllClose(field, expected_out[i])
        else:
            self.assertAllEqual(field, expected_out[i])
else:
    with self.assertRaisesWithPredicateMatch(Exception, expected_err_re):
        decode = parsing_ops.decode_csv(**args)
        self.evaluate(decode)
