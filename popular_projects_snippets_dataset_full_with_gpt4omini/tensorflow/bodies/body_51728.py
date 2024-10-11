# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_context_test.py
self.assertFalse(save_context.in_save_context())
with self.assertRaisesRegex(ValueError, 'Not in a SaveContext'):
    save_context.get_save_options()

options = save_options.SaveOptions(save_debug_info=True)
with save_context.save_context(options):
    self.assertTrue(save_context.in_save_context())
    self.assertTrue(save_context.get_save_options().save_debug_info)

    entered_context_in_thread = threading.Event()
    continue_thread = threading.Event()

    def thread_fn():
        self.assertFalse(save_context.in_save_context())
        with self.assertRaisesRegex(ValueError, 'Not in a SaveContext'):
            save_context.get_save_options()

        options = save_options.SaveOptions(save_debug_info=False)
        with save_context.save_context(options):
            self.assertTrue(save_context.in_save_context())
            # save_debug_info has a different value in this thread.
            self.assertFalse(save_context.get_save_options().save_debug_info)
            entered_context_in_thread.set()
            continue_thread.wait()

        self.assertFalse(save_context.in_save_context())
        with self.assertRaisesRegex(ValueError, 'Not in a SaveContext'):
            save_context.get_save_options()

    t = threading.Thread(target=thread_fn)
    t.start()

    entered_context_in_thread.wait()
    # Another thread shouldn't affect this thread.
    self.assertTrue(save_context.in_save_context())
    self.assertTrue(save_context.get_save_options().save_debug_info)

    continue_thread.set()
    t.join()
    # Another thread exiting SaveContext shouldn't affect this thread.
    self.assertTrue(save_context.in_save_context())
    self.assertTrue(save_context.get_save_options().save_debug_info)

self.assertFalse(save_context.in_save_context())
with self.assertRaisesRegex(ValueError, 'Not in a SaveContext'):
    save_context.get_save_options()
