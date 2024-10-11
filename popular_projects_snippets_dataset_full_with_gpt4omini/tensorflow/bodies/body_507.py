# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2.py
self.upgrade_compat_v1_import = upgrade_compat_v1_import

# Maps from a function name to a dictionary that describes how to
# map from an old argument keyword to the new argument keyword.
# If the new argument is None, it will be removed.
# Only keyword args are handled, so make sure to also put any function in
# function_reorders to ensure that all args are made into keywords first.
self.function_keyword_renames = {
    # TODO(b/129398290)
    # "tf.string_split": {
    #     "delimiter": "sep",
    # },
    "tf.test.assert_equal_graph_def": {
        "checkpoint_v2": None,
        "hash_table_shared_name": None,
    },
    "tf.autograph.to_code": {
        "arg_types": None,
        "arg_values": None,
        "indentation": None,
    },
    "tf.autograph.to_graph": {
        "arg_types": None,
        "arg_values": None,
    },
    "tf.nn.embedding_lookup": {
        "validate_indices": None,
    },
    "tf.image.sample_distorted_bounding_box": {
        "seed2": None,
    },
    "tf.gradients": {
        "colocate_gradients_with_ops": None,
    },
    "tf.hessians": {
        "colocate_gradients_with_ops": None,
    },
    "*.minimize": {
        "colocate_gradients_with_ops": None,
    },
    "*.compute_gradients": {
        "colocate_gradients_with_ops": None,
    },
    "tf.cond": {
        "strict": None,
        "fn1": "true_fn",
        "fn2": "false_fn"
    },
    "tf.argmin": {
        "dimension": "axis",
    },
    "tf.argmax": {
        "dimension": "axis",
    },
    "tf.arg_min": {
        "dimension": "axis",
    },
    "tf.arg_max": {
        "dimension": "axis",
    },
    "tf.math.argmin": {
        "dimension": "axis",
    },
    "tf.math.argmax": {
        "dimension": "axis",
    },
    "tf.image.crop_and_resize": {
        "box_ind": "box_indices",
    },
    "tf.extract_image_patches": {
        "ksizes": "sizes",
    },
    "tf.image.extract_image_patches": {
        "ksizes": "sizes",
    },
    "tf.image.resize": {
        "align_corners": None,
    },
    "tf.image.resize_images": {
        "align_corners": None,
    },
    "tf.expand_dims": {
        "dim": "axis",
    },
    "tf.batch_to_space": {
        "block_size": "block_shape",
    },
    "tf.space_to_batch": {
        "block_size": "block_shape",
    },
    "tf.nn.space_to_batch": {
        "block_size": "block_shape",
    },
    "tf.constant": {
        "verify_shape": "verify_shape_is_now_always_true",
    },
    "tf.convert_to_tensor": {
        "preferred_dtype": "dtype_hint"
    },
    "tf.nn.softmax_cross_entropy_with_logits": {
        "dim": "axis",
    },
    "tf.nn.softmax_cross_entropy_with_logits_v2": {
        "dim": "axis"
    },
    "tf.linalg.l2_normalize": {
        "dim": "axis",
    },
    "tf.linalg.norm": {
        "keep_dims": "keepdims",
    },
    "tf.norm": {
        "keep_dims": "keepdims",
    },
    "tf.load_file_system_library": {
        "library_filename": "library_location",
    },
    "tf.count_nonzero": {
        "input_tensor": "input",
        "keep_dims": "keepdims",
        "reduction_indices": "axis",
    },
    "tf.math.count_nonzero": {
        "input_tensor": "input",
        "keep_dims": "keepdims",
        "reduction_indices": "axis",
    },
    "tf.nn.erosion2d": {
        "kernel": "filters",
        "rates": "dilations",
    },
    "tf.math.l2_normalize": {
        "dim": "axis",
    },
    "tf.math.log_softmax": {
        "dim": "axis",
    },
    "tf.math.softmax": {
        "dim": "axis"
    },
    "tf.nn.l2_normalize": {
        "dim": "axis",
    },
    "tf.nn.log_softmax": {
        "dim": "axis",
    },
    "tf.nn.moments": {
        "keep_dims": "keepdims",
    },
    "tf.nn.pool": {
        "dilation_rate": "dilations"
    },
    "tf.nn.separable_conv2d": {
        "rate": "dilations"
    },
    "tf.nn.depthwise_conv2d": {
        "rate": "dilations"
    },
    "tf.nn.softmax": {
        "dim": "axis"
    },
    "tf.nn.sufficient_statistics": {
        "keep_dims": "keepdims"
    },
    "tf.debugging.assert_all_finite": {
        "t": "x",
        "msg": "message",
    },
    "tf.verify_tensor_all_finite": {
        "t": "x",
        "msg": "message",
    },
    "tf.sparse.add": {
        "thresh": "threshold",
    },
    "tf.sparse_add": {
        "thresh": "threshold",
    },
    "tf.sparse.concat": {
        "concat_dim": "axis",
        "expand_nonconcat_dim": "expand_nonconcat_dims",
    },
    "tf.sparse_concat": {
        "concat_dim": "axis",
        "expand_nonconcat_dim": "expand_nonconcat_dims",
    },
    "tf.sparse.split": {
        "split_dim": "axis",
    },
    "tf.sparse_split": {
        "split_dim": "axis",
    },
    "tf.sparse.reduce_max": {
        "reduction_axes": "axis",
        "keep_dims": "keepdims",
    },
    "tf.sparse_reduce_max": {
        "reduction_axes": "axis",
        "keep_dims": "keepdims",
    },
    "tf.sparse.reduce_sum": {
        "reduction_axes": "axis",
        "keep_dims": "keepdims",
    },
    "tf.sparse_reduce_sum": {
        "reduction_axes": "axis",
        "keep_dims": "keepdims",
    },
    "tf.nn.max_pool_with_argmax": {
        "Targmax": "output_dtype",
    },
    "tf.nn.max_pool": {
        "value": "input"
    },
    "tf.nn.avg_pool": {
        "value": "input"
    },
    "tf.nn.avg_pool2d": {
        "value": "input"
    },
    "tf.multinomial": {
        "output_dtype": "dtype",
    },
    "tf.random.multinomial": {
        "output_dtype": "dtype",
    },
    "tf.reverse_sequence": {
        "seq_dim": "seq_axis",
        "batch_dim": "batch_axis",
    },
    "tf.nn.batch_norm_with_global_normalization": {
        "t": "input",
        "m": "mean",
        "v": "variance",
    },
    "tf.nn.dilation2d": {
        "filter": "filters",
        "rates": "dilations",
    },
    "tf.nn.conv3d": {
        "filter": "filters"
    },
    "tf.zeros_like": {
        "tensor": "input",
    },
    "tf.ones_like": {
        "tensor": "input",
    },
    "tf.nn.conv2d_transpose": {
        "value": "input",
        "filter": "filters",
    },
    "tf.nn.conv3d_transpose": {
        "value": "input",
        "filter": "filters",
    },
    "tf.nn.convolution": {
        "filter": "filters",
        "dilation_rate": "dilations",
    },
    "tf.gfile.Exists": {
        "filename": "path",
    },
    "tf.gfile.Remove": {
        "filename": "path",
    },
    "tf.gfile.Stat": {
        "filename": "path",
    },
    "tf.gfile.Glob": {
        "filename": "pattern",
    },
    "tf.gfile.MkDir": {
        "dirname": "path",
    },
    "tf.gfile.MakeDirs": {
        "dirname": "path",
    },
    "tf.gfile.DeleteRecursively": {
        "dirname": "path",
    },
    "tf.gfile.IsDirectory": {
        "dirname": "path",
    },
    "tf.gfile.ListDirectory": {
        "dirname": "path",
    },
    "tf.gfile.Copy": {
        "oldpath": "src",
        "newpath": "dst",
    },
    "tf.gfile.Rename": {
        "oldname": "src",
        "newname": "dst",
    },
    "tf.gfile.Walk": {
        "in_order": "topdown",
    },
    "tf.random.stateless_multinomial": {
        "output_dtype": "dtype",
    },
    "tf.string_to_number": {
        "string_tensor": "input",
    },
    "tf.strings.to_number": {
        "string_tensor": "input",
    },
    "tf.string_to_hash_bucket": {
        "string_tensor": "input",
    },
    "tf.strings.to_hash_bucket": {
        "string_tensor": "input",
    },
    "tf.reduce_all": {
        "reduction_indices": "axis",
        "keep_dims": "keepdims",
    },
    "tf.math.reduce_all": {
        "reduction_indices": "axis",
        "keep_dims": "keepdims",
    },
    "tf.reduce_any": {
        "reduction_indices": "axis",
        "keep_dims": "keepdims",
    },
    "tf.math.reduce_any": {
        "reduction_indices": "axis",
        "keep_dims": "keepdims",
    },
    "tf.reduce_min": {
        "reduction_indices": "axis",
        "keep_dims": "keepdims",
    },
    "tf.math.reduce_min": {
        "reduction_indices": "axis",
        "keep_dims": "keepdims",
    },
    "tf.reduce_max": {
        "reduction_indices": "axis",
        "keep_dims": "keepdims",
    },
    "tf.math.reduce_max": {
        "reduction_indices": "axis",
        "keep_dims": "keepdims",
    },
    "tf.reduce_sum": {
        "reduction_indices": "axis",
        "keep_dims": "keepdims",
    },
    "tf.math.reduce_sum": {
        "reduction_indices": "axis",
        "keep_dims": "keepdims",
    },
    "tf.reduce_mean": {
        "reduction_indices": "axis",
        "keep_dims": "keepdims",
    },
    "tf.math.reduce_mean": {
        "reduction_indices": "axis",
        "keep_dims": "keepdims",
    },
    "tf.reduce_prod": {
        "reduction_indices": "axis",
        "keep_dims": "keepdims",
    },
    "tf.math.reduce_prod": {
        "reduction_indices": "axis",
        "keep_dims": "keepdims",
    },
    "tf.reduce_logsumexp": {
        "reduction_indices": "axis",
        "keep_dims": "keepdims",
    },
    "tf.math.reduce_logsumexp": {
        "reduction_indices": "axis",
        "keep_dims": "keepdims",
    },
    "tf.reduce_join": {
        "keep_dims": "keepdims",
        "reduction_indices": "axis"
    },
    "tf.strings.reduce_join": {
        "keep_dims": "keepdims",
        "reduction_indices": "axis"
    },
    "tf.squeeze": {
        "squeeze_dims": "axis",
    },
    "tf.nn.weighted_moments": {
        "keep_dims": "keepdims"
    },
    "tf.nn.conv1d": {
        "value": "input",
        "use_cudnn_on_gpu": None,
    },
    "tf.nn.conv2d": {
        "filter": "filters",
        "use_cudnn_on_gpu": None,
    },
    "tf.nn.conv2d_backprop_input": {
        "use_cudnn_on_gpu": None,
        "input_sizes": "output_shape",
        "out_backprop": "input",
        "filter": "filters",
    },
    "tf.contrib.summary.audio": {
        "tensor": "data",
        "family": None,
    },
    "tf.contrib.summary.create_file_writer": {
        "name": None,
    },
    "tf.contrib.summary.generic": {
        "name": "tag",
        "tensor": "data",
        "family": None,
    },
    "tf.contrib.summary.histogram": {
        "tensor": "data",
        "family": None,
    },
    "tf.contrib.summary.image": {
        "tensor": "data",
        "bad_color": None,
        "max_images": "max_outputs",
        "family": None,
    },
    "tf.contrib.summary.scalar": {
        "tensor": "data",
        "family": None,
    },
    "tf.nn.weighted_cross_entropy_with_logits": {
        "targets": "labels",
    },
    "tf.decode_raw": {
        "bytes": "input_bytes",
    },
    "tf.io.decode_raw": {
        "bytes": "input_bytes",
    },
    "tf.contrib.framework.load_variable": {
        "checkpoint_dir": "ckpt_dir_or_file",
    }
}
all_renames_v2.add_contrib_direct_import_support(
    self.function_keyword_renames)

