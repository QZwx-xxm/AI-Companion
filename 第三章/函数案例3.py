# 定义一个函数，用于根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额。
# 具体规则如下：
# 1.优惠券需要商品金额满5000才可以使用，且优惠券金额不能超过商品总价。
# 2.积分抵扣需要商品总金额满5000才可以使用，100积分抵扣1元（且抵扣金额不能超过商品总价，积分只能整百抵扣）。
def product_amount(*args, coupon, points, freight):
    shopping_price = [goods[1] * goods[2] for goods in args]
    origin_price=sum(shopping_price)
    if origin_price>=5000 and origin_price<=coupon:
        total_price=origin_price-coupon
    if origin_price >= 5000 and points//100 <= origin_price :
        finish_price=total_price-points//100
    total=finish_price+freight
