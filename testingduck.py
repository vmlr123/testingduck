import pytest
import requests


def test_presidents_in_response():
    rq = requests.get('https://api.duckduckgo.com/?q=presidents+of+the+united+states&format=json')
    data = rq.json()
    related_topics = data['RelatedTopics']
    presidents = [
        'Washington',
        'Adams',
        'Jefferson',
        'Madison',
        'Monroe',
        'Jackson',
        'Van Buren',
        'Harrison',
        'Tyler',
        'Polk',
        'Taylor',
        'Fillmore',
        'Pierce',
        'Buchanan',
        'Lincoln',
        'Johnson',
        'Grant',
        'Hayes',
        'Garfield',
        'Arthur',
        'Cleveland',
        'Harrison',
        'McKinley',
        'Roosevelt',
        'Taft',
        'Wilson',
        'Harding',
        'Coolidge',
        'Hoover',
        'Roosevelt',
        'Truman',
        'Eisenhower',
        'Kennedy',
        'Johnson',
        'Nixon',
        'Ford',
        'Carter',
        'Reagan',
        'Bush',
        'Clinton',
        'Bush',
        'Obama',
        'Trump',
        'Biden'
    ]
    for topic in related_topics:
        if topic['Text'] in presidents:
            presidents.remove(topic['Text'])
    assert len(presidents) == 0
