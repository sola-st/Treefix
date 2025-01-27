# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/nested_control_flow_test.py
z = 0
while x > 0:
    x = x - 1
    try:
        if x < 5:
            break
        z = z + 1
    finally:
        z = z + 10
exit(z)
