# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/inspect_utils_test.py
foo = object()
qux = imp.new_module('quxmodule')
bar = imp.new_module('barmodule')
baz = object()
bar.baz = baz

ns = {
    'foo': foo,
    'bar': bar,
    'qux': qux,
}

self.assertIsNone(inspect_utils.getqualifiedname(ns, inspect_utils))
self.assertEqual(inspect_utils.getqualifiedname(ns, foo), 'foo')
self.assertEqual(inspect_utils.getqualifiedname(ns, bar), 'bar')
self.assertEqual(inspect_utils.getqualifiedname(ns, baz), 'bar.baz')
