from dataclasses import dataclass


class MagicList:

    def __init__(self, cls_type=None):
        self.cls_type = cls_type
        self.array = []
        self.max_index = 0

    def __getitem__(self, item):
        if item > self.max_index:
            raise IndexError("list index out of range")

        if item == self.max_index:
            if self.cls_type is None:
                raise IndexError("list index out of range")
            else:
                new_item = self.cls_type()
                self.array.append(new_item)
                self.max_index += 1
                return new_item

        else:
            return self.array[item]

    def __setitem__(self, key, value):
        if key > self.max_index:
            raise IndexError("list index out of range")
        elif key == self.max_index:
                self.max_index += 1
                self.array.append(value)
        else:
                self.array[key] = value

    def __repr__(self):
        return str(self.array)


if __name__ == "__main__":

    @dataclass
    class Person:
        age: int = 1

    a = MagicList(cls_type=Person)
    a[0].age = 5
    # a[1] = 3
    # a[0] = 2
    print(a)
