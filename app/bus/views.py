import re

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


def won_bus_crawling():
    req = Request("http://www.inje-pti.com/index.php?mp=p3_3_1")
    res = urlopen(req)
    html = res.read()
    bs = BeautifulSoup(html, 'html.parser')
    city_title_soup = bs.select('#content > div > div.bus_area > div > h6')
    bus_time_soup = bs.select('#content > div > div.bus_area > div ')

    city_key = list()
    bus_time_value = list()

    for city_tags in city_title_soup:
        city = city_tags.get_text()
        city_key.append(city)

    for bus_tags in bus_time_soup:
        bus_time = bus_tags.get_text(',', strip=True).split(',')
        bus_time_value.append(bus_time)

    city_timetable = dict.fromkeys(city_key)

    for i in range(len(city_key)):
        city_timetable[city_key[i]] = bus_time_value[i][1:]

    return city_timetable


def inje_bus_crawling():
    req = Request("http://www.inje-pti.com/index.php?mp=p3_3_2")
    res = urlopen(req)
    html = res.read()
    bs = BeautifulSoup(html, 'html.parser')
    city_title_soup = bs.select('#content > div.bus_area > div > h6')
    bus_time_soup = bs.select('#content > div.bus_area > div')

    city_key = list()
    bus_time_value = list()

    for city_tags in city_title_soup:
        city = city_tags.get_text()
        city_key.append(city)

    for bus_tags in bus_time_soup:
        bus_time = bus_tags.get_text(',', strip=True).split(',')
        bus_time_value.append(bus_time)

    # for value in bus_time:
    #     if value in city_value:
    #         continue
    #     else:
    #         bus_time_value.append(value)
    city_timetable = dict.fromkeys(city_key)

    for i in range(len(city_key)):
        city_timetable[city_key[i]] = bus_time_value[i][1:]

    return city_timetable


def hun_bus_crawling():
    req = Request("http://www.inje-pti.com/index.php?mp=p3_3_3")
    res = urlopen(req)
    html = res.read()
    bs = BeautifulSoup(html, 'html.parser')
    city_title_soup = bs.select('#content > div.bus_area > div > h6')
    bus_time_soup = bs.select('#content > div.bus_area > div ')

    city_key = list()
    bus_time_value = list()

    for city_tags in city_title_soup:
        city = city_tags.get_text()
        city_key.append(city)

    for bus_tags in bus_time_soup:
        bus_time = bus_tags.get_text(',', strip=True).split(',')
        bus_time_value.append(bus_time)

    city_timetable = dict.fromkeys(city_key)

    for i in range(len(city_key)):
        city_timetable[city_key[i]] = bus_time_value[i][2:]

    return city_timetable


print('인제: ', inje_bus_crawling())
print('원통:', won_bus_crawling())
print('현리:', hun_bus_crawling())
