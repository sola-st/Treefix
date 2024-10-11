self = type('Mock', (object,), {'cached_session': lambda: tf.compat.v1.Session(), 'assertAllClose': lambda x, y: tf.test.TestCase().assertAllClose(x, y), 'assertRaisesOpError': lambda *args: tf.test.TestCase().assertRaises(*args)})() # pragma: no cover
good_pairs = [('3.14', 3.14), ('-1.0', -1.0)] # pragma: no cover
bad_pairs = [('abc', 'expected a float, got abc')] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/string_to_number_op_test.py
from l3.Runtime import _l_
with self.cached_session():
    _l_(9329)

    # Build a small testing graph.
    input_string = array_ops.placeholder(dtypes.string)
    _l_(9321)
    output = parsing_ops.string_to_number(
        input_string, out_type=tf_type)
    _l_(9322)

    # Check all the good input/output pairs.
    for instr, outnum in good_pairs:
        _l_(9325)

        result, = output.eval(feed_dict={input_string: [instr]})
        _l_(9323)
        self.assertAllClose([outnum], [result])
        _l_(9324)

    # Check that the bad inputs produce the right errors.
    for instr, outstr in bad_pairs:
        _l_(9328)

        with self.assertRaisesOpError(outstr):
            _l_(9327)

            output.eval(feed_dict={input_string: [instr]})
            _l_(9326)
