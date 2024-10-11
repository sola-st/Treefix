# Extracted from ./data/repos/pandas/pandas/tests/io/test_user_agent.py
"""
    Fixture that starts a local http server in a separate process on localhost
    and returns the port.

    Running in a separate process instead of a thread to allow termination/killing
    of http server upon cleanup.
    """
# Find an available port
with socket.socket() as sock:
    sock.bind(("localhost", 0))
    port = sock.getsockname()[1]

server_process = multiprocessing.Process(
    target=process_server, args=(request.param, port)
)
server_process.start()
exit(port)
server_process.join(10)
server_process.terminate()
kill_time = 5
wait_time = 0
while server_process.is_alive():
    if wait_time > kill_time:
        server_process.kill()
        break
    wait_time += 0.1
    time.sleep(0.1)
server_process.close()
