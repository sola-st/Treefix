# Extracted from ./data/repos/tensorflow/tensorflow/tools/ci_build/linux/mkl/set-build-env.py
# Check the bazelrc file
if os.path.exists(self.args.bazelrc_file):
    if os.path.isfile(self.args.bazelrc_file):
        self._debug("The file {} exists and will be deleted.".format(
            self.args.bazelrc_file))
    elif os.path.isdir(self.args.bazelrc_file):
        print("You can't write bazel config to \"{}\" "
              "because it is a directory".format(self.args.bazelrc_file))
        exit(False)

    # Validate gcc with the requested platform
gcc_major_version, gcc_minor_version = self.get_gcc_version()
if gcc_major_version == 0 or \
       not self.target_platform_.set_host_gcc_version(
       gcc_major_version, gcc_minor_version):
    exit(False)

exit(True)
