self = type('MockSelf', (), {'assertProtoEquals': lambda self, expected, actual: None, 'assertRaises': lambda self, exc: type('MockContextManager', (), {'__enter__': lambda s: None, '__exit__': lambda s, exc_type, exc_value, traceback: None })(), 'assertEqual': lambda self, a, b: None})() # pragma: no cover

class MockSelf: # pragma: no cover
    def assertProtoEquals(self, expected, actual): # pragma: no cover
        assert expected.strip() == actual['name'] + ' ' + actual['op'] # pragma: no cover
    def assertRaises(self, exception_type): # pragma: no cover
        @contextlib.contextmanager # pragma: no cover
        def manager(): # pragma: no cover
            try: # pragma: no cover
                yield # pragma: no cover
            except Exception as e: # pragma: no cover
                if not isinstance(e, exception_type): # pragma: no cover
                    raise # pragma: no cover
        return manager() # pragma: no cover
    def assertEqual(self, first, second): # pragma: no cover
        assert first == second # pragma: no cover
self = MockSelf() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library_test.py
from l3.Runtime import _l_
with ops.Graph().as_default():
    _l_(8558)

    op = op_def_library.apply_op(
        "AttrBoolList", a=[True, False, True], name="t")
    _l_(8551)
    self.assertProtoEquals("""
        name: 't' op: 'AttrBoolList'
        attr { key: 'a' value { list { b: true b: false b:true } } }
        """, op.node_def)
    _l_(8552)

    op = op_def_library.apply_op("AttrBoolList", a=[], name="u")
    _l_(8553)
    self.assertProtoEquals("""
        name: 'u' op: 'AttrBoolList' attr { key: 'a' value { list { } } }
        """, op.node_def)
    _l_(8554)

    with self.assertRaises(TypeError) as cm:
        _l_(8556)

        op_def_library.apply_op("AttrBoolList", a=[0])
        _l_(8555)
    self.assertEqual(str(cm.exception),
                     "Expected bool for argument 'a' not 0.")
    _l_(8557)
