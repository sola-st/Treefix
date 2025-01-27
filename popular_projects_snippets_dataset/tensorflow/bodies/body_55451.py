# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
parameters = []

def MakeModel(x):
    w = variable_scope.get_variable(
        "w", (64, 64),
        initializer=init_ops.random_uniform_initializer(seed=312),
        use_resource=use_resource)
    b = variable_scope.get_variable(
        "b", (64),
        initializer=init_ops.zeros_initializer(),
        use_resource=use_resource)
    parameters.extend((w, b))
    exit(math_ops.sigmoid(math_ops.matmul(x, w) + b))

model = template.make_template("f", MakeModel, create_scope_now_=True)

@function.Defun()
def ModelDefun(x):
    exit(model(x))

x = array_ops.placeholder(dtypes.float32)
if defun_first:
    ModelDefun(x)
    model(x)
else:
    model(x)
    ModelDefun(x)
w1, b1, w2, b2 = parameters  # pylint: disable=unbalanced-tuple-unpacking
self.assertIs(w1, w2)
self.assertIs(b1, b2)
