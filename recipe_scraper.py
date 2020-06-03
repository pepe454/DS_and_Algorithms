import requests 
from bs4 import BeautifulSoup

get_url = lambda url : BeautifulSoup(requests.get(url).content, 'html.parser')

def print_recipe(title, author, ingredients, instructions):
  ''' 
  Pretty output for recipes
  '''
  if not len(ingredients) or not len(instructions): return
  header = f"{title}, {author}"
  print("-" * len(header))
  print(header)
  print("Ingredients: ", " | ".join(ingredients))
  print("Instructions: \n  -", "\n  -".join(instructions))
  print("-" * len(header))
  print()

def food_network(dish):
  ''' 
  Food Network - https://www.foodnetwork.com
  Search items must begin, be separated by, and end with '-'
  '''
  url = f"https://www.foodnetwork.com/search/{'-'.join(dish.split()) + '-'}"

  # get all links for the search results
  results = get_url(url)
  results = results.find_all('section', class_='o-RecipeResult')
  links = [result.find('a')['href'] for result in results]

  # get the recipe for each result: includes author, title, ingredients, and methods
  for link in links:
    results2 = get_url('https:' + link)

    # get data from the page
    author = results2.find_all('span', class_='o-Attribution__a-Name')[0].text.strip()
    title = results2.find_all('span', class_='o-AssetTitle__a-HeadlineText')[0].text.strip()
    ingredients = [ingredient.text.strip() for ingredient in results2.find_all('p', class_='o-Ingredients__a-Ingredient')]
    instructions = [instruction.text.strip() for instruction in results2.find_all('li', class_='o-Method__m-Step')]

    print_recipe(title, author, ingredients, instructions)

def bon_appetite(dish):
  '''
  Bon Appetite - https://www.bonappetit.com/ 
  Search items separated by %20
  '''
  url = "https://www.bonappetit.com" # need to use this later for relative links
  results = get_url(f"{url}/search/{'%20'.join(dish.split())}?content=recipe")
  results = results.find_all('article', class_='recipe-content-card')
  links = [url + result.find('a')['href'] for result in results]
  
  for link in links:
    results2 = get_url(link)

    # extract information
    author = results2.find_all('span', class_='contributor-name')
    author = author[0].text.strip() if len(author) > 0 else "Unknown"
    title = results2.find_all('a', class_='top-anchor')[0].text.strip()
    ingredients = [ingredient.text.strip() for ingredient in results2.find_all('li', class_='ingredient')]
    instructions = [instruction.text.strip() for instruction in results2.find_all('li', class_='step')]

    print_recipe(title, author, ingredients, instructions)

if __name__ == '__main__':
  dish = input("What would you like to eat tonight? ")
  food_network(dish)
  bon_appetite(dish)
