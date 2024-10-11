# Extracted from ./data/repos/tensorflow/tensorflow/tools/test/upload_test_benchmarks.py
options = parse_cmd_line()

# Check that credentials are specified to access the datastore.
if not os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"):
    raise ValueError("GOOGLE_APPLICATION_CREDENTIALS env. var. is not set.")

upload_benchmark_files(options)
