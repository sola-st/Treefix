class MockTest(object): # pragma: no cover
    def cached_session(self): # pragma: no cover
        return tf.compat.v1.Session().__enter__() # pragma: no cover
 # pragma: no cover
    def assertAllClose(self, a, b): # pragma: no cover
        tf.debugging.assert_near(a, b) # pragma: no cover
 # pragma: no cover
    def assertRaisesOpError(self, expected_message): # pragma: no cover
        class ContextManager: # pragma: no cover
            def __enter__(self): # pragma: no cover
                return self # pragma: no cover
 # pragma: no cover
            def __exit__(self, exc_type, exc_value, traceback): # pragma: no cover
                if exc_type is tf.errors.InvalidArgumentError and expected_message in str(exc_value): # pragma: no cover
                    return True # pragma: no cover
                raise exc_value # pragma: no cover
        return ContextManager() # pragma: no cover
 # pragma: no cover
self = MockTest() # pragma: no cover
good_pairs = [('1.0', 1.0), ('2.5', 2.5), ('-3', -3.0)] # pragma: no cover
bad_pairs = [('abc', 'could not convert string to float: abc'), ('xyz', 'could not convert string to float: xyz')] # pragma: no cover

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
