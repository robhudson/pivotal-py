import unittest

from pivotal import Pivotal, BASE_URL, PROTO_SWITCH

class PivotalTest(unittest.TestCase):

    def test_protocol_switch(self):
        self.assertEqual(PROTO_SWITCH[True], 'https://')
        self.assertEqual(PROTO_SWITCH[False], 'http://')


    def _test_url_strings(self, use_https):
        pv = Pivotal('ABCDEF', use_https=use_https)

        url = PROTO_SWITCH[use_https] + BASE_URL
        
        self.assertEqual(pv.projects().url, url + 'projects')
        self.assertEqual(pv.projects(123).url, url + 'projects/123')
        self.assertEqual(pv.projects('123').url, url + 'projects/123')
        self.assertEqual(pv.projects('123').stories().url, 
                      url + 'projects/123/stories')
        self.assertEqual(pv.projects('123').stories(filter='state:unstarted').url,
                      url + 'projects/123/stories?filter=state%3Aunstarted')

    def test_https_urls(self):
        self._test_url_strings(use_https=True)

    def test_http_urls(self):
        self._test_url_strings(use_https=False)


if __name__ == '__main__':
    unittest.main()
