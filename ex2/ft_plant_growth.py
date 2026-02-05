#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.__name = name
        self.__height = height
        self.__age = age
        self.__old_height = height

    def grow(self, amount: int) -> None:
        self.__height += amount

    def age(self, days: int) -> None:
        self.__age += days

    def display(self) -> None:
        print(f"{self.__name}: {self.__height}cm, {self.__age} days old")

    def get_info(self) -> None:
        day_grow = self.__height - self.__old_height
        print(f"Growth this week: +{day_grow}cm")
        self.__old_height = self.__height


plant1 = Plant("Rose", 25, 30)
print("=== Day 1 ===")
plant1.display()
plant1.grow(6)
plant1.age(6)
print("=== Day 7 ===")
plant1.display()
plant1.get_info()
