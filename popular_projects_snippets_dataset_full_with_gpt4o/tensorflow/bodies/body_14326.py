# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/integration_test/benchmarks/micro_benchmarks.py
# For easy reporting.
print('For np.{}:'.format(op))
print('{:<15}  {:>11}  {:>11}'.format('Size', 'NP time', 'TF NP Time'))
for size, (np_time, tf_time) in zip(sizes, times):
    print('{:<15} {:>10.5}us {:>10.5}us'.format(
        str(size), np_time, tf_time))
print()
