import requests 
from bs4 import BeautifulSoup

def print_recipe(title, author, ingredients, instructions):
  header = f"{title}, {author}"
  print("-" * len(header))
  print(header)
  print("Ingredients: \n  -", "\n  -".join(ingredients))
  print("Instructions: \n  -", "\n  -".join(instructions))
  print("-" * len(header))
  print()

def food_network(dish, limit):
  ''' 
  Food Network - https://www.foodnetwork.com
  Search items joined and ended with '-'
  '''
  url1 = f"https://www.foodnetwork.com/search/{'-'.join(dish.split()) + '-'}"

  results = requests.get(url1).content
  results = BeautifulSoup(results, 'html.parser')
  results = results.find_all('section', class_='o-RecipeResult')
  links = [result.find('a')['href'] for result in results]

  count = 0

  for link in links:
    if count == limit: break
    results2 = requests.get('https:' + link).content
    results2 = BeautifulSoup(results2, 'html.parser')
    author = results2.find_all('span', class_='o-Attribution__a-Name')[0].text.strip()
    title = results2.find_all('span', class_='o-AssetTitle__a-HeadlineText')[0].text.strip()
    ingredients = [ingredient.text.strip() for ingredient in results2.find_all('p', class_='o-Ingredients__a-Ingredient')]
    instructions = [instruction.text.strip() for instruction in results2.find_all('li', class_='o-Method__m-Step')]
    if (len(ingredients) > 0) and (len(instructions) > 0):
      print_recipe(title, author, ingredients, instructions)
      count = count + 1


dish = input("What would you like to eat tonight? ")
food_network(dish, 3)