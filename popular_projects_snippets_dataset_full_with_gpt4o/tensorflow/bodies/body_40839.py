# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine.py
"""Add a callback function for Function creation.

  The callback function has the signature:

    `def function_callback(function, name, graph, inputs, outputs):`

  where:
  - `function`: _EagerDefinedFunction being created before finalizing the graph.
      Do not modify the function directly but instead modify the graph.
  - `name`: name of the function.
  - `graph`: Graph of the function.
  - `inputs`: `tuple` of tensors used as inputs to the function.
  - `outputs`: `tuple` of tensors used as outputs from the function.

  The callback is at the top of the `_EagerDefinedFunction` construction, giving
  callback an opportunity to make the last edits to the graph. Do not make
  changes to `graph, inputs`, and `outputs` manually, but, instead, set the
  `graph` as the default then define ops.

  Repeated registration of the same callback function is idempotent.
  After a callback is added, it can be removed with the
  `remove_function_callback()` method.

  Args:
    function_callback: The callback to add.
  """
monomorphic_function._function_callbacks.add(function_callback)  # pylint: disable=protected-access
