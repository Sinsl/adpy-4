
def flat_generator(some_list):
    print('Start generator')
    if not isinstance(some_list, list):
        raise Exception('Аргумент не является списком')
    
    for item_one_level in some_list:
        if isinstance(item_one_level, list):
            for item_two_level in item_one_level:
                yield item_two_level
        else:
            yield item_one_level