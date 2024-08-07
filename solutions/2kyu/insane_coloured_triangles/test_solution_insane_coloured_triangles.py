"""https://www.codewars.com/kata/5a331ea7ee1aae8f24000175"""

import unittest

from parameterized import parameterized

from solution_insane_coloured_triangles import triangle


class InsaneColouredTriangles(unittest.TestCase):
    @parameterized.expand([
        ['B', 'B'],
        ['GB', 'R'],
        ['RRR', 'R'],
        ['RGBG', 'B'],
        ['RBRGBRB', 'G'],
        ['RBRGBRBGGRRRBGBBBGG', 'G'],
        ['BBRGBRBGGGRG', 'G'],
        ['BBRGBRBGGGG', 'R'],
        ['BBRGBRBGGG', 'R'],
    ])
    def test_basic_cases(self, _in, _out):
        self.assertEqual(triangle(_in), _out)

    @parameterized.expand([
        ['GRRBRRGGGGGGBBGBRRGRRGBGGRBBGBBGBRRBGBBGGBRRRRRGBBBBRRGBRBBBBBGGRBGBBRRRGRRBBGGBRBRGBRGRGGGGGRRBRG', 'G'],
        [
            'BRRBRRGGGGGGBBGBRRGRRGBGGRBBGBBGBRRBGBBGGBRRRRRGBBBBRRGBRBBBBBGGRBGBBRRRGRRBBGGBRBRGBRGRGGGGGRRBRGGBRBRBBGGGRBGRRBRBBRRBRBGBGBRRGGBRGRGBGRGBBBRRGBRRGGGRRBRRBRGRBRBBGBGGGBGRBRGRBGRBGRRRBRGRBGBGRRBBRGBRBRRGRRGGGGBGBBGRRGBGGGRBBGGBBBGRRBBGRBRBBRBRGGGBRRGRGRRRGBGBBRGRGBGGGBBRRRGRRBRBGGBBRGB',
            'G'],
        [
            'RRGRRRRGRGBRRRBBRGGBRBRGRBBBGBRGRBRBBBGBRRGRRGBGRBGBGBRRRRGRBGBBGBBGBRRBRRGBRRGBBGGRGGRRBBRRRRRGRRBBBBBRGRGRGBBGGBBGRGRRGRGBGBGRBBBGGRGGBGRBBRBGGBGRBRBRRGRRRGRRGGRRGRRGBGBRBRBGBRRGGRRBBGBGBBBRGGRRRBRBRBGGRGBRBGRRRRRRRBGBGBGRGBRGGGBGRGGRGGRGRBRRGBGGGRGRRRBBBRRBGRBBRRGRBBGRGBRGRGGRRRGRRGGBGBBGBGBGRGGBBBGRBBGRBRGGBGRBBGBGBBGGGRBGGGRGGGRGBGRGBBBBRGRRRRGRGRBRBGBRRBGBGRBGGRGRRRBRRGRBBGBGGBBRBBGRGBBGBGRGRRRBRRRRBBRGGGBRBGGBBRBGGRRGGRBGRBRGBGRRGRRBBBGBBBGRBRRBRBBGBRBBBRRGGGBBBRRGRRBRRRBRGRGGRBBRGBGRRBRBRGGBGRBGBBBGGGRGBRBRGGRBRRRGRRGBBGBBRRGGGGGRBGRGRBRGGGBBRBRBGGRBGRGBRRRGGGBBBGGGBGGBRRBBGRGBBRGBGBGGBGGBRRGGGGBRRBGBGRBGBRBRGRBRBBGRGBRRBBBRGGBRBGBBGBBGBBBRBBGGGBGRGBBBRRBBBRBBGRBGBRGBRRBRGBBBBBBBGGBBRGRBBRBRGRGGRGBBBRBGBRGRG',
            'G'],
        [
            'RRGRRRRGRGBRRRBBRGGBRRGRBBBGBRGRBRBBBGBRRGRRGBGRBGBGBRRRRGRBGBBGBBGBRRBRRGBRRGBBGGRGGRRBBRRRRRGRRBBBBBRGRGRGBBGGBBGRGRRGRGBGBGRBBBGGRGGBGRBBRBGGBGRBRBRRGRRRGRRGGRRGRRGBGBRBRBGBRRGGRRBBGBGBBBRGGRRRBRBRBGGRGBRBGRRRRRRRBGBGBGRGBRGGGBGRGGRGGRGRBRRGBGGGRGRRRBBBRRBGRBBRRGRBBGRGBRGRGGRRRGRRGGBGBBGBGBGRGGBBBGRBBGRBRGGBGRBBGBGBBGGGRBGGGRGGGRGBGRGBBBBRGRRRRGRGRBRBGBRRBGBGRBGGRGRRRBRRGRBBGBGGBBRBBGRGBBGBGRGRRRBRRRRBBRGGGBRBGGBBRBGGRRGGRBGRBRGBGRRGRRBBBGBBBGRBRRBRBBGBRBBBRRGGGBBBRRGRRBRRRBRGRGGRBBRGBGRRBRBRGGBGRBGBBBGGGRGBRBRGGRBRRRGRRGBBGBBRRGGGGGRBGRGRBRGGGBBRBRBGGRBGRGBRRRGGGBBBGGGBGGBRRBBGRGBBRGBGBGGBGGBRRGGGGBRRBGBGRBGBRBRGRBRBBGRGBRRBBBRGGBRBGBBGBBGBBBRBBGGGBGRGBBBRRBBBRBBGRBGBRGBRRBRGBBBBBBBGGBBRGRBBRBRGRGGRGBBBRBGBRGRG',
            'B'],
    ])
    def test_advanced_cases(self, _in, _out):
        self.assertEqual(triangle(_in), _out)
