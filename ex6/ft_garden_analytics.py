class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height
        self.total_growth = 0

    def grow(self, amount=1):
        self.height += amount
        self.total_growth += amount
        print(f"{self.name} grew {amount}cm")

    def describe(self):
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color
        self.is_blooming = True

    def bloom(self):
        self.is_blooming = True
        print(f"{self.name} is blooming!")

    def describe(self):
        state = "blooming" if self.is_blooming else "not blooming"
        return f"{self.name}: {self.height}cm, {self.color} flowers ({state})"


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, prize_points):
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def describe(self):
        state = "blooming" if self.is_blooming else "not blooming"
        return (
            f"{self.name}: {self.height}cm, {self.color} flowers ({state}), "
            f"Prize points: {self.prize_points}"
        )


class Garden:
    def __init__(self, owner):
        self.owner = owner
        self.plants = []

    def add_plant(self, plant):
        self.plants.append(plant)

    def help_all_grow(self):
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(1)


class GardenManager:
    managed_gardens_count = 0

    class GardenStats:
        @staticmethod
        def plants_added(garden):
            return len(garden.plants)

        @staticmethod
        def total_growth(garden):
            total = 0
            for plant in garden.plants:
                total += plant.total_growth
            return total

        @staticmethod
        def type_breakdown(garden):
            regular = 0
            flowering = 0
            prize = 0

            for plant in garden.plants:
                if isinstance(plant, PrizeFlower):
                    prize += 1
                elif isinstance(plant, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1

            return regular, flowering, prize

        @staticmethod
        def garden_score(garden):
            score = 0
            for plant in garden.plants:
                score += plant.height
                if isinstance(plant, PrizeFlower):
                    score += plant.prize_points * 10
            return score

    def __init__(self):
        self.gardens = {}

    def get_or_create_garden(self, owner):
        if owner not in self.gardens:
            self.gardens[owner] = Garden(owner)
            GardenManager.managed_gardens_count += 1
        return self.gardens[owner]

    def add_plant_to_garden(self, owner, plant):
        garden = self.get_or_create_garden(owner)
        garden.add_plant(plant)
        print(f"Added {plant.name} to {owner}'s garden")

    def print_garden_report(self, owner):
        garden = self.get_or_create_garden(owner)

        print(f"=== {owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in garden.plants:
            print(f"- {plant.describe()}")

        added = GardenManager.GardenStats.plants_added(garden)
        growth = GardenManager.GardenStats.total_growth(garden)
        regular, flowering, prize = GardenManager.GardenStats.type_breakdown(garden)

        print(f"Plants added: {added}, Total growth: {growth}cm")
        print(f"Plant types: {regular} regular, {flowering} flowering, {prize} prize flowers")

    @staticmethod
    def validate_height(height):
        return isinstance(height, int) and height >= 0

    @classmethod
    def create_garden_network(cls):
        manager = cls()
        manager.get_or_create_garden("Alice")
        manager.get_or_create_garden("Bob")
        return manager


# def test_plant_chain():
#     oak = Plant("Oak Tree", 100)
#     rose = FloweringPlant("Rose", 25, "red")
#     sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

#     oak.grow(1)
#     rose.grow(1)
#     sunflower.grow(1)

#     print(oak.describe())
#     print(rose.describe())
#     print(sunflower.describe())


def test_manager_demo():
    print("=== Garden Management System Demo ===")

    manager = GardenManager.create_garden_network()

    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

    manager.add_plant_to_garden("Alice", oak)
    manager.add_plant_to_garden("Alice", rose)
    manager.add_plant_to_garden("Alice", sunflower)

    manager.gardens["Alice"].help_all_grow()

    manager.print_garden_report("Alice")

    print(f"Height validation test: {GardenManager.validate_height(10)}")

    alice_score = GardenManager.GardenStats.garden_score(manager.gardens["Alice"])
    bob_score = GardenManager.GardenStats.garden_score(manager.gardens["Bob"])
    print(f"Garden scores - Alice: {alice_score}, Bob: {bob_score}")

    print(f"Total gardens managed: {GardenManager.managed_gardens_count}")


if __name__ == "__main__":
    # Tests first
    # test_plant_chain()
    # Then full demo
    test_manager_demo()
