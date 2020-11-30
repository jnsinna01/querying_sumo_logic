from . models import SumoLogic
import requests
from django.shortcuts import render
from .forms import SumoLogicForm
import json


def query_output(request):
    url = 'https://api.ca.sumologic.com/api/v1/search/jobs'
    header_data = {
        'Authorization': 'Basic c3VnSDFkb2M1TkxzZG06Q1d6d29MWWtTbEJxYkZmSVp6MHJvZmdvSldsanY1aWs1VkhEbjlJTFcwdTFEN1ZmQ3NSTnY5NXFqR0hycEppSQ==',
        'Accept': 'application/json',
        'Content-type': 'application/json'}
    data = {
        "query": "",
        "from": "",
        "to": "",
        "timeZone": "EST"
    }
    if request.method == 'POST':
        form = SumoLogicForm(request.POST)
        form.save()
    form = SumoLogicForm()
    user_query = SumoLogic.objects.all()
    for query in user_query:
        data['query'] = query.Query
        data['from'] = query.From_Date_Time
        data['to'] = query.To_Date_Time
    r = requests.post(url, data=json.dumps(data), headers=header_data)
    print(r.status_code)
    response_dict = r.json()
    print(response_dict.keys())
    link_dicts = response_dict['link']
    print(link_dicts.keys())
    if link_dicts:
        url = link_dicts['href'] + '/messages?offset=0&limit=10'
        print(url)
        r = requests.get(url, headers=header_data)
        print(r.status_code)
        response_dict = r.json()
        sumo_response = {
            'field': response_dict['fields'][0]['name'],
            'blockid': response_dict['messages'][0]['map']['_blockid'],
            'messagetime': response_dict['messages'][0]['map']['_messagetime'],
            'raw': response_dict['messages'][0]['map']['_raw'],
            'collectorid': response_dict['messages'][0]['map']['_collectorid'],
            'sourceid': response_dict['messages'][0]['map']['_sourceid'],
            'collector': response_dict['messages'][0]['map']['_collector'],
            'sourcehost': response_dict['messages'][0]['map']['_sourcehost'],
            'messageid': response_dict['messages'][0]['map']['_messageid'],
            'sourcename': response_dict['messages'][0]['map']['_sourcename'],
            'sourcecategory': response_dict['messages'][0]['map']['_sourcecategory'],
        }
        print(sumo_response)
        context = {'sumo_response': sumo_response, 'form': form}
        return render(request, 'home.html', context)