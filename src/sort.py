from Animal import Animal


def merge(l1, l2):
    """
    Merge two lists together
    :param l1: The left list
    :param l2: The right list
    :return: A merged list of the left and right lists.
    """
    i = 0
    j = 0
    tmp = []

    # make the comparisons between the two lists
    while i < len(l1) and j < len(l2):
        if l1[i].resource_amount > l2[j].resource_amount:  # using > since want largest resource at top of list
            tmp.append(l1[i])
            i += 1
        else:
            tmp.append(l2[j])
            j += 1

    # append what was left over in l1
    while i < len(l1):
        tmp.append(l1[i])
        i += 1

    # append what was left over in l2
    while j < len(l2):
        tmp.append(l2[j])
        j += 1

    return tmp


def mergesort(orig_list: list[Animal], n):
    """
    Perform mergesort on an unsorted list. Runtime: O(nlogn).
    :param orig_list: The original list
    :param n: The length of the list.
    :return:
    """
    if n == 1:
        return orig_list

    # get the middle index of the array
    middle = int(n/2)

    # split the array into two half's
    left = orig_list[:middle]
    right = orig_list[middle:]

    # recursively split the arrays
    lefts = mergesort(left, middle)
    rights = mergesort(right, n-middle)

    return merge(lefts, rights)
