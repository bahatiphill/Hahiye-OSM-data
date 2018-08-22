# Hahiye-OSM-data


this take kigali OpenStreet Map (OSM) data and filter them to get public and entertaining places and return data into json format
those places could be like __[bar, barbecue, nightclub, restaurant ]__
___________________
read about OSM here (https://wiki.openstreetmap.org/wiki/About_OpenStreetMap)
___________________


## How to use it ?


__This is Python2__

0. (optional) you can download new update Kigali OSM data file here:
  `https://www.openstreetmap.org/api/0.6/map?bbox=29.9831%2C-2.0746%2C30.2845%2C-1.7768`
 
1. `git clone https://github.com/gur79/Hahiye-OSM-data.git`

2. install requirements
    `python2 -m pip install -r requirements.txt`
    
3. run the "run.py" file with an OSM data file
    `python2 run.py KigaliMapdata.xml`
    
/!\ if you have downloaded new kigali data remember to change the name "kigaliMapData.xml" to the name of the downloaded data file

==> the result json file can be found in the **result_data** directory.

You can even check it right here, right now, without touching anything :)  on `https://github.com/gur79/Hahiye-OSM-data/blob/master/result_data/resultjson.json`

### Cheers
