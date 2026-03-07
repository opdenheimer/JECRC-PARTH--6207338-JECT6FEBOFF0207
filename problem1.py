#E-Commerce Order Revenue Analyzer
class Solution:

    def city_revenue(self, orders):
        revenue = {}
        ## Write your code here and don't forget to return value.
        for order in orders:
            city = order["city"]
            amount = order["amount"]

            if city in revenue:
                revenue[city] += amount
            else:
                revenue[city] = amount

        highest_city = max(revenue, key=revenue.get)
        l1=[]
        l1.append(revenue)
        l1.append(highest_city)
        return l1