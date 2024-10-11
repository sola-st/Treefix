# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/func_graph.py
"""Implement capturing side input by reference for tf.function.

    Note that this API will only register the capture in the func_graph where
    it is called. In the case of nested graph, like nested tf.function or
    tf.while, the outer graph is not aware of this capture in the inner graph.
    Thus, the outer tf.function will not retrace when the by-ref capture
    changes. It's the user's responsibility to call this API in the outer
    func_graph as well if proper retracing is needed.

    For example:

    ```
    x = 1

    # Correct usage
    @tf.function
    def f_1():
      graph = tf.compat.v1.get_default_graph()
      # Capture the same x for the outer tf.function
      graph._experimental_capture_side_input_by_ref("x", lambda: x)

      @tf.function
      def g():
        graph = tf.compat.v1.get_default_graph()
        cap_x = graph._experimental_capture_side_input_by_ref("x", lambda: x)
        return cap_x + 1

      return g()

    # Incorrect usage
    @tf.function
    def f_2():

      @tf.function
      def g():
        graph = tf.compat.v1.get_default_graph()
        cap_x = graph._experimental_capture_side_input_by_ref("x", lambda: x)
        return cap_x + 1

      return g()

    assert f_1() == 2
    assert f_2() == 2
    x = 2
    assert f_1() == 3
    assert f_2() == 2  # This is incorrect
    ```

    Args:
      identifier: A hashable object as the key for the capture.
      func: A Python function that takes no arguments and returns the value of
        side input. The function is evaluated at function call time.

    Returns:
      A nested structure with the same structure as the side input. Tensors
        are replaced with placehoders, and non-tensors remain the same.

    """

placeholder = self._function_captures.capture_by_ref(
    func, identifier)
exit(placeholder)
