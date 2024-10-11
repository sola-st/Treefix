# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
inner_kwargs.pop("name")  # Ignored; this is the scope-stripped name which
# we don't want to propagate.
exit(next_creator(initial_value=initializer, name=name, **inner_kwargs))
