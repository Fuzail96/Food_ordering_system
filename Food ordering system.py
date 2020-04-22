#!/usr/bin/env python
# coding: utf-8

# In[5]:


class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        print(self.name + " $ " + self.price)

    def get_total_price(self, count):
            if count <= 3:
                total_price = self.price * count
            elif count > 3:
                total_price *= 0.9
            return round(total_price)


class Food(MenuItem):
    def __init__(self, name, price, calorie_count):
        super().__init__(name, price)
        self.calorie_count = calorie_count

    def info(self):
        print(self.name + " : $ " + str(self.price) + " (" + str(self.calorie_count) + "Kcal)"
              )


class Drink(MenuItem):
    def __init__(self, name, price, volume):
        super().__init__(name, price)
        self.volume = volume

    def info(self):
        print(self.name + " : $ " + str(self.price) + " (" + str(self.volume) + "ml)"
              )


food1 = Food("Sandwich", 2, 150)
food2 = Food("Chocolate_cake", 3, 200)
food3 = Food("Cream_Puff", 4, 180)

foods = [food1, food2, food3]

drink1 = Drink("Cococola", 5, 150)
drink2 = Drink("Mojito", 7, 100)
drink3 = Drink("Blue_Ice", 5, 150)

drinks = [drink1, drink2, drink3]

print("Foods")

index = 0

for food in foods:
    a=str(food.info())
    print(str(index) + ". " + a)
    index += 1

print("Drinks")

index = 0
for drink in drinks:
    b=str(drink.info())
    print(str(index) + ". " + b)
    index += 1

print("...................")

food_order = int(input("Enter the Food item no. :"))
selected_food = foods[food_order]
foodCount = int(input(" How many " + selected_food.name + " you want ?  (10% off for 3 or more) :"))

drink_order = int(input("Enter the Drink item no. :"))
selected_drink = drinks[drink_order]
drinkCount = int(input(" How many " + selected_drink.name + " you want ? (10% off for 3 or more) :"))


result=selected_food.get_total_price(foodCount)+selected_drink.get_total_price(drinkCount)

print("Your total is $" + str(result))


# In[ ]:




