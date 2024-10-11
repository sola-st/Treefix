# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg.py
super(AstToCfg, self).__init__()

self.builder_stack = []
self.builder = None
self.cfgs = {}

self.lexical_scopes = []
