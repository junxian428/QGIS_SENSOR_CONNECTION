from flask import Flask, jsonify

app = Flask(__name__)

data = {
    "value": [
        {
            "name": "Datastreams",
            "url": "http://localhost:5000/v1.1/Datastreams"
        },
        {
            "name": "FeaturesOfInterest",
            "url": "http://localhost:5000/v1.1/FeaturesOfInterest"
        },
        {
            "name": "HistoricalLocations",
            "url": "http://localhost:5000/v1.1/HistoricalLocations"
        },
        {
            "name": "Locations",
            "url": "http://localhost:5000/v1.1/Locations"
        },
        {
            "name": "MultiDatastreams",
            "url": "http://localhost:5000/v1.1/MultiDatastreams"
        },
        {
            "name": "Observations",
            "url": "http://localhost:5000/v1.1/Observations"
        },
        {
            "name": "ObservedProperties",
            "url": "http://localhost:5000/v1.1/ObservedProperties"
        },
        {
            "name": "Sensors",
            "url": "http://localhost:5000/v1.1/Sensors"
        },
        {
            "name": "Things",
            "url": "http://localhost:5000/v1.1/Things"
        }
    ],
    "serverSettings": {
        "conformance": [
            "http://www.opengis.net/spec/iot_sensing/1.1/req/batch-request/batch-request",
            "http://www.opengis.net/spec/iot_sensing/1.1/req/create-observations-via-mqtt/observations-creation",
            "http://www.opengis.net/spec/iot_sensing/1.1/req/create-update-delete",
            "http://www.opengis.net/spec/iot_sensing/1.1/req/data-array/data-array",
            "http://www.opengis.net/spec/iot_sensing/1.1/req/datamodel",
            "http://www.opengis.net/spec/iot_sensing/1.1/req/multi-datastream",
            "http://www.opengis.net/spec/iot_sensing/1.1/req/receive-updates-via-mqtt/receive-updates",
            "http://www.opengis.net/spec/iot_sensing/1.1/req/request-data",
            "http://www.opengis.net/spec/iot_sensing/1.1/req/resource-path/resource-path-to-entities",
            "https://fraunhoferiosb.github.io/FROST-Server/extensions/DeepSelect.html",
            "https://fraunhoferiosb.github.io/FROST-Server/extensions/GeoJSON-ResultFormat.html",
            "https://fraunhoferiosb.github.io/FROST-Server/extensions/JsonBatchRequest.html",
            "https://fraunhoferiosb.github.io/FROST-Server/extensions/OpenAPI.html",
            "https://fraunhoferiosb.github.io/FROST-Server/extensions/ResponseMetadata.html",
            "https://fraunhoferiosb.github.io/FROST-Server/extensions/SelectDistinct.html",
            "https://github.com/INSIDE-information-systems/SensorThingsAPI/blob/master/CSV-ResultFormat/CSV-ResultFormat.md",
            "https://github.com/INSIDE-information-systems/SensorThingsAPI/blob/master/EntityLinking/Linking.md#Expand",
            "https://github.com/INSIDE-information-systems/SensorThingsAPI/blob/master/EntityLinking/Linking.md#Filter",
            "https://github.com/INSIDE-information-systems/SensorThingsAPI/blob/master/EntityLinking/Linking.md#NavigationLinks"
        ],
        "http://www.opengis.net/spec/iot_sensing/1.1/req/create-observations-via-mqtt/observations-creation": {
            "endpoints": [
                "ws://localhost:5000/mqtt"
            ]
        },
        "http://www.opengis.net/spec/iot_sensing/1.1/req/receive-updates-via-mqtt/receive-updates": {
            "endpoints": [
                "ws://localhost:5000/mqtt"
            ]
        }
    }
}




######

#
#
#


