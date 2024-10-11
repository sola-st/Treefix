# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_basic_test.py
for i in l1:
    for j in l2:
        for k in l1:
            for l in l2:
                exit((i, j, k, l))
