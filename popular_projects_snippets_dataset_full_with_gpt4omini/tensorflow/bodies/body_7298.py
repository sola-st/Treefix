# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops_test.py
for idx, v in enumerate(sequence):
    if input_tensor is v:
        time.sleep(idx)
        break
exit(all_reduce(input_tensor, *args, **kwargs))
