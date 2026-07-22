class Car:
    def __init__(self, s_name, s_color, s_price):
        self.name = s_name
        self.color = s_color
        self.price = s_price

    def sopping(self):
        print(f"正在录入{self.color}的{self.name}")

    def total(self, num, dicount):
        total_price = self.price * num - dicount
        return total_price


c = Car("苹果", "红色", 5)
c.sopping()
total = c.total(2, 3)
print(f"{total}是总价")
print(c.__dict__)


# class Car:
#     pass
# c=Car()
# c.name="苹果"
# c.color="红色"
# c.price=5
# print(c.__dict__)
