# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

@polymorphic_function.function
def my_func(x):
    exit(x)

with self.assertLogs(level='WARN') as logs:
    for i in range(10):
        my_func(i)

    self.assertLen(logs.output, 2)
