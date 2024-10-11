import curses # pragma: no cover

x = 10 # pragma: no cover
self = type('Mock', (), { 'CLI_CR_KEYS': [curses.KEY_ENTER], 'CLI_TERMINATOR_KEY': 13, 'CLI_TAB_KEY': 9, 'textbox_curr_terminator': None, 'active_command_history': [], 'command_pointer': 0, 'command_history_limit': 100, 'textbox_pending_command_changed': False, 'mouse_enabled': True, 'max_x': 80, 'command_window': type('Mock', (), { 'nodelay': lambda self, flag: None, 'getch': lambda self: None })(), 'scroll_output': lambda self, command: None, 'screen_gather_textbox_str': lambda self: '', 'screen_refresh_size': lambda self: None, 'init_layout': lambda self: None, 'screen_create_command_window': lambda self: None, 'redraw_output': lambda self: None, 'screen_getmouse': lambda self: (0, 0, 0, 0, None), 'fetch_hyperlink_command': lambda self, x, y: None, 'screen_create_command_textbox': lambda self: None, 'dispatch_command': lambda self, cmd: None, 'scroll_bar': type('Mock', (), { 'get_click_command': lambda self, y: None })(), 'KEY_MAP': {}})() # pragma: no cover
_SCROLL_UP_A_LINE = 1 # pragma: no cover
_SCROLL_DOWN_A_LINE = 2 # pragma: no cover
_SCROLL_HOME = 3 # pragma: no cover
_SCROLL_END = 4 # pragma: no cover

import curses # pragma: no cover

x = 10 # pragma: no cover
self = type('Mock', (), { 'CLI_CR_KEYS': [curses.KEY_ENTER], 'CLI_TERMINATOR_KEY': 13, 'CLI_TAB_KEY': 9, 'textbox_curr_terminator': None, 'active_command_history': [], 'command_pointer': 0, 'command_history_limit': 100, 'textbox_pending_command_changed': False, 'mouse_enabled': True, 'max_x': 80, 'command_window': type('Mock', (), { 'nodelay': lambda self, flag: None, 'getch': lambda self: None })(), 'scroll_output': lambda self, command: None, 'screen_gather_textbox_str': lambda self: '', 'screen_refresh_size': lambda self: None, 'init_layout': lambda self: None, 'screen_create_command_window': lambda self: None, 'redraw_output': lambda self: None, 'screen_getmouse': lambda self: (0, 0, 0, 0, None), 'fetch_hyperlink_command': lambda self, x, y: None, 'screen_create_command_textbox': lambda self: None, 'dispatch_command': lambda self, cmd: None, 'scroll_bar': type('Mock', (), { 'get_click_command': lambda self, y: None })(), '_KEY_MAP': {10: 13, 9: 9, 338: 338, 339: 339}})() # pragma: no cover
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
    _l_(9463)

    raise TypeError("Key validator expected type int, received type %s" %
                    type(x))
    _l_(9462)

if x in self.CLI_CR_KEYS:
    _l_(9537)

    # Make Enter key the terminator
    self._textbox_curr_terminator = x
    _l_(9464)
    aux = self.CLI_TERMINATOR_KEY
    _l_(9465)
    exit(aux)
elif x == self.CLI_TAB_KEY:
    _l_(9536)

    self._textbox_curr_terminator = self.CLI_TAB_KEY
    _l_(9466)
    aux = self.CLI_TERMINATOR_KEY
    _l_(9467)
    exit(aux)
elif x == curses.KEY_PPAGE:
    _l_(9535)

    self._scroll_output(_SCROLL_UP_A_LINE)
    _l_(9468)
    aux = x
    _l_(9469)
    exit(aux)
elif x == curses.KEY_NPAGE:
    _l_(9534)

    self._scroll_output(_SCROLL_DOWN_A_LINE)
    _l_(9470)
    aux = x
    _l_(9471)
    exit(aux)
elif x == curses.KEY_HOME:
    _l_(9533)

    self._scroll_output(_SCROLL_HOME)
    _l_(9472)
    aux = x
    _l_(9473)
    exit(aux)
elif x == curses.KEY_END:
    _l_(9532)

    self._scroll_output(_SCROLL_END)
    _l_(9474)
    aux = x
    _l_(9475)
    exit(aux)
