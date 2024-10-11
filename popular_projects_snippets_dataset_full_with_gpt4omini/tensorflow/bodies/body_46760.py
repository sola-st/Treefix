# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/qual_names_test.py
samples = """
      a
      a.b
      (c, d.e)
      [f, (g.h.i)]
      j(k, l)
    """
nodes = parser.parse(textwrap.dedent(samples), single_node=False)
nodes = tuple(resolve(node).value for node in nodes)

self.assertQNStringIs(nodes[0], 'a')
self.assertQNStringIs(nodes[1], 'a.b')
self.assertQNStringIs(nodes[2].elts[0], 'c')
self.assertQNStringIs(nodes[2].elts[1], 'd.e')
self.assertQNStringIs(nodes[3].elts[0], 'f')
self.assertQNStringIs(nodes[3].elts[1], 'g.h.i')
self.assertQNStringIs(nodes[4].func, 'j')
self.assertQNStringIs(nodes[4].args[0], 'k')
self.assertQNStringIs(nodes[4].args[1], 'l')