# Mapping from function to the new name of the function
# Add additional renames not in renames_v2.py to all_renames_v2.py.
self.symbol_renames = all_renames_v2.symbol_renames
self.import_rename = import_rename
if self.import_rename:
    self.import_renames = {
        "tensorflow":
            ast_edits.ImportRename(
                "tensorflow.compat.v2",
                excluded_prefixes=[
                    "tensorflow.contrib", "tensorflow.flags",
                    "tensorflow.compat.v1", "tensorflow.compat.v2",
                    "tensorflow.google"
                ],
            )
    }
else:
    self.import_renames = {}

# Variables that should be changed to functions.
self.change_to_function = {}

# pylint: disable=line-too-long
# This list should just contain names of functions that had
# their arguments reordered. After adding a function name to the list
# run the following to update reorders_v2.py:
# bazel run tensorflow/tools/compatibility/update:generate_v2_reorders_map
# pylint: enable=line-too-long
self.reordered_function_names = {
    "tf.io.serialize_sparse",
    "tf.io.serialize_many_sparse",
    "tf.argmax",
    "tf.argmin",
    "tf.batch_to_space",
    "tf.cond",
    "tf.nn.space_to_batch",
    "tf.boolean_mask",
    "tf.convert_to_tensor",
    "tf.nn.conv1d",
    "tf.nn.conv2d",
    "tf.nn.conv2d_backprop_input",
    "tf.nn.ctc_beam_search_decoder",
    "tf.nn.moments",
    "tf.nn.convolution",
    "tf.nn.crelu",
    "tf.nn.weighted_moments",
    "tf.nn.pool",
    "tf.nn.separable_conv2d",
    "tf.nn.depthwise_conv2d",
    "tf.multinomial",
    "tf.random.multinomial",
    "tf.pad",
    "tf.quantize_v2",
    "tf.feature_column.categorical_column_with_vocabulary_file",
    "tf.shape",
    "tf.size",
    # TODO(b/129398290)
    # "tf.string_split",
    "tf.random.poisson",
    "tf.sparse.add",
    "tf.sparse_add",
    "tf.sparse.concat",
    "tf.sparse_concat",
    "tf.sparse.segment_mean",
    "tf.sparse.segment_sqrt_n",
    "tf.sparse.segment_sum",
    "tf.sparse_matmul",
    "tf.sparse.reduce_max",
    "tf.sparse_reduce_max",
    "tf.io.decode_csv",
    "tf.strings.length",
    "tf.strings.reduce_join",
    "tf.strings.substr",
    "tf.substr",
    "tf.transpose",
    "tf.tuple",
    "tf.parse_example",
    "tf.parse_single_example",
    "tf.io.parse_example",
    "tf.io.parse_single_example",
    "tf.while_loop",
    "tf.reduce_all",
    "tf.math.reduce_all",
    "tf.reduce_any",
    "tf.math.reduce_any",
    "tf.reduce_min",
    "tf.math.reduce_min",
    "tf.reduce_max",
    "tf.math.reduce_max",
    "tf.reduce_sum",
    "tf.math.reduce_sum",
    "tf.reduce_mean",
    "tf.math.reduce_mean",
    "tf.reduce_prod",
    "tf.math.reduce_prod",
    "tf.reduce_logsumexp",
    "tf.math.reduce_logsumexp",
    "tf.reduce_join",
    "tf.confusion_matrix",
    "tf.math.confusion_matrix",
    "tf.math.in_top_k",
    "tf.nn.depth_to_space",
    "tf.nn.embedding_lookup",
    "tf.nn.embedding_lookup_sparse",
    "tf.nn.in_top_k",
    "tf.nn.space_to_depth",
    "tf.test.assert_equal_graph_def",
    "tf.linalg.norm",
    "tf.norm",
    "tf.reverse_sequence",
    "tf.sparse_split",
    # tf.nn.softmax_cross_entropy_with_logits *must* be called with
    # keyword arguments. Add keyword arguments in rare case when they
    # are not specified.
    "tf.nn.softmax_cross_entropy_with_logits",
    "tf.nn.fractional_avg_pool",
    "tf.nn.fractional_max_pool",
    "tf.image.sample_distorted_bounding_box",
    "tf.gradients",
    "tf.hessians",
    "tf.nn.max_pool",
    "tf.nn.avg_pool",
    "tf.estimator.LinearClassifier",
    "tf.estimator.LinearRegressor",
    "tf.estimator.DNNLinearCombinedClassifier",
    "tf.estimator.DNNLinearCombinedRegressor",
    "tf.estimator.DNNRegressor",
    "tf.estimator.DNNClassifier",
    "tf.estimator.BaselineClassifier",
    "tf.estimator.BaselineRegressor",
    "tf.initializers.uniform_unit_scaling",
    "tf.uniform_unit_scaling_initializer",
    "tf.train.sdca_fprint",
    "tf.train.sdca_optimizer",
    "tf.train.sdca_shrink_l1",
    "tf.data.experimental.TensorStructure",
    "tf.data.experimental.SparseTensorStructure",
    "tf.data.experimental.RaggedTensorStructure",
    "tf.data.experimental.TensorArrayStructure",
    "tf.debugging.assert_all_finite",
    "tf.gather_nd",
}

