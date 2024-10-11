# Extracted from ./data/repos/pandas/pandas/tests/io/generate_legacy_storage_files.py
# force our cwd to be the first searched
sys.path.insert(0, ".")

if not 3 <= len(sys.argv) <= 4:
    sys.exit(
        "Specify output directory and storage type: generate_legacy_"
        "storage_files.py <output_dir> <storage_type> "
    )

output_dir = str(sys.argv[1])
storage_type = str(sys.argv[2])

if storage_type == "pickle":
    write_legacy_pickles(output_dir=output_dir)
else:
    sys.exit("storage_type must be one of {'pickle'}")
