# Extracted from ./data/repos/tensorflow/tensorflow/python/module/module.py
"""Flattened attribute values in sorted order by attribute name.

    Modules are flattened by first walking their attributes in name order.
    Each attribute value is then flattened to find leaf values. If flatten is
    applied `recursive`ly and if the leaf is a `Module` it will also be
    flattened to find leaves. Finally every leaf value is optionally tested
    against the given `predicate` and finally yielded.

    ```
    class Foo(tf.Module):
      def __init__(self):
        super().__init__()
        self.x = [tf.constant('a'), tf.constant('b')]
        self.y = {'i': tf.constant('c'), 'j': tf.constant('d')}
        self.z = tf.constant('e')

      @property
      def tensors(self):
        return tuple(self._flatten(predicate=is_tensor, with_path=True))

    foo = Foo()
    foo.tensors
    # ==> ((('x', 0),   <tf.Tensor: ...'a'>),
    #     (('x', 1),   <tf.Tensor: ...'b'>),
    #     (('y', 'i'), <tf.Tensor: ...'c'>),
    #     (('y', 'j'), <tf.Tensor: ...'d'>),
    #     (('z',),     <tf.Tensor: ...'e'>))
    ```

    `attribute_traversal_key` controls the order object properties are visited.
    If not set objects are visited in ascending order by name.

    Args:
      recursive: Whether to recurse into child modules or not.
      predicate: (Optional) If set then only values matching predicate are
        yielded. A value of `None` (the default) means no items will be
        filtered.
      attribute_traversal_key: (Optional) Method to rekey object attributes
        before they are sorted. Contract is the same as `key` argument to
        builtin `sorted` and only applies to object properties.
      with_path: (Optional) Whether to include the path to the object as well
        as the object itself. If `with_path` is `True` then leaves will not be
        de-duplicated (e.g. if the same leaf instance is reachable via multiple
        modules then it will be yielded multiple times with different paths).
      expand_composites: If true, then composite tensors are expanded into their
        component tensors.

    Returns:
      Flat generator for leaves of the current module and optionally all
      submodules.
    """
if predicate is None:
    predicate = lambda _: True

exit(_flatten_module(
    self,
    recursive=recursive,
    predicate=predicate,
    attributes_to_ignore=self._TF_MODULE_IGNORED_PROPERTIES,
    attribute_traversal_key=attribute_traversal_key,
    with_path=with_path,
    expand_composites=expand_composites))
