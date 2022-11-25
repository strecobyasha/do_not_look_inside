from copy import copy
from random import randint
from typing import Union


def bubble(data: list) -> list:
    repeat = True
    while repeat:
        repeat = False
        for index, element in enumerate(data[:-1]):
            if element > data[index+1]:
                data[index], data[index+1] = data[index+1], data[index]
                repeat = True

    return data


def selection(data: list) -> list:
    for i in range(len(data)-1):
        index_of_smallest_element = i
        for j in range(i+1, len(data)):
            if data[j] < data[index_of_smallest_element]:
                index_of_smallest_element = j
        data[i], data[index_of_smallest_element] = data[index_of_smallest_element], data[i]

    return data


def insertion(data: list) -> list:
    for index, element in enumerate(data[1:]):
        while index >= 0 and data[index] > element:
            data[index+1] = data[index]
            index -= 1
        data[index+1] = element

    return data


class Heap:

    def __init__(self, data: list):
        self.data = data
        self.size = len(data)

    def heapify(self, index: int, size: int) -> None:
        left_index = index * 2 + 1
        right_index = index * 2 + 2
        largest_element_index = index

        if left_index < size and self.data[left_index] > self.data[index]:
            largest_element_index = left_index
        if right_index < size and self.data[right_index] > self.data[largest_element_index]:
            largest_element_index = right_index

        if largest_element_index != index:
            self.data[index], self.data[largest_element_index] = self.data[largest_element_index], self.data[index]
            self.heapify(largest_element_index, size)

    def sort(self) -> list:
        for index in range(self.size, -1, -1):
            self.heapify(index, self.size)
        for index in range(self.size-1, 0, -1):
            self.data[0], self.data[index] = self.data[index], self.data[0]
            self.heapify(0, index)

        return self.data


class MergeSorting:

    def data_iterator(self, data: iter, counter: int) -> tuple[Union[int, None], int]:
        try:
            element = next(data)
        except StopIteration:
            element = None
        finally:
            counter -= 1

        return element, counter

    def merge(self, left: iter, right: iter, left_counter: int, right_counter: int) -> list:
        sorted_data = []
        left_element, left_counter = self.data_iterator(left, left_counter+1)
        right_element, right_counter = self.data_iterator(right, right_counter+1)

        while left_counter + right_counter > 0:
            if right_element is None or isinstance(left_element, int) and left_element < right_element:
                sorted_data.append(left_element)
                left_element, left_counter = self.data_iterator(left, left_counter)
            else:
                sorted_data.append(right_element)
                right_element, right_counter = self.data_iterator(right, right_counter)

        return sorted_data

    def split(self, data: list) -> list:
        data_length = len(data)
        if data_length > 1:
            left, right = self.split(data[:data_length//2]), self.split(data[data_length//2:])
            return self.merge(iter(left), iter(right), len(left), len(right))
        else:
            return data


def quick(data: list) -> list:
    def _quick(start: int, end: int):
        pointer = (start + end) // 2
        pivot = data[pointer]
        x, y = start, end
        while x < y:
            x += 1
            while data[x] < pivot:
                x += 1
            while data[y] > pivot and y > x:
                y -= 1
            data[x], data[y] = data[y], data[x]

        pointer = x
        if pointer - start - 1 > 1:
            _quick(start, pointer-1)
        if end - pointer > 1:
            _quick(pointer, end)

    _quick(-1, len(data)-1)

    return data


lst = [randint(1, 20) for _ in range(7)]


def test_bubble_sorting():
    lst_buble_sorted = bubble(copy(lst))
    assert lst_buble_sorted == sorted(lst)


def test_selection_sorting():
    lst_selection_sorted = selection(copy(lst))
    assert lst_selection_sorted == sorted(lst)


def test_insertion_sorting():
    lst_insertion_sorted = insertion(copy(lst))
    assert lst_insertion_sorted == sorted(lst)


def test_heap_sorting():
    heap = Heap(copy(lst))
    lst_heap_sorted = heap.sort()
    assert lst_heap_sorted == sorted(lst)


def test_merge_sorting():
    merge = MergeSorting()
    lst_merge_sorted = merge.split(copy(lst))
    assert lst_merge_sorted == sorted(lst)


def test_quick_sorting():
    lst_quick_sorted = quick(copy(lst))
    assert lst_quick_sorted == sorted(lst)