# Manual mapping of function names to be reordered to their list of argument
# names, in order. Only use this if argument names cannot be autodetected,
# e.g. if the functions are in contrib.
self.manual_function_reorders = {
    "tf.contrib.summary.audio": [
        "name", "tensor", "sample_rate", "max_outputs", "family", "step"],
    "tf.contrib.summary.create_file_writer": [
        "logdir", "max_queue", "flush_millis", "filename_suffix", "name"],
    "tf.contrib.summary.generic": [
        "name", "tensor", "metadata", "family", "step"],
    "tf.contrib.summary.histogram": [
        "name", "tensor", "family", "step"],
    "tf.contrib.summary.image": [
        "name", "tensor", "bad_color", "max_images", "family", "step"],
    "tf.contrib.summary.scalar": [
        "name", "tensor", "family", "step"],
}
# Functions that were reordered should be changed to the new keyword args
# for safety, if positional arguments are used. If you have reversed the
# positional arguments yourself, this could do the wrong thing.
self.function_reorders = dict(reorders_v2.reorders)
self.function_reorders.update(self.manual_function_reorders)

decay_function_comment = (
    ast_edits.INFO,
    "To use learning rate decay schedules with TensorFlow 2.0, switch to "
    "the schedules in `tf.keras.optimizers.schedules`.\n"
)

assert_return_type_comment = (
    ast_edits.INFO,
    "<function name> has been changed to return None, the "
    "data argument has been removed, and arguments have been reordered."
    "\nThe calls have been converted to compat.v1 for safety (even though "
    " they may already have been correct)."
)

assert_rank_comment = (
    ast_edits.INFO,
    "<function name> has been changed to return None, and"
    " the data and summarize arguments have been removed."
    "\nThe calls have been converted to compat.v1 for safety (even though "
    " they may already have been correct)."
)

contrib_layers_layer_norm_comment = (
    ast_edits.WARNING,
    "(Manual edit required) `tf.contrib.layers.layer_norm` has been "
    "deprecated, and its implementation has been integrated with "
    "`tf.keras.layers.LayerNormalization` in TensorFlow 2.0. "
    "Note that, the default value of `epsilon` is changed to `1e-3` in the "
    "new API from `1e-12`, and this may introduce numerical differences. "
    "Please check the new API and use that instead."
)

contrib_estimator_head_comment = (
    ast_edits.WARNING,
    "(Manual edit required) `tf.contrib.estimator.*_head` has been "
    "deprecated, and its implementation has been integrated with "
    "`tf.estimator.*Head` in TensorFlow 2.0. "
    "Please check the new API and use that instead."
)

initializers_no_dtype_comment = (
    ast_edits.INFO, "Initializers no longer have the "
    "dtype argument in the constructor or partition_info argument in the "
    "__call__ method.\nThe calls have been converted to compat.v1 for "
    "safety (even though they may already have been correct).")

metrics_comment = (
    ast_edits.INFO,
    "tf.metrics have been replaced with object oriented versions in"
    " TF 2.0 and after. The metric function calls have been converted to "
    "compat.v1 for backward compatibility. Please update these calls to "
    "the TF 2.0 versions.")

losses_comment = (
    ast_edits.INFO,
    "tf.losses have been replaced with object oriented versions in"
    " TF 2.0 and after. The loss function calls have been converted to "
    "compat.v1 for backward compatibility. Please update these calls to "
    "the TF 2.0 versions.")

# This could be done with a _rename_if_arg_not_found_transformer
deprecate_partition_strategy_comment = (
    ast_edits.WARNING,
    "`partition_strategy` has been removed from <function name>. "
    " The 'div' strategy will be used by default.")

# make change instead
uniform_unit_scaling_initializer_comment = (
    ast_edits.ERROR,
    "uniform_unit_scaling_initializer has been removed. Please use"
    " tf.initializers.variance_scaling instead with distribution=uniform "
    "to get equivalent behaviour.")

# Make change instead (issue warning about strip_...)
export_saved_model_renamed = (
    ast_edits.ERROR,
    "(Manual edit required) Please rename the method export_savedmodel() "
    "to export_saved_model(). Two things to note:\n\t(1) The argument "
    "strip_default_attributes has been removed. The function will always "
    "strip the default attributes from ops. If this breaks your code, "
    "please switch to tf.compat.v1.estimator.Estimator.\n\t(2) This change "
    "only effects core estimator. If you are using "
    "tf.contrib.learn.Estimator, please switch to using core estimator.")

