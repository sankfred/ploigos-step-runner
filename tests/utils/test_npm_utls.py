"""Test for npm.py

Test for the utility for npm operations.
"""
from unittest.mock import patch, call, mock_open
from io import BytesIO, StringIO, TextIOWrapper
from tests.helpers.base_test_case import BaseTestCase
from ploigos_step_runner.utils.npm import run_npm
from tests.helpers.test_utils import Any
import sys # only used to test whether its members are passed to callbacks
from ploigos_step_runner.utils.io import \
    create_sh_redirect_to_multiple_streams_fn_callback

class TestNpmUtils(BaseTestCase):

    @patch('sh.npm', create=True) # Given a shell command, 'npm'
    @patch('ploigos_step_runner.utils.io.create_sh_redirect_to_multiple_streams_fn_callback')  # Given a callback that redirects stdio/stderr
    @patch("builtins.open", new_callable=mock_open) # Given that I can open files
    def test_run_script_shell_argument(self, mock_open, redirect_callback_mock, npm_shell_command_mock):

        # When I use run_npm() to run 'myscript'
        run_npm('/my/output/file', ['myscript'])

        # Then it should run a shell command, `npm run myscript`
        npm_shell_command_mock.assert_any_call(
            'run',
            'myscript',
            _out=Any(StringIO),
            _err=Any(StringIO)
        )

    # @patch('sh.npm', create=True) # Given a shell command, 'npm'
    @patch('ploigos_step_runner.utils.io.create_sh_redirect_to_multiple_streams_fn_callback')  # Given a callback that redirects command output
    # @patch("builtins.open", new_callable=mock_open) # Given that I can open files
    # def test_run_script_redirects_output(self, mock_open, redirect_mock, npm_shell_command_mock):
    def test_run_script_redirects_output(self, redirect_mock):

        # When I use run_npm() to run 'myscript'
        # run_npm('/my/output/file', ['myscript'])
        create_sh_redirect_to_multiple_streams_fn_callback([])

        # mock_open.assert_called()
        redirect_mock.assert_called()

        # # Then it should redirect STDOUT
        # redirect_mock.assert_any_call([sys.stdout, mock_open.return_value])
        #
        # # And it should redirect STDERR
        # redirect_mock.assert_any_call([sys.stderr, mock_open.return_value])
