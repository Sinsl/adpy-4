from FlatIterator import FlatIterator
from flatGenerator import flat_generator
import types

list_of_lists = [
	['a', 'b', 'c'],
    2,
	['d', 'e', 'f', 'h', False],
    'element',
	[1, 2, None],
]
# list_of_lists = {'1': 1}

def main_iterator():
    '''Проверка только на один уровень, список там или нет'''

    try:
        for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists),
            ['a', 'b', 'c', 2, 'd', 'e', 'f', 'h', False, 'element', 1, 2, None]
        ):
            assert flat_iterator_item == check_item
            print(flat_iterator_item)

        assert list(FlatIterator(list_of_lists)) == ['a', 'b', 'c', 2, 'd', 'e', 'f', 'h', False, 'element', 1, 2, None]

    except Exception as error:
        print('Caught this error: ' + repr(error))


def main_generator():
    '''Проверка только на один уровень, список там или нет'''

    try:

        for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists),
            ['a', 'b', 'c', 2, 'd', 'e', 'f', 'h', False, 'element', 1, 2, None]
        ):
            assert flat_iterator_item == check_item
            print(flat_iterator_item)

        assert list(flat_generator(list_of_lists)) == ['a', 'b', 'c', 2, 'd', 'e', 'f', 'h', False, 'element', 1, 2, None]

        assert isinstance(flat_generator(list_of_lists), types.GeneratorType)
    
    except Exception as error:
        print('Caught this error: ' + repr(error))



if __name__ == '__main__':
    main_iterator()
    main_generator()