from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


def citybus_crawling():
    req = Request("http://www.inje-pti.com/index.php?mp=p2_4")
    res = urlopen(req)
    print(res)
    html = res.read()
    bs = BeautifulSoup(html, 'html.parser')

    bustime_key = bs.select('#content > div.bus_area > div > h6')
    bustime_value = bs.select('#content > div.bus_area > div ')

    key_list = []
    value_list = []

    for keys in bustime_key:
        key = keys.get_text("")
        key_list.append(key)

    for values in bustime_value:
        value = values.get_text(',', strip=True).split(',')
        value_list.append(value)

    city_timetable = dict.fromkeys(key_list)

    for i in range(len(key_list)):
        city_timetable[key_list[i]] = value_list[i]
    return city_timetable


def intercitybus_crawling():
    req = Request("http://www.inje-pti.com/index.php?mp=p3_3_2")
    res = urlopen(req)
    html = res.read()
    bs = BeautifulSoup(html, 'html.parser')
    bustime_key = bs.select('#content > div.bus_area > div > h6')
    bustime_value = bs.select('#content > div.bus_area > div ')

    key_list = []
    value_list = []

    for keys in bustime_key:
        key = keys.get_text("")
        key_list.append(key)

    for values in bustime_value:
        value = values.get_text(',', strip=True).split(',')
        value_list.append(value)

    intercity_timetable = dict.fromkeys(key_list)

    for i in range(len(key_list)):
        intercity_timetable[key_list[i]] = value_list[i]
    return intercity_timetable


intercitybus_crawling()