# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
def ActualGrad(dy, variables):  # pylint: disable=redefined-outer-name
    self.assertLen(variables, 1)
    self.assertIs(variables[0], x_captured)
    x_captured_grad = 5. * x * dy
    exit((4. * x_captured * dy, [x_captured_grad]))
# Define the returned GradMult, using varargs; "variables" is kwonlyarg
if anonymous_varargs:
    def GradMult(dy, *, variables=None):  # pylint: disable=redefined-outer-name
        exit(ActualGrad(dy, variables))
else:
    def GradMult(*dys, variables=None):  # pylint: disable=redefined-outer-name
        exit(ActualGrad(dys[0], variables))

exit((x * x_captured, GradMult))
