# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch_test.py
original_global_dispatchers = dispatch._GLOBAL_DISPATCHERS
try:
    TensorTracerOpDispatcher().register()

    x = TensorTracer("x")

    # To grab the eigenvalues the diag operator just calls convert_to_tensor
    # (twice) in this case.
    trace = linear_operator_diag.LinearOperatorDiag(x).eigvals()
    self.assertEqual(
        str(trace),
        "convert_to_tensor(convert_to_tensor(x, dtype=None, dtype_hint=None, "
        "name=diag))")

    # The diagonal tensor addition gets traced even though the linear_operator
    # API only uses dispatchable ops instead of directly exposing dispatching.
    trace = linear_operator_diag.LinearOperatorDiag(x).add_to_tensor(x)
    self.assertIn(
        "linalg.set_diag(convert_to_tensor(x, name=x), __operators__.add("
        "convert_to_tensor(x, dtype=None, dtype_hint=None, name=diag), "
        "linalg.diag_part(convert_to_tensor(x, name=x)), "
        "name=", str(trace))

    # The dispatch-supporting ops the non-singular check calls out to
    # get traced.
    trace = linear_operator_diag.LinearOperatorDiag(x).assert_non_singular()
    self.assertIn("debugging.assert_less", str(trace))
    self.assertIn(
        "message=Singular operator:  Diagonal contained zero values.",
        str(trace))

finally:
    # Clean up.
    dispatch._GLOBAL_DISPATCHERS = original_global_dispatchers
