"""https://www.codewars.com/kata/coloured-triangles"""
from utils_anviks import stopwatch


@stopwatch
def triangle(row: str):
    colours = 0b111
    mapper = {
        'R': 1 << 0,
        'G': 1 << 1,
        'B': 1 << 2
    }
    row = [mapper[char] for char in row]
    len_row = len(row)

    for j in range(len_row, 0, -1):
        for i in range(1, j):
            if row[i - 1] != row[i]:
                # row[i - 1] = chr(colours - ord(row[i - 1]) - ord(row[i]))
                row[i - 1] = colours - (row[i - 1] | row[i])

    return list(mapper.keys())[row[0] >> 1]


def main():
    print(triangle('GB'), 'R')
    print(triangle('RRR'), 'R')
    print(triangle('RGBG'), 'B')
    print(triangle('RBRGBRB'), 'G')
    print(triangle('RBRGBRBGGRRRBGBBBGG'), 'G')
    print(triangle('B'), 'B')
    print(triangle(
        'BRRBRRGGGGGGBBGBRRGRRGBGGRBBGBBGBRRBGBBGGBRRRRRGBBBBRRGBRBBBBBGGRBGBBRRRGRRBBGGBRBRGBRGRGGGGGRRBRGGBRBRBBGGGRBGRRBRBBRRBRBGBGBRRGGBRGRGBGRGBBBRRGBRRGGGRRBRRBRGRBRBBGBGGGBGRBRGRBGRBGRRRBRGRBGBGRRBBRGBRBRRGRRGGGGBGBBGRRGBGGGRBBGGBBBGRRBBGRBRBBRBRGGGBRRGRGRRRGBGBBRGRGBGGGBBRRRGRRBRBGGBBRGB'))
    print(triangle(
        'RRGRRRRGRGBRRRBBRGGBRBRGRBBBGBRGRBRBBBGBRRGRRGBGRBGBGBRRRRGRBGBBGBBGBRRBRRGBRRGBBGGRGGRRBBRRRRRGRRBBBBBRGRGRGBBGGBBGRGRRGRGBGBGRBBBGGRGGBGRBBRBGGBGRBRBRRGRRRGRRGGRRGRRGBGBRBRBGBRRGGRRBBGBGBBBRGGRRRBRBRBGGRGBRBGRRRRRRRBGBGBGRGBRGGGBGRGGRGGRGRBRRGBGGGRGRRRBBBRRBGRBBRRGRBBGRGBRGRGGRRRGRRGGBGBBGBGBGRGGBBBGRBBGRBRGGBGRBBGBGBBGGGRBGGGRGGGRGBGRGBBBBRGRRRRGRGRBRBGBRRBGBGRBGGRGRRRBRRGRBBGBGGBBRBBGRGBBGBGRGRRRBRRRRBBRGGGBRBGGBBRBGGRRGGRBGRBRGBGRRGRRBBBGBBBGRBRRBRBBGBRBBBRRGGGBBBRRGRRBRRRBRGRGGRBBRGBGRRBRBRGGBGRBGBBBGGGRGBRBRGGRBRRRGRRGBBGBBRRGGGGGRBGRGRBRGGGBBRBRBGGRBGRGBRRRGGGBBBGGGBGGBRRBBGRGBBRGBGBGGBGGBRRGGGGBRRBGBGRBGBRBRGRBRBBGRGBRRBBBRGGBRBGBBGBBGBBBRBBGGGBGRGBBBRRBBBRBBGRBGBRGBRRBRGBBBBBBBGGBBRGRBBRBRGRGGRGBBBRBGBRGRG'))


if __name__ == '__main__':
    main()