summary_api_comment = (
    ast_edits.INFO,
    "The TF 1.x summary API cannot be automatically migrated to TF 2.0, so "
    "symbols have been converted to tf.compat.v1.summary.* and must be "
    "migrated manually. Typical usage will only require changes to the "
    "summary writing logic, not to individual calls like scalar(). "
    "For examples of the new summary API, see the Effective TF 2.0 "
    "migration document or check the TF 2.0 TensorBoard tutorials.")

contrib_summary_comment = (
    ast_edits.WARNING,
    "tf.contrib.summary.* functions have been migrated best-effort to "
    "tf.compat.v2.summary.* equivalents where possible, but the resulting "
    "code is not guaranteed to work, so please check carefully. For more "
    "information about the new summary API, see the Effective TF 2.0 "
    "migration document or check the updated TensorBoard tutorials.")

contrib_summary_family_arg_comment = (
    ast_edits.WARNING,
    "<function name> replacement does not accept a 'family' argument; "
    "instead regular name scoping should be used. This call site specifies "
    "a family argument that has been removed on conversion, so the emitted "
    "tag names may be incorrect without manual editing.")

contrib_create_file_writer_comment = (
    ast_edits.WARNING,
    "tf.contrib.summary.create_file_writer() has been ported to the new "
    "tf.compat.v2.summary.create_file_writer(), which no longer re-uses "
    "existing event files for the same logdir; instead it always opens a "
    "new writer/file. The python writer objects must be re-used explicitly "
    "if the reusing behavior is desired.")

contrib_summary_record_every_n_comment = (
    ast_edits.ERROR,
    "(Manual edit required) "
    "tf.contrib.summary.record_summaries_every_n_global_steps(n, step) "
    "should be replaced by a call to tf.compat.v2.summary.record_if() with "
    "the argument `lambda: tf.math.equal(0, global_step % n)` (or in graph "
    "mode, the lambda body can be used directly). If no global step was "
    "passed, instead use tf.compat.v1.train.get_or_create_global_step().")

contrib_summary_graph_comment = (
    ast_edits.ERROR,
    "(Manual edit required) tf.contrib.summary.graph() has no direct "
    "equivalent in TF 2.0 because manual graph construction has been "
    "superseded by use of tf.function. To log tf.function execution graphs "
    "to the summary writer, use the new tf.compat.v2.summary.trace_* "
    "functions instead.")

contrib_summary_import_event_comment = (
    ast_edits.ERROR,
    "(Manual edit required) tf.contrib.summary.import_event() has no "
    "direct equivalent in TF 2.0. For a similar experimental feature, try "
    "tf.compat.v2.summary.experimental.write_raw_pb() which also accepts "
    "serialized summary protocol buffer input, but for tf.Summary "
    "protobufs rather than tf.Events.")

keras_default_save_format_comment = (
    ast_edits.WARNING,
    "(This warning is only applicable if the code saves a tf.Keras model) "
    "Keras model.save now saves to the Tensorflow SavedModel format by "
    "default, instead of HDF5. To continue saving to HDF5, add the "
    "argument save_format='h5' to the save() function.")

distribute_strategy_api_changes = (
    "If you're using the strategy with a "
    "custom training loop, note the following changes in methods: "
    "make_dataset_iterator->experimental_distribute_dataset, "
    "experimental_make_numpy_iterator->experimental_make_numpy_dataset, "
    "extended.call_for_each_replica->run, "
    "reduce requires an axis argument, "
    "unwrap->experimental_local_results "
    "experimental_initialize and experimental_finalize no longer needed ")

contrib_mirrored_strategy_warning = (
    ast_edits.ERROR,
    "(Manual edit required) tf.contrib.distribute.MirroredStrategy has "
    "been migrated to tf.distribute.MirroredStrategy. Things to note: "
    "Constructor arguments have changed. If you are using "
    "MirroredStrategy with Keras training framework, the input provided to "
    "`model.fit` will be assumed to have global batch size and split "
    "across the replicas. " + distribute_strategy_api_changes)

core_mirrored_strategy_warning = (
    ast_edits.WARNING,
    "(Manual edit may be required) tf.distribute.MirroredStrategy API has "
    "changed. " + distribute_strategy_api_changes)

contrib_one_device_strategy_warning = (
    ast_edits.ERROR,
    "(Manual edit required) tf.contrib.distribute.OneDeviceStrategy has "
    "been migrated to tf.distribute.OneDeviceStrategy. " +
    distribute_strategy_api_changes)

contrib_tpu_strategy_warning = (
    ast_edits.ERROR,
    "(Manual edit required) tf.contrib.distribute.TPUStrategy has "
    "been migrated to tf.distribute.TPUStrategy. Note the "
    "slight changes in constructor. " + distribute_strategy_api_changes)

contrib_collective_strategy_warning = (
    ast_edits.ERROR,
    "(Manual edit required) "
    "tf.contrib.distribute.CollectiveAllReduceStrategy has "
    "been migrated to "
    "tf.distribute.experimental.MultiWorkerMirroredStrategy. Note the "
    "changes in constructor. " + distribute_strategy_api_changes)

contrib_ps_strategy_warning = (
    ast_edits.ERROR, "(Manual edit required) "
    "tf.contrib.distribute.ParameterServerStrategy has "
    "been migrated to "
    "tf.compat.v1.distribute.experimental.ParameterServerStrategy (multi "
    "machine) and tf.distribute.experimental.CentralStorageStrategy (one "
    "machine). Note the changes in constructors. " +
    distribute_strategy_api_changes)

keras_experimental_export_comment = (
    ast_edits.WARNING,
    "tf.keras.experimental.export_saved_model and "
    "tf.keras.experimental.load_from_saved_model have been deprecated."
    "Please use model.save(path, save_format='tf') "
    "(or alternatively tf.keras.models.save_model), and "
    "tf.keras.models.load_model(path) instead.")

saved_model_load_warning = (
    ast_edits.WARNING,
    "tf.saved_model.load works differently in 2.0 compared to 1.0. See "
    "migration information in the documentation of "
    "tf.compat.v1.saved_model.load."
    "\nThe calls have been converted to compat.v1.")

