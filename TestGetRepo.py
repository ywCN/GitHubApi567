from unittest import TestCase
from unittest.mock import patch, Mock

import GetRepo

expected_commit_info = ['Repo: test1 Number of commits: 3',
                        'Repo: test2 Number of commits: 2',
                        'Repo: Triangle567 Number of commits: 1']

class TestGetRepo(TestCase):
    @patch('GetRepo.get_commit_info', return_value=expected_commit_info)
    def test_get_user_info(self, get_commit_info):
        expected = ['User: ywang567',
                    'Repo: test1 Number of commits: 3',
                    'Repo: test2 Number of commits: 2',
                    'Repo: Triangle567 Number of commits: 1']
        self.assertEqual(GetRepo.get_user_info(get_commit_info()), expected)


if __name__ == '__main__':
    unittest.main()

