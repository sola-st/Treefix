# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/registration/tf_registration_test.py
allowlist = set([
    s.strip()
    for s in file_io.read_file_to_string(allowlist_file).splitlines()
    if s.strip() and not s.startswith("#")
])
registered_names = set(registrations)

missing_from_allowlist = registered_names - allowlist
self.assertIn("tf.NotInAllowlistExample", missing_from_allowlist)
missing_from_allowlist.remove("tf.NotInAllowlistExample")

if missing_from_allowlist:
    msg = ("[NEEDS ATTENTION] Registered names found that were not added to "
           "the allowlist. Add the following names to the list:\n\t" +
           "\n\t".join(missing_from_allowlist))
else:
    msg = "[OK] All registered names have been added to the allowlist.  ✓"

msg += "\n\n"

missing_registered_names = allowlist - registered_names
if missing_registered_names:
    msg += ("[NEEDS ATTENTION] Some names were found in the allowlist that "
            "are not registered in TensorFlow. This could mean that a "
            "registration was removed from the codebase. If this was "
            "intended, please remove the following from the allowlist:\n\t" +
            "\n\t".join(missing_registered_names))
else:
    msg += ("[OK] All allowlisted names are registered in the Tensorflow "
            "library. ✓")

if missing_from_allowlist or missing_registered_names:
    raise AssertionError(
        "Error found in the registration allowlist.\nPlease update the "
        "allowlist at .../tensorflow/python/saved_model/registration/"
        f"{os.path.basename(allowlist_file)}.\n\n" + msg +
        "\n\nAfter making changes, request approval from "
        " tf-saved-model-owners@.")
