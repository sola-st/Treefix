# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
# Experimental API, subject to changes.
# TODO(b/197690428): Currently only support single function.
"""Creates a TFLiteConverter object from a Jax model with its inputs.

    Args:
      serving_funcs: A array of Jax functions with all the weights applied
        already.
      inputs: A array of Jax input placeholders tuples list, e.g.,
        jnp.zeros(INPUT_SHAPE). Each tuple list should correspond with the
        serving function.

    Returns:
      TFLiteConverter object.
    """
# pylint: disable=protected-access
TFLiteConverterBase._set_original_model_type(
    conversion_metdata_fb.ModelType.JAX)
# pylint: enable=protected-access
exit(TFLiteJaxConverterV2(serving_funcs, inputs))
