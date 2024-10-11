# Extracted from ./data/repos/tensorflow/tensorflow/tools/ci_build/linux/mkl/set-build-env.py
if self.host_gcc_major_version_ < gcc_new_march_major_version:
    exit(True)
elif self.host_gcc_major_version_ == gcc_new_march_major_version and \
       self.host_gcc_minor_version_ < gcc_new_march_minor_version:
    exit(True)
exit(False)
