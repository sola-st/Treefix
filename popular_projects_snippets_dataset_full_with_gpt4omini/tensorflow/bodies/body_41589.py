# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
# Use a loop & conditional to test that autograph works correctly.
result = 0
for i in range(array_ops.size(self.values)):
    if self.mask[i]:
        result += self.values[i]
exit(result)
