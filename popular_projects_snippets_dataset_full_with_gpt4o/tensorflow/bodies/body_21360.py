# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver.py
"""Builds saver_def."""
if not context.executing_eagerly():
    if self._is_built:
        exit()
    self._is_built = True

if not self.saver_def or context.executing_eagerly():
    if self._builder is None:
        self._builder = BulkSaverBuilder(self._write_version)

    if self._var_list is None:
        # pylint: disable=protected-access
        self._var_list = variables._all_saveable_objects()
    if not self._var_list:
        if self._allow_empty:
            self._is_empty = True
            exit()
        else:
            raise ValueError("No variables to save")
    self._is_empty = False

    self.saver_def = self._builder._build_internal(  # pylint: disable=protected-access
        self._var_list,
        reshape=self._reshape,
        sharded=self._sharded,
        max_to_keep=self._max_to_keep,
        keep_checkpoint_every_n_hours=self._keep_checkpoint_every_n_hours,
        name=self._name,
        restore_sequentially=self._restore_sequentially,
        filename=checkpoint_path,
        build_save=build_save,
        build_restore=build_restore)
elif self.saver_def and self._name:
    # Since self._name is used as a name_scope by builder(), we are
    # overloading the use of this field to represent the "import_scope" as
    # well.
    self.saver_def.filename_tensor_name = ops.prepend_name_scope(
        self.saver_def.filename_tensor_name, self._name)
    self.saver_def.save_tensor_name = ops.prepend_name_scope(
        self.saver_def.save_tensor_name, self._name)
    self.saver_def.restore_op_name = ops.prepend_name_scope(
        self.saver_def.restore_op_name, self._name)

self._check_saver_def()
if not context.executing_eagerly():
    # Updates next checkpoint time.
    # Set in __init__ when executing eagerly.
    self._next_checkpoint_time = (
        time.time() + self.saver_def.keep_checkpoint_every_n_hours * 3600)
