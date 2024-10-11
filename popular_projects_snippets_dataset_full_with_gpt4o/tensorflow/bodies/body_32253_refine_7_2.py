self = type('Mock', (object,), {'cached_session': lambda self: contextlib.nullcontext(), 'assertAllClose': staticmethod(lambda a, b: None), 'assertRaisesOpError': staticmethod(lambda x: contextlib.nullcontext())})() # pragma: no cover
good_pairs = [('3.14', 3.14), ('0', 0.0), ('-7', -7.0)] # pragma: no cover
bad_pairs = [('abc', 'Cannot convert'), ('123abc', 'Invalid argument')] # pragma: no cover

import contextlib # pragma: no cover

self = type('Mock', (object,), {'cached_session': lambda self: contextlib.nullcontext(), 'assertAllClose': staticmethod(lambda a, b: None), 'assertRaisesOpError': staticmethod(lambda x: contextlib.nullcontext())})() # pragma: no cover
good_pairs = [('3.14', 3.14), ('0', 0.0), ('-7', -7.0)] # pragma: no cover
bad_pairs = [('abc', 'Invalid argument'), ('123abc', 'Invalid argument')] # pragma: no cover

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
