import json
import os
from geopy.distance import vincenty as distance


def load_data(filepath):
    with open(filepath, 'r') as infile:
        json_content = json.loads(infile.read())
    return json_content


def get_biggest_bar(json_content):
    bg_bar = \
        max(json_content['features'],
            key=lambda bar: bar['properties']['Attributes']['SeatsCount'])
    return bg_bar

def get_smallest_bar(json_content):
    sm_bar = \
        min(json_content['features'],
            key=lambda bar: bar['properties']['Attributes']['SeatsCount'])
    return sm_bar


def get_closest_bar(json_content, longitude, latitude):
    cl_bar = \
        min(json_content['features'],
            key=lambda bar: distance(bar['geometry']['coordinates'],
                                     (longitude, latitude)).km)
    return cl_bar


if __name__ == '__main__':
    input_file = 'bars.json'
    if not os.path.exists(input_file):
        exit("File {} doesn't exists")
    json_content = load_data('bars.json')
    if json_content:
        try:
            my_longtude = float(input('Enter your longtude: '))
            my_latitude = float(input('Enter your latutude: '))
        except ValueError:
            exit("Longtude and latitude should be a numbers")
    biggest_bar = get_biggest_bar(json_content)
    smallest_bar = get_smallest_bar(json_content)
    closest_bar = get_closest_bar(json_content, my_longtude, my_latitude)

    name_biggest_bar = \
        biggest_bar['properties']['Attributes']['Name']
    seats_count_biggest_bar = \
        biggest_bar['properties']['Attributes']['SeatsCount']

    name_smallest_bar = \
        smallest_bar['properties']['Attributes']['Name']
    seats_count_smallest_bar = \
        smallest_bar['properties']['Attributes']['SeatsCount']

    name_closest_bar = \
        closest_bar['properties']['Attributes']['Name']
    distance_closet_bar = distance(closest_bar['geometry']['coordinates'],
                                   (my_longtude, my_latitude)).meters

    print(u'The biggest bar: {} with {} seats'
          .format(name_biggest_bar, seats_count_biggest_bar))
    print(u'The smallest bar: {} with {} seats'
          .format(name_smallest_bar, seats_count_smallest_bar))
    print(u'The closest bar: {} distance: {} meters'
          .format(name_closest_bar, round(distance_closet_bar, 2)))
