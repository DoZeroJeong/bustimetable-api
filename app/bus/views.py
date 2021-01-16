from rest_framework import status, views, filters
from rest_framework.response import Response

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


def won_bus_crawling():
    req = Request("http://www.inje-pti.com/index.php?mp=p3_3_1")
    res = urlopen(req)
    html = res.read()
    bs = BeautifulSoup(html, 'html.parser')
    city_title_soup = bs.select('#content > div > div.bus_area > div > h6')
    bus_time_soup = bs.select('#content > div > div.bus_area > div ')

    city_value = list()
    bus_time_value = list()

    for city_tags in city_title_soup:
        city = city_tags.get_text()
        city_value.append(city)

    for bus_tags in bus_time_soup:
        bus_time = bus_tags.get_text(',', strip=True).split(',')
        bus_time_value.append(bus_time)

    return city_value, bus_time_value


def inje_bus_crawling():
    req = Request("http://www.inje-pti.com/index.php?mp=p3_3_2")
    res = urlopen(req)
    html = res.read()
    bs = BeautifulSoup(html, 'html.parser')
    city_title_soup = bs.select('#content > div.bus_area > div > h6')
    bus_time_soup = bs.select('#content > div.bus_area > div')

    city_value = list()
    bus_time_value = list()

    for city_tags in city_title_soup:
        city = city_tags.get_text()
        city_value.append(city)

    for bus_tags in bus_time_soup:
        bus_time = bus_tags.get_text(',', strip=True).split(',')
        bus_time_value.append(bus_time)

    return city_value, bus_time_value


def hyun_bus_crawling():
    req = Request("http://www.inje-pti.com/index.php?mp=p3_3_3")
    res = urlopen(req)
    html = res.read()
    bs = BeautifulSoup(html, 'html.parser')
    city_title_soup = bs.select('#content > div.bus_area > div > h6')
    bus_time_soup = bs.select('#content > div.bus_area > div ')

    city_value = list()
    bus_time_value = list()

    for city_tags in city_title_soup:
        city = city_tags.get_text()
        city_value.append(city)

    for bus_tags in bus_time_soup:
        bus_time = bus_tags.get_text(',', strip=True).split(',')
        bus_time_value.append(bus_time)

    return city_value, bus_time_value


class TimeTableView(views.APIView):
    """BusTime List APIView"""

    def get(self, request, city):

        if city in 'inje':
            city_data, time_data = inje_bus_crawling()
        elif city in 'won':
            city_data, time_data = won_bus_crawling()
        elif city in 'hyun':
            city_data, time_data = hyun_bus_crawling()

        if len(city_data) > 0 and len(time_data) > 0:
            timetable = list()
            for i in range(len(city_data)):
                timetable.append(
                    {'city': f'{city_data[i]}',
                     'items': [
                         {
                             'time': time_data[i][1:]
                         }
                     ]})

            return Response(data={'response': timetable}, status=status.HTTP_200_OK)

        return Response(data={
            'response': {
                "message": "No data"
            }
        }, status=status.HTTP_204_NO_CONTENT)
