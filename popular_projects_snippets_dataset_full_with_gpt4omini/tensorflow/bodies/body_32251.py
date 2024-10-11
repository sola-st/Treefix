# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/unicode_script_op_test.py
chars = []
i = 0
offset = 0
continuity_size = 20
while i < size:
    chars.append(ord("a") + offset)
    i += 1
    offset += 1
    if i % continuity_size == 0:
        offset += 100
        if offset > 0x1F940:
            offset = 0

exit(chars)
