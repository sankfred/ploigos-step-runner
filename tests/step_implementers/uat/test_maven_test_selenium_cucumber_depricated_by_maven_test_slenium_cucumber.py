
from unittest.mock import patch

from ploigos_step_runner import WorkflowResult
from ploigos_step_runner.step_implementers.uat import MavenSeleniumCucumber
from tests.helpers.base_step_implementer_test_case import \
    BaseStepImplementerTestCase


@patch("ploigos_step_runner.step_implementers.uat.MavenTestSeleniumCucumber.__init__")
class TestStepImplementerMaven_UnitTestOld___init__(BaseStepImplementerTestCase):
    def test_defaults(self, mock_super_init):
        workflow_result = WorkflowResult()
        parent_work_dir_path = '/fake/path'
        config = {}

        MavenSeleniumCucumber(
            workflow_result=workflow_result,
            parent_work_dir_path=parent_work_dir_path,
            config=config
        )

        mock_super_init.assert_called_once_with(
            workflow_result=workflow_result,
            parent_work_dir_path=parent_work_dir_path,
            config=config,
            environment=None
        )
