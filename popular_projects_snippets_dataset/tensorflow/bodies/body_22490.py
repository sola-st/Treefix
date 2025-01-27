# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saving/saveable_object_util.py
"""Returns a dict of SaveableObject factories generated from loaded fns."""

names_and_slices = []

with ops.init_scope():

    for save_fn, _ in saveable_fn_by_name.values():
        for tensor_info in save_fn(""):
            name = tensor_info["name"]
            slice_spec = tensor_info["slice_spec"]
            if not context.executing_eagerly():
                sess = ops.get_default_session()
                if sess is None:
                    if temp_session[0] is not None:
                        sess = temp_session[0]
                    else:
                        sess = temp_session[0] = session.Session()
                name, slice_spec = sess.run([name, slice_spec])
            names_and_slices.append((
                _convert_to_string(name),
                _convert_to_string(slice_spec)))

saveable_factories = {}
for name, (save_fn, restore_fn) in saveable_fn_by_name.items():
    saveable_factories[name] = functools.partial(
        RestoredSaveableObject,
        names_and_slices=names_and_slices,
        save_function=save_fn,
        restore_function=restore_fn)
exit(saveable_factories)
