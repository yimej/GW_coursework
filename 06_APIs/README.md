

```python
#Dependencies
import matplotlib.pyplot as plt
import requests
import json
import pandas as pd
import random
import numpy as np
from config import api_key
from citipy import citipy
```


```python
#Generate 500 random cities
cities, cloudiness, country, date, humidity, lat, lng, maxtemp, windspeed = [],[],[],[],[],[],[],[],[]
query_url = f'http://api.openweathermap.org/data/2.5/weather?appid={api_key}&units=imperial&q='

while len(cities) < 500:
    city = citipy.nearest_city(np.random.randint(-180, 180),np.random.randint(-180, 180)).city_name
    urltest = requests.get(query_url + city).status_code
    if urltest == 200:
        cities.append(city)
        cities = list(set(cities))
len(cities)
```




    500




```python
#API calls and print log
count = 0
for city in cities:
    count += 1
    response = requests.get(query_url + city).json()
    cloudiness.append(response['clouds']['all'])
    country.append(response['sys']['country'])
    date.append(response['dt'])
    humidity.append(response['main']['humidity'])
    lat.append(response['coord']['lat'])
    lng.append(response['coord']['lon'])
    maxtemp.append(response['main']['temp_max'])
    windspeed.append(response['wind']['speed'])
    print(f'{count} {city} {query_url}{city}')
```

    1 azare http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=azare
    2 cabo san lucas http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=cabo san lucas
    3 warrnambool http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=warrnambool
    4 paamiut http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=paamiut
    5 sao miguel do araguaia http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=sao miguel do araguaia
    6 mogadishu http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=mogadishu
    7 notse http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=notse
    8 nanortalik http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=nanortalik
    9 krasnoarmeysk http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=krasnoarmeysk
    10 new norfolk http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=new norfolk
    11 zhigansk http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=zhigansk
    12 katsuura http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=katsuura
    13 kalabo http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=kalabo
    14 boralday http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=boralday
    15 taber http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=taber
    16 kudahuvadhoo http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=kudahuvadhoo
    17 ixtapa http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=ixtapa
    18 florian http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=florian
    19 torbay http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=torbay
    20 vestmannaeyjar http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=vestmannaeyjar
    21 puqi http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=puqi
    22 plyussa http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=plyussa
    23 grand gaube http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=grand gaube
    24 yurla http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=yurla
    25 college http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=college
    26 lukovetskiy http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=lukovetskiy
    27 edd http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=edd
    28 sivaki http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=sivaki
    29 charyshskoye http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=charyshskoye
    30 mana http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=mana
    31 port lincoln http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=port lincoln
    32 marzuq http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=marzuq
    33 lorengau http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=lorengau
    34 saint-pierre http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=saint-pierre
    35 shache http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=shache
    36 ikwiriri http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=ikwiriri
    37 vilhena http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=vilhena
    38 barrow http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=barrow
    39 pirenopolis http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=pirenopolis
    40 caravelas http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=caravelas
    41 ribeira grande http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=ribeira grande
    42 muscat http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=muscat
    43 saint-augustin http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=saint-augustin
    44 husavik http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=husavik
    45 miraflores http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=miraflores
    46 nova olimpia http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=nova olimpia
    47 fare http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=fare
    48 bara http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=bara
    49 grindavik http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=grindavik
    50 birin http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=birin
    51 labuhan http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=labuhan
    52 ulladulla http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=ulladulla
    53 biltine http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=biltine
    54 wanning http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=wanning
    55 sorong http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=sorong
    56 lao cai http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=lao cai
    57 catalao http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=catalao
    58 taoudenni http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=taoudenni
    59 tigil http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=tigil
    60 port moresby http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=port moresby
    61 dingzhou http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=dingzhou
    62 aksarka http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=aksarka
    63 peace river http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=peace river
    64 gushikawa http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=gushikawa
    65 baiyin http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=baiyin
    66 saldanha http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=saldanha
    67 butaritari http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=butaritari
    68 prince albert http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=prince albert
    69 chuy http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=chuy
    70 raudeberg http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=raudeberg
    71 qinhuangdao http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=qinhuangdao
    72 vieste http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=vieste
    73 cherskiy http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=cherskiy
    74 manokwari http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=manokwari
    75 birjand http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=birjand
    76 hobart http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=hobart
    77 san quintin http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=san quintin
    78 saladoblanco http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=saladoblanco
    79 vila velha http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=vila velha
    80 cam ranh http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=cam ranh
    81 kyren http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=kyren
    82 chicama http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=chicama
    83 victoria http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=victoria
    84 zanjan http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=zanjan
    85 richards bay http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=richards bay
    86 westport http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=westport
    87 norsup http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=norsup
    88 ponta do sol http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=ponta do sol
    89 kieta http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=kieta
    90 danilov http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=danilov
    91 provideniya http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=provideniya
    92 la romana http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=la romana
    93 nosy varika http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=nosy varika
    94 san policarpo http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=san policarpo
    95 hofn http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=hofn
    96 longyearbyen http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=longyearbyen
    97 jamestown http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=jamestown
    98 saint-philippe http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=saint-philippe
    99 simao http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=simao
    100 seydi http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=seydi
    101 terra santa http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=terra santa
    102 pamanukan http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=pamanukan
    103 sindor http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=sindor
    104 marevo http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=marevo
    105 kisangani http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=kisangani
    106 carballo http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=carballo
    107 kamenka http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=kamenka
    108 avarua http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=avarua
    109 svetlogorsk http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=svetlogorsk
    110 waddan http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=waddan
    111 monrovia http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=monrovia
    112 mount gambier http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=mount gambier
    113 nalut http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=nalut
    114 whitianga http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=whitianga
    115 kreminna http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=kreminna
    116 busselton http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=busselton
    117 morehead http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=morehead
    118 klaksvik http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=klaksvik
    119 tomari http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=tomari
    120 karhal http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=karhal
    121 gravdal http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=gravdal
    122 wakkanai http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=wakkanai
    123 ensenada http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=ensenada
    124 castro http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=castro
    125 karratha http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=karratha
    126 dikson http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=dikson
    127 shelburne http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=shelburne
    128 orodara http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=orodara
    129 gamba http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=gamba
    130 hermanus http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=hermanus
    131 pankrushikha http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=pankrushikha
    132 kamogawa http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=kamogawa
    133 seoul http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=seoul
    134 hervey bay http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=hervey bay
    135 bandarbeyla http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=bandarbeyla
    136 lakatoro http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=lakatoro
    137 muhos http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=muhos
    138 luderitz http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=luderitz
    139 hvide sande http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=hvide sande
    140 aloleng http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=aloleng
    141 terrak http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=terrak
    142 hithadhoo http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=hithadhoo
    143 peresichna http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=peresichna
    144 nemuro http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=nemuro
    145 basoko http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=basoko
    146 guerrero negro http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=guerrero negro
    147 yumen http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=yumen
    148 tiksi http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=tiksi
    149 vila http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=vila
    150 kandrian http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=kandrian
    151 stokmarknes http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=stokmarknes
    152 khash http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=khash
    153 bodden town http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=bodden town
    154 siocon http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=siocon
    155 atasu http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=atasu
    156 walvis bay http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=walvis bay
    157 sangar http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=sangar
    158 hirara http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=hirara
    159 salalah http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=salalah
    160 baie-comeau http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=baie-comeau
    161 rikitea http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=rikitea
    162 rach gia http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=rach gia
    163 bambous virieux http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=bambous virieux
    164 geraldton http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=geraldton
    165 shush http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=shush
    166 sao joao da barra http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=sao joao da barra
    167 marienburg http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=marienburg
    168 severo-yeniseyskiy http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=severo-yeniseyskiy
    169 the pas http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=the pas
    170 san patricio http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=san patricio
    171 kaitangata http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=kaitangata
    172 komsomolskiy http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=komsomolskiy
    173 cayenne http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=cayenne
    174 berlevag http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=berlevag
    175 tayoltita http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=tayoltita
    176 kopavogur http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=kopavogur
    177 rochelle http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=rochelle
    178 predivinsk http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=predivinsk
    179 jining http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=jining
    180 haverhill http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=haverhill
    181 te anau http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=te anau
    182 muisne http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=muisne
    183 basco http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=basco
    184 armizonskoye http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=armizonskoye
    185 kovylkino http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=kovylkino
    186 ilulissat http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=ilulissat
    187 albany http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=albany
    188 amantea http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=amantea
    189 xuddur http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=xuddur
    190 pemba http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=pemba
    191 arraial do cabo http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=arraial do cabo
    192 octeville http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=octeville
    193 qaqortoq http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=qaqortoq
    194 kahului http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=kahului
    195 lajas http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=lajas
    196 winslow http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=winslow
    197 high point http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=high point
    198 araouane http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=araouane
    199 port hardy http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=port hardy
    200 gat http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=gat
    201 puerto cabello http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=puerto cabello
    202 agidel http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=agidel
    203 kodinar http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=kodinar
    204 mataura http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=mataura
    205 talaya http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=talaya
    206 madang http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=madang
    207 fukue http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=fukue
    208 ketchikan http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=ketchikan
    209 khatanga http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=khatanga
    210 pangkalanbuun http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=pangkalanbuun
    211 marquette http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=marquette
    212 fortuna http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=fortuna
    213 havre-saint-pierre http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=havre-saint-pierre
    214 noumea http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=noumea
    215 arman http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=arman
    216 chany http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=chany
    217 dongobesh http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=dongobesh
    218 tempio pausania http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=tempio pausania
    219 ocosingo http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=ocosingo
    220 tekeli http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=tekeli
    221 kutum http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=kutum
    222 canyon http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=canyon
    223 san ramon http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=san ramon
    224 qaanaaq http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=qaanaaq
    225 teguise http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=teguise
    226 agucadoura http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=agucadoura
    227 saint anthony http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=saint anthony
    228 makakilo city http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=makakilo city
    229 yellowknife http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=yellowknife
    230 boa vista http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=boa vista
    231 tautira http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=tautira
    232 fort nelson http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=fort nelson
    233 mastic beach http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=mastic beach
    234 saint george http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=saint george
    235 brenham http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=brenham
    236 alofi http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=alofi
    237 hambantota http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=hambantota
    238 itarema http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=itarema
    239 lerwick http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=lerwick
    240 san jose de guanipa http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=san jose de guanipa
    241 angren http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=angren
    242 punta arenas http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=punta arenas
    243 naze http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=naze
    244 lagoa http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=lagoa
    245 durango http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=durango
    246 marti http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=marti
    247 mitsamiouli http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=mitsamiouli
    248 monster http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=monster
    249 barcelos http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=barcelos
    250 kundiawa http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=kundiawa
    251 bathsheba http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=bathsheba
    252 severo-kurilsk http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=severo-kurilsk
    253 benguela http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=benguela
    254 kerrville http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=kerrville
    255 ngunguru http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=ngunguru
    256 sol-iletsk http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=sol-iletsk
    257 hami http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=hami
    258 namibe http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=namibe
    259 leningradskiy http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=leningradskiy
    260 martin http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=martin
    261 channagiri http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=channagiri
    262 necochea http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=necochea
    263 beringovskiy http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=beringovskiy
    264 pyshma http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=pyshma
    265 atuona http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=atuona
    266 nisia floresta http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=nisia floresta
    267 qingdao http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=qingdao
    268 bogalusa http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=bogalusa
    269 kulhudhuffushi http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=kulhudhuffushi
    270 ingham http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=ingham
    271 east london http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=east london
    272 cap malheureux http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=cap malheureux
    273 mount isa http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=mount isa
    274 fairbanks http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=fairbanks
    275 faanui http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=faanui
    276 byron bay http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=byron bay
    277 kavieng http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=kavieng
    278 zhangjiakou http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=zhangjiakou
    279 lukaya http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=lukaya
    280 pampa http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=pampa
    281 kanevskaya http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=kanevskaya
    282 souillac http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=souillac
    283 clyde river http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=clyde river
    284 hovd http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=hovd
    285 narsaq http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=narsaq
    286 isangel http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=isangel
    287 banda aceh http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=banda aceh
    288 portland http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=portland
    289 constitucion http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=constitucion
    290 todos santos http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=todos santos
    291 tierralta http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=tierralta
    292 faya http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=faya
    293 ostrovnoy http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=ostrovnoy
    294 podor http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=podor
    295 ancud http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=ancud
    296 chokurdakh http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=chokurdakh
    297 pathardi http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=pathardi
    298 masumbwe http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=masumbwe
    299 upernavik http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=upernavik
    300 okha http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=okha
    301 lebu http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=lebu
    302 tuktoyaktuk http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=tuktoyaktuk
    303 alice springs http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=alice springs
    304 the valley http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=the valley
    305 omsukchan http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=omsukchan
    306 tucuman http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=tucuman
    307 terrace bay http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=terrace bay
    308 codrington http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=codrington
    309 hamilton http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=hamilton
    310 barentu http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=barentu
    311 pokrovsk http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=pokrovsk
    312 port elizabeth http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=port elizabeth
    313 leo http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=leo
    314 grafton http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=grafton
    315 lompoc http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=lompoc
    316 barillas http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=barillas
    317 saskylakh http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=saskylakh
    318 ouesso http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=ouesso
    319 havoysund http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=havoysund
    320 acacias http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=acacias
    321 chihuahua http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=chihuahua
    322 cape town http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=cape town
    323 thinadhoo http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=thinadhoo
    324 novyye burasy http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=novyye burasy
    325 wamba http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=wamba
    326 gadsden http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=gadsden
    327 lidkoping http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=lidkoping
    328 nikolskoye http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=nikolskoye
    329 qasigiannguit http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=qasigiannguit
    330 omaruru http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=omaruru
    331 lavrentiya http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=lavrentiya
    332 lethem http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=lethem
    333 sun city west http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=sun city west
    334 gladstone http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=gladstone
    335 srednekolymsk http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=srednekolymsk
    336 kununurra http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=kununurra
    337 mongoumba http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=mongoumba
    338 inverness http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=inverness
    339 canon city http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=canon city
    340 sola http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=sola
    341 sirjan http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=sirjan
    342 yerbogachen http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=yerbogachen
    343 henties bay http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=henties bay
    344 laguna http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=laguna
    345 huarmey http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=huarmey
    346 sangmelima http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=sangmelima
    347 picota http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=picota
    348 xingcheng http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=xingcheng
    349 talcahuano http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=talcahuano
    350 norman wells http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=norman wells
    351 kodiak http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=kodiak
    352 hutchinson http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=hutchinson
    353 boma http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=boma
    354 tasiilaq http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=tasiilaq
    355 filadelfia http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=filadelfia
    356 namatanai http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=namatanai
    357 volovo http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=volovo
    358 iqaluit http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=iqaluit
    359 santiago del estero http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=santiago del estero
    360 mokhsogollokh http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=mokhsogollokh
    361 amot http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=amot
    362 severnyy-kospashskiy http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=severnyy-kospashskiy
    363 bredasdorp http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=bredasdorp
    364 sainte-suzanne http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=sainte-suzanne
    365 dori http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=dori
    366 honiara http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=honiara
    367 vilyuysk http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=vilyuysk
    368 indiana http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=indiana
    369 sabinov http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=sabinov
    370 sibolga http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=sibolga
    371 jambi http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=jambi
    372 nijar http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=nijar
    373 thompson http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=thompson
    374 kapaa http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=kapaa
    375 duekoue http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=duekoue
    376 talnakh http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=talnakh
    377 kruisfontein http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=kruisfontein
    378 vardo http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=vardo
    379 aklavik http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=aklavik
    380 esperance http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=esperance
    381 damaturu http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=damaturu
    382 bilma http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=bilma
    383 gunupur http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=gunupur
    384 parabel http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=parabel
    385 kungurtug http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=kungurtug
    386 zhicheng http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=zhicheng
    387 batavia http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=batavia
    388 hasaki http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=hasaki
    389 singaparna http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=singaparna
    390 sazonovo http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=sazonovo
    391 cidreira http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=cidreira
    392 vaini http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=vaini
    393 mar del plata http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=mar del plata
    394 oussouye http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=oussouye
    395 mahibadhoo http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=mahibadhoo
    396 tefe http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=tefe
    397 hilo http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=hilo
    398 buraydah http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=buraydah
    399 tahoua http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=tahoua
    400 randazzo http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=randazzo
    401 yinchuan http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=yinchuan
    402 rio grande http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=rio grande
    403 sioux lookout http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=sioux lookout
    404 saint-joseph http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=saint-joseph
    405 meadow lake http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=meadow lake
    406 carnarvon http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=carnarvon
    407 hudson bay http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=hudson bay
    408 chiredzi http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=chiredzi
    409 vao http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=vao
    410 borgarnes http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=borgarnes
    411 takoradi http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=takoradi
    412 arlit http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=arlit
    413 praxedis guerrero http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=praxedis guerrero
    414 georgetown http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=georgetown
    415 aykhal http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=aykhal
    416 gao http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=gao
    417 wasilla http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=wasilla
    418 port hedland http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=port hedland
    419 los llanos de aridane http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=los llanos de aridane
    420 roebourne http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=roebourne
    421 nishihara http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=nishihara
    422 safford http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=safford
    423 darhan http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=darhan
    424 tiznit http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=tiznit
    425 nicoya http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=nicoya
    426 coquimbo http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=coquimbo
    427 karpathos http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=karpathos
    428 darnah http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=darnah
    429 hailin http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=hailin
    430 jumla http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=jumla
    431 itoman http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=itoman
    432 ajdabiya http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=ajdabiya
    433 san andres http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=san andres
    434 whitehorse http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=whitehorse
    435 yafran http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=yafran
    436 danane http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=danane
    437 pevek http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=pevek
    438 ceres http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=ceres
    439 coahuayana http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=coahuayana
    440 chara http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=chara
    441 ushuaia http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=ushuaia
    442 matara http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=matara
    443 puerto ayora http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=puerto ayora
    444 viedma http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=viedma
    445 morant bay http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=morant bay
    446 yarada http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=yarada
    447 wembley http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=wembley
    448 egvekinot http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=egvekinot
    449 dingle http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=dingle
    450 claveria http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=claveria
    451 keffi http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=keffi
    452 tuatapere http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=tuatapere
    453 kimbe http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=kimbe
    454 novokuznetsk http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=novokuznetsk
    455 vostok http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=vostok
    456 yar-sale http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=yar-sale
    457 kuchera http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=kuchera
    458 lazarev http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=lazarev
    459 luang prabang http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=luang prabang
    460 sobolevo http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=sobolevo
    461 waingapu http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=waingapu
    462 airai http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=airai
    463 abu dhabi http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=abu dhabi
    464 northam http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=northam
    465 altay http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=altay
    466 zaysan http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=zaysan
    467 xining http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=xining
    468 bluff http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=bluff
    469 vangaindrano http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=vangaindrano
    470 ahuimanu http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=ahuimanu
    471 homer http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=homer
    472 angoche http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=angoche
    473 san cristobal http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=san cristobal
    474 grootfontein http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=grootfontein
    475 aswan http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=aswan
    476 shenjiamen http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=shenjiamen
    477 dwarka http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=dwarka
    478 petropavlovsk-kamchatskiy http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=petropavlovsk-kamchatskiy
    479 fram http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=fram
    480 yulara http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=yulara
    481 ahipara http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=ahipara
    482 zeya http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=zeya
    483 poplar bluff http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=poplar bluff
    484 bethel http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=bethel
    485 havelock http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=havelock
    486 patrocinio http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=patrocinio
    487 ulaangom http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=ulaangom
    488 bijie http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=bijie
    489 port alfred http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=port alfred
    490 wanaka http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=wanaka
    491 tezu http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=tezu
    492 coihaique http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=coihaique
    493 moussoro http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=moussoro
    494 moyale http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=moyale
    495 houma http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=houma
    496 jiaonan http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=jiaonan
    497 ust-barguzin http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=ust-barguzin
    498 avera http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=avera
    499 pitimbu http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=pitimbu
    500 mahebourg http://api.openweathermap.org/data/2.5/weather?appid=4067b3eb20413d8e37f3d1bb67007825&units=imperial&q=mahebourg
    


