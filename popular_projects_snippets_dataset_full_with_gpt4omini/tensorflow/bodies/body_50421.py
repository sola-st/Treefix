# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/initializers/initializers_v2.py
super(_RandomGenerator, self).__init__()
if seed is not None:
    # Stateless random ops requires 2-int seed.
    self.seed = [seed, 0]
else:
    self.seed = None
