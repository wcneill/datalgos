
def longest_ss(s):
    """
    find the longest sub-string with no repeated characters.
    :param s: String
    :return: longest sub-string of s with no repeating characters
    """

    # starting with size = 2, create a sliding window
    # move window across string s until finding first sub-string w/ no repeats
    # add that sub-string to "max string"
    # when found, move on to size +=1
    # repeat
    # when size of window = size of string, exit.

    max_string = s[0]
    for n in range(2, len(s)):
        diff = len(s) - n
        for i in range(diff + 1):
            if not repeats(s, i, i + n):
                max_string = s[i: i+n]
                print(f'start {i}, end {i + n}, string: {max_string}')
                break

    return max_string


def repeats(s, i, j):
    """
    Return true if repeating characters found in s[i, j]
    :param s: The string to analyze
    :param i: Start index of sub-string
    :param j: End of sub-string
    :return:
    """

    unique = set(s[i: j])
    if len(unique) < len(s[i: j]):
        return True
    return False


if __name__ == '__main__':

    test = 'bbbesttlight'
    print(f'longest string is {longest_ss(test)}')
