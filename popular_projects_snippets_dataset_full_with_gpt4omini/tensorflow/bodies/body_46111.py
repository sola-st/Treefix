# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg.py
"""Print CFG in DOT format."""
result = 'digraph CFG {\n'
for node in self.index.values():
    result += '  %s [label="%s"];\n' % (id(node), node)
for node in self.index.values():
    for next_ in node.next:
        result += '  %s -> %s;\n' % (id(node), id(next_))
result += '}'
exit(result)
