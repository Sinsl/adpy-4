from FlatIterator import FlatIterator
from flatGenerator import flat_generator

nested_list = [
	['a', 'b', 'c'],
    2,
	['d', 'e', 'f', 'h', False],
    'element',
	[1, 2, None],
]
# nested_list = {'1': 1}

def main_iterator():
    '''Проверка только на один уровень, список там или нет'''

    try:
        for item in FlatIterator(nested_list):
            print(item)

        flat_list = [item for item in FlatIterator(nested_list)]
        print(flat_list)

    except Exception as error:
        print('Caught this error: ' + repr(error))


def main_generator():
    '''Проверка только на один уровень, список там или нет'''

    try:

        for item in  flat_generator(nested_list):
            print(item)

        new_flat = [item for item in flat_generator(nested_list)]
        print(new_flat)
    
    except Exception as error:
        print('Caught this error: ' + repr(error))



if __name__ == '__main__':
    main_iterator()
    main_generator()