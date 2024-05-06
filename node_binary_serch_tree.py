from __future__ import annotations
from typing import TypeVar, Generic


T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, data: T, right_node=None, left_node=None):
        self.__data = data
        self.__left: Node | None = left_node
        self.__right: Node | None = right_node

    def is_leaf(self):
        return self.__left is None and self.__right is None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, new_data):
        self.__data = new_data

    @property
    def left(self):
        return self.__left

    @property
    def right(self):
        return self.__right

    @left.setter
    def left(self, left_node: Node[T]):
        self.__left = left_node

    @right.setter
    def right(self, right_node: Node[T]):
        self.__right = right_node
