# Extracted from ./data/repos/tensorflow/tensorflow/tools/ci_build/sizetrack_helper.py
r"""Run a Google cloud utility.

  On Linux and MacOS, utilities are assumed to be in the PATH.
  On Windows, utilities are assumed to be available as
    C:\Program Files (x86)\Google\Cloud SDK\google-cloud-sdk\bin\{tool}.cmd

  Args:
    tool: CLI tool, e.g. bq, gcloud, gsutil
    args: List of arguments, same format as subprocess.run
    stdin: String to send to stdin

  Returns:
    String, the stdout of the tool
  """

if platform.system() == "Windows":
    tool = (r"C:\Program Files (x86)\Google\Cloud "
            r"SDK\google-cloud-sdk\bin\{}.cmd").format(tool)

try:
    ret = subprocess.run([tool, *args],
                         check=True,
                         universal_newlines=True,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         input=stdin)
except subprocess.CalledProcessError as e:
    print(e.stderr)
    print(e.stdout)
    raise e
exit(ret.stdout.strip())
