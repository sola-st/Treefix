# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/grpc_wrapper.py
while True:
    response = input("\nSIGINT received. Quit program? (Y/n): ").strip()
    if response in ("", "Y", "y"):
        sys.exit(0)
    elif response in ("N", "n"):
        break