# Function warnings. <function name> placeholder inside warnings will be
# replaced by function name.
# You can use *. to add items which do not check the FQN, and apply to e.g.,
# methods.
self.function_warnings = {
    "*.export_savedmodel":
        export_saved_model_renamed,
    "*.save":
        keras_default_save_format_comment,
    "tf.assert_equal":
        assert_return_type_comment,
    "tf.assert_none_equal":
        assert_return_type_comment,
    "tf.assert_negative":
        assert_return_type_comment,
    "tf.assert_positive":
        assert_return_type_comment,
    "tf.assert_non_negative":
        assert_return_type_comment,
    "tf.assert_non_positive":
        assert_return_type_comment,
    "tf.assert_near":
        assert_return_type_comment,
    "tf.assert_less":
        assert_return_type_comment,
    "tf.assert_less_equal":
        assert_return_type_comment,
    "tf.assert_greater":
        assert_return_type_comment,
    "tf.assert_greater_equal":
        assert_return_type_comment,
    "tf.assert_integer":
        assert_return_type_comment,
    "tf.assert_type":
        assert_return_type_comment,
    "tf.assert_scalar":
        assert_return_type_comment,
    "tf.assert_rank":
        assert_rank_comment,
    "tf.assert_rank_at_least":
        assert_rank_comment,
    "tf.assert_rank_in":
        assert_rank_comment,
    "tf.contrib.layers.layer_norm":
        contrib_layers_layer_norm_comment,
    "tf.contrib.estimator.binary_classification_head":
        contrib_estimator_head_comment,
    "tf.contrib.estimator.logistic_regression_head":
        contrib_estimator_head_comment,
    "tf.contrib.estimator.multi_class_head":
        contrib_estimator_head_comment,
    "tf.contrib.estimator.multi_head":
        contrib_estimator_head_comment,
    "tf.contrib.estimator.multi_label_head":
        contrib_estimator_head_comment,
    "tf.contrib.estimator.poisson_regression_head":
        contrib_estimator_head_comment,
    "tf.contrib.estimator.regression_head":
        contrib_estimator_head_comment,
    "tf.contrib.saved_model.load_keras_model":
        keras_experimental_export_comment,
    "tf.contrib.saved_model.save_keras_model":
        keras_experimental_export_comment,
    "tf.contrib.summary.all_summary_ops":
        contrib_summary_comment,
    "tf.contrib.summary.audio":
        contrib_summary_comment,
    "tf.contrib.summary.create_file_writer":
        contrib_create_file_writer_comment,
    "tf.contrib.summary.generic":
        contrib_summary_comment,
    "tf.contrib.summary.graph":
        contrib_summary_graph_comment,
    "tf.contrib.summary.histogram":
        contrib_summary_comment,
    "tf.contrib.summary.import_event":
        contrib_summary_import_event_comment,
    "tf.contrib.summary.image":
        contrib_summary_comment,
    "tf.contrib.summary.record_summaries_every_n_global_steps":
        contrib_summary_record_every_n_comment,
    "tf.contrib.summary.scalar":
        contrib_summary_comment,
    "tf.debugging.assert_equal":
        assert_return_type_comment,
    "tf.debugging.assert_greater":
        assert_return_type_comment,
    "tf.debugging.assert_greater_equal":
        assert_return_type_comment,
    "tf.debugging.assert_integer":
        assert_return_type_comment,
    "tf.debugging.assert_less":
        assert_return_type_comment,
    "tf.debugging.assert_less_equal":
        assert_return_type_comment,
    "tf.debugging.assert_near":
        assert_return_type_comment,
    "tf.debugging.assert_negative":
        assert_return_type_comment,
    "tf.debugging.assert_non_negative":
        assert_return_type_comment,
    "tf.debugging.assert_non_positive":
        assert_return_type_comment,
    "tf.debugging.assert_none_equal":
        assert_return_type_comment,
    "tf.debugging.assert_positive":
        assert_return_type_comment,
    "tf.debugging.assert_type":
        assert_return_type_comment,
    "tf.debugging.assert_scalar":
        assert_return_type_comment,
    "tf.debugging.assert_rank":
        assert_rank_comment,
    "tf.debugging.assert_rank_at_least":
        assert_rank_comment,
    "tf.debugging.assert_rank_in":
        assert_rank_comment,
    "tf.train.exponential_decay":
        decay_function_comment,
    "tf.train.piecewise_constant_decay":
        decay_function_comment,
    "tf.train.polynomial_decay":
        decay_function_comment,
    "tf.train.natural_exp_decay":
        decay_function_comment,
    "tf.train.inverse_time_decay":
        decay_function_comment,
    "tf.train.cosine_decay":
        decay_function_comment,
    "tf.train.cosine_decay_restarts":
        decay_function_comment,
    "tf.train.linear_cosine_decay":
        decay_function_comment,
    "tf.train.noisy_linear_cosine_decay":
        decay_function_comment,
    "tf.nn.embedding_lookup":
        deprecate_partition_strategy_comment,
    "tf.nn.embedding_lookup_sparse":
        deprecate_partition_strategy_comment,
    "tf.nn.nce_loss":
        deprecate_partition_strategy_comment,
    "tf.nn.safe_embedding_lookup_sparse":
        deprecate_partition_strategy_comment,
    "tf.nn.sampled_softmax_loss":
        deprecate_partition_strategy_comment,
    "tf.keras.estimator.model_to_estimator":
        (ast_edits.WARNING,
         "Estimators from <function name> will save object-based "
         "checkpoints (format used by `keras_model.save_weights` and "
         "`keras_model.load_weights`) by default in 2.0. To continue "
         "saving name-based checkpoints, set `checkpoint_format='saver'`."),
    "tf.keras.experimental.export_saved_model":
        keras_experimental_export_comment,
    "tf.keras.experimental.load_from_saved_model":
        keras_experimental_export_comment,
    "tf.keras.initializers.Zeros":
        initializers_no_dtype_comment,
    "tf.keras.initializers.zeros":
        initializers_no_dtype_comment,
    "tf.keras.initializers.Ones":
        initializers_no_dtype_comment,
    "tf.keras.initializers.ones":
        initializers_no_dtype_comment,
    "tf.keras.initializers.Constant":
        initializers_no_dtype_comment,
    "tf.keras.initializers.constant":
        initializers_no_dtype_comment,
    "tf.keras.initializers.VarianceScaling":
        initializers_no_dtype_comment,
    "tf.keras.initializers.Orthogonal":
        initializers_no_dtype_comment,
    "tf.keras.initializers.orthogonal":
        initializers_no_dtype_comment,
    "tf.keras.initializers.Identity":
        initializers_no_dtype_comment,
    "tf.keras.initializers.identity":
        initializers_no_dtype_comment,
    "tf.keras.initializers.glorot_uniform":
        initializers_no_dtype_comment,
    "tf.keras.initializers.glorot_normal":
        initializers_no_dtype_comment,
    "tf.initializers.zeros":
        initializers_no_dtype_comment,
    "tf.zeros_initializer":
        initializers_no_dtype_comment,
    "tf.initializers.ones":
        initializers_no_dtype_comment,
    "tf.ones_initializer":
        initializers_no_dtype_comment,
    "tf.initializers.constant":
        initializers_no_dtype_comment,
    "tf.constant_initializer":
        initializers_no_dtype_comment,
    "tf.initializers.random_uniform":
        initializers_no_dtype_comment,
    "tf.random_uniform_initializer":
        initializers_no_dtype_comment,
    "tf.initializers.random_normal":
        initializers_no_dtype_comment,
    "tf.random_normal_initializer":
        initializers_no_dtype_comment,
    "tf.initializers.truncated_normal":
        initializers_no_dtype_comment,
    "tf.truncated_normal_initializer":
        initializers_no_dtype_comment,
    "tf.initializers.variance_scaling":
        initializers_no_dtype_comment,
    "tf.variance_scaling_initializer":
        initializers_no_dtype_comment,
    "tf.initializers.orthogonal":
        initializers_no_dtype_comment,
    "tf.orthogonal_initializer":
        initializers_no_dtype_comment,
    "tf.initializers.identity":
        initializers_no_dtype_comment,
    "tf.glorot_uniform_initializer":
        initializers_no_dtype_comment,
    "tf.initializers.glorot_uniform":
        initializers_no_dtype_comment,
    "tf.glorot_normal_initializer":
        initializers_no_dtype_comment,
    "tf.initializers.glorot_normal":
        initializers_no_dtype_comment,
    "tf.losses.absolute_difference":
        losses_comment,
    "tf.losses.add_loss":
        losses_comment,
    "tf.losses.compute_weighted_loss":
        losses_comment,
    "tf.losses.cosine_distance":
        losses_comment,
    "tf.losses.get_losses":
        losses_comment,
    "tf.losses.get_regularization_loss":
        losses_comment,
    "tf.losses.get_regularization_losses":
        losses_comment,
    "tf.losses.get_total_loss":
        losses_comment,
    "tf.losses.hinge_loss":
        losses_comment,
    "tf.losses.huber_loss":
        losses_comment,
    "tf.losses.log_loss":
        losses_comment,
    "tf.losses.mean_pairwise_squared_error":
        losses_comment,
    "tf.losses.mean_squared_error":
        losses_comment,
    "tf.losses.sigmoid_cross_entropy":
        losses_comment,
    "tf.losses.softmax_cross_entropy":
        losses_comment,
    "tf.losses.sparse_softmax_cross_entropy":
        losses_comment,
    "tf.metrics.accuracy":
        metrics_comment,
    "tf.metrics.auc":
        metrics_comment,
    "tf.metrics.average_precision_at_k":
        metrics_comment,
    "tf.metrics.false_negatives":
        metrics_comment,
    "tf.metrics.false_negatives_at_thresholds":
        metrics_comment,
    "tf.metrics.false_positives":
        metrics_comment,
    "tf.metrics.false_positives_at_thresholds":
        metrics_comment,
    "tf.metrics.mean":
        metrics_comment,
    "tf.metrics.mean_absolute_error":
        metrics_comment,
    "tf.metrics.mean_cosine_distance":
        metrics_comment,
    "tf.metrics.mean_iou":
        metrics_comment,
    "tf.metrics.mean_per_class_accuracy":
        metrics_comment,
    "tf.metrics.mean_relative_error":
        metrics_comment,
    "tf.metrics.mean_squared_error":
        metrics_comment,
    "tf.metrics.mean_tensor":
        metrics_comment,
    "tf.metrics.percentage_below":
        metrics_comment,
    "tf.metrics.precision":
        metrics_comment,
    "tf.metrics.precision_at_k":
        metrics_comment,
    "tf.metrics.precision_at_thresholds":
        metrics_comment,
    "tf.metrics.precision_at_top_k":
        metrics_comment,
    "tf.metrics.recall":
        metrics_comment,
    "tf.metrics.recall_at_k":
        metrics_comment,
    "tf.metrics.recall_at_thresholds":
        metrics_comment,
    "tf.metrics.recall_at_top_k":
        metrics_comment,
    "tf.metrics.root_mean_squared_error":
        metrics_comment,
    "tf.metrics.sensitivity_at_specificity":
        metrics_comment,
    "tf.metrics.sparse_average_precision_at_k":
        metrics_comment,
    "tf.metrics.sparse_precision_at_k":
        metrics_comment,
    "tf.metrics.specificity_at_sensitivity":
        metrics_comment,
    "tf.metrics.true_negatives":
        metrics_comment,
    "tf.metrics.true_negatives_at_thresholds":
        metrics_comment,
    "tf.metrics.true_positives":
        metrics_comment,
    "tf.metrics.true_positives_at_thresholds":
        metrics_comment,
    "tf.get_variable":
        (ast_edits.WARNING,
         "<function name> returns ResourceVariables by default in 2.0, "
         "which have well-defined semantics and are stricter about shapes. "
         "You can disable this behavior by passing use_resource=False, or "
         "by calling tf.compat.v1.disable_resource_variables()."),
    "tf.pywrap_tensorflow":
        (ast_edits.ERROR,
         "<function name> cannot be converted automatically. "
         "`tf.pywrap_tensorflow` will not be distributed with "
         "TensorFlow 2.0, please consider an alternative in public "
         "TensorFlow APIs."),
    "tf.contrib.distribute.MirroredStrategy":
        contrib_mirrored_strategy_warning,
    "tf.distribute.MirroredStrategy":
        core_mirrored_strategy_warning,
    "tf.contrib.distribute.OneDeviceStrategy":
        contrib_one_device_strategy_warning,
    "tf.contrib.distribute.TPUStrategy":
        contrib_tpu_strategy_warning,
    "tf.contrib.distribute.CollectiveAllReduceStrategy":
        contrib_collective_strategy_warning,
    "tf.contrib.distribute.ParameterServerStrategy":
        contrib_ps_strategy_warning,
    "tf.summary.FileWriter": summary_api_comment,
    "tf.summary.FileWriterCache": summary_api_comment,
    "tf.summary.Summary": summary_api_comment,
    "tf.summary.audio": summary_api_comment,
    "tf.summary.histogram": summary_api_comment,
    "tf.summary.image": summary_api_comment,
    "tf.summary.merge": summary_api_comment,
    "tf.summary.merge_all": summary_api_comment,
    "tf.summary.scalar": summary_api_comment,
    "tf.summary.tensor_summary": summary_api_comment,
    "tf.summary.text": summary_api_comment,
    "tf.saved_model.load": saved_model_load_warning,
    "tf.saved_model.loader.load": saved_model_load_warning,
}
all_renames_v2.add_contrib_direct_import_support(self.function_warnings)

