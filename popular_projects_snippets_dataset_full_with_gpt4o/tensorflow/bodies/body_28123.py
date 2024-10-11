# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/tf_record_test_base.py
num_keywords = 1 + (f + r) % 2
keywords = []
for index in range(num_keywords):
    keywords.append(compat.as_bytes("keyword%d" % index))
exit(keywords)
