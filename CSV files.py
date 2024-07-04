import csv

def write_holiday_cities(first_letter):
    visited_cities = set()
    want_to_visit_cities = set()
    never_visited_cities = set()

    with open('travel_notes.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            name = row[0]  # Get the first column (name)
            cities = row[1:]  # Get the remaining columns as a list
            if name[0].lower() == first_letter.lower():
                for city_group in cities:
                    city_list = city_group.split(',')  # Split cities in each group
                    if city_group.endswith(';'):  # Check if it's a visited cities group
                        visited_cities.update(city_list)
                    else:
                        want_to_visit_cities.update(city_list)

    never_visited_cities = want_to_visit_cities - visited_cities

    with open('holiday.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Посетили:', ', '.join(sorted(visited_cities))])
        writer.writerow(['Хотят посетить:', ', '.join(sorted(want_to_visit_cities))])
        writer.writerow(['Никогда не были в:', ', '.join(sorted(never_visited_cities))])
        if len(never_visited_cities) > 0:
            writer.writerow(['Следующим городом будет:', min(never_visited_cities)])
        else:
            writer.writerow(['Следующим городом будет:', 'Нет городов в списке'])

write_holiday_cities('L')
write_holiday_cities('R')