for symbol, replacement in all_renames_v2.addons_symbol_mappings.items():
    warning = (
        ast_edits.WARNING, (
            "(Manual edit required) `{}` has been migrated to `{}` in "
            "TensorFlow Addons. The API spec may have changed during the "
            "migration. Please see https://github.com/tensorflow/addons "
            "for more info.").format(symbol, replacement))
    self.function_warnings[symbol] = warning

# Warnings that are emitted only if a specific arg is found.
self.function_arg_warnings = {
    "tf.nn.conv1d": {
        ("use_cudnn_on_gpu", 4):
            (ast_edits.WARNING,
             "use_cudnn_on_gpu has been removed, behavior is now equivalent"
             "to setting it to True."),
    },
    "tf.nn.conv2d": {
        ("use_cudnn_on_gpu", 4):
            (ast_edits.WARNING,
             "use_cudnn_on_gpu has been removed, behavior is now equivalent"
             "to setting it to True."),
    },
    "tf.nn.conv2d_backprop_filter": {
        ("use_cudnn_on_gpu", 5):
            (ast_edits.WARNING,
             "use_cudnn_on_gpu has been removed, behavior is now equivalent"
             "to setting it to True."),
    },
    "tf.nn.conv2d_backprop_input": {
        ("use_cudnn_on_gpu", 5):
            (ast_edits.WARNING,
             "use_cudnn_on_gpu has been removed, behavior is now equivalent"
             "to setting it to True."),
    },
    "tf.gradients": {
        ("colocate_gradients_with_ops", 4):
            (ast_edits.INFO, "tf.gradients no longer takes "
             "'colocate_gradients_with_ops' argument, it behaves as if it "
             "was set to True."),
    },
    "tf.hessians": {
        ("colocate_gradients_with_ops", 3):
            (ast_edits.INFO, "tf.hessians no longer takes "
             "'colocate_gradients_with_ops' argument, it behaves as if it "
             "was set to True."),
    },
    "*.minimize": {
        ("colocate_gradients_with_ops", 5):
            (ast_edits.INFO, "Optimizer.minimize no longer takes "
             "'colocate_gradients_with_ops' argument, it behaves as if it "
             "was set to True."),
    },
    "*.compute_gradients": {
        ("colocate_gradients_with_ops", 4):
            (ast_edits.INFO, "Optimizer.compute_gradients no "
             "longer takes 'colocate_gradients_with_ops' argument, it "
             "behaves as if it was set to True."),
    },
    "tf.cond": {
        ("strict", 3):
            (ast_edits.WARNING,
             "tf.cond no longer takes 'strict' argument, it behaves as "
             "if was set to True.")
    },
    "tf.contrib.summary.audio": {
        ("family", 4): contrib_summary_family_arg_comment,
    },
    "tf.contrib.summary.create_file_writer": {
        ("name", 4):
            (ast_edits.WARNING,
             "tf.contrib.summary.create_file_writer() no longer supports "
             "implicit writer re-use based on shared logdirs or resource "
             "names; this call site passed a 'name' argument that has been "
             "removed. The new tf.compat.v2.summary.create_file_writer() "
             "replacement has a 'name' parameter but the semantics are "
             "the usual ones to name the op itself and do not control "
             "writer re-use; writers must be manually re-used if desired.")
    },
    "tf.contrib.summary.generic": {
        ("name", 0): (
            ast_edits.WARNING,
            "tf.contrib.summary.generic() takes a 'name' argument for the "
            "op name that also determines the emitted tag (prefixed by any "
            "active name scopes), but tf.compat.v2.summary.write(), which "
            "replaces it, separates these into 'tag' and 'name' arguments. "
            "The 'name' argument here has been converted to 'tag' to "
            "preserve a meaningful tag, but any name scopes will not be "
            "reflected in the tag without manual editing."),
        ("family", 3): contrib_summary_family_arg_comment,
    },
    "tf.contrib.summary.histogram": {
        ("family", 2): contrib_summary_family_arg_comment,
    },
    "tf.contrib.summary.image": {
        ("bad_color", 2): (
            ast_edits.WARNING,
            "tf.contrib.summary.image no longer takes the 'bad_color' "
            "argument; caller must now preprocess if needed. This call "
            "site specifies a bad_color argument so it cannot be converted "
            "safely."),
        ("family", 4): contrib_summary_family_arg_comment,
    },
    "tf.contrib.summary.scalar": {
        ("family", 2): contrib_summary_family_arg_comment,
    },
    "tf.image.resize": {
        ("align_corners", 3):
            (ast_edits.WARNING,
             "align_corners is not supported by tf.image.resize, the new "
             "default transformation is close to what v1 provided. If you "
             "require exactly the same transformation as before, use "
             "compat.v1.image.resize."),
    },
    "tf.image.resize_bilinear": {
        ("align_corners", 2):
            (ast_edits.WARNING,
             "align_corners is not supported by tf.image.resize, the new "
             "default transformation is close to what v1 provided. If you "
             "require exactly the same transformation as before, use "
             "compat.v1.image.resize_bilinear."),
    },
    "tf.image.resize_area": {
        ("align_corners", 2):
            (ast_edits.WARNING,
             "align_corners is not supported by tf.image.resize, the new "
             "default transformation is close to what v1 provided. If you "
             "require exactly the same transformation as before, use "
             "compat.v1.image.resize_area."),
    },
    "tf.image.resize_bicubic": {
        ("align_corners", 2):
            (ast_edits.WARNING,
             "align_corners is not supported by tf.image.resize, the new "
             "default transformation is close to what v1 provided. If you "
             "require exactly the same transformation as before, use "
             "compat.v1.image.resize_bicubic."),
    },
    "tf.image.resize_nearest_neighbor": {
        ("align_corners", 2):
            (ast_edits.WARNING,
             "align_corners is not supported by tf.image.resize, the new "
             "default transformation is close to what v1 provided. If you "
             "require exactly the same transformation as before, use "
             "compat.v1.image.resize_nearest_neighbor."),
    },
}
all_renames_v2.add_contrib_direct_import_support(self.function_arg_warnings)