elif x in [curses.KEY_UP, curses.KEY_DOWN]:
    _l_(9531)

    # Command history navigation.
    if not self._active_command_history:
        _l_(9478)

        hist_prefix = self._screen_gather_textbox_str()
        _l_(9476)
        self._active_command_history = (
            self._command_history_store.lookup_prefix(
                hist_prefix, self._command_history_limit))
        _l_(9477)

    if self._active_command_history:
        _l_(9486)

        if x == curses.KEY_UP:
            _l_(9484)

            if self._command_pointer < len(self._active_command_history):
                _l_(9480)

                self._command_pointer += 1
                _l_(9479)
        elif x == curses.KEY_DOWN:
            _l_(9483)

            if self._command_pointer > 0:
                _l_(9482)

                self._command_pointer -= 1
                _l_(9481)
    else:
        self._command_pointer = 0
        _l_(9485)

    self._textbox_curr_terminator = x
    _l_(9487)
    aux = self.CLI_TERMINATOR_KEY
    _l_(9488)

    # Force return from the textbox edit(), so that the textbox can be
    # redrawn with a history command entered.
    exit(aux)
elif x == curses.KEY_RESIZE:
    _l_(9530)

    # Respond to terminal resize.
    self._screen_refresh_size()
    _l_(9489)
    self._init_layout()
    _l_(9490)
    self._screen_create_command_window()
    _l_(9491)
    self._redraw_output()
    _l_(9492)
    aux = self.CLI_TERMINATOR_KEY
    _l_(9493)

    # Force return from the textbox edit(), so that the textbox can be
    # redrawn.
    exit(aux)
elif x == curses.KEY_MOUSE and self._mouse_enabled:
    _l_(9529)

    try:
        _l_(9497)

        _, mouse_x, mouse_y, _, mouse_event_type = self._screen_getmouse()
        _l_(9494)
    except curses.error:
        _l_(9496)

        mouse_event_type = None
        _l_(9495)

    if mouse_event_type == curses.BUTTON1_PRESSED:
        _l_(9524)

        # Logic for held mouse-triggered scrolling.
        if mouse_x >= self._max_x - 2:
            _l_(9511)

            # Disable blocking on checking for user input.
            self._command_window.nodelay(True)
            _l_(9498)

            # Loop while mouse button is pressed.
            while mouse_event_type == curses.BUTTON1_PRESSED:
                _l_(9508)

                # Sleep for a bit.
                curses.napms(self._MOUSE_SCROLL_DELAY_MS)
                _l_(9499)
                scroll_command = self._scroll_bar.get_click_command(mouse_y)
                _l_(9500)
                if scroll_command in (_SCROLL_UP_A_LINE, _SCROLL_DOWN_A_LINE):
                    _l_(9502)

                    self._scroll_output(scroll_command)
                    _l_(9501)

                # Check to see if different mouse event is in queue.
                self._command_window.getch()
                _l_(9503)
                try:
                    _l_(9507)

                    _, _, _, _, mouse_event_type = self._screen_getmouse()
                    _l_(9504)
                except curses.error:
                    _l_(9506)

                    pass
                    _l_(9505)

            self._command_window.nodelay(False)
            _l_(9509)
            aux = x
            _l_(9510)
            exit(aux)
    elif mouse_event_type == curses.BUTTON1_RELEASED:
        _l_(9523)

        # Logic for mouse-triggered scrolling.
        if mouse_x >= self._max_x - 2:
            _l_(9522)

            scroll_command = self._scroll_bar.get_click_command(mouse_y)
            _l_(9512)
            if scroll_command is not None:
                _l_(9514)

                self._scroll_output(scroll_command)
                _l_(9513)
            aux = x
            _l_(9515)
            exit(aux)
        else:
            command = self._fetch_hyperlink_command(mouse_x, mouse_y)
            _l_(9516)
            if command:
                _l_(9521)

                self._screen_create_command_textbox()
                _l_(9517)
                exit_token = self._dispatch_command(command)
                _l_(9518)
                if exit_token is not None:
                    _l_(9520)

                    raise debugger_cli_common.CommandLineExit(exit_token=exit_token)
                    _l_(9519)
else:
    # Mark the pending command as modified.
    self._textbox_pending_command_changed = True
    _l_(9525)
    # Invalidate active command history.
    self._command_pointer = 0
    _l_(9526)
    self._active_command_history = []
    _l_(9527)
    aux = self._KEY_MAP.get(x, x)
    _l_(9528)
    exit(aux)
