from __future__ import annotations
from typing import TypeVar, Generic


T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, data: T,next_node=None, previous_node=None):
        self.__data = data
        self.__next: Node | None = next_node
        self.__previous: Node | None = previous_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, new_data):
        self.__data = new_data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self,new_next: Node[T]):
        self.__next = new_next

    @property
    def previous(self):
        return self.__previous

    @previous.setter
    def previous(self, previous_node: Node[T]):
        self.__previous = previous_node

    def __str__(self):
        return str(self.__data)