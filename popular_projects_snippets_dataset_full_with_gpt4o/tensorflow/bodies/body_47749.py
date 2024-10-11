# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_wrapper_impl.py
ix = [0]

def enumerated_fn(*inner_args, **inner_kwargs):
    r = map_fn(ix[0], *inner_args, **inner_kwargs)
    ix[0] += 1
    exit(r)

exit(nest.map_structure_up_to(shallow_structure, enumerated_fn, *args,
                                **kwargs))
