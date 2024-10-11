# Extracted from ./data/repos/pandas/pandas/tests/io/generate_legacy_storage_files.py

version = pandas.__version__

print(
    "This script generates a storage file for the current arch, system, "
    "and python version"
)
print(f"  pandas version: {version}")
print(f"  output dir    : {output_dir}")
print("  storage format: pickle")

pth = f"{platform_name()}.pickle"

with open(os.path.join(output_dir, pth), "wb") as fh:
    pickle.dump(create_pickle_data(), fh, pickle.DEFAULT_PROTOCOL)

print(f"created pickle file: {pth}")
