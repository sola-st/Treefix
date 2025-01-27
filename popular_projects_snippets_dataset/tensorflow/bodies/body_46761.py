# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/qual_names_test.py
samples = """
      x[i]
      x[i.b]
      a.b[c]
      a.b[x.y]
      a[z[c]]
      a[b[c[d]]]
      a[b].c
      a.b.c[d].e.f
      a.b[c[d]].e.f
      a.b[c[d.e.f].g].h
    """
nodes = parser.parse(textwrap.dedent(samples), single_node=False)
nodes = tuple(resolve(node).value for node in nodes)

self.assertQNStringIs(nodes[0], 'x[i]')
self.assertQNStringIs(nodes[1], 'x[i.b]')
self.assertQNStringIs(nodes[2], 'a.b[c]')
self.assertQNStringIs(nodes[3], 'a.b[x.y]')
self.assertQNStringIs(nodes[4], 'a[z[c]]')
self.assertQNStringIs(nodes[5], 'a[b[c[d]]]')
self.assertQNStringIs(nodes[6], 'a[b].c')
self.assertQNStringIs(nodes[7], 'a.b.c[d].e.f')
self.assertQNStringIs(nodes[8], 'a.b[c[d]].e.f')
self.assertQNStringIs(nodes[9], 'a.b[c[d.e.f].g].h')
