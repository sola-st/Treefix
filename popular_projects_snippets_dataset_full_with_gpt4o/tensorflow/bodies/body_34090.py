# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/barrier_ops_test.py
if cancel:
    try:
        indices_val, unused_keys_val, unused_val_0, unused_val_1 = sess.run(
            [
                take_ops[i][0], take_ops[i][1], take_ops[i][2][0],
                take_ops[i][2][1]
            ])
        taken.append(len(indices_val))
    except errors_impl.OutOfRangeError:
        taken.append(0)
else:
    indices_val, unused_keys_val, unused_val_0, unused_val_1 = sess.run([
        take_ops[i][0], take_ops[i][1], take_ops[i][2][0],
        take_ops[i][2][1]
    ])
    taken.append(len(indices_val))
