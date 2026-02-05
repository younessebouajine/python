#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def display_info(self, plant_type: str) -> None:
        message = (
            f"{self.name} ({plant_type}): "
            f"{self.height}cm, {self.age} days"
        )
        print(message, end="")


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def display_info(self) -> None:
        super().display_info("Flower")
        print(f", {self.color} color")

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: int,
                 age: int, trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def display_info(self) -> None:
        super().display_info("Tree")
        print(f", {self.trunk_diameter}cm diameter")

    def produce_shade(self) -> None:
        print(f"{self.name} provides 78 square meters of shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: int,
                 age: int, harvest_season: str, nutritional_value: str):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def display_info(self) -> None:
        super().display_info("Vegetable")
        print(f", {self.harvest_season} harvest")

    def show_benefits(self) -> None:
        print(f"{self.name} is rich in {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    flower = Flower("Rose", 25, 30, "red")
    tree = Tree("Oak", 500, 1825, 50)
    vegetable = Vegetable("Tomato", 80, 90, "summer", "vitamin c")

    print()
    flower.display_info()
    flower.bloom()

    print()
    tree.display_info()
    tree.produce_shade()

    print()
    vegetable.display_info()
    vegetable.show_benefits()
