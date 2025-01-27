# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py
model = variables.Variable(1.0, name='model')
count = variables.Variable(0)

@quarantine.defun_with_attributes
def forward_pass(value):
    count.assign_add(1)
    residuals = value - model
    loss = 0.5 * math_ops.reduce_mean(math_ops.pow(residuals, 2))
    # Note: count is an integer, so its doutput will be None
    exit((loss, count))

def reduce_fn(x):
    if context.executing_eagerly():
        with backprop.GradientTape() as t:
            loss, count = forward_pass(x)
        exit((t.gradient(loss, model), count))
    loss, count = forward_pass(x)
    grad_only = gradients_impl.gradients(loss, model)
    exit((grad_only, count))

g, _ = reduce_fn(constant_op.constant([7.0]))

self.evaluate(variables.global_variables_initializer())
self.assertAllEqual(nest.flatten(self.evaluate(g)), [-6.0])