```python
#Save data as csv
weather = {'city': cities, 'country': country, 'date': date, 'lat': lat, 'lon': lng,
           'humidity':  humidity, 'cloudiness': cloudiness, 'wind speed': windspeed, 'max temp': maxtemp}
weather_df = pd.DataFrame(weather)
weather_df.to_csv('weather_hw.csv')
weather_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>cloudiness</th>
      <th>country</th>
      <th>date</th>
      <th>humidity</th>
      <th>lat</th>
      <th>lon</th>
      <th>max temp</th>
      <th>wind speed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>azare</td>
      <td>0</td>
      <td>NG</td>
      <td>1523227806</td>
      <td>33</td>
      <td>11.67</td>
      <td>10.19</td>
      <td>71.14</td>
      <td>4.43</td>
    </tr>
    <tr>
      <th>1</th>
      <td>cabo san lucas</td>
      <td>5</td>
      <td>MX</td>
      <td>1523224440</td>
      <td>44</td>
      <td>22.89</td>
      <td>-109.91</td>
      <td>86.00</td>
      <td>12.75</td>
    </tr>
    <tr>
      <th>2</th>
      <td>warrnambool</td>
      <td>0</td>
      <td>AU</td>
      <td>1523227991</td>
      <td>92</td>
      <td>-38.38</td>
      <td>142.48</td>
      <td>62.86</td>
      <td>1.63</td>
    </tr>
    <tr>
      <th>3</th>
      <td>paamiut</td>
      <td>76</td>
      <td>GL</td>
      <td>1523228034</td>
      <td>95</td>
      <td>61.99</td>
      <td>-49.67</td>
      <td>30.73</td>
      <td>18.86</td>
    </tr>
    <tr>
      <th>4</th>
      <td>sao miguel do araguaia</td>
      <td>56</td>
      <td>BR</td>
      <td>1523227939</td>
      <td>96</td>
      <td>-13.28</td>
      <td>-50.16</td>
      <td>72.49</td>
      <td>3.87</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Latitude vs. Temperature (F)
plt.scatter(weather_df['lat'], weather_df['max temp'])#, marker='o')
plt.title('City Latitude vs. Maximum Temperature')
plt.xlabel('City Latitude')
plt.ylabel('Maximum Temperature (Farenheit)')
plt.grid(True)

plt.savefig('lat_maxtemp.png')

plt.show()
```


![png](output_4_0.png)



```python
#Latitude vs. Humidity (%)
plt.scatter(weather_df['lat'], weather_df['humidity'])#, marker='o')
plt.title('City Latitude vs. Humidity')
plt.xlabel('City Latitude')
plt.ylabel('Humidity (%)')
plt.grid(True)

plt.savefig('lat_humidity.png')

plt.show()
```


![png](output_5_0.png)



```python
#Latitude vs. Cloudiness (%)
plt.scatter(weather_df['lat'], weather_df['cloudiness'])#, marker='o')
plt.title('City Latitude vs. Cloudiness')
plt.xlabel('City Latitude')
plt.ylabel('Cloudiness (%)')
plt.grid(True)

plt.savefig('lat_cloudiness.png')

plt.show()
```


![png](output_6_0.png)



```python
#Latitude vs. Wind Speed (mph)
plt.scatter(weather_df['lat'], weather_df['wind speed'])#, marker='o')
plt.title('City Latitude vs. Wind Speed')
plt.xlabel('City Latitude')
plt.ylabel('Wind Speed (mph)')
plt.grid(True)

plt.savefig('lat_windspeed.png')

plt.show()
```


![png](output_7_0.png)

