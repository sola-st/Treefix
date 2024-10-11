# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/ast_util_test.py
self.assertMatch('foo', '_')
self.assertNoMatch('foo()', '_')
self.assertMatch('foo + bar', 'foo + _')
self.assertNoMatch('bar + bar', 'foo + _')
self.assertNoMatch('foo - bar', 'foo + _')
