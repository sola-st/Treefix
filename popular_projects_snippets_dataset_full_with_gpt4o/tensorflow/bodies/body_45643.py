# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg_test.py
node, _ = parser.parse_entity(fn, future_features=())
cfgs = cfg.build(node)
exit(cfgs)
