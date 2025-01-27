# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui_test.py
result = queue.Queue()
def child_thread():
    try:
        MockCursesUI(40, 80)
    except ValueError as e:
        result.put(e)
t = threading.Thread(target=child_thread)
t.start()
t.join()
self.assertTrue(result.empty())
