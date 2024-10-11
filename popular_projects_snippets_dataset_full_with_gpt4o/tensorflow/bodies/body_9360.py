# Extracted from ./data/repos/tensorflow/tensorflow/python/types/trace.py
"""Creates a placeholder for tracing.

    tf.funcion traces with the placeholder value rather than the actual value.
    For example, a placeholder value can represent multiple different
    actual values. This means that the trace generated with that placeholder
    value is more general and reusable which saves expensive retracing.

    Args:
      placeholder_context: A `PlaceholderContext` container for context
                           information when creating a placeholder value.

    For the `Fruit` example shared above, implementing:

    ```python
    class FruitTraceType:
      def placeholder_value(self, placeholder_context=None):
        return Fruit()
    ```
    instructs tf.function to trace with the `Fruit()` objects
    instead of the actual `Apple()` and `Mango()` objects when it receives a
    call to `get_mixed_flavor(Apple(), Mango())`. For example, Tensor arguments
    are replaced with Tensors of similar shape and dtype, output from
    a tf.Placeholder op.

    More generally, placeholder values are the arguments of a tf.function,
    as seen from the function's body:
    ```python
    @tf.function
    def foo(x):
      # Here `x` is be the placeholder value
      ...

    foo(x) # Here `x` is the actual value
    ```
    """
