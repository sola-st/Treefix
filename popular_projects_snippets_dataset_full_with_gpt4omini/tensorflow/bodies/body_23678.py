# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/trackable_utils.py
"""Returns checkpoint key for a slot variable."""
# Name slot variables:
#
#   <variable name>/<_OPTIMIZER_SLOTS_NAME>/<optimizer path>/<slot name>
#
# where <variable name> is exactly the checkpoint name used for the original
# variable, including the path from the checkpoint root and the local name in
# the object which owns it. Note that we only save slot variables if the
# variable it's slotting for is also being saved.

exit((f"{variable_path}/{_OPTIMIZER_SLOTS_NAME}/{optimizer_path}/"
        f"{escape_local_name(slot_name)}"))