locations_data = {
    "value": [
        {
            "@iot.selfLink": "https://airquality-frost.k8s.ilt-dmz.iosb.fraunhofer.de/v1.1/Locations(1)",
            "@iot.id": 1,
            "name": "STA.09.LIES",
            "description": "Location of station STA.09.LIES",
            "encodingType": "application/geo+json",
            "location": {
                "type": "Point",
                "coordinates": [
                    16.301278,
                    48.14125
                ]
            },
            "properties": {
                "AirQualityStationArea": "suburban",
                "countryCode": "AT",
                "localId": "STA.09.LIES",
                "metadata": "http://discomap.eea.europa.eu/map/fme/metadata/PanEuropean_metadata.csv",
                "namespace": "AT.0008.20.AQ",
                "owner": "http://dd.eionet.europa.eu"
            },
            "HistoricalLocations@iot.navigationLink": "https://airquality-frost.k8s.ilt-dmz.iosb.fraunhofer.de/v1.1/Locations(1)/HistoricalLocations",
            "Things@iot.navigationLink": "https://airquality-frost.k8s.ilt-dmz.iosb.fraunhofer.de/v1.1/Locations(1)/Things"
        },
        {
            "@iot.selfLink": "https://airquality-frost.k8s.ilt-dmz.iosb.fraunhofer.de/v1.1/Locations(2)",
            "@iot.id": 2,
            "name": "STA.06.170",
            "description": "Location of station STA.06.170",
            "encodingType": "application/geo+json",
            "location": {
                "type": "Point",
                "coordinates": [
                    15.43308,
                    47.04172
                ]
            },
            "properties": {
                "AirQualityStationArea": "suburban",
                "countryCode": "AT",
                "localId": "STA.06.170",
                "metadata": "http://discomap.eea.europa.eu/map/fme/metadata/PanEuropean_metadata.csv",
                "namespace": "AT.0008.20.AQ",
                "owner": "http://dd.eionet.europa.eu"
            },
            "HistoricalLocations@iot.navigationLink": "https://airquality-frost.k8s.ilt-dmz.iosb.fraunhofer.de/v1.1/Locations(2)/HistoricalLocations",
            "Things@iot.navigationLink": "https://airquality-frost.k8s.ilt-dmz.iosb.fraunhofer.de/v1.1/Locations(2)/Things"
        },
        {
            "@iot.selfLink": "https://airquality-frost.k8s.ilt-dmz.iosb.fraunhofer.de/v1.1/Locations(3)",
            "@iot.id": 3,
            "name": "Lustenau Wiesenrain",
            "description": "Location of air quality station Lustenau Wiesenrain",
            "encodingType": "application/geo+json",
            "location": {
                "type": "Point",
                "coordinates": [
                    9.653713,
                    47.410164
                ]
            },
            "properties": {
                "countryCode": "AT",
                "localId": "STA.08.0706",
                "metadata": "http://luft.umweltbundesamt.at/inspire/wfs?service=WFS&version=2.0.0&request=GetFeature&typeName=aqd:AQD_Station",
                "namespace": "AT.0008.20.AQ",
                "owner": "http://luft.umweltbundesamt.at"
            },
            "HistoricalLocations@iot.navigationLink": "https://airquality-frost.k8s.ilt-dmz.iosb.fraunhofer.de/v1.1/Locations(3)/HistoricalLocations",
            "Things@iot.navigationLink": "https://airquality-frost.k8s.ilt-dmz.iosb.fraunhofer.de/v1.1/Locations(3)/Things"
        },
        {
            "@iot.selfLink": "https://airquality-frost.k8s.ilt-dmz.iosb.fraunhofer.de/v1.1/Locations(4)",
            "@iot.id": 4,
            "name": "Dornbirn Stadtstraße",
            "description": "Location of air quality station Dornbirn Stadtstraße",
            "encodingType": "application/geo+json",
            "location": {
                "type": "Point",
                "coordinates": [
                    9.7432,
                    47.40945
                ]
            },
            "properties": {
                "countryCode": "AT",
                "localId": "STA.08.0807",
                "metadata": "http://luft.umweltbundesamt.at/inspire/wfs?service=WFS&version=2.0.0&request=GetFeature&typeName=aqd:AQD_Station",
                "namespace": "AT.0008.20.AQ",
                "owner": "http://luft.umweltbundesamt.at"
            },
            "HistoricalLocations@iot.navigationLink": "https://airquality-frost.k8s.ilt-dmz.iosb.fraunhofer.de/v1.1/Locations(4)/HistoricalLocations",
            "Things@iot.navigationLink": "https://airquality-frost.k8s.ilt-dmz.iosb.fraunhofer.de/v1.1/Locations(4)/Things"
        }
    ]
}

##
@app.route('/v1.1/Datastreams', methods=['GET'])
def datastreams():
    return jsonify({"message": "This is the Datastreams endpoint."})

@app.route('/v1.1/FeaturesOfInterest', methods=['GET'])
def features_of_interest():
    return jsonify({"message": "This is the FeaturesOfInterest endpoint."})

@app.route('/v1.1/HistoricalLocations', methods=['GET'])
def historical_locations():
    return jsonify({"message": "This is the HistoricalLocations endpoint."})

@app.route('/v1.1/Locations', methods=['GET'])
def locations():
    return jsonify(locations_data)

@app.route('/v1.1/MultiDatastreams', methods=['GET'])
def multi_datastreams():
    return jsonify({"message": "This is the MultiDatastreams endpoint."})

@app.route('/v1.1/Observations', methods=['GET'])
def observations():
    return jsonify({"message": "This is the Observations endpoint."})

@app.route('/v1.1/ObservedProperties', methods=['GET'])
def observed_properties():
    return jsonify({"message": "This is the ObservedProperties endpoint."})

@app.route('/v1.1/Sensors', methods=['GET'])
def sensors():
    return jsonify({"message": "This is the Sensors endpoint."})

@app.route('/v1.1/Things', methods=['GET'])
def things():
    return jsonify({"message": "This is the Things endpoint."})

@app.route('/serverSettings', methods=['GET'])
def server_settings():
    return jsonify(data['serverSettings'])


@app.route('/v1.1/', methods=['GET'])
def default_endpoint():
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
