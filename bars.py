import json
import os
from geopy.distance import vincenty
import sys


def load_data(filepath):
    with open(filepath, 'r') as infile:
        json_content = json.loads(infile.read())
    return json_content['features']


def get_biggest_bar(json_content):
    biggest_bar = max(
        json_content,
        key=lambda bar: bar['properties']['Attributes']['SeatsCount']
    )
    return biggest_bar

def get_smallest_bar(json_content):
    smallest_bar = min(
        json_content,
        key=lambda bar: bar['properties']['Attributes']['SeatsCount']
    )
    return smallest_bar

def get_distance(bar, coordinates):
    return vincenty(bar['geometry']['coordinates'], coordinates).meters



def get_closest_bar(json_content, coordinates):
    closest_bar = min(
        json_content,
        key=lambda bar: get_distance(bar, coordinates)
    )
    return closest_bar


def print_bar_info(bar, coordinates):
    name = bar['properties']['Attributes']['Name']
    seats_count = bar['properties']['Attributes']['SeatsCount']
    way = get_distance(bar, coordinates)
    print('Name: {}'.format(name))
    print('Seats count: {}'.format(seats_count))
    print('Distance to bar: {} meters'.format(round(way, 2)))
    print('\n')


if __name__ == '__main__':
    if not sys.argv[1:] or not os.path.isfile(sys.argv[1]):
        exit('Usage: python bars.py <path to file>')
    input_file = sys.argv[1]

    json_content = load_data(input_file)
    if json_content:
        try:
            my_longtude = float(input('Enter your longtude: '))
            my_latitude = float(input('Enter your latutude: '))
        except ValueError:
            exit('Longtude and latitude should be a numbers')
    coordinates = (my_longtude, my_latitude)
    biggest_bar = get_biggest_bar(json_content)
    smallest_bar = get_smallest_bar(json_content)
    closest_bar = get_closest_bar(json_content, coordinates)


    print('The biggest bar:' )
    print_bar_info(biggest_bar, coordinates)

    print('The smallest bar: ')
    print_bar_info(smallest_bar, coordinates)

    print('The closest bar: ')
    print_bar_info(closest_bar, coordinates)
