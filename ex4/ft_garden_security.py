class SecurePlant:
    def __init__(self, name, height, age):
        self.__name = name.capitalize()
        self.__height = 0
        self.__age = 0

        print(f"Plant created: {self.__name}")
        self.set_height(height)
        self.set_age(age)

        message1 = (
            f"Current plant: "
            f"{self.__name} ({self.__height}cm, {self.__age} days)"
        )
        print(message1, end="")

    def get_height(self):
        return self.__height

    def set_height(self, new_height):
        if new_height >= 0:
            self.__height = new_height
            print(f"Height updated: {self.__height}cm [OK]")
        else:
            message2 = (
                f"Invalid operation attempted: "
                f"height {new_height}cm [REJECTED]"
            )
            print(message2)
            print("Security: Negative height rejected")

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if new_age >= 0:
            self.__age = new_age
            print(f"Age updated: {self.__age} days [OK]")
        else:
            message3 = (
                f"Invalid operation attempted: "
                f"age {new_age} days [REJECTED]"
            )
            print(message3)
            print("Security: Negative age rejected")


print("=== Garden Security System ===")
plant1 = SecurePlant("Rose", -25, -30)
