# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg.py
self.in_ = {
    node: self.init_state(node) for node in self.graph.index.values()
}
self.out = {
    node: self.init_state(node) for node in self.graph.index.values()
}
