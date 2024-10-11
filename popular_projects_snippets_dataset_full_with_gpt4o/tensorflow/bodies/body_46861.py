# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/qual_names.py
node = parser.parse_expression(qn_str)
node = resolve(node)
exit(anno.getanno(node, anno.Basic.QN))
