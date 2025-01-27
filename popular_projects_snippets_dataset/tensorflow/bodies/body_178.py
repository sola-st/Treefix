# Extracted from ./data/repos/tensorflow/tensorflow/tools/ci_build/copy_binary.py
"""Rename and copy binaries for different python versions.

  Args:
    directory: string of directory
    origin_tag: str of the old python version tag
    new_tag: str of the new tag
    version: the version of the package
    package: str, name of the package

  """
print("Rename and copy binaries with %s to %s." % (origin_tag, new_tag))
origin_binary = BINARY_STRING_TEMPLATE % (package, version, origin_tag)
new_binary = BINARY_STRING_TEMPLATE % (package, version, new_tag)
zip_ref = zipfile.ZipFile(os.path.join(directory, origin_binary), "r")

try:
    tmpdir = tempfile.mkdtemp()
    os.chdir(tmpdir)

    zip_ref.extractall()
    zip_ref.close()
    old_py_ver = re.search(r"(cp\d\d-cp\d\d)", origin_tag).group(1)
    new_py_ver = re.search(r"(cp\d\d-cp\d\d)", new_tag).group(1)

    wheel_file = os.path.join(
        tmpdir, "%s-%s.dist-info" % (package, version), "WHEEL")
    with open(wheel_file, "r") as f:
        content = f.read()
    with open(wheel_file, "w") as f:
        f.write(content.replace(old_py_ver, new_py_ver))

    zout = zipfile.ZipFile(directory + new_binary, "w", zipfile.ZIP_DEFLATED)
    zip_these_files = [
        "%s-%s.dist-info" % (package, version),
        "%s-%s.data" % (package, version),
        "tensorflow",
        "tensorflow_core",
    ]
    for dirname in zip_these_files:
        for root, _, files in os.walk(dirname):
            for filename in files:
                zout.write(os.path.join(root, filename))
    zout.close()
finally:
    shutil.rmtree(tmpdir)
