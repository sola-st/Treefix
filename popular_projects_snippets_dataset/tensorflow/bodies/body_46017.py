# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/parser_test.py

code = """
  ###
    def f(x):
###
      if x > 0:
  ###
        return -x
          ###
  ###
      return x
      ###
    """

f = self._eval_code(parser.dedent_block(code), 'f')
self.assertEqual(f(1), -1)
self.assertEqual(f(-1), -1)
