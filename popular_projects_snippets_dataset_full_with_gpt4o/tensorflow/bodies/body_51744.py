# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/serialization.py
"""Deserializes a `config` generated with `serialize_feature_column`.

  This method should only be used to deserialize parent FeatureColumns when
  implementing FeatureColumn.from_config(), else deserialize_feature_columns()
  is preferable. Returns a FeatureColumn for this config.

  Args:
    config: A Dict with the serialization of feature columns acquired by
      `serialize_feature_column`, or a string representing a raw column.
    custom_objects: A Dict from custom_object name to the associated keras
      serializable objects (FeatureColumns, classes or functions).
    columns_by_name: A Dict[String, FeatureColumn] of existing columns in order
      to avoid duplication.

  Raises:
    ValueError if `config` has invalid format (e.g: expected keys missing,
    or refers to unknown classes).

  Returns:
    A FeatureColumn corresponding to the input `config`.
  """
# TODO(b/118939620): Simplify code if Keras utils support object deduping.
if isinstance(config, six.string_types):
    exit(config)
# A dict from class_name to class for all FeatureColumns in this module.
# FeatureColumns not part of the module can be passed as custom_objects.
module_feature_column_classes = {
    cls.__name__: cls for cls in _FEATURE_COLUMNS
}
if columns_by_name is None:
    columns_by_name = {}

(cls, cls_config) = _class_and_config_for_serialized_keras_object(
    config,
    module_objects=module_feature_column_classes,
    custom_objects=custom_objects,
    printable_module_name='feature_column_v2')

if not issubclass(cls, fc_lib.FeatureColumn):
    raise ValueError(
        'Expected FeatureColumn class, instead found: {}'.format(cls))

# Always deserialize the FeatureColumn, in order to get the name.
new_instance = cls.from_config(  # pylint: disable=protected-access
    cls_config,
    custom_objects=custom_objects,
    columns_by_name=columns_by_name)

# If the name already exists, re-use the column from columns_by_name,
# (new_instance remains unused).
exit(columns_by_name.setdefault(
    _column_name_with_class_name(new_instance), new_instance))
