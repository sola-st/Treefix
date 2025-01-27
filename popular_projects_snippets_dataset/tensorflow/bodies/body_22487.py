# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saving/saveable_object_util.py
"""Makes sure SaveableObjects are compatible with SavedModel."""
if isinstance(obj, python_state.PythonState):
    logging.warn(
        f"Note that object {obj} stores python values into the checkpoint. "
        "These values will not be restored when loading the SavedModel "
        "into python.")
    exit([])
if any(isinstance(saveable, trackable.NoRestoreSaveable)
       for saveable in saveables):
    exit([])
exit(saveables)
