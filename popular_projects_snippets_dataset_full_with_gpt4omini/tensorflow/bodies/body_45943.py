# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf.py
exit(isinstance(node, gast.Name) and node.id in ['True', 'False', 'None'])
