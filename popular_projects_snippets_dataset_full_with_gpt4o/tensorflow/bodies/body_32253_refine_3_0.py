class MockTest(object): # pragma: no cover
    def cached_session(self): # pragma: no cover
        return tf.compat.v1.Session() # pragma: no cover
 # pragma: no cover
    def assertAllClose(self, a, b): # pragma: no cover
        return tf.test.TestCase().assertAllClose(a, b) # pragma: no cover
 # pragma: no cover
    def assertRaisesOpError(self, msg): # pragma: no cover
        class OpErrorContextManager: # pragma: no cover
            def __enter__(self_c): # pragma: no cover
                pass # pragma: no cover
 # pragma: no cover
            def __exit__(self_c, exc_type, exc_val, exc_tb): # pragma: no cover
                if exc_type is not None and msg in str(exc_val): # pragma: no cover
                    return True  # Suppress the exception # pragma: no cover
                return False  # Do not suppress other exceptions # pragma: no cover
        return OpErrorContextManager() # pragma: no cover
 # pragma: no cover
self = MockTest() # pragma: no cover
good_pairs = [('3.14', 3.14), ('-42', -42.0)] # pragma: no cover
bad_pairs = [('abc', 'invalid literal for float()')] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/string_to_number_op_test.py
from l3.Runtime import _l_
with self.cached_session():
    _l_(21711)

    # Build a small testing graph.
    input_string = array_ops.placeholder(dtypes.string)
    _l_(21703)
    output = parsing_ops.string_to_number(
        input_string, out_type=tf_type)
    _l_(21704)

    # Check all the good input/output pairs.
    for instr, outnum in good_pairs:
        _l_(21707)

        result, = output.eval(feed_dict={input_string: [instr]})
        _l_(21705)
        self.assertAllClose([outnum], [result])
        _l_(21706)

    # Check that the bad inputs produce the right errors.
    for instr, outstr in bad_pairs:
        _l_(21710)

        with self.assertRaisesOpError(outstr):
            _l_(21709)

            output.eval(feed_dict={input_string: [instr]})
            _l_(21708)
