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

def find_recipes(url, prefix,
                result_type, result_class, 
                author_type, author_class, 
                title_type, title_class, 
                ingredient_type, ingredient_class, 
                instruction_type, instruction_class):
  '''
  Generic way to get recipes:
    1. Search for recipe, limiting results only to recipe
    2. For each result, extract the link
    3. Follow each link and extract title, author, recipe, and instructions
  '''

  # search for a recipe and extract the link of each result
  results = get_url(url)
  results = results.find_all(result_type, result_class)
  links = [prefix + result.find('a')['href'] for result in results]

  # find title, author, and recipe for each link result
  for link in links:
    results2 = get_url(link)
    # extract data from the secondary links
    author = results2.find_all(author_type, class_=author_class)
    author = author[0].text.strip() if len(author) > 0 else "Unknown"
    title = results2.find_all(title_type, class_=title_class)
    title = title[0].text.strip() if len(title) > 0 else "Unknown"
    ingredients = [ingredient.text.strip() for ingredient in results2.find_all(ingredient_type, class_=ingredient_class)]
    instructions = [instruction.text.strip() for instruction in results2.find_all(instruction_type, class_=instruction_class)]

    print_recipe(title, author, ingredients, instructions)

if __name__ == '__main__':
  dish = input("What would you like to eat tonight? ")
  # Bon Appetite
  find_recipes(f"https://www.bonappetit.com/search/{'%20'.join(dish.split())}?content=recipe", 'https://www.bonappetit.com', 
              'article', 'recipe-content-card', 'span', 'contributor-name', 'a', 'top-anchor', 
              'li', 'ingredient', 'li','step')

  # Food Network
  find_recipes(f"https://www.foodnetwork.com/search/{'-'.join(dish.split()) + '-'}", 'https:',
               'section', 'o-RecipeResult', 'span', 'o-Attribution__a-Name', 
               'span', 'o-AssetTitle__a-HeadlineText', 'p', 'o-Ingredients__a-Ingredient',
               'li', 'o-Method__m-Step')