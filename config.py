flask_host_port = "http://aurora.cs.rutgers.edu:8960"
flask_port = 8960
flask_app_context = "/gramusik/v1/predict/"

style_port1 = dict(
    blues="http://aurora.cs.rutgers.edu:8000",
    classical="http://aurora.cs.rutgers.edu:8001",
    country="http://aurora.cs.rutgers.edu:8002",
    electronic="http://aurora.cs.rutgers.edu:8003",
    funk="http://aurora.cs.rutgers.edu:8004",
    hiphop="http://aurora.cs.rutgers.edu:8005",
    jazz="http://aurora.cs.rutgers.edu:8007",
    latin="http://aurora.cs.rutgers.edu:8008",
    pop="http://aurora.cs.rutgers.edu:9000",
    raggae="http://aurora.cs.rutgers.edu:9001",
    reggae="http://aurora.cs.rutgers.edu:9001",
    rock="http://aurora.cs.rutgers.edu:9002"
)

style_port = {
    'blues':"http://aurora.cs.rutgers.edu:8000",
    'classical':"http://aurora.cs.rutgers.edu:8001",
    'country':"http://aurora.cs.rutgers.edu:8002",
    'electronic':"http://aurora.cs.rutgers.edu:8003",
    'funk':"http://aurora.cs.rutgers.edu:8004",
    'hiphop':"http://aurora.cs.rutgers.edu:8005",
    'hip-hop':"http://aurora.cs.rutgers.edu:8005",
    'jazz':"http://aurora.cs.rutgers.edu:8007",
    'latin':"http://aurora.cs.rutgers.edu:8008",
    'pop':"http://aurora.cs.rutgers.edu:9000",
    'raggae':"http://aurora.cs.rutgers.edu:9001",
    'reggae':"http://aurora.cs.rutgers.edu:9001",
    #'rock':"http://aurora.cs.rutgers.edu:9002",
    'rock':"http://aurora.cs.rutgers.edu:12001",
    'metal':"http://aurora.cs.rutgers.edu:12004",
    'heavy':"http://aurora.cs.rutgers.edu:12004",
    'indu':"http://aurora.cs.rutgers.edu:12005"
}

"""
for rock 2nd level

http://aurora.cs.rutgers.edu:12001/gramusik/v1/predict/tAGnKpE4NCI

that splits it into two   Metal and classic

for metal http://aurora.cs.rutgers.edu:12002/gramusik/v1/predict/tAGnKpE4NCI

splits into 2 heavy metal  and Industrial metal

heavy metal http://aurora.cs.rutgers.edu:12004/gramusik/v1/predict/tAGnKpE4NCI

industrial metal http://aurora.cs.rutgers.edu:12005/gramusik/v1/predict/0zhV99Bvrgg
"""
