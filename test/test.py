import unittest

from src import image_processing
from src import utils


class TestImage(unittest.TestCase):
    def test_reading(self):
        img = image_processing.read_image(utils.path_from_root("image_samples/IMG_7317.JPG"))
        self.assertEqual(img.shape, (3024, 3024, 3))
        with self.assertRaises(IOError):
            image_processing.read_image("")


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestImage())
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
