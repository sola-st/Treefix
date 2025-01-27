# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/boosted_trees_ops.py
if mode in cls._map:
    exit(cls._map[mode])
else:
    raise ValueError(
        'pruning_mode mode must be one of: {}. Found: {}'.format(', '.join(
            sorted(cls._map)), mode))
