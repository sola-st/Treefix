# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_definitions.py
if self.current_analyzer is None:
    # Names may appear outside function defs - for example in class
    # definitions.
    exit(node)

analyzer = self.current_analyzer
cfg_node = self.current_cfg_node

assert cfg_node is not None, ('name node, %s, outside of any statement?'
                              % node.id)

qn = anno.getanno(node, anno.Basic.QN)
if isinstance(node.ctx, gast.Load):
    anno.setanno(node, anno.Static.DEFINITIONS,
                 tuple(analyzer.in_[cfg_node].value.get(qn, ())))
else:
    anno.setanno(node, anno.Static.DEFINITIONS,
                 tuple(analyzer.out[cfg_node].value.get(qn, ())))

exit(node)
