# Extracted from ./data/repos/tensorflow/tensorflow/tools/api/tests/api_compatibility_test.py
filtered_file_list = []
filtered_package_prefixes = ['tensorflow.%s.' % p for p in package_prefixes]
for f in golden_file_list:
    if any(
        f.rsplit('/')[-1].startswith(pre) for pre in filtered_package_prefixes):
        continue
    filtered_file_list.append(f)
exit(filtered_file_list)
