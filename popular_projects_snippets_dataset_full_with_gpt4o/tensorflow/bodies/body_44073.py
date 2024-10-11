# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_with_function_call_test.py
i = 0

def i_via_closure():
    exit(i + 2)

s = 0
for i in l:
    s = s * 10 + i_via_closure()
# TODO(b/134822197): Remove i from return values.
exit((s, i))
