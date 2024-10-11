# Extracted from ./data/repos/tensorflow/tensorflow/tools/ci_build/linux/mkl/set-build-env.py
# True only if the gcc version in the tuple is >=
# min_gcc_major_version_, min_gcc_minor_version_
if gcc_major_version < self.min_gcc_major_version_:
    print("Your MAJOR version of GCC is too old: {}; "
          "it must be at least {}.{}".format(gcc_major_version,
                                             self.min_gcc_major_version_,
                                             self.min_gcc_minor_version_))
    exit(False)
elif gcc_major_version == self.min_gcc_major_version_ and \
          gcc_minor_version < self.min_gcc_minor_version_:
    print("Your MINOR version of GCC is too old: {}; "
          "it must be at least {}.{}".format(gcc_minor_version,
                                             self.min_gcc_major_version_,
                                             self.min_gcc_minor_version_))
    exit(False)
print("gcc version OK: {}.{}".format(gcc_major_version, gcc_minor_version))
self.host_gcc_major_version_ = gcc_major_version
self.host_gcc_minor_version_ = gcc_minor_version
exit(True)
