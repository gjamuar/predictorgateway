import requests
from flask import Flask, jsonify, abort, make_response, request
# from genres_predictor import GenrePredictor
import json
# import db_utility
import loggingmodule
import argparse
import os
import config

skipdb = True

app = Flask(__name__)
params = {}
tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


# genres_predictor = GenrePredictor('models_for_prediction/1st_level/', '9353', 4)
# style_predictor = GenrePredictor('models_for_prediction/2nd_level/blues/', '8231', 13)
@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


def get_genresCount():
    filename = os.path.join(params['path'], 'genres.txt')
    if (os.path.exists(filename)):
        fo = open(filename, "rw+")
        genreCount = len(fo.readlines())
    else:
        genreCount = -1
    print 'Returning :' + str(genreCount)
    return genreCount


def get_predictorname():
    list_meta_files = [os.path.join(params['path'], f) for f in os.listdir(params['path']) if f.endswith(".meta")]
    # files = os.system('find '+params['path']+' -name "[0-9]*.meta" ')
    predict_name = ''
    if (len(list_meta_files) > 0):
        predict_name = os.path.splitext(os.path.basename(list_meta_files[0]))[0]
    else:
        print 'cant find meta file'
    print predict_name
    return predict_name


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})


@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/gramusik/v1/predictmultilayer/<string:youtube_id>', methods=['GET'])
def predict_multilayer(youtube_id):
    req = config.flask_host_port + config.flask_app_context + youtube_id
    print(req)
    r = requests.get(req)
    respobj = json.loads(r.text)
    style1 = respobj['combinedprediction_withlable'][0][0]
    resultlist = []

    resultlist.append(respobj)

    while style1 in config.style_port:
        print(style1)
        style1Req = config.style_port[style1] + config.flask_app_context + youtube_id
        print(style1Req)
        try:
            style1Resp = requests.get(style1Req)
            style1RespObj = json.loads(style1Resp.text)
            resultlist.append(style1RespObj)

            style1 = style1RespObj['combinedprediction_withlable'][0][0]
        except Exception as e:
            print(e)
            break

    combinedresult  = updateMultilayerResult(resultlist, 3)

    # return jsonify(resultlist)
    return jsonify(combinedresult)

@app.route('/gramusik/v1/predictcombined/<string:youtube_id>', methods=['GET'])
def predict_combined(youtube_id):
    req = config.flask_host_port + config.flask_app_context + youtube_id
    print(req)
    r = requests.get(req)
    respobj = json.loads(r.text)
    style1 = respobj['combinedprediction_withlable'][0][0]
    style2 = respobj['combinedprediction_withlable'][1][0]
    print(style1)
    print(style2)
    if style1 in config.style_port:
        style1Req = config.style_port[style1] + config.flask_app_context + youtube_id
        print(style1Req)
        style1Resp = requests.get(style1Req)
        style1RespObj = json.loads(style1Resp.text)

    if style2 in config.style_port:
        style2Req = config.style_port[style2] + config.flask_app_context + youtube_id
        print(style2Req)
        style2Resp = requests.get(style2Req)
        style2RespObj = json.loads(style2Resp.text)

    combinedresult  = updateGenreResult(respobj, style1RespObj, style2RespObj, 4, 3)

    return jsonify(combinedresult)


def updateGenreResult(genreresult, style1RespObj, style2RespObj, genrelevel, stylelevel):
    combinedlable = []

    buildLable(combinedlable, genreresult, genrelevel)
    buildLable(combinedlable, style1RespObj, stylelevel)
    buildLable(combinedlable, style2RespObj, stylelevel)
    combinedlable.append(u'others')
    print(combinedlable)

    genredataset = []

    for i in range(len(genreresult['incremental_prediction'])):
        row = []
        others = 100
        for j in range(len(combinedlable)):
            if j < genrelevel:
                value = genreresult['incremental_prediction'][i][genreresult['label'].index(combinedlable[j])]
                others = others - value
                row.append(value)
            elif j < (len(combinedlable) - 1):
                row.append(0)
            else:
                row.append(others)
        genredataset.append(row)

    # print(genredataset)

    style1dataset = []

    for i in range(len(style1RespObj['incremental_prediction'])):
        row = []
        others = 100
        for j in range(len(combinedlable)):
            if j < genrelevel:
                row.append(0)
            elif j < (len(combinedlable) - stylelevel - 1):
                value = style1RespObj['incremental_prediction'][i][style1RespObj['label'].index(combinedlable[j])]
                others = others - value
                row.append(value)
            elif j < (len(combinedlable) - 1):
                row.append(0)
            else:
                row.append(others)
        style1dataset.append(row)

    # print(style1dataset)

    style2dataset = []

    for i in range(len(style2RespObj['incremental_prediction'])):
        row = []
        others = 100
        for j in range(len(combinedlable)):
            if j < genrelevel:
                row.append(0)
            elif j < (len(combinedlable) - stylelevel - 1):
                row.append(0)
            elif j < (len(combinedlable) - 1):
                value = style2RespObj['incremental_prediction'][i][style2RespObj['label'].index(combinedlable[j])]
                others = others - value
                row.append(value)
            else:
                row.append(others)
        style2dataset.append(row)

    # print(style2dataset)

    finalresult = {
        'label': combinedlable,
        'genredataset': {
            'label': combinedlable,
            'incremental_prediction': genredataset
        },
        'style1dataset': {
            'label': combinedlable,
            'incremental_prediction': style1dataset
        },
        'style2dataset': {
            'label': combinedlable,
            'incremental_prediction': style2dataset
        },
    }

    return finalresult

