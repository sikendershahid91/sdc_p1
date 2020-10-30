import unittest
import numpy as np
import src.image_processing as imp

class ImageProcessingTest( unittest.TestCase ):
    def test_canary(self):
        self.assertTrue(self)

    def test_get_canny_filter(self):
        print( imp.get_canny_filter() )
        pass
