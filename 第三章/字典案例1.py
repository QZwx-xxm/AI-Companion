# 开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用字典结构存储商品数据，通过控制台菜单与用户交互。具体功能如下：
#
# 1.添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
# 2.修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
# 3.删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
# 4.查询购物车：将购物车中的商品信息展示出来，格式为："商品名称：xxx，商品价格：xxx，商品数量：xxx"。
# 5.退出购物车
shopping_goods = {}
while True:
    print("########## 购物车系统 ##########")
    print("#        1. 添加购物车         #")
    print("#        2. 修改购物车         #")
    print("#        3. 删除购物车         #")
    print("#        4. 查询购物车         #")
    print("#        5. 退出购物车         #")
    print("################################")
    choice = input("请选择你要执行的项目（1-5）：")
    match choice:
        case "1":
            goods_name = input("请输入您想添加的商品名：")
            goods_price = float(input("请输入您想添加的商品价格："))
            goods_number = int(input("请输入您想添加的商品数量："))
            if goods_name in shopping_goods:
                print("已添加过此商品！")
            else:
                shopping_goods[goods_name] = {"price": goods_price, "number": goods_number}
                print("商品添加完成！")
        case "2":
            goods_name = input("请输入您想修改的商品名：")
            if goods_name not in shopping_goods:
                print("商品出现问题，请重新输入！")
                continue
            else:
                goods_price = float(input("请输入您想修改的商品价格："))
                goods_number = int(input("请输入您想修改的商品数量："))
                shopping_goods[goods_name] = {"price": goods_price, "number": goods_number}
                print("商品修改完成！")


        case "3":
            goods_name = input("请输入您想删除的商品名：")
            if goods_name not in shopping_goods:
                print("商品出现问题，请重新输入！")
            else:
                del shopping_goods[goods_name]
                print("商品删除完成！")
        case "4":
            for goods_name in shopping_goods:
                goods_info = shopping_goods[goods_name]
                print(f"商品名：{goods_name}，商品价格：{goods_info["price"]}，商品数量：{goods_info["number"]}")
        case "5":
            print("Byb~")
            break
        case _:
            print("非法输入，请重试！")
