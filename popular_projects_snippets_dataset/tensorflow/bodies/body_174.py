# Extracted from ./data/repos/tensorflow/tensorflow/tools/ci_build/linux/mkl/set-build-env.py
self._debug("Writing build flags: {}".format(self.bazel_flags_))
with open(self.args.bazelrc_file, "w") as f:
    f.write(self.bazel_flags_ + "\n")
