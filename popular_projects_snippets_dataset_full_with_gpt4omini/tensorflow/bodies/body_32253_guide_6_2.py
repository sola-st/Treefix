class Mock:  # Mock class to simulate test environment # pragma: no cover
    def cached_session(self): # pragma: no cover
        return tf.compat.v1.Session() # pragma: no cover
    def assertAllClose(self, x, y): # pragma: no cover
        assert x == y, f'Expected {x} to be close to {y}' # pragma: no cover
    def assertRaisesOpError(self, func): # pragma: no cover
        try: # pragma: no cover
            func() # pragma: no cover
        except tf.errors.InvalidArgumentError as e: # pragma: no cover
            return # pragma: no cover
        raise AssertionError('Expected an error but none occurred.') # pragma: no cover
self = Mock() # pragma: no cover
good_pairs = [('1.0', 1.0), ('-2.5', -2.5)] # pragma: no cover
bad_pairs = [('not_a_number', 'could not convert string to float: not_a_number')] # pragma: no cover

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
