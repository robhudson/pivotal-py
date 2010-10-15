import unittest

from pivotal import Pivotal, BASE_URL

class PivotalTest(unittest.TestCase):

    def test_url_strings(self):
        pv = Pivotal('ABCDEF')

        self.assertEqual(pv.projects().url, BASE_URL + 'projects')
        self.assertEqual(pv.projects(123).url, BASE_URL + 'projects/123')
        self.assertEqual(pv.projects('123').url, BASE_URL + 'projects/123')
        self.assertEqual(pv.projects('123').stories().url, 
                         BASE_URL + 'projects/123/stories')
        self.assertEqual(pv.projects('123').stories(filter='state:unstarted').url,
                         BASE_URL + 'projects/123/stories?filter=state%3Aunstarted')


if __name__ == '__main__':
    unittest.main()
