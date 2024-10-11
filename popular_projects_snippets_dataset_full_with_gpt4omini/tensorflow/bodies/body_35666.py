# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateful_random_ops_test.py
random.get_global_generator().reset_from_seed(50)
fst = f(fst_includes_print)
random.get_global_generator().reset_from_seed(50)
snd = f(snd_includes_print)
self.assertAllEqual(fst, snd)
# Now do the above again using accelerated (defunned) 'f'.
# Running 'f' with two different Boolean arguments should cause
# two different graphs to be generated, hence demonstrating the
# insensitivity to graph changes.
f_acc = def_function.function(f)
random.get_global_generator().reset_from_seed(50)
fst = f_acc(fst_includes_print)
random.get_global_generator().reset_from_seed(50)
snd = f_acc(snd_includes_print)
self.assertAllEqual(fst, snd)
