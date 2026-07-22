# 练习
# 采用面向对象的编程思想，开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用自定义对象存储商品数据，通过控制台菜单与用户交互。具体功能如下：
# 1.添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
# 2.修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
# 3.删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
# 4.查询购物车：将购物车中的商品信息展示出来，格式为："商品名称：xxx，商品价格：xxx，商品数量：xxx"。
# 5.退出购物车
# 商品类Goods
class Goods:
    # 商品信息
    def __init__(self, name, price, num):
        self.name = name
        self.price = price
        self.num = num

    # 修改商品信息
    def update(self, price, num):
        self.price = price
        self.num = num

    # 输出格式
    def __str__(self):
        return f"商品名称：{self.name}，商品价格：{self.price}，商品数量：{self.num}"


# c=Goods("苹果","12","1")
# d=Goods("葡萄","10","2")
# print(c)
# print(d)
# c.update(20,2)
# print(c)

# 购物车管理系统ShoppingCart
class ShoppingCart:
    version = 1.2

    def __init__(self):
        self.shopping_list = []

    # 添加购物车
    def add_goods(self):
        name = input("请输入想要添加的商品名:")
        for s in self.shopping_list:
            if name == s.name:
                print("商品已存在，请重新加入商品！")
                return
        price = float(input("请输入此商品的金额："))
        num = float(input("请输入此商品的数量："))
        s = Goods(name, price, num)
        self.shopping_list.append(s)
        print("商品添加成功！！")

    # 修改购物车:要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
    def update(self):
        name = input("请输入想要修改的商品名：")
        for s in self.shopping_list:
            if name == s.name:
                print(s)
                price = float(input("请输入想要修改的商品的金额："))
                num = float(input("请输入想要修改的商品的数量："))
                s.update(price, num)
                print(s)
                print("商品修改成功！！")
                return
        print("商品不存在，请重新输入商品！")
        return

    # 删除购物车:要求用户输入要删除的购物车名称，根据名称删除购物车中的商品
    def lat(self):
        name = input("请输入想要删除的商品名：")
        for s in self.shopping_list:
            if name == s.name:
                self.shopping_list.remove(s)
                print("商品删除成功！！")
                return
        else:
            print("商品不存在，请重新输入商品名称！")
            return

    # 查询购物车:将购物车中的商品信息展示出来，格式为："商品名称：xxx，商品价格：xxx，商品数量：xxx"
    def select(self):
        name = input("请输入想要查询的商品名：")
        for s in self.shopping_list:
            if name == s.name:
                self.shopping_list.remove(s)
                print(s)
        return

    # 列出购物车
    def list(self):
        for s in self.shopping_list:
            print(s)
        return

    # 运行购物车
    def run(self):
        print(f"欢迎使用教务系统{ShoppingCart.version}")
        bet = """
        ####################################【教务系统】####################################
        # 1. 添加购物车  2. 修改购物车  3. 删除购物车  4. 查询购物车  5. 列出购物车  6. 退出系统  #
        ##################################################################################
        """
        while True:
            print(bet)
            choice = input("请输入您想要进行的操作（1-7）:")
            match choice:
                case "1":
                    self.add_goods()
                case "2":
                    self.update()
                case "3":
                    self.lat()
                case "4":
                    self.select()
                case "5":
                    self.list()
                case "6":
                    print("欢迎下次使用~")
                    break
                case _:
                    print("输入有误，请重新输入~")


if __name__ == '__main__':
    shopping_cart = ShoppingCart()
    shopping_cart.run()
