
"""
Search for pubs in an osm file and list their names.
"""
import osmium
import sys
import csv

class NamesHandler(osmium.SimpleHandler):

    

    def write_to_csv(self, tags, lat, lon):
        amenities = ['bar','pub','fast_food','ice_cream','food_court','cafe','bbq','biergarten','swingerclub', 'stripclub', 'nightclub', 'gamling', 'casion', 'community_center', 'brothel', 'restaurant']

        if tags.get('amenity') in amenities:
            if 'name' in tags:
                with open('KigaliPubs.csv', mode='a') as file:
                    file_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    
                    print('## Writing: ', [tags['name'], tags['amenity'], lat, lon] )
                    file_writer.writerow([tags['name'], tags['amenity'], lat, lon])
                


    def node(self, n):
        #print('####### id:', n.id, ' visible: ', n.visible, ' version: ', n.version, ' timestamp: ', n.timestamp, ' lon: ', n.location.lon , ' lat: ', n.location.lat)
        lat = n.location.lat
        lon = n.location.lon
        self.write_to_csv(n.tags, lat, lon)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python pub_names.py <osmfile>")
        sys.exit(-1)

    NamesHandler().apply_file(sys.argv[1])