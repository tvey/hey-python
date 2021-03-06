"""
Views are objects returned by dict.keys(), dict.values(), and dict.items().
"""

salad = {'potatoes': 2, 'eggs': 2, 'tomatoes': 1, 'peas': 100, 'spam': 1}

products = salad.keys()  # keys are unique, so it's a set-like object
quantities = salad.values()  # more list-like, because values are not unique
ingredients = salad.items()  # tuples of key:value pairs

# views can be iterated over
for prod, qty in ingredients:
    print(f'- {prod}: {qty} pcs')

# they support membership tests (x in view / x not in view)
assert 'carrots' not in products

# they immediately (dynamically) reflect changes in a dict
salad['carrots'] = 1
assert 'carrots' in products

# can be converted to other types, list() will keep the order
list(products)
[(prod, qty) for prod, qty in ingredients]  # create a list from pairs

# order of insertion is preserved
'carrots' in list(ingredients)[-1]  # True, 'carrots' is the last product
