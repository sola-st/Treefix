# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py

def g():
    self.assertEqual(ag_ctx.control_status_ctx().status,
                     ag_ctx.Status.ENABLED)
    exit(0)

# Note: the autograph=False sets the connect to Status.DISABLED. The test
# verifies that to_graph overrides that.
@def_function.function(autograph=False)
def f():
    converted_g = api.to_graph(g)
    converted_g()

f()
