# Extracted from ./data/repos/pandas/pandas/tests/test_downstream.py
# GH 23868
# To ensure proper isolation, we pass these flags
# -S : disable site-packages
# -s : disable user site-packages
# -E : disable PYTHON* env vars, especially PYTHONPATH
# https://github.com/MacPython/pandas-wheels/pull/50

pyexe = sys.executable.replace("\\", "/")

# We skip this test if pandas is installed as a site package. We first
# import the package normally and check the path to the module before
# executing the test which imports pandas with site packages disabled.
call = [pyexe, "-c", "import pandas;print(pandas.__file__)"]
output = subprocess.check_output(call).decode()
if "site-packages" in output:
    pytest.skip("pandas installed as site package")

# This test will fail if pandas is installed as a site package. The flags
# prevent pandas being imported and the test will report Failed: DID NOT
# RAISE <class 'subprocess.CalledProcessError'>
call = [pyexe, "-sSE", "-c", "import pandas"]

msg = (
    rf"Command '\['{pyexe}', '-sSE', '-c', 'import pandas'\]' "
    "returned non-zero exit status 1."
)

with pytest.raises(subprocess.CalledProcessError, match=msg) as exc:
    subprocess.check_output(call, stderr=subprocess.STDOUT)

output = exc.value.stdout.decode()
for name in ["numpy", "pytz", "dateutil"]:
    assert name in output
