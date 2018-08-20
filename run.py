import extract
import convert
import sys
import threading


def converting_to_csv():

    osm_handler = extract.NodesHandler()
    to_csv = osm_handler.apply_file(sys.argv[1])


def converting_to_json():
    to_jsn = convert.to_json()
    if to_jsn:
        print("")
        print("Done!!")
        print("Now check file called 'resultjson.json' in result_data directory")


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python run.py <osmfile.xml>")
        sys.exit(-1)

    converting_to_csv()
    converting_to_json()