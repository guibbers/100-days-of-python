#Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

travel_log = {
    "France":  {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"citis_to_visit": ["Berlin", "Hamburg", "Stuttgart"], "money_needed": 2000}
}

#Nesting Dictionary in a List

travel_log = [
    {
        "country": "France", 
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 12
    },
    {
       "country": "Germany", 
       "citis_to_visit": ["Berlin", "Hamburg", "Stuttgart"], 
       "money_needed": 2000
    },
]

def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)