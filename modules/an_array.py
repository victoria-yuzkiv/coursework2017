import ctypes


class AnArray:
    """
    Creates an array and gives some tools to work with it.
    """
    def __init__(self, size):
        """
        Creates an array with the length size.

        :param size: the size of the array.
        """
        assert size > 0, "Array size must be > 0"
        self._size = size
        pyarraytype = ctypes.py_object * size
        self._elements = pyarraytype()
        for i in range(len(self)):
            self._elements[i] = None

    def __len__(self):
        """
        Returns the length of the array.

        :return: the size of the array. 
        """
        return self._size

    def __getitem__(self, index):
        """
        Gets the value of the element.

        :param index: the index of element.
        :return: value of the element.
        """
        if not 0 <= index < self._size:
            raise IndexError('Invalid index')
        return self._elements[index]

    def __setitem__(self, index, value):
        """
        Puts the value in the array element at index position.

        :param index: the index element.
        :param value: the value of element.
        """
        if not 0 <= index < self._size:
            raise IndexError('Invalid index')
        self._elements[index] = value
