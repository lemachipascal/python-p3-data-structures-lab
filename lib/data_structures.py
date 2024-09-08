spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]
print(get_names(spicy_foods))

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]
print(get_spiciest_foods(spicy_foods))

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
         name = food['name']
         cuisine = food['cuisine']
         heat_level = food['heat_level']
         print(f"{name} ({cuisine}) | Heat Level: {'🌶' * heat_level}")

print(print_spicy_foods(spicy_foods))

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
         if food['cuisine'] == cuisine:
              return food
    return None

print(get_spicy_food_by_cuisine(spicy_foods,'Mexican'))

def print_spiciest_foods(spicy_foods):
    def get_spiciest_foods(spicy_foods):
        return [food for food in spicy_foods if food['heat_level'] > 5]

    spiciest_foods = get_spiciest_foods(spicy_foods)
    
    for food in spiciest_foods:
        name = food['name']
        cuisine = food['cuisine']
        heat_level = food['heat_level']
        print(f"{name} ({cuisine}) | Heat Level: {'🌶' * heat_level}")

print(print_spiciest_foods(spicy_foods))

def get_average_heat_level(spicy_foods):
    if not spicy_foods:
        return 0  # Return 0 if the list is empty to avoid division by zero
    
    total_heat = sum(food['heat_level'] for food in spicy_foods)
    number_of_foods = len(spicy_foods)
    average_heat = total_heat // number_of_foods  # Use integer division
    
    return average_heat
print(get_average_heat_level(spicy_foods))

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

print(create_spicy_food(spicy_foods, spicy_foods))