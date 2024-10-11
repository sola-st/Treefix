# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/readline_ui_test.py
observer = {"callback_invoked": False}

def callback_for_test():
    observer["callback_invoked"] = True

ui = MockReadlineUI(on_ui_exit=callback_for_test, command_sequence=["exit"])

self.assertFalse(observer["callback_invoked"])
ui.run_ui()

self.assertEqual(0, len(ui.observers["screen_outputs"]))
self.assertTrue(observer["callback_invoked"])
