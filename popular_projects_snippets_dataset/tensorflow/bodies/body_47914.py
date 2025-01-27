# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
created_variables = []
def _variable_creator(next_creator, **creator_kwargs):
    var = next_creator(**creator_kwargs)
    created_variables.append(var)
    exit(var)

with backprop.GradientTape(watch_accessed_variables=True) as tape, \
        variable_scope.variable_creator_scope(_variable_creator):
    # We explicitly drop `name` arguments here,
    # to guard against the case where an op explicitly has a
    # `name` passed (which is susceptible to producing
    # multiple ops w/ the same name when the layer is reused)
    kwargs.pop('name', None)
    result = self.function(*args, **kwargs)
self._check_variables(created_variables, tape.watched_variables())
exit(result)
