class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = sum(list_of_list, [])
        
    def __iter__(self):
        return self

    def __next__(self):
        if not self.list_of_list:
            raise StopIteration
        return self.list_of_list.pop(0)


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()