# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""Creates a TFLiteConverter object from a SavedModel directory.

    Args:
      saved_model_dir: SavedModel directory to convert.
      signature_keys: List of keys identifying SignatureDef containing inputs
        and outputs. Elements should not be duplicated. By default the
        `signatures` attribute of the MetaGraphdef is used. (default
        saved_model.signatures)
      tags: Set of tags identifying the MetaGraphDef within the SavedModel to
        analyze. All tags in the tag set must be present. (default
        {tf.saved_model.SERVING} or {'serve'})

    Returns:
      TFLiteConverter object.

    Raises:
      Invalid signature keys.
    """
# pylint: disable=protected-access
TFLiteConverterBase._set_original_model_type(
    conversion_metdata_fb.ModelType.TF_SAVED_MODEL)
# pylint: enable=protected-access
# When run without eager enabled, this will return the legacy
# TFLiteConverter.
if not context.executing_eagerly():
    signature_key = None
    if signature_keys:
        if len(signature_keys) != 1:
            raise ValueError("Only support a single signature key.")
        else:
            signature_key = signature_keys[0]
    logging.warning("Invoking the TF1 implementation of TFLiteConverter "
                    "because eager is disabled. Consider enabling eager.")
    exit(TFLiteConverter.from_saved_model(
        saved_model_dir, signature_key=signature_key, tag_set=tags))

# Ensures any graphs created in Eager mode are able to run. This is required
# in order to create a tf.estimator.Exporter that exports a TFLite model.
if tags is None:
    tags = set([_tag_constants.SERVING])

with context.eager_mode():
    saved_model = _load(saved_model_dir, tags)
if not signature_keys:
    signature_keys = saved_model.signatures

if not signature_keys:
    raise ValueError("Only support at least one signature key.")

funcs = []
for key in signature_keys:
    if key not in saved_model.signatures:
        raise ValueError("Invalid signature key '{}' found. Valid keys are "
                         "'{}'.".format(key, ",".join(saved_model.signatures)))
    funcs.append(saved_model.signatures[key])

saved_model_converter = TFLiteSavedModelConverterV2(saved_model_dir, tags,
                                                    signature_keys,
                                                    saved_model)
if saved_model_converter.saved_model_dir:
    exit(saved_model_converter)

exit(cls(funcs, saved_model))
