class Mock: pass# pragma: no cover
self = Mock() # pragma: no cover
array_ops = Mock()# pragma: no cover
array_ops.placeholder = staticmethod(lambda dtype: 'mock_placeholder') # pragma: no cover
dtypes = Mock()# pragma: no cover
dtypes.string = 'string' # pragma: no cover
parsing_ops = Mock()# pragma: no cover
parsing_ops.string_to_number = staticmethod(lambda input_string, out_type: 'mock_output') # pragma: no cover
tf_type = dtypes.string # pragma: no cover
good_pairs = [('1', 1), ('2.5', 2.5)] # pragma: no cover
bad_pairs = [('abc', 'Invalid input: not a number'), ('1.2e3', 'Invalid input: not a number')] # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.cached_session = lambda: self # pragma: no cover
self.__enter__ = lambda: None # pragma: no cover
self.__exit__ = lambda exc_type, exc_value, traceback: None # pragma: no cover
array_ops = Mock() # pragma: no cover
array_ops.placeholder = staticmethod(lambda dtype: 'mock_placeholder') # pragma: no cover
dtypes = Mock() # pragma: no cover
dtypes.string = 'string' # pragma: no cover
parsing_ops = Mock() # pragma: no cover
parsing_ops.string_to_number = staticmethod(lambda input_string, out_type: tf.constant(42, dtype=out_type)) # pragma: no cover
good_pairs = [('1', 1), ('2.5', 2.5)] # pragma: no cover
bad_pairs = [('abc', 'ValueError: could not convert string to float: abc'), ('1.2e3', 'ValueError: could not convert string to float: 1.2e3')] # pragma: no cover
self.assertAllClose = lambda a, b: None # pragma: no cover
self.assertRaisesOpError = lambda message: None # pragma: no cover

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
