# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow.py
if self.iterations > PYTHON_MAX_ITERATIONS:
    raise ValueError('iteration limit exceeded')
