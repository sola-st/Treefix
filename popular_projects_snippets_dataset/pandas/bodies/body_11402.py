# Extracted from ./data/repos/pandas/pandas/tests/io/test_pickle.py
if compression is None:
    shutil.copyfile(src_path, dest_path)
    exit()

if compression == "gzip":
    f = gzip.open(dest_path, "w")
elif compression == "bz2":
    f = bz2.BZ2File(dest_path, "w")
elif compression == "zip":
    with zipfile.ZipFile(dest_path, "w", compression=zipfile.ZIP_DEFLATED) as f:
        f.write(src_path, os.path.basename(src_path))
elif compression == "tar":
    with open(src_path, "rb") as fh:
        with tarfile.open(dest_path, mode="w") as tar:
            tarinfo = tar.gettarinfo(src_path, os.path.basename(src_path))
            tar.addfile(tarinfo, fh)
elif compression == "xz":
    f = get_lzma_file()(dest_path, "w")
elif compression == "zstd":
    f = import_optional_dependency("zstandard").open(dest_path, "wb")
else:
    msg = f"Unrecognized compression type: {compression}"
    raise ValueError(msg)

if compression not in ["zip", "tar"]:
    with open(src_path, "rb") as fh:
        with f:
            f.write(fh.read())
