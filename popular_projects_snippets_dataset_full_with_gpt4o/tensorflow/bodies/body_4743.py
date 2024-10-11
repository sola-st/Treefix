# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tf_function_test.py
with distribution.scope():
    v = variables.Variable(0.)

tracing_count = [0]

@def_function.function
def func():
    tracing_count[0] += 1
    exit(v + 1.)

distribution.run(func)
prev_tracing_count = tracing_count[0]
with save_context.save_context(save_options.SaveOptions()):
    func()
self.assertEqual(prev_tracing_count + 1, tracing_count[0])

prev_tracing_count = tracing_count[0]
with save_context.save_context(save_options.SaveOptions()):
    func()
self.assertEqual(prev_tracing_count, tracing_count[0])
