from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.workflow_bulk_resource_api import WorkflowBulkResourceApi  # noqa: E501
from swagger_client.rest import ApiException


class TestWorkflowBulkResourceApi(unittest.TestCase):
    """WorkflowBulkResourceApi unit test stubs"""

    def setUp(self):
        self.api = WorkflowBulkResourceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_pause_workflow1(self):
        """Test case for pause_workflow1

        Pause the list of workflows  # noqa: E501
        """
        pass

    def test_restart1(self):
        """Test case for restart1

        Restart the list of completed workflow  # noqa: E501
        """
        pass

    def test_resume_workflow1(self):
        """Test case for resume_workflow1

        Resume the list of workflows  # noqa: E501
        """
        pass

    def test_retry1(self):
        """Test case for retry1

        Retry the last failed task for each workflow from the list  # noqa: E501
        """
        pass

    def test_terminate(self):
        """Test case for terminate

        Terminate workflows execution  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()