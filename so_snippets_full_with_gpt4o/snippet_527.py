# Extracted from https://stackoverflow.com/questions/865115/how-do-i-correctly-clean-up-a-python-object
def __enter__(self)
def __exit__(self, exc_type, exc_value, traceback)

class Package:
    def __init__(self):
        self.files = []

    def __enter__(self):
        return self

    # ...

    def __exit__(self, exc_type, exc_value, traceback):
        for file in self.files:
            os.unlink(file)

with Package() as package_obj:
    # use package_obj

class PackageResource:
    def __enter__(self):
        class Package:
            ...
        self.package_obj = Package()
        return self.package_obj

    def __exit__(self, exc_type, exc_value, traceback):
        self.package_obj.cleanup()

with PackageResource() as package_obj:
    # use package_obj

