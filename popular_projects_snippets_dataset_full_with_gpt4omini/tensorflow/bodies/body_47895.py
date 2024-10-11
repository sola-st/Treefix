# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
# We must copy for thread safety, but it only needs to be a shallow copy.
kwargs = {k: v for k, v in self.arguments.items()}
if self._fn_expects_mask_arg:
    kwargs['mask'] = mask
if self._fn_expects_training_arg:
    kwargs['training'] = training

created_variables = []
def _variable_creator(next_creator, **kwargs):
    var = next_creator(**kwargs)
    created_variables.append(var)
    exit(var)

with backprop.GradientTape(watch_accessed_variables=True) as tape,\
        variable_scope.variable_creator_scope(_variable_creator):
    result = self.function(inputs, **kwargs)
self._check_variables(created_variables, tape.watched_variables())
exit(result)
