#!/usr/bin/python
# coding: utf-8

import Adafruit_DHT as DHT

SENSOR_TYPE = DHT.DHT11

DHT_GPIO = 22

h,t = DHT.read_retry(SENSOR_TYPE, DHT_GPIO)

discomfort = 0.81*t+0.01*h*(0.99*t-14.3)+46.3

if discomfort > 85:
    experience = "暑くてたまらない"
elif discomfort >80 and discomfort <=85:
    experience = "暑くて汗が出る"
elif discomfort > 75 and discomfort <=80:
    experience = "やや暑い"
elif discomfort > 70 and discomfort <=75:
    experience = "暑さを感じ始める"
elif discomfort > 65 and discomfort <=70:
    experience = "快適"
elif discomfort > 60 and discomfort <=65:
    experience = "何も感じない"
elif discomfort > 55 and discomfort <=60:
    experience = "肌寒い"
elif discomfort <=55:
    experience = "寒い"


print "現在の部屋の温度は{0:0.1f}℃、\n湿度は{1:0.1f}%です。\n\
不快指数は{2:0.1f}で{3}でしょう。".format(t,h,discomfort,experience)
