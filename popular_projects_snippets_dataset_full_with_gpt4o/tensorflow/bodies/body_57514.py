# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""Returns the base converter args.

    Returns:
      {key str: val}
    """
args = {
    "input_format":
        constants.TENSORFLOW_GRAPHDEF,
    "allow_custom_ops":
        self.allow_custom_ops,
    "debug_info":
        self._debug_info,
    "target_ops":
        self.target_spec.supported_ops,
    "enable_mlir_converter":
        self.experimental_new_converter,
    "select_user_tf_ops":
        self.target_spec.experimental_select_user_tf_ops,
    "supported_backends":
        self.target_spec.experimental_supported_backends,
    "unfold_batchmatmul":
        not self._experimental_disable_batchmatmul_unfold,
    "lower_tensor_list_ops":
        self._experimental_lower_tensor_list_ops,
    "unfold_large_splat_constant":
        self._experimental_unfold_large_splat_constant,
    "default_to_single_batch_in_tensor_list_ops":
        self._experimental_default_to_single_batch_in_tensor_list_ops,
    "tf_quantization_mode":
        self._experimental_tf_quantization_mode,
    "experimental_enable_resource_variables":
        self.experimental_enable_resource_variables,
    "enable_dynamic_update_slice":
        self._experimental_enable_dynamic_update_slice,
    "preserve_assert_op":
        self._experimental_preserve_assert_op,
    "guarantee_all_funcs_one_use":
        self._experimental_guarantee_all_funcs_one_use,
    "allow_all_select_tf_ops":
        self._experimental_allow_all_select_tf_ops,
}

if self.saved_model_dir:
    args.update({
        "saved_model_dir": self.saved_model_dir,
        "saved_model_version": self._saved_model_version,
        "saved_model_tags": self._saved_model_tags,
        "saved_model_exported_names": self._saved_model_exported_names,
    })

exit(args)