# Specially handled functions
# Each transformer is a callable which will be called with the arguments
#   transformer(parent, node, full_name, name, logs)
# Where logs is a list to which (level, line, col, msg) tuples can be
# appended, full_name is the FQN of the function called (or None if that is
# unknown), name is the name of the function called (or None is that is
# unknown). node is an ast.Call node representing this function call, and
# parent is its parent in the AST.
# The function may modify node (but not parent), and must return
# - none, if nothing was modified
# - node, if node was modified in place (make sure to use
#   pasta.ast_utils.replace_child to swap out children, otherwise formatting
#   may get messy)
# - a replacement for node, if the whole call node was replaced. The caller
#   will take care of changing parent.
canned_estimator_msg_optimizer = (
    "tf.keras.optimizers.* only, so the call was converted to compat.v1. "
    "Please note that tf.train.Optimizers have one-to-one correspondents "
    "in tf.keras.optimizers, so you may be able to convert to the new "
    "optimizers directly (See https://www.tensorflow.org/api_docs/python"
    "/tf/keras/optimizers). Checkpoint compatibility is not guaranteed, "
    "but there is a checkpoint converter tool that you can use.")
canned_estimator_msg = (
    "no longer takes `input_layer_partitioner` arg, and it supports "
    + canned_estimator_msg_optimizer)
