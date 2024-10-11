# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg.py
visitor = AstToCfg()
visitor.visit(node)
exit(visitor.cfgs)
