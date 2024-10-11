good_pairs = [('1.0', 1.0), ('2.5', 2.5), ('-3.0', -3.0)] # pragma: no cover
bad_pairs = [('abc', 'invalid value'), ('1.a', 'invalid value')] # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.cached_session = lambda: tf.compat.v1.Session() # pragma: no cover
self.assertRaisesOpError = lambda err_msg: tf.test.TestCase().assertRaises # pragma: no cover
good_pairs = [('1.0', 1.0), ('2.5', 2.5), ('-3.0', -3.0)] # pragma: no cover
bad_pairs = [('abc', 'invalid value'), ('1.a', 'invalid value')] # pragma: no cover

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
