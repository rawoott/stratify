#!/usr/bin/env python3

import unittest
import os
import stratify

this_dir = os.path.dirname(__file__)


class TestExclude(unittest.TestCase):

    def setUp(self):
        self.test_data = stratify.inputData(os.path.join(this_dir,"sample.evec"))


    def test_centre1(self):
        c1 = stratify.getCentroid(self.test_data[0],1,self.test_data[1]["KS3"])
        self.assertAlmostEqual(c1,-0.014050000000)



if __name__ == '__main__':


    unittest.main()
