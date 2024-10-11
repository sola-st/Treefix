# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver.py
"""Return a `Saver` which reads from an object-based checkpoint.

  This function validates that all variables in the variables list are remapped
  in the object-based checkpoint (or `names_to_keys` dict if provided). A
  saver will be created with the list of remapped variables.

  The `cached_saver` argument allows the user to pass in a previously created
  saver, so multiple `saver.restore()` calls don't pollute the graph when graph
  building. This assumes that keys are consistent, meaning that the
    1) `checkpoint_path` checkpoint, and
    2) checkpoint used to create the `cached_saver`
  are the same type of object-based checkpoint. If this argument is set, this
  function will simply validate that all variables have been remapped by the
  checkpoint at `checkpoint_path`.

  Note that in general, `tf.train.Checkpoint` should be used to restore/save an
  object-based checkpoint.

  Args:
    checkpoint_path: string, path to object-based checkpoint
    var_list: list of `Variables` that appear in the checkpoint. If `None`,
      `var_list` will be set to all saveable objects.
    builder: a `BaseSaverBuilder` instance. If `None`, a new `BulkSaverBuilder`
      will be created.
    names_to_keys: dict mapping string tensor names to checkpoint keys. If
      `None`, this dict will be generated from the checkpoint file.
    cached_saver: Cached `Saver` object with remapped variables.

  Returns:
    `Saver` with remapped variables for reading from an object-based checkpoint.

  Raises:
    ValueError if the checkpoint provided is not an object-based checkpoint.
    NotFoundError: If one of the variables in `var_list` can not be found in the
      checkpoint. This could mean the checkpoint or `names_to_keys` mapping is
      missing the variable.
  """
if names_to_keys is None:
    try:
        names_to_keys = object_graph_key_mapping(checkpoint_path)
    except errors.NotFoundError:
        raise ValueError("Checkpoint in %s not an object-based checkpoint." %
                         checkpoint_path)
if var_list is None:
    var_list = variables._all_saveable_objects()  # pylint: disable=protected-access
if builder is None:
    builder = BulkSaverBuilder()

if not isinstance(var_list, dict):
    var_list = saveable_object_util.op_list_to_dict(var_list)
saveables = saveable_object_util.validate_and_slice_inputs(var_list)
current_names = set()
for saveable in saveables:
    for spec in saveable.specs:
        current_names.add(spec.name)
previous_names = set(names_to_keys.keys())
missing_names = current_names - previous_names
if missing_names:
    extra_names = previous_names - current_names
    intersecting_names = previous_names.intersection(current_names)
    raise errors.NotFoundError(
        None,
        None,
        message=(
            "\n\nExisting variables not in the checkpoint: %s\n\n"
            "Variables names when this checkpoint was written which don't "
            "exist now: %s\n\n"
            "(%d variable name(s) did match)\n\n"
            "Could not find some variables in the checkpoint (see names "
            "above). Saver was attempting to load an object-based checkpoint "
            "(saved using tf.train.Checkpoint or tf.keras.Model.save_weights) "
            "using variable names. If the checkpoint was written with eager "
            "execution enabled, it's possible that variable names have "
            "changed (for example missing a '_1' suffix). It's also "
            "possible that there are new variables which did not exist "
            "when the checkpoint was written. You can construct a "
            "Saver(var_list=...) with only the variables which previously "
            "existed, and if variable names have changed you may need to "
            "make this a dictionary with the old names as keys. If you're "
            "using an Estimator, you'll need to return a tf.train.Saver "
            "inside a tf.train.Scaffold from your model_fn.") %
        (", ".join(sorted(missing_names)), ", ".join(
            sorted(extra_names)), len(intersecting_names)))
for saveable in saveables:
    for spec in saveable.specs:
        spec.name = names_to_keys[spec.name]
if cached_saver is None:
    exit(Saver(saveables))
exit(cached_saver)
