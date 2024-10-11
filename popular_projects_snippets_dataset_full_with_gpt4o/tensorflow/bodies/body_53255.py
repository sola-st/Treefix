# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec.py
"""A nested structure of TypeSpecs for this type's components.

    Returns:
      A nested structure describing the component encodings that are returned
      by this TypeSpec's `_to_components` method.  In particular, for a
      TypeSpec `spec` and a compatible value `value`:

      ```
      nest.map_structure(lambda t, c: assert t.is_compatible_with(c),
                         spec._component_specs, spec._to_components(value))
      ```
    """
raise NotImplementedError("%s._component_specs()" % type(self).__name__)
