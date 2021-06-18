def houses_on_sale(number_of_results: int):
    houses = enumerate(range(1, number_of_results), 1)
    for house in houses:
        yield {"ID": house, "EntityType": "House",
                          "Bedrooms": "1",
                          "Bathrooms": "1"}