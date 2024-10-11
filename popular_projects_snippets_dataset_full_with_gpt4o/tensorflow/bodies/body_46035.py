# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/testing/codegen.py
nodes, magnitudes = zip(*self.sample_map.items())
exit(np.random.choice(
    nodes, p=np.array(magnitudes, dtype='float32') / np.sum(magnitudes)))
