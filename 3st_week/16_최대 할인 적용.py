shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    prices.sort(reverse=True)
    coupons.sort(reverse=True)
    priceIdx = 0
    couponIdx = 0
    discount_price = 0

    while priceIdx < len(prices) and couponIdx < len(coupons):
        discount_price += prices[priceIdx] * (100 - coupons[couponIdx]) // 100
        priceIdx += 1
        couponIdx += 1
    while priceIdx < len(prices):
        discount_price += prices[priceIdx]
        priceIdx += 1

    return discount_price


print("정답 = 926000 / 현재 풀이 값 = ", get_max_discounted_price([30000, 2000, 1500000], [20, 40]))
print("정답 = 485000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], [10, 70, 30, 20]))
print("정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], []))
print("정답 = 1458000 / 현재 풀이 값 = ", get_max_discounted_price([20000, 100000, 1500000], [10, 10, 10]))