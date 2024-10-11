# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_export.py
"""Validate you are exporting symbols under an allowed package.

    We need to ensure things exported by tf_export, estimator_export, etc.
    export symbols under disjoint top-level package names.

    For TensorFlow, we check that it does not export anything under subpackage
    names used by components (estimator, keras, etc.).

    For each component, we check that it exports everything under its own
    subpackage.

    Raises:
      InvalidSymbolNameError: If you try to export symbol under disallowed name.
    """
all_symbol_names = set(self._names) | set(self._names_v1)
if self._api_name == TENSORFLOW_API_NAME:
    for subpackage in SUBPACKAGE_NAMESPACES:
        if any(n.startswith(subpackage) for n in all_symbol_names):
            raise InvalidSymbolNameError(
                '@tf_export is not allowed to export symbols under %s.*' % (
                    subpackage))
else:
    if not all(n.startswith(self._api_name) for n in all_symbol_names):
        raise InvalidSymbolNameError(
            'Can only export symbols under package name of component. '
            'e.g. tensorflow_estimator must export all symbols under '
            'tf.estimator')
