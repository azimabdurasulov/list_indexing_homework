def main(list_num):
    """
    A list of numbers consisting of several elements is given. Return the largest between the first and last elements.
    Args:
        list_num (list): parameter
    Returns:
        int: return answer
    """
    max = 0

    if list_num[0] <= list_num[-1]:
        max += list_num[-1]
    else:
        max += list_num[0]

    return max

print(main([7, 2, 3, 4, 6, 5]))