self.function_transformers = {
    "*.make_initializable_iterator": _iterator_transformer,
    "*.make_one_shot_iterator": _iterator_transformer,
    "tf.nn.dropout": _dropout_transformer,
    "tf.to_bfloat16": _cast_transformer,
    "tf.to_complex128": _cast_transformer,
    "tf.to_complex64": _cast_transformer,
    "tf.to_double": _cast_transformer,
    "tf.to_float": _cast_transformer,
    "tf.to_int32": _cast_transformer,
    "tf.to_int64": _cast_transformer,
    "tf.nn.softmax_cross_entropy_with_logits":
        _softmax_cross_entropy_with_logits_transformer,
    "tf.image.extract_glimpse": _extract_glimpse_transformer,
    "tf.image.resize_area": _image_resize_transformer,
    "tf.image.resize_bicubic": _image_resize_transformer,
    "tf.image.resize_bilinear": _image_resize_transformer,
    "tf.image.resize_nearest_neighbor": _image_resize_transformer,
    "tf.nn.fractional_avg_pool": _pool_seed_transformer,
    "tf.nn.fractional_max_pool": _pool_seed_transformer,
    "tf.name_scope": _name_scope_transformer,
    # TODO(b/129398290)
    # "tf.string_split": _string_split_transformer,
    "tf.strings.split": _string_split_rtype_transformer,
    "tf.estimator.BaselineEstimator":
        functools.partial(
            _rename_if_arg_found_transformer,
            arg_name="optimizer",
            message=("tf.estimator.BaselineEstimator supports "
                     + canned_estimator_msg_optimizer),
        ),
    "tf.estimator.BaselineClassifier":
        functools.partial(
            _rename_if_arg_found_and_add_loss_reduction_transformer,
            arg_names=["optimizer"],
            message=("tf.estimator.BaselineClassifier supports "
                     + canned_estimator_msg_optimizer),
        ),
    "tf.estimator.BaselineRegressor":
        functools.partial(
            _rename_if_arg_found_and_add_loss_reduction_transformer,
            arg_names=["input_layer_partitioner", "optimizer"],
            message=("tf.estimator.BaselineRegressor supports "
                     + canned_estimator_msg_optimizer),
        ),
    "tf.estimator.DNNEstimator":
        functools.partial(
            _rename_if_any_arg_found_transformer,
            arg_names=["input_layer_partitioner", "optimizer"],
            message="tf.estimator.DNNEstimator no longer takes "
            "input_layer_partitioner, so the call was converted to "
            "compat.v1."
        ),
    "tf.estimator.DNNClassifier":
        functools.partial(
            _rename_if_arg_found_and_add_loss_reduction_transformer,
            arg_names=["input_layer_partitioner", "optimizer"],
            message="tf.estimator.DNNClassifier " + canned_estimator_msg,
        ),
    "tf.estimator.DNNRegressor":
        functools.partial(
            _rename_if_arg_found_and_add_loss_reduction_transformer,
            arg_names=["input_layer_partitioner", "optimizer"],
            message="tf.estimator.DNNRegressor " + canned_estimator_msg,
        ),
    "tf.estimator.LinearEstimator":
        functools.partial(
            _rename_if_any_arg_found_transformer,
            arg_names=["input_layer_partitioner", "optimizer"],
            message="tf.estimator.LinearEstimator " + canned_estimator_msg,
        ),
    "tf.estimator.LinearClassifier":
        functools.partial(
            _rename_if_arg_found_and_add_loss_reduction_transformer,
            arg_names=["input_layer_partitioner", "optimizer"],
            message="tf.estimator.LinearClassifier " + canned_estimator_msg,
        ),
    "tf.estimator.LinearRegressor":
        functools.partial(
            _rename_if_arg_found_and_add_loss_reduction_transformer,
            arg_names=["input_layer_partitioner", "optimizer"],
            message="tf.estimator.LinearRegressor " + canned_estimator_msg,
        ),
    "tf.estimator.DNNLinearCombinedEstimator":
        functools.partial(
            _rename_if_any_arg_found_transformer,
            arg_names=[
                "input_layer_partitioner", "dnn_optimizer",
                "linear_optimizer"
            ],
            message=("tf.estimator.DNNLinearCombinedEstimator "
                     + canned_estimator_msg),
        ),
    "tf.estimator.DNNLinearCombinedClassifier":
        functools.partial(
            _rename_if_arg_found_and_add_loss_reduction_transformer,
            arg_names=[
                "input_layer_partitioner", "dnn_optimizer",
                "linear_optimizer"
            ],
            message=("tf.estimator.DNNLinearCombinedClassifier "
                     + canned_estimator_msg),
        ),
    "tf.estimator.DNNLinearCombinedRegressor":
        functools.partial(
            _rename_if_arg_found_and_add_loss_reduction_transformer,
            arg_names=[
                "input_layer_partitioner", "dnn_optimizer",
                "linear_optimizer"
            ],
            message=("tf.estimator.DNNLinearCombinedRegressor "
                     + canned_estimator_msg),
        ),
    "tf.device": functools.partial(
        _rename_if_arg_found_transformer, arg_name="device_name",
        arg_ok_predicate=_is_ast_str, remove_if_ok=False,
        message="tf.device no longer takes functions as an argument. "
        "We could not determine that the argument value is a string, so "
        "the call was converted to compat.v1."),
    "tf.zeros_like": functools.partial(
        _rename_if_arg_found_transformer, arg_name="optimize",
        arg_ok_predicate=_is_ast_true, remove_if_ok=True,
        message="tf.zeros_like no longer takes an optimize argument, and "
        "behaves as if optimize=True. This call site specifies something "
        "other than optimize=True, so it was converted to compat.v1."),
    "tf.ones_like": functools.partial(
        _rename_if_arg_found_transformer, arg_name="optimize",
        arg_ok_predicate=_is_ast_true, remove_if_ok=True,
        message="tf.ones_like no longer takes an optimize argument, and "
        "behaves as if optimize=True. This call site specifies something "
        "other than optimize=True, so it was converted to compat.v1."),
    "tf.while_loop": functools.partial(
        _rename_if_arg_found_transformer,
        arg_name="return_same_structure",
        arg_ok_predicate=_is_ast_true, remove_if_ok=True,
        message="tf.while_loop no longer takes 'return_same_structure' "
        "argument and behaves as if return_same_structure=True. This call "
        "site specifies something other than return_same_structure=True, "
        "so it was converted to compat.v1."),
    "tf.nn.ctc_beam_search_decoder": functools.partial(
        _rename_if_arg_found_transformer,
        arg_name="merge_repeated",
        arg_ok_predicate=_is_ast_false, remove_if_ok=True,
        message="tf.nn.ctc_beam_search_decoder no longer takes the "
        "'merge_repeated' argument and behaves as if merge_repeated=False. "
        "This call site specifies something other than "
        "merge_repeated=False, so it was converted to compat.v1."),
    "tf.nn.dilation2d": functools.partial(
        _add_argument_transformer,
        arg_name="data_format",
        arg_value_ast=ast.Str("NHWC")),
    "tf.nn.erosion2d": functools.partial(
        _add_argument_transformer,
        arg_name="data_format",
        arg_value_ast=ast.Str("NHWC")),
    "tf.contrib.summary.always_record_summaries": functools.partial(
        _add_summary_recording_cond_transformer, cond="True"),
    "tf.contrib.summary.audio": _add_summary_step_transformer,
    "tf.contrib.summary.generic": _add_summary_step_transformer,
    "tf.contrib.summary.histogram": _add_summary_step_transformer,
    "tf.contrib.summary.image": _add_summary_step_transformer,
    "tf.contrib.summary.never_record_summaries": functools.partial(
        _add_summary_recording_cond_transformer, cond="False"),
    "tf.contrib.summary.scalar": _add_summary_step_transformer,
    "tf.contrib.layers.l1_regularizer":
        _contrib_layers_l1_regularizer_transformer,
    "tf.contrib.layers.l2_regularizer":
        _contrib_layers_l2_regularizer_transformer,
    "tf.contrib.layers.xavier_initializer":
        _contrib_layers_xavier_initializer_transformer,
    "tf.contrib.layers.xavier_initializer_conv2d":
        _contrib_layers_xavier_initializer_transformer,
    "tf.contrib.layers.variance_scaling_initializer":
        _contrib_layers_variance_scaling_initializer_transformer,
    "tf.initializers.uniform_unit_scaling":
        _add_uniform_scaling_initializer_transformer,
    "tf.uniform_unit_scaling_initializer":
        _add_uniform_scaling_initializer_transformer,
    "slim.l1_regularizer":
        _contrib_layers_l1_regularizer_transformer,
    "slim.l2_regularizer":
        _contrib_layers_l2_regularizer_transformer,
    "slim.xavier_initializer":
        _contrib_layers_xavier_initializer_transformer,
    "slim.xavier_initializer_conv2d":
        _contrib_layers_xavier_initializer_transformer,
    "slim.variance_scaling_initializer":
        _contrib_layers_variance_scaling_initializer_transformer,
    "tf.keras.models.save_model": functools.partial(
        _add_argument_transformer,
        arg_name="save_format",
        arg_value_ast=ast.Str("h5")),
}
all_renames_v2.add_contrib_direct_import_support(self.function_transformers)

self.module_deprecations = module_deprecations_v2.MODULE_DEPRECATIONS
