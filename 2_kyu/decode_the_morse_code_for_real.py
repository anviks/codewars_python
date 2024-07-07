"""https://www.codewars.com/kata/decode-the-morse-code-for-real"""

from preloaded import MORSE_CODE

MORSE_CODE[""] = ""


def decode_bits_advanced(bits: str):
    bits = bits.strip("0")

    if bits == "":
        return ""

    consecutive_bit_counts = []
    consecutive_count = 0
    previous_bit = bits[0]

    for bit in bits:
        if bit == previous_bit:
            consecutive_count += 1
        else:
            consecutive_bit_counts.append(consecutive_count)
            consecutive_count = 1
        previous_bit = bit
    consecutive_bit_counts.append(consecutive_count)

    bits_per_dot = min(consecutive_bit_counts)
    print(consecutive_bit_counts.count(bits_per_dot - 1), consecutive_bit_counts.count(bits_per_dot),
          consecutive_bit_counts.count(bits_per_dot + 1))

    return bits.replace('0000000' * bits_per_dot, '   ') \
        .replace('000000' * bits_per_dot, '   ') \
        .replace('111' * bits_per_dot, '-') \
        .replace('11' * bits_per_dot, '-') \
        .replace('000' * bits_per_dot, ' ') \
        .replace('00' * bits_per_dot, ' ') \
        .replace('1' * bits_per_dot, '.') \
        .replace('0' * bits_per_dot, '')


def decode_morse(morse_code):
    return " ".join(
        ["".join([str(MORSE_CODE.get(letter)) for letter in word.split(" ")]) for word in
         morse_code.split("   ")]).strip()


if __name__ == '__main__':
    print("Example from description")
    print((decode_bits_advanced(
        "000000001101101001110000011000000111111010011111001111110000000000011101111111101111101111100000010110001111"
        "1100000111110011101100000100000"
    )))
    # HEY JUDE

    print("\nVery short messages:")
    print(decode_morse(decode_bits_advanced("")))  #
    print(decode_morse(decode_bits_advanced("0")))  #
    print(decode_morse(decode_bits_advanced("000000000000000000000000000000000000000000")))  #
    print(decode_morse(decode_bits_advanced("1")))  # E
    print(decode_morse(decode_bits_advanced("101")))  # I
    print(decode_morse(decode_bits_advanced("1001")))  # EE
    print(decode_morse(decode_bits_advanced("10001")))  # EE
    print(decode_morse(decode_bits_advanced("100001")))  # EE
    print(decode_morse(decode_bits_advanced("10000001")))  # E E
    print(decode_morse(decode_bits_advanced("100000001")))  # E E
    print(decode_morse(decode_bits_advanced("1000000001")))  # E E
    print(decode_morse(decode_bits_advanced("10000000001")))  # E E
    print(decode_morse(decode_bits_advanced("10111")))  # A
    print(decode_morse(decode_bits_advanced("1110111")))  # M
    print(decode_morse(decode_bits_advanced("111000111")))  # I

    print("\nMultiple bits per dot:")
    print(decode_morse(decode_bits_advanced("111")))  # E
    print(decode_morse(decode_bits_advanced("1111111")))  # E
    print(decode_morse(decode_bits_advanced("110011")))  # I
    print(decode_morse(decode_bits_advanced("111110000011111")))  # I
    print(decode_morse(decode_bits_advanced("11111100111111")))  # M

    print("\nExtra zeros:")
    print(decode_morse(decode_bits_advanced("01110")))  # E
    print(decode_morse(decode_bits_advanced("000000011100000")))  # E

    print("\nLong messages:")
    print(decode_morse(decode_bits_advanced(
        "110011001100110000001100000011111100110011111100111111000000000000001100111111001111110011111100000011001100"
        "1111110000001111110011001100000011"
    )))  # HEY JUDE
    print(decode_morse(decode_bits_advanced(
        "00000000000111"  # - > T
        "1111000000110100011101110000000011100000000000000000011111110111111000011011111000001111001111"
        "000111111000000010111000000111111100100011111001100000111111001011111000000000000001111111000011110101100000"
        "110001111100100000111111100011111100111111100000100011111100011111111000000011111111011100000000000000101100"
        "001111111101111000001111101111100111111100000000111110010110111110000000000001110111110111110111110000000100"
        "010011111000001111101111111100000011100111111000111110100000011000010010000000000000000001111111100111110111"
        "111000000100010010000111110000001000000001011111010000000000000111111000000111101000010011000000000011100000"
        "000000000011011111011110001000001000011111111100000000011111100111111000111011000001111110000110111110001111"
        "110000000000000000011111100001001100000111111011111110111111111000000011111100011111000010000000000000000000"
        "00000000000000000000000000000000000000000"
    )))  # THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
    print(decode_morse(decode_bits_advanced(
        "111110000011111110000111111000001111111111111110000111111111111110000001111111111111111000011100000111111000"
        "000011110000000000000000111111111111110000001111100000111111111111111000000111100000111111111111111000011111"
        "111111111100000000000000000000000000000000000111111111111111100000000000000011110000001111100000111100000001"
        "111000000000000001111100000000000000000000000000000000000111111111111111000001111111111111110000111110000011"
        "111111111111000000000000000011111110000001111110000000111111111111110000000000000000111100000011111000000000"
        "000000111111111111111000001111110001111111111111110000111100000000000000001111111111111100000001111000001111"
        "111111111100000000000000000000000000000000000111111111111111000001111110000111110000001111100000000000000011"
        "111100001111111111111111000000111100000000000000111111111111111000011111111111111100001111111111111100000000"
        "000000011111000000011111111111111100000001111111111111111100000000000000001111111111111110000011111000000000"
        "000000000000000000000000000111100011111000000111111111111111100000111000000000000000111111111111111100000111"
        "111111111100000011111111111111110000000000000011111111111111100000011111000011111100000011111111111111110000"
        "000000000000000000000000000000111100000111111111111111000000111111111111111000011111111111111110000000000000"
        "011111100011110000111111111111000000000000000011111111111111000000111111111111111000000000000001100000111111"
        "111111111000001111111111111111000001111100000000000000011111100001111100001111110000000000000000000000000000"
        "000000111111111111111100011111111111111110000011111111111111110000000000000001111000001111100001111000001111"
        "111111111110000000000000001111110000000000000001110000001111111111111110001111000000000000000000000000000000"
        "000000111111111111111000000000000000111111100001111000001111110000011111100000000000000011111100000000000000"
        "000000000000000000000001111110001111111111111111000001111000000111111100000000000000111100001111111111111110"
        "000000000000111111111111110000011111111111111110000011111000011111000000000000000111111111111110000011111100"
        "000111111111111111110000111111111111111000000000000000000000000000000000000011111111111111110000011111100000"
        "111100000000000001111111111111110000011111111111111110000111111111111111100000000000000011111111111111000000"
        "111111111111111000001111000000000000000111111000001111111111111100000011100000111111111111111100000111110000"
        "11111111111111"
    )))  # SOS! THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.