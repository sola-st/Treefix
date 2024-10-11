# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/fingerprinting_test.py
model = self._create_model_with_function()
# Save the model with signatures specified in SaveOptions.
sig_dir = os.path.join(self.get_temp_dir(), "saved_model")
save.save(
    model,
    sig_dir,
    signatures=model.f.get_concrete_function(
        tensor_spec.TensorSpec(None, dtypes.float32)))
# Save the model without signatures.
no_sig_dir = os.path.join(self.get_temp_dir(), "saved_model2")
save.save(model, no_sig_dir)
# Save the model with an input signature specified.
input_sig_dir = os.path.join(self.get_temp_dir(), "saved_model3")
save.save(self._create_model_with_input_signature(), input_sig_dir)

fingerprint_sig = self._read_fingerprint(
    file_io.join(sig_dir, constants.FINGERPRINT_FILENAME))
fingerprint_no_sig = self._read_fingerprint(
    file_io.join(no_sig_dir, constants.FINGERPRINT_FILENAME))
fingerprint_input_sig = self._read_fingerprint(
    file_io.join(input_sig_dir, constants.FINGERPRINT_FILENAME))

# Check that the model saved with different options has different
# SignatureDef hashes.
self.assertNotEqual(fingerprint_sig.signature_def_hash,
                    fingerprint_no_sig.signature_def_hash)
# Check that the model saved with the same concrete function has the same
# regularized hashes.
self.assertEqual(fingerprint_sig.graph_def_program_hash,
                 fingerprint_input_sig.graph_def_program_hash)
self.assertEqual(fingerprint_sig.signature_def_hash,
                 fingerprint_input_sig.signature_def_hash)
