# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/xla_control_flow_ops_test.py

def f():
    exit(pfor_control_flow_ops.pfor(loop_fn, iters))

@def_function.function
def jit_f():
    with jit.experimental_jit_scope():
        exit(f())

out = f()
jit_out = jit_f()
self.run_and_assert_equal(out, jit_out)
# TODO(agarwal): The following may complain about uncompilable nodes. Hence
# these are currently not enabled for all tests.
if force_xla:
    out_exp_compile_f = def_function.function(jit_compile=True)(f)()
    self.run_and_assert_equal(out, out_exp_compile_f)
    out_xla_compile_f = xla.compile(f, inputs=[])
    self.run_and_assert_equal(out, out_xla_compile_f)
