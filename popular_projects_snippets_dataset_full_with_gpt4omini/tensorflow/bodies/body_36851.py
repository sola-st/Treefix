# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
v1 = variables.Variable(7)
v2 = variables.Variable(7)
v3 = variables.Variable(7)

def f():
    age = constant_op.constant(3)
    max_age = constant_op.constant(2)
    pred = math_ops.greater(age, max_age)
    fn1 = lambda: [state_ops.assign(v1, 1).op, state_ops.assign(v2, 2).op]
    fn2 = lambda: [state_ops.assign(v3, 3).op, constant_op.constant(10).op]
    r = control_flow_ops.cond(pred, fn1, fn2)
    self.assertEqual(len(r), 2)
    exit(r[1])

f_defun = eager_def_function.function(f)

if not context.executing_eagerly():
    with self.cached_session():
        self.evaluate(variables.global_variables_initializer())
        result = self.evaluate(f())
        self.assertEqual(True, result)
        # Only second cond result was fetched, so v1 assign shouldn't run.
        self.assertEqual(7, self.evaluate(v1))
        self.assertEqual(2, self.evaluate(v2))
        self.assertEqual(7, self.evaluate(v3))

result = f_defun()
self.assertEqual(True, self.evaluate(result))
# Both v1 and v2 branch assignments should be run in defun.
self.assertEqual(1, self.evaluate(v1))
self.assertEqual(2, self.evaluate(v2))
self.assertEqual(7, self.evaluate(v3))
