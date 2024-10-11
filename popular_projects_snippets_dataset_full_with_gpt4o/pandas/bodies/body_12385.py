# Extracted from ./data/repos/pandas/pandas/tests/io/conftest.py
"""
    Fixture for mocking S3 interaction.

    Sets up moto server in separate process locally
    Return url for motoserver/moto CI service
    """
pytest.importorskip("s3fs")
pytest.importorskip("boto3")

with tm.ensure_safe_environment_variables():
    # temporary workaround as moto fails for botocore >= 1.11 otherwise,
    # see https://github.com/spulec/moto/issues/1924 & 1952
    os.environ.setdefault("AWS_ACCESS_KEY_ID", "foobar_key")
    os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "foobar_secret")
    if is_ci_environment():
        if is_platform_arm() or is_platform_mac() or is_platform_windows():
            # NOT RUN on Windows/macOS/ARM, only Ubuntu
            # - subprocess in CI can cause timeouts
            # - GitHub Actions do not support
            #   container services for the above OSs
            # - CircleCI will probably hit the Docker rate pull limit
            pytest.skip(
                "S3 tests do not have a corresponding service in "
                "Windows, macOS or ARM platforms"
            )
        else:
            exit("http://localhost:5000")
    else:
        requests = pytest.importorskip("requests")
        pytest.importorskip("moto", minversion="1.3.14")
        pytest.importorskip("flask")  # server mode needs flask too

        # Launching moto in server mode, i.e., as a separate process
        # with an S3 endpoint on localhost

        worker_id = "5" if worker_id == "master" else worker_id.lstrip("gw")
        endpoint_port = f"555{worker_id}"
        endpoint_uri = f"http://127.0.0.1:{endpoint_port}/"

        # pipe to null to avoid logging in terminal
        with subprocess.Popen(
            shlex.split(f"moto_server s3 -p {endpoint_port}"),
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        ) as proc:

            timeout = 5
            while timeout > 0:
                try:
                    # OK to go once server is accepting connections
                    r = requests.get(endpoint_uri)
                    if r.ok:
                        break
                except Exception:
                    pass
                timeout -= 0.1
                time.sleep(0.1)
            exit(endpoint_uri)

            proc.terminate()