def buildLable(combinedlable, resultObj, level):
    for i in range(level):
        combinedlable.append(resultObj['combinedprediction_withlable'][i][0])


def buildLableWithIndex(combinedlable, resultObj, level, index_dict, i):
    lable_size = len(resultObj['combinedprediction_withlable'])
    rangesize = level
    if lable_size < level:
        rangesize = lable_size

    index_dict[i] = rangesize

    for i in range(level):
        combinedlable.append(resultObj['combinedprediction_withlable'][i][0])




def updateMultilayerResult(resultList, genrelevel):
    genreresult = ''
    style1RespObj = ''
    style2RespObj = ''
    combinedlable = []
    index_dict = {}

    for i, result in enumerate(resultList):
        index_dict[i] = genrelevel
        buildLableWithIndex(combinedlable, result, min(genrelevel,len(result['label'])),index_dict, i)

    combinedlable.append(u'others')
    print('combinedlable: {}'.format(combinedlable))
    print('index_dict: {}'.format(index_dict))
    combined_result = []
    start = 0
    end = 0
    for i, result in enumerate(resultList):
        genredataset = []
        end = start + index_dict[i]
        skip = index_dict[i]
        for i in range(len(result['incremental_prediction'])):
            row = []
            others = 100
            for j in range(len(combinedlable)):
                if j < start:
                    row.append(0)
                elif j < end:

                    value = result['incremental_prediction'][i][result['label'].index(combinedlable[j])]
                    others = others - value
                    row.append(value)
                elif j < (len(combinedlable) - 1):
                    row.append(0)
                else:
                    row.append(others)
            genredataset.append(row)
        start = end

        resultmap = {
            'label': combinedlable,
            'incremental_prediction': genredataset
        }
        combined_result.append(resultmap)
        # print(resultmap)



    finalresult = {
        'label': combinedlable,
        'genredataset': {
            'label': combinedlable,
            'incremental_prediction': combined_result
        },
        # 'style1dataset': {
        #     'label': combinedlable,
        #     'incremental_prediction': style1dataset
        # },
        # 'style2dataset': {
        #     'label': combinedlable,
        #     'incremental_prediction': style2dataset
        # },
    }
    return combined_result

    # return combined_result



if __name__ == '__main__':
    global genres_predictor
    # logger_predict = loggingmodule.initialize_logger('predictor','genre_predictor.log')
    parser = argparse.ArgumentParser()
    parser.add_argument('-path', "--path", help="path to the data model")

    # parser = argparse.ArgumentParser()
    parser.add_argument('-port', "--port", help="port number of the application")

    # parser = argparse.ArgumentParser()
    # parser.add_argument('-n',"--name", help="name of the predictor")

    # parser = argparse.ArgumentParser()
    # parser.add_argument('-g',"--genrescount", help="number of genres")

    args = parser.parse_args()
    if ('path' in args and args.path != ''):
        params['path'] = args.path
    else:
        params['path'] = 'models_for_prediction/1st_level/'
    if ('port' in args and args.port != ''):
        params['port'] = int(args.port)
    else:
        params['port'] = 8970
    # params['name'] = args.name
    # params['genrescount'] = int(args.genrescount)

    # genreCount = get_genresCount()
    # if(genreCount == -1):
    #     print 'genres.txt not found'
    # predict_name = get_predictorname();
    # genres_predictor = GenrePredictor(params['path'], predict_name, genreCount)

    app.run(host='0.0.0.0', port=params['port'])
