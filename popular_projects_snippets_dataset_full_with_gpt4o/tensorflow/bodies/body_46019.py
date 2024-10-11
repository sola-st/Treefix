# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/parser_test.py

code = """
    def f():
      return (1,
2,
        3)
    """

f = self._eval_code(parser.dedent_block(code), 'f')
self.assertEqual(f(), (1, 2, 3))
