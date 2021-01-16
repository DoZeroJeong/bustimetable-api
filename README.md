# bustimetable-api
Refactoring bustimetable-api repository
1. Docker deploy setting
2. Separated to settings.py
3. Security settings(Secret key, DB setting) 
etc.
----------------------------------------------

# Technologies

* Python
* DRF(DjangoRestFramework)
* Beautifulsoup
* Git, Github

# API Documentation

```
city : inje
GET   /timetable/<str:city>
{
    "response": [
        {
            "city": "동서울",
            "items": [
                {
                    "time": [
                        "06:55",
                        "07:50",
                        "08:30",
                           '
                           '
                           ' 
                    ]
                }
            ]
        },
    ]
}
```