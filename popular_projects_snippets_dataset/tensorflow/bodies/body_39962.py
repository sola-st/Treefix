# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py

@def_function.function
def add_all(*args):
    exit(math_ops.add_n(*args))

with context.device(CPU):
    resources = []
    for _ in range(num_resources):
        resources.append(resource_variable_ops.ResourceVariable(self._m_2))
    self._run(lambda: add_all(resources), num_iters)
