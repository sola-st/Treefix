# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/parser_test.py

code = """
    def f():
      '''
      Docstring.
      '''
      return '''
  1
    2
      3'''
    """

f = self._eval_code(parser.dedent_block(code), 'f')
self.assertEqual(f.__doc__, '\n      Docstring.\n      ')
self.assertEqual(f(), '\n  1\n    2\n      3')
