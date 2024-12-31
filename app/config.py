# host = "aurora.cs.rutgers.edu"
host = "jedi"
flask_host_port = "http://" + host + ":8960"
flask_port = 8960
flask_app_context = "/gramusik/v1/predict/"

style_port1 = dict(
    blues="http://" + host + ":8000",
    classical="http://" + host + ":8001",
    country="http://" + host + ":8002",
    electronic="http://" + host + ":8003",
    funk="http://" + host + ":8004",
    hiphop="http://" + host + ":8005",
    jazz="http://" + host + ":8007",
    latin="http://" + host + ":8008",
    pop="http://" + host + ":9000",
    raggae="http://" + host + ":9001",
    reggae="http://" + host + ":9001",
    rock="http://" + host + ":9002"
)

style_port = {
    'blues': "http://" + host + ":8000",
    'classical': "http://" + host + ":8001",
    # /home/gjamuar/Gramusik_Projects/Rutgers_Prof_Backup-imp/4seconds/hierarchical
    'country': "http://" + host + ":8002",
    'electronic': "http://" + host + ":8003",
    'funk': "http://" + host + ":8004",  # hickle_data_16_wav_funksoul2wav_8841_9851
    'hiphop': "http://" + host + ":8005",
    'hip-hop': "http://" + host + ":8005",
    'jazz': "http://" + host + ":8007",
    'latin': "http://" + host + ":8008",
    'pop': "http://" + host + ":9000",
    'raggae': "http://" + host + ":9001",
    'reggae': "http://" + host + ":9001",
    'rock': "http://" + host + ":9002",
    # 'rock':"http://"+host+":12001",
    'metal': "http://" + host + ":12004",
    'heavy': "http://" + host + ":12004",
    'indu': "http://" + host + ":12005"
}

"""
for rock 2nd level

http://"+host+":12001/gramusik/v1/predict/tAGnKpE4NCI

that splits it into two   Metal and classic

for metal http://"+host+":12002/gramusik/v1/predict/tAGnKpE4NCI

splits into 2 heavy metal  and Industrial metal

heavy metal http://"+host+":12004/gramusik/v1/predict/tAGnKpE4NCI

industrial metal http://"+host+":12005/gramusik/v1/predict/0zhV99Bvrgg
"""
