

class FlatIterator:

    def __init__(self, some_list):
        if not isinstance(some_list, list):
            raise Exception('Аргумент не является списком')
        self.some_list = some_list

    def __iter__(self):
        print('Start iterator')
        self.counter_one_level = 0
        self.counter_two_level = 0
        return self

    def __next__(self):

        if self.counter_one_level >= len(self.some_list):
            raise StopIteration

        result = None

        if isinstance(self.some_list[self.counter_one_level], list):
            result = self.some_list[self.counter_one_level][self.counter_two_level]
            if self.counter_two_level >= len(self.some_list[self.counter_one_level]) - 1:
                self.counter_two_level = 0
                self.counter_one_level += 1
            else:
                self.counter_two_level += 1
        else:
            result = self.some_list[self.counter_one_level]
            self.counter_one_level += 1

        return result