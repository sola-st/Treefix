# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/ast_util_test.py
self.assertMatch('super(Foo, self).__init__(arg1, arg2)',
                 'super(_).__init__(_)')
self.assertMatch('super().__init__()', 'super(_).__init__(_)')
self.assertNoMatch('super(Foo, self).bar(arg1, arg2)',
                   'super(_).__init__(_)')
self.assertMatch('super(Foo, self).__init__()', 'super(Foo, _).__init__(_)')
self.assertNoMatch('super(Foo, self).__init__()',
                   'super(Bar, _).__init__(_)')
