# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/summary_test.py
with self.cached_session():
    with self.assertRaises(ValueError):
        num = array_ops.constant(1)
        summary_lib.text('foo', num)

    # The API accepts vectors.
    arr = array_ops.constant(['one', 'two', 'three'])
    summ = summary_lib.text('foo', arr)
    self.assertEqual(summ.op.type, 'TensorSummaryV2')

    # the API accepts scalars
    summ = summary_lib.text('foo', array_ops.constant('one'))
    self.assertEqual(summ.op.type, 'TensorSummaryV2')
