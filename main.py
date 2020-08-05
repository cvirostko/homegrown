#! python3
import requests

#counter to loop through paginated results that return from swapi
current_page = 1
#send a call to determine length of total starships from swapi
get_total_ships = requests.get(f'https://swapi.dev/api/starships/?page=1').json()
#get the total number of pages to paginate my requests through
total_pages = round(get_total_ships['count'] / 10)
#function that will take in a response (per page) and print the starships that have pilots and their pilot names
def print_piloted_ships_on_page(response):
    for starship in response['results']:
        print('\nStarship: ' + starship['name'])
        print('    Starship Class: ' + starship['starship_class'])
        if starship['pilots']:
            print('        Pilots: ')
            for pilots in starship['pilots']:
                print('                ' + requests.get(url=pilots).json()['name'].encode('utf-8').decode('latin-1'))
#function to iterate over all of the returned pages
def get_ships_by_page(current_page):
    return requests.get(f'https://swapi.dev/api/starships/?page={current_page}').json()
#function to execute the entire script and increment my counter
while current_page < total_pages:
    print_piloted_ships_on_page(get_ships_by_page(current_page))
    current_page += 1
