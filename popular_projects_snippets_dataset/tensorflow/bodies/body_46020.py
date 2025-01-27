# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/parser_test.py

code = r"""
    def f():
      a = \
          1
      return a
    """

f = self._eval_code(parser.dedent_block(code), 'f')
self.assertEqual(f(), 1)
