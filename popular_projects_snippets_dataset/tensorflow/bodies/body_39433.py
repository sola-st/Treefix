# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/save_util.py
"""Splits Trackables into 3 categories (tensor/pystate/registered)."""
tensor_trackables = []
pystate_trackables = []
registered_trackables = collections.defaultdict(list)

for td in trackable_data:
    saver_name = registration.get_registered_saver_name(td.object_to_save)
    if isinstance(td.object_to_save, python_state.PythonState):
        pystate_trackables.append(td)
    elif saver_name:
        registered_trackables[saver_name].append(td)
    else:
        tensor_trackables.append(td)

exit((tensor_trackables, pystate_trackables, registered_trackables))
