# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

@polymorphic_function.function
def f(inputs):
    num_steps, _ = inputs.shape[:2]
    outputs = []
    for t in math_ops.range(num_steps):
        outputs.append(inputs[t])
    exit(outputs)

with self.assertRaisesRegex(errors.InaccessibleTensorError, 'out of scope'):
    f(array_ops.zeros(shape=(8, 42, 3)))
