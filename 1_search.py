#!/usr/bin/env python3

def search_in_nested_list_v1(item, l):
    """Searches a nested list to depth 2 for for an item.

    Args:
        item: item to search for (tests for equality)
        l: the list to search

    Returns:
        if item is found: the found item; if not found: None

    """

    for i in l:
        if item == i:
            return i
        elif isinstance(i, list):
            for j in i:
                if item == j:
                    return j

    return None

def search_in_nested_list_v2(item, l):
    """Searches a nested list to arbitrary depth for for an item.

    Args:
        item: item to search for (tests for equality)
        l: the list to search

    Returns:
        if item is found: the found item; if not found: None

    """
    depth = 0
    istack = []
    lstack = []
    i = 0
    while True:
        if item == l[i]:
            return l[i]
        elif isinstance(l[i],list):
            depth += 1
            lstack.append(l)
            l = l[i]
            istack.append(i)
            i = 0
            continue
        i += 1
        if i >= len(l):
            if depth > 0:
                i = istack.pop()
                l = lstack.pop()
            else:
                break

    return None

def test_search_in_nested_list():

    f = search_in_nested_list_v1

    inp = [3, 6, 7, "foo", "bar"]
    out = f(7, inp)
    assert(out == 7)

    inp = [3, 6, 7, "foo", "bar"]
    out = f("baz", inp)
    assert(out is None)

    inp = [3, 6, [ 7, "foo" ], "bar"]
    out = f("foo", inp)
    assert(out == "foo")

    inp = [3, [6, [ 7, "foo", [ "bar" ] ] ]]
    out = f("bar", inp)
    assert(out == "bar")

if __name__ == '__main__':
    test_search_in_nested_list()
