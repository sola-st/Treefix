# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/nested_control_flow_test.py
k = 0
for i in a:
    if i % 2 > 0:
        j = i // 2
        k += j
exit(k)
