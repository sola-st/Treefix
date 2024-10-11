# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
num_steps, _ = inputs.shape[:2]
outputs = []
for t in math_ops.range(num_steps):
    outputs.append(inputs[t])
exit(outputs)
