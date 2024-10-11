# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""EXPERIMENTAL: A context manager for setting kernel labels.

    This context manager can be used to select particular
    implementations of kernels within the scope of the context.

    For example:

        with ops.Graph().as_default() as g:
          f_1 = Foo()  # Uses the default registered kernel for the Foo op.
          with g.kernel_label_map({"Foo": "v_2"}):
            f_2 = Foo()  # Uses the registered kernel with label "v_2"
                         # for the Foo op.
            with g.kernel_label_map({"Foo": "v_3"}):
              f_3 = Foo()  # Uses the registered kernel with label "v_3"
                           # for the Foo op.
              with g.kernel_label_map({"Foo": ""}):
                f_4 = Foo()  # Uses the default registered kernel
                             # for the Foo op.

    Args:
      op_to_kernel_label_map: A dictionary mapping op type strings to kernel
        label strings.

    Returns:
      A context manager that sets the kernel label to be used for one or more
      ops created in that context.

    Raises:
      TypeError: If op_to_kernel_label_map is not a dictionary mapping
        strings to strings.
    """
if not isinstance(op_to_kernel_label_map, dict):
    raise TypeError("op_to_kernel_label_map must be a dictionary mapping "
                    "strings to strings")
# The saved_labels dictionary stores any currently-set labels that
# will be overridden by this context manager.
saved_labels = {}
# Install the given label
for op_type, label in op_to_kernel_label_map.items():
    if not (isinstance(op_type, str) and
            isinstance(label, str)):
        raise TypeError("op_to_kernel_label_map must be a dictionary mapping "
                        "strings to strings")
    try:
        saved_labels[op_type] = self._op_to_kernel_label_map[op_type]
    except KeyError:
        pass
    self._op_to_kernel_label_map[op_type] = label
try:
    exit()  # The code within the context runs here.
finally:
    # Remove the labels set for this context, and restore any saved labels.
    for op_type, label in op_to_kernel_label_map.items():
        try:
            self._op_to_kernel_label_map[op_type] = saved_labels[op_type]
        except KeyError:
            del self._op_to_kernel_label_map[op_type]
