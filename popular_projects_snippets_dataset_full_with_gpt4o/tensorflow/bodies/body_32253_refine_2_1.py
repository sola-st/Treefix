good_pairs = [('3.14', 3.14), ('-42', -42.0)] # pragma: no cover
bad_pairs = [('abc', 'InvalidArgumentError')] # pragma: no cover

class MockSessionManager: # pragma: no cover
    def cached_session(self): # pragma: no cover
        return tf.compat.v1.Session().__enter__ # pragma: no cover
 # pragma: no cover
    def assertAllClose(self, a, b): # pragma: no cover
        tf.debugging.assert_near(a, b) # pragma: no cover
 # pragma: no cover
    def assertRaisesOpError(self, expected_message): # pragma: no cover
        @contextmanager # pragma: no cover
        def raiser(): # pragma: no cover
            try: # pragma: no cover
                yield # pragma: no cover
            except tf.errors.InvalidArgumentError as e: # pragma: no cover
                assert expected_message in str(e), f"Expected '{expected_message}', but got '{str(e)}'" # pragma: no cover
            else: # pragma: no cover
                raise AssertionError(f"Expected tf.errors.InvalidArgumentError with message '{expected_message}'") # pragma: no cover
        return raiser() # pragma: no cover
 # pragma: no cover
self = MockSessionManager() # pragma: no cover
good_pairs = [('3.14', 3.14), ('-42', -42.0)] # pragma: no cover
bad_pairs = [('abc', 'invalid literal for float()'), ('nan', 'invalid literal for float()')] # pragma: no cover

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
