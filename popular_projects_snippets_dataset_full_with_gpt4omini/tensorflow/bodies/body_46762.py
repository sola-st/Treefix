# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/qual_names_test.py
samples = """
      a.b
      a.b()
      a().b
      z[i]
      z[i]()
      z()[i]
    """
nodes = parser.parse(textwrap.dedent(samples), single_node=False)
nodes = tuple(resolve(node).value for node in nodes)
self.assertQNStringIs(nodes[0], 'a.b')
self.assertQNStringIs(nodes[1].func, 'a.b')
self.assertQNStringIs(nodes[2].value.func, 'a')
self.assertQNStringIs(nodes[3], 'z[i]')
self.assertQNStringIs(nodes[4].func, 'z[i]')
self.assertQNStringIs(nodes[5].value.func, 'z')
