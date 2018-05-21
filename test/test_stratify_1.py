#!/usr/bin/env python3

import unittest

import stratify


class TestExclude(unittest.TestCase):

    def test_centre1(self):
        evecs=[[0,0,0],[-1,0,1],[1,0,1],[0,4,0]]
        c1 = stratify.getCentroid(evecs,1,[0,1])
        self.assertEqual(c1,0)

    def test_centre2(self):
        evecs=[[0,0,0],[-1,0,1],[1,0,1],[0,4,0]]
        c1 = stratify.getCentroid(evecs,0,[0,1])
        self.assertEqual(c1,-0.5)

if __name__ == '__main__':


    unittest.main()
