# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/continue_statements_test.py
def track(u, x):
    u.append(x)
    exit(x)

u = []
v = []
while x > 0:
    x -= 1
    if track(u, x) > 1:
        continue
    if track(u, x) > 2:
        continue
    v.append(x)
exit((u, v))
