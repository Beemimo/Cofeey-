# # Assignment Solution

# for i in range (100, 333):
#     multiple = str (i*3)
#     last_num = (str(i)[-1])*3
#     # print(multiple, last_num)
#     if multiple == last_num:
#         print(i)
#         print(i, i*3)

# Month = ["Jan", "Feb", "Mar", "Apr", "May", "June"]
# Sales = [5, 4, 5, 3, 5, 3]
# Price = [300, 300, 300, 200, 215, 300]

# # You can do this
# lab = 0
# for lab in range (lab, len(Month)):
#     print(Month[lab], Sales[lab])

# # ZIP Test 1
# zipped = zip(Month, Sales, Price)
# data = list(zipped)
# print(data[1])
# print(data)

# # ZIP Test 2
# zipped = zip(Month, Sales, Price)
# data = list(zipped)
# lab = 0
# for lab in range (lab, len(Month)):
#     print(data[lab])
# print(data)

# # OR This
# for Month, Sales, Price in list(zip(Month, Sales, Price))[1::2]:
#     print(Month, "-", Sales, "-", Price)


# # # CW 1: I DID IT!
# zipped = zip(Month, Sales, Price)
# data = list(zipped)
# lab = 1
# for lab in range (lab, len(Month), 2):
#     print(data[lab])
# print(data)

# FruitWork
Products = {"fruits" : ['apple', 'peer', 'mango']}
print(Products)
New_stock = ["passion", "bread fruit", "banana", "grape"]

for fruit in New_stock:
    Products["fruits"].append(fruit)

print(Products)
print(type(Products))
print(Products["fruits"])
fruits = Products["fruits"][0]
print(fruits)
print(type(fruits))

# Products["Shoes"] = []
# print(Products)

# new_shoes = ["Nike air", "Jordans", "Skates", "Toms"]
# for shuuus in new_shoes:
#     Products["Shoes"].append(shuuus)

# Products["Electronics"] = []
# new_electronics = ["TVs", "Fans", "Radios"]
# for electronics in new_electronics:
#     Products["Electronics"].append(electronics)

# print(Products)

# products = {"fruits": ["apples", "oranges"], "shoes": ["Jordans", "air"], "electronics": ["TVs", "radios"]}

# new_products = {}

# for key in products:
#     # print(key, products[key])
#     stock = products[key]
#     new_products[key] = []

#     for item in stock:
#         price = len(item) * 100
#         print(item, price)
#         template = {
#             "name": item,
#             "price":price
#         }
#         new_products[key].append(template)

# # print(new_products)

# print("Hello welcome to our fresh store")
# print("\nHere are the categories available\n")
# print("To finish your shopping type 'bill' ")
# user_cart = []

# for _ in range (4):
#     for key in new_products:
#         print(key.upper())



#     user_category = input("\nPlease select a category : ").lower()
#     if user_category == "bill" :
#         break
#     selected_category = new_products[user_category]


#     print("Here are available items : \n")
#     for product in selected_category:
#         print(product["name"].upper(), product["price"])

#     user_product = input("\nPlease select a product : ").lower()

#     for product in selected_category:
#         if product["name"] == user_product.lower():
#             user_cart.append(product)
   
# #print(user_cart)
# bill = 0 
# for item in user_cart:
#     bill += item["price"]

# print("Your Bill is : ", bill)

# import requests

# url = "http://checklight.pythonanywhere.com/predictions/1x0d001/"

# response = requests.get(url)

# print(response)

# data = response.json()

# print(type(data))
# print((data.keys()))
# print(data['day'])
# print(type(data['predictions']))

# for data_point in data['predictions']:
#     print(data_point)
#     print(f"Hour : {data_point['hour']}, predictions : {data_point['predictions']}, confidence : {data_point['confidence']}")

# url = "http://jumia.com"

# response = requests.get(url)

# print(response.content)

# # # FUNKTEZT
# def mahFunk(a, b, c, d):
#     num = a + b + c + d
#     return num
#     print (num)

# result = mahFunk(23, 74, 76, 25) 
# print(result)

# # # Still A FUNKTEZT
# def make_request(url):
#     import requests
#     response = requests.get(url)
#     data = response.content
#     return data
# url = "http://7cups.com"
# response = make_request(url)
# print (response)

# def MatTails(_list):

#     name = f"{_list[0]} {_list[1]}"
#     age = f"{_list[2]}"
#     height = f"{_list[3]}"
#     CatEgg = {'Name' : name, 'Age' : age, 'Height' : height}

#     return CatEgg

# gogo = ['Bimisola', 'Babalola', '15', '5ft 8']

# print(MatTails(gogo))