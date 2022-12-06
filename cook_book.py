
#from pprint import pprint
def get_shop_list_by_dishes(dishes, person_count):
    order_list = {}
    
    with open('recipes.txt', 'r', encoding='utf-8') as f:
        cook_book = {}
        for line in f:
            dish_name = line.strip()
            ingredient_count = int(f.readline())
            ingredients = []
            for i in range(ingredient_count):
                ingredient = f.readline().strip()
                ingredient_name, quantity, measure = ingredient.split(' | ')
                ingredients.append({
                #'ingredient_count' : ingredient_count,
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
                })
            cook_book[dish_name] = ingredients
            f.readline()   
#pprint(cook_book)
    
    
    
    
    for dish in dishes:
        for order_pos in cook_book[dish]:
            name, amount, string = order_pos.values()
            if name in order_list.keys():
                order_list[name]['quantity'] += int(amount) * person_count
            else:
                order_list[name] = {'measure': string, 'quantity': int(amount) * person_count}
    return order_list

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))