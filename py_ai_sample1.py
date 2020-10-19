import sys
import math
import json


with open('temp.json') as json_file:
    json_data = json.load(json_file)


MAX_NUMBER = 16000


my_position = []
your_position = []

for key in json_data["my_position"].keys():
    my_position.append(json_data["my_position"][key])

for key in json_data["your_position"].keys():
    your_position.append(json_data["your_position"][key])


current_stone_number = 0
index = 0
min_length = MAX_NUMBER
x_length = MAX_NUMBER
y_length = MAX_NUMBER

your_min_length = MAX_NUMBER
your_x = MAX_NUMBER
your_y = MAX_NUMBER


inclination = 0
flag = True

#돌이 가장 좁게 모여있는 것의 중앙 좌표
for your in your_position:
    for y in your_position:
        if(y[0]==your[0] and y[1]==your[1]):
            continue
        else:
            x_distance = abs(y[0] - your[0])
            y_distance = abs(y[1] - your[1])
            current_distance = math.sqrt(x_distance * x_distance + y_distance * y_distance)
        if your_min_length> current_distance and current_distance < 110:
            your_min_length = current_distance
            your_x = (y[0] + your[0])/2
            your_y = (y[1] + your[1])/2

#가장 좁은 돌 사이의 거리가 130 이하면
if your_min_length != MAX_NUMBER:
    for my in my_position:
        x_distance = abs(my[0] - your_x)
        y_distance = abs(my[1] - your_y)
        current_distance = math.sqrt(x_distance * x_distance + y_distance * y_distance)
        if min_length > current_distance:
            current_stone_number = index
            min_length = current_distance
            x_length = your_x- my[0]
            y_length = your_y - my[1]
        index = index + 1
#아니면 가장 가까이에 있는 돌 침
else :
    for my in my_position:
        for your in your_position:
            x_distance = abs(my[0] - your[0])
            y_distance = abs(my[1] - your[1])
            current_distance = math.sqrt(x_distance * x_distance + y_distance * y_distance)

            #기울기
            inclination = (my[1] - your[1])/(my[0] - your[0])

            for m in my_position:
                if m[0]==my[0] and m[1]==my[1]:
                    continue
                if inclination + 1 > (m[1] - your[1])/(m[0] - your[0]) and inclination - 1 < (m[1] - your[1])/(m[0] - your[0]):
                    flag = False

            if min_length > current_distance and flag==True:
                current_stone_number = index
                min_length = current_distance
                x_length = your[0] - my[0]
                y_length = your[1] - my[1]
            flag=True
        index = index + 1





#Return values
message = ""
stone_number = current_stone_number
stone_x_strength = x_length * 10
stone_y_strength = y_length * 10
result = [stone_number, stone_x_strength, stone_y_strength, message]


print(str(result)[1:-1].replace("'", ""))
