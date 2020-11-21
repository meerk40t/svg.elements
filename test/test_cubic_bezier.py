from __future__ import print_function

import unittest
from random import *

from svgelements import *


def get_random_cubic_bezier():
    return CubicBezier((random() * 50, random() * 50), (random() * 50, random() * 50),
                       (random() * 50, random() * 50), (random() * 50, random() * 50))


class TestElementCubicBezierLength(unittest.TestCase):

    def test_cubic_bezier_length(self):
        n = 100
        error = 0
        for _ in range(n):
            b = get_random_cubic_bezier()
            l1 = b._length_scipy()
            l2 = b._length_default(error=1e-6)
            c = abs(l1 - l2)
            error += c
            self.assertAlmostEqual(l1, l2, places=1)
        print("Average cubic-line error: %g" % (error / n))


class TestElementCubicBezierPoint(unittest.TestCase):

    def test_cubic_bezier_point_start_stop(self):
        for _ in range(1000):
            b = get_random_cubic_bezier()
            self.assertEqual(b.start, b.point(0))
            self.assertEqual(b.end, b.point(1))
            self.assertEqual(Point(np.array([list(b.start), list(b.end)])),
                             b.point(np.array([0, 1])))

    def test_cubic_bezier_point_implementations_match(self):
        for _ in range(1000):
            b = get_random_cubic_bezier()

            pos = np.linspace(0, 1, 100)
            vec_res = b.point(pos)

            for p, x, y in zip(pos, vec_res.x, vec_res.y):
                self.assertEqual(b.point(p), Point(x, y))
