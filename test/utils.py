import io
from contextlib import redirect_stdout
from typing import Callable


def capture_stdout(function_under_test: Callable) -> str:
    stdout_value = ''
    with io.StringIO() as stdout:
        with redirect_stdout(stdout):
            function_under_test()
        stdout_value = stdout.getvalue()
    return stdout_value
