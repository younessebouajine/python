
class Plant:
    Total_Plant = 0

    def __init__(self, name: str, start_height: float, start_age: int) -> None:
        Plant.Total_Plant += 1
        self.name = name.capitalize()
        self.starting_height = start_height
        self.starting_age = start_age
        message = (
            f"Created: {self.name} "
            f"({self.starting_height}cm, {self.starting_age} days)"
        )
        print(message)

    def Display_Total(self) -> None:
        print(f"\nTotal plants created: {self.Total_Plant}", end="")


print("=== Plant Factory Output ===")
plant1 = Plant("Rose", 25, 30)
plant2 = Plant("Oak", 200, 365)
plant3 = Plant("Cactus", 5, 90)
plant4 = Plant("Sunflower", 80, 45)
plant5 = Plant("Fern", 15, 120)
plant1.Display_Total()
