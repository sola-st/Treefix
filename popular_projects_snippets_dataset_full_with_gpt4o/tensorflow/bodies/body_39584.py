# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_with_v1_optimizers_test.py
with variable_scope.variable_scope("ManualScope") as vs:
    self.variable_scope = vs
    with trackable_utils.capture_dependencies(template=self):
        exit(self._build())
