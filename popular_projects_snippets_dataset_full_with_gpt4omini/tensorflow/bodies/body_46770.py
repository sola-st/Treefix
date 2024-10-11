# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/pretty_printer_test.py
source = textwrap.dedent('''
    def f():
      return b'b', u'u', 'depends_py2_py3'
    ''')
node = ast.parse(source)
self.assertIsNotNone(pretty_printer.fmt(node))
