#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: str, age: str) -> None:
        self.name = name
        self.height = height
        self.age = age

    def disply(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


patnt1 = Plant("Rose", "25", "30")
patnt2 = Plant("Sunflower", "80", "45")
patnt3 = Plant("Cactus", "15", "120")
print("=== Garden Plant Registry ===")
patnt1.disply()
patnt2.disply()
patnt3.disply()
