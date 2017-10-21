import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds055752.mlab.com:55752/warmwinter
host = "ds055752.mlab.com"
port = 55752
db_name = "warmwinter"
user_name = "admin"
password = "minhsuper"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
