import curses # pragma: no cover
from types import SimpleNamespace # pragma: no cover

x = 10 # pragma: no cover
self = SimpleNamespace() # pragma: no cover
self.CLI_CR_KEYS = {10, 13, 36} # pragma: no cover
self._textbox_curr_terminator = None # pragma: no cover
self.CLI_TERMINATOR_KEY = 27 # pragma: no cover
self.CLI_TAB_KEY = 9 # pragma: no cover
_SCROLL_UP_A_LINE = -1 # pragma: no cover
_SCROLL_DOWN_A_LINE = 1 # pragma: no cover
_SCROLL_HOME = 0 # pragma: no cover
_SCROLL_END = 100 # pragma: no cover
class MockDebuggerCliCommon: CommandLineExit = type('CommandLineExit', (Exception,), {}) # pragma: no cover
debugger_cli_common = MockDebuggerCliCommon() # pragma: no cover
self._scroll_output = lambda x: None # pragma: no cover
self._active_command_history = [] # pragma: no cover
self._screen_gather_textbox_str = lambda: '' # pragma: no cover
self._command_history_store = SimpleNamespace(lookup_prefix=lambda prefix, limit: []) # pragma: no cover
self._command_history_limit = 10 # pragma: no cover
self._command_pointer = 0 # pragma: no cover
self._screen_refresh_size = lambda: None # pragma: no cover
self._init_layout = lambda: None # pragma: no cover
self._screen_create_command_window = lambda: None # pragma: no cover
self._redraw_output = lambda: None # pragma: no cover
self._mouse_enabled = False # pragma: no cover
self._screen_getmouse = lambda: (0, 0, 0, 0, 0) # pragma: no cover
self._max_x = 80 # pragma: no cover
self._command_window = SimpleNamespace(nodelay=lambda flag: None, getch=lambda: None) # pragma: no cover
self._MOUSE_SCROLL_DELAY_MS = 100 # pragma: no cover
self._scroll_bar = SimpleNamespace(get_click_command=lambda y: None) # pragma: no cover
self._fetch_hyperlink_command = lambda x, y: None # pragma: no cover
self._screen_create_command_textbox = lambda: None # pragma: no cover
self._dispatch_command = lambda command: None # pragma: no cover
self._textbox_pending_command_changed = False # pragma: no cover
self._KEY_MAP = {} # pragma: no cover

import curses # pragma: no cover

x = 10 # pragma: no cover
self = type('Mock', (object,), { # pragma: no cover
   'CLI_CR_KEYS': {10, 13}, # pragma: no cover
   'CLI_TERMINATOR_KEY': 1000, # pragma: no cover
   'CLI_TAB_KEY': 9, # pragma: no cover
   '_textbox_curr_terminator': None, # pragma: no cover
   '_scroll_output': lambda self, cmd: None, # pragma: no cover
   '_active_command_history': [], # pragma: no cover
   '_screen_gather_textbox_str': lambda self: '', # pragma: no cover
   '_command_history_store': type('MockStore', (object,), { # pragma: no cover
       'lookup_prefix': lambda self, prefix, limit: []})(), # pragma: no cover
   '_command_history_limit': 10, # pragma: no cover
   '_command_pointer': 0, # pragma: no cover
   '_screen_refresh_size': lambda self: None, # pragma: no cover
   '_init_layout': lambda self: None, # pragma: no cover
   '_screen_create_command_window': lambda self: None, # pragma: no cover
   '_redraw_output': lambda self: None, # pragma: no cover
   '_mouse_enabled': True, # pragma: no cover
   '_screen_getmouse': lambda self: (0, 0, 0, 0, curses.BUTTON1_PRESSED), # pragma: no cover
   '_max_x': 80, # pragma: no cover
   '_command_window': type('MockWindow', (object,), { # pragma: no cover
       'nodelay': lambda self, flag: None, # pragma: no cover
       'getch': lambda self: None})(), # pragma: no cover
   '_MOUSE_SCROLL_DELAY_MS': 100, # pragma: no cover
   '_scroll_bar': type('MockScrollBar', (object,), { # pragma: no cover
      'get_click_command': lambda self, y: None})(), # pragma: no cover
   '_fetch_hyperlink_command': lambda self, x, y: None, # pragma: no cover
   '_screen_create_command_textbox': lambda self: None, # pragma: no cover
   '_dispatch_command': lambda self, command: None, # pragma: no cover
   '_textbox_pending_command_changed': False, # pragma: no cover
   '_KEY_MAP': {}})() # pragma: no cover
_SCROLL_UP_A_LINE = 1 # pragma: no cover
_SCROLL_DOWN_A_LINE = 2 # pragma: no cover
_SCROLL_HOME = 3 # pragma: no cover
_SCROLL_END = 4 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui.py
from l3.Runtime import _l_
"""Text box key validator: Callback of key strokes.

    Handles a user's keypress in the input text box. Translates certain keys to
    terminator keys for the textbox to allow its edit() method to return.
    Also handles special key-triggered events such as PgUp/PgDown scrolling of
    the screen output.

    Args:
      x: (int) Key code.

    Returns:
      (int) A translated key code. In most cases, this is identical to the
        input x. However, if x is a Return key, the return value will be
        CLI_TERMINATOR_KEY, so that the text box's edit() method can return.

    Raises:
      TypeError: If the input x is not of type int.
      debugger_cli_common.CommandLineExit: If a mouse-triggered command returns
        an exit token when dispatched.
    """
if not isinstance(x, int):
    _l_(21827)

    raise TypeError("Key validator expected type int, received type %s" %
                    type(x))
    _l_(21826)

