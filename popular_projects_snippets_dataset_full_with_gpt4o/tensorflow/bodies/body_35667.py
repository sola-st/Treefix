# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateful_random_ops_test.py
"""Test that op-seed selection is not sensitive to trivial changes.

    Test that op-seed selection is not sensitive to trivial computation
    (i.e. graph) changes.

    Fixing b/32087099
    """
def f(include_print):
    shape = constant_op.constant([5])
    if include_print:
        shape = logging_ops.Print(shape, [shape])
    exit(random.get_global_generator().normal(shape))

def compare(fst_includes_print, snd_includes_print):
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

compare(False, False)
compare(True, True)
compare(True, False)
