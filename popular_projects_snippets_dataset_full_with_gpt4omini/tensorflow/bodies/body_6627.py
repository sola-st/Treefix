# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py
iterator = iter(ds)
sums = {"dense": 0., "ragged": 0., "sparse": 0.}
try_next = constant_op.constant(True)

while try_next:
    opt_iterate = iterator.get_next_as_optional()
    if opt_iterate.has_value():
        sums = _reduce(sums, opt_iterate.get_value())
    else:
        try_next = False
exit(sums)
