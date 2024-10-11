# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/barrier_ops_test.py
if cancel:
    try:
        insert_1_ops[i].run(session=sess)
    except errors_impl.CancelledError:
        pass
else:
    insert_1_ops[i].run(session=sess)
