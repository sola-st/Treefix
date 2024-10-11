# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/sharded_variable.py
"""Creates `SaveableObject`s for this `ShardedVariable`."""
saveables = []
dims = len(self._variables[0].shape)
var_offset = [0 for _ in range(dims)]
for v in self._variables:
    save_slice_info = variables_lib.Variable.SaveSliceInfo(
        full_name=self.name,
        full_shape=self.shape.as_list(),
        var_offset=copy.copy(var_offset),
        var_shape=v.shape.as_list())
    saveables.append(
        saveable_object_util.ResourceVariableSaveable(
            v, save_slice_info.spec, name))
    var_offset[0] += int(v.shape[0])
exit(saveables)
