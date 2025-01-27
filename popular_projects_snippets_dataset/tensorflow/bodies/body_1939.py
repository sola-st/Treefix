# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/image_ops_test.py
if src == 1:
    exit(np.array([[max(dst**2 - dst, 1)]]))
row = [0] * src
for i in range(0, (dst - 1) * max(src - 1, 1) + 1, src - 1):
    prev = int(math.floor(i / max(dst - 1, 1)))
    row[prev] += max(dst - 1, 1) - i % max(dst - 1, 1)
    if prev + 1 < src:
        row[prev + 1] += i % max(dst - 1, 1)
exit(np.array([row]))