if x in self.CLI_CR_KEYS:
    _l_(21901)

    # Make Enter key the terminator
    self._textbox_curr_terminator = x
    _l_(21828)
    aux = self.CLI_TERMINATOR_KEY
    _l_(21829)
    exit(aux)
elif x == self.CLI_TAB_KEY:
    _l_(21900)

    self._textbox_curr_terminator = self.CLI_TAB_KEY
    _l_(21830)
    aux = self.CLI_TERMINATOR_KEY
    _l_(21831)
    exit(aux)
elif x == curses.KEY_PPAGE:
    _l_(21899)

    self._scroll_output(_SCROLL_UP_A_LINE)
    _l_(21832)
    aux = x
    _l_(21833)
    exit(aux)
elif x == curses.KEY_NPAGE:
    _l_(21898)

    self._scroll_output(_SCROLL_DOWN_A_LINE)
    _l_(21834)
    aux = x
    _l_(21835)
    exit(aux)
elif x == curses.KEY_HOME:
    _l_(21897)

    self._scroll_output(_SCROLL_HOME)
    _l_(21836)
    aux = x
    _l_(21837)
    exit(aux)
elif x == curses.KEY_END:
    _l_(21896)

    self._scroll_output(_SCROLL_END)
    _l_(21838)
    aux = x
    _l_(21839)
    exit(aux)
elif x in [curses.KEY_UP, curses.KEY_DOWN]:
    _l_(21895)

    # Command history navigation.
    if not self._active_command_history:
        _l_(21842)

        hist_prefix = self._screen_gather_textbox_str()
        _l_(21840)
        self._active_command_history = (
            self._command_history_store.lookup_prefix(
                hist_prefix, self._command_history_limit))
        _l_(21841)

    if self._active_command_history:
        _l_(21850)

        if x == curses.KEY_UP:
            _l_(21848)

            if self._command_pointer < len(self._active_command_history):
                _l_(21844)

                self._command_pointer += 1
                _l_(21843)
        elif x == curses.KEY_DOWN:
            _l_(21847)

            if self._command_pointer > 0:
                _l_(21846)

                self._command_pointer -= 1
                _l_(21845)
    else:
        self._command_pointer = 0
        _l_(21849)

    self._textbox_curr_terminator = x
    _l_(21851)
    aux = self.CLI_TERMINATOR_KEY
    _l_(21852)

    # Force return from the textbox edit(), so that the textbox can be
    # redrawn with a history command entered.
    exit(aux)
elif x == curses.KEY_RESIZE:
    _l_(21894)

    # Respond to terminal resize.
    self._screen_refresh_size()
    _l_(21853)
    self._init_layout()
    _l_(21854)
    self._screen_create_command_window()
    _l_(21855)
    self._redraw_output()
    _l_(21856)
    aux = self.CLI_TERMINATOR_KEY
    _l_(21857)

    # Force return from the textbox edit(), so that the textbox can be
    # redrawn.
    exit(aux)
elif x == curses.KEY_MOUSE and self._mouse_enabled:
    _l_(21893)

    try:
        _l_(21861)

        _, mouse_x, mouse_y, _, mouse_event_type = self._screen_getmouse()
        _l_(21858)
    except curses.error:
        _l_(21860)

        mouse_event_type = None
        _l_(21859)

    if mouse_event_type == curses.BUTTON1_PRESSED:
        _l_(21888)

        # Logic for held mouse-triggered scrolling.
        if mouse_x >= self._max_x - 2:
            _l_(21875)

            # Disable blocking on checking for user input.
            self._command_window.nodelay(True)
            _l_(21862)

            # Loop while mouse button is pressed.
            while mouse_event_type == curses.BUTTON1_PRESSED:
                _l_(21872)

                # Sleep for a bit.
                curses.napms(self._MOUSE_SCROLL_DELAY_MS)
                _l_(21863)
                scroll_command = self._scroll_bar.get_click_command(mouse_y)
                _l_(21864)
                if scroll_command in (_SCROLL_UP_A_LINE, _SCROLL_DOWN_A_LINE):
                    _l_(21866)

                    self._scroll_output(scroll_command)
                    _l_(21865)

                # Check to see if different mouse event is in queue.
                self._command_window.getch()
                _l_(21867)
                try:
                    _l_(21871)

                    _, _, _, _, mouse_event_type = self._screen_getmouse()
                    _l_(21868)
                except curses.error:
                    _l_(21870)

                    pass
                    _l_(21869)

            self._command_window.nodelay(False)
            _l_(21873)
            aux = x
            _l_(21874)
            exit(aux)
    elif mouse_event_type == curses.BUTTON1_RELEASED:
        _l_(21887)

        # Logic for mouse-triggered scrolling.
        if mouse_x >= self._max_x - 2:
            _l_(21886)

            scroll_command = self._scroll_bar.get_click_command(mouse_y)
            _l_(21876)
            if scroll_command is not None:
                _l_(21878)

                self._scroll_output(scroll_command)
                _l_(21877)
            aux = x
            _l_(21879)
            exit(aux)
        else:
            command = self._fetch_hyperlink_command(mouse_x, mouse_y)
            _l_(21880)
            if command:
                _l_(21885)

                self._screen_create_command_textbox()
                _l_(21881)
                exit_token = self._dispatch_command(command)
                _l_(21882)
                if exit_token is not None:
                    _l_(21884)

                    raise debugger_cli_common.CommandLineExit(exit_token=exit_token)
                    _l_(21883)
else:
    # Mark the pending command as modified.
    self._textbox_pending_command_changed = True
    _l_(21889)
    # Invalidate active command history.
    self._command_pointer = 0
    _l_(21890)
    self._active_command_history = []
    _l_(21891)
    aux = self._KEY_MAP.get(x, x)
    _l_(21892)
    exit(aux)
