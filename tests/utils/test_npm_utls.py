"""Test for npm.py

Test for the utility for npm operations.
"""
from unittest.mock import patch, call, mock_open
from tests.helpers.base_test_case import BaseTestCase
from ploigos_step_runner.utils.io import \
    create_sh_redirect_to_multiple_streams_fn_callback

class TestNpmUtils(BaseTestCase):

    @patch('ploigos_step_runner.utils.io.create_sh_redirect_to_multiple_streams_fn_callback')
    def test_run_script_redirects_output(self, redirect_mock):
        create_sh_redirect_to_multiple_streams_fn_callback([])
        redirect_mock.assert_called()
