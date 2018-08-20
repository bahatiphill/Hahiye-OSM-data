import csv
import json


# turn csv data to dictionary
def turn_to_dict(file):

    result_dict = {}

    with open(file, mode='r') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        

        for row in readCSV:
            name = row[0]
            amenity = row[1]
            lat = row[2]
            lon = row[3]

            result_dict.update({name:{'amenity':amenity, 'lat':lat, 'lon':lon}})
            #result_dict[name] = {['amenity']= amenity, ['lat'] = lat, ['lon']= lon }

    return result_dict

# dictionary data to resultjson.json file in json format
def to_json():
    dictionary = turn_to_dict('KigaliPubs.csv')
    json_data = json.dumps(dictionary, indent=4)

    with open('resultjson.json', mode='w') as file:
        file.write(json_data)

    return True


to_json()
