"""Test for npm.py

Test for the utility for npm operations.
"""
from unittest.mock import patch, call, mock_open
from io import BytesIO, StringIO, TextIOWrapper
from tests.helpers.base_test_case import BaseTestCase
from ploigos_step_runner.utils.npm import run_npm
from tests.helpers.test_utils import Any

class TestNpmUtils(BaseTestCase):

    @patch('sh.npm', create=True)
    @patch('ploigos_step_runner.utils.io.create_sh_redirect_to_multiple_streams_fn_callback')  # Given a callback that redirects stdio/stderr
    @patch("builtins.open", new_callable=mock_open)
    def test_run_script(self, mock_open, redirect_callback_mock, npm_shell_command_mock):

        # When I use run_npm() to run 'myscript'
        run_npm('/my/output/file', ['myscript'])

        # Then it should run a shell command, `npm run myscript`
        npm_shell_command_mock.assert_any_call(
            'run',
            'myscript',
            _out=Any(StringIO),
            _err=Any(StringIO)
        )
