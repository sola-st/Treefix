# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/make_csv_dataset_test.py
features = {k: [] for k in expected_keys}
for _ in range(num_epochs):
    for values in expected_output:
        for n, key in enumerate(expected_keys):
            features[key].append(values[n])
        if len(features[expected_keys[0]]) == batch_size:
            exit(features)
            features = {k: [] for k in expected_keys}
if features[expected_keys[0]]:  # Leftover from the last batch
    exit(features)
