import sys
import math
import json
import random


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

# 산하
my_min_length=MAX_NUMBER
my_current_distance=0
my_dol_index_bottom=0
my_dol_index_top=0
my_moong={}
my_moong=set()
#my_moong_2=[]
my_avg_moong_x=[]
my_avg_moong_y=[]
distance=0
flag = True
inclination = 0
# 해야할 것 : 뭉친 돌 중 하나가 나가게 할 것

#돌이 가장 좁게 모여있는 것의 중앙 좌표
for your in your_position:
    for y in your_position:
        # x와 y좌표가 같으면
        if(y[0]==your[0] and y[1]==your[1]):
            continue
        else:
            x_distance = abs(y[0] - your[0])
            y_distance = abs(y[1] - your[1])
            current_distance = math.sqrt(x_distance * x_distance + y_distance * y_distance)

            # 상대방 돌들 중 뭉친것 같다는 거리 설정
            if your_min_length> current_distance and current_distance < 80:
                your_min_length = current_distance
                your_x = (y[0] + your[0])/2
                your_y = (y[1] + your[1])/2


######################## 내 돌들 중 뭉친 돌 찾기###################################


# 내 돌 인덱스는 0번부터시작 (my_dol_index)

for my in my_position:
    my_dol_index_bottom=0
    for m_y in my_position:
        # 똑같은 돌끼리 비교 방지 0번부터 비교
        if(m_y[0]==my[0] and m_y[1]==my[1]):
            my_dol_index_bottom=my_dol_index_bottom+1
            continue
        else:
            x_distance = abs(m_y[0] - my[0])
            y_distance = abs(m_y[1] - my[1])
            my_current_distance = math.sqrt(x_distance * x_distance + y_distance * y_distance)

            # 내 돌들 중 가장 뭉친것 같다는 돌 선정식 ^^
            if my_min_length> my_current_distance and my_current_distance < 80:
                my_min_length = my_current_distance
                # 뭉친 돌 번호 저장 셋이라 중복 허가 안함
                #my_moong.add(my_dol_index_top)
                my_moong.add(my_dol_index_top)
                my_moong.add(my_dol_index_bottom)
                #my_moong_2.append(my_dol_index_bottom)

                # 그리고 이돌들의 x,y평균값을 리스트로 구한다.
                #my_avg_moong_x.append=(m_y[0] + my[0])/2
                #my_avg_moong_y.append=(m_y[1] + my[1])/2
                
        my_dol_index_bottom=my_dol_index_bottom+1
    my_dol_index_top=my_dol_index_top+1
    #my_dol_index_top=my_dol_index_top+1
    
    

######################## 내 돌들 중 뭉친 돌 선정 완료###################################
if len(my_position) > len(your_position):
    message="my>your"
    for my in my_position:
        for your in your_position:
            x_distance = abs(my[0] - your[0])
            y_distance = abs(my[1] - your[1])
            current_distance = math.sqrt(x_distance * x_distance + y_distance * y_distance)
            if min_length > current_distance:
                current_stone_number = index
                min_length = current_distance
                x_length = your[0] - my[0]
                y_length = your[1] - my[1]
        index = index + 1
    

else :
        
    #가장 좁은 돌 사이의 거리가 100 이하면
    if your_min_length != MAX_NUMBER:

        # 만약 내 돌 중 뭉쳐있는 돌이 있다면
        # if my_min_length != MAX_NUMBER:
        #     message = "you o my o"
        #     # 상대방의 뭉친 지점은 이미 정해져 있으므로 내 뭉친 돌들과의 거리를 비교한다.
        #     #moong_index=0
        #     distance=0
        #     min_length=MAX_NUMBER


        #     # my_moong에는 돌의 번호만 들어가있음
        #     for my in my_moong:
        #         x_distance=abs(my_position[my][0]-your_x)
        #         y_distance=abs(my_position[my][1]-your_y)
        #         distance=math.sqrt(x_distance * x_distance + y_distance * y_distance)

        #         # 내 뭉친돌과 상대방 뭉친돌 사이 가장 짧은 거리를 측정해 내돌선정
        #         if min_length> distance:
        #             min_length = distance
        #             current_stone_number = index
        #             x_length = your_x-my_position[my][0]
        #             y_length = your_y-my_position[my][1]

        #             current_stone_number = my
        #         index=index+1

        #         #moong_index=moong_index+1



        # # 내 돌 중 가장 뭉친돌 중간 지점과 가장 가까운 돌 셀렉트
        # else:
            message = "you o my x"
            index=0
            for my in my_position:
                x_distance = abs(my[0] - your_x)
                y_distance = abs(my[1] - your_y)
                current_distance = math.sqrt(x_distance * x_distance + y_distance * y_distance)
                # 가장 가까운 돌 찾는 중
                if min_length> current_distance:
                
                    current_stone_number = index
                    min_length = current_distance
                    x_length = your_x- my[0]+random.randint(-5,5)
                    y_length = your_y - my[1]+random.randint(-5,5)

                index=index+1
                



    #상대방 돌 중에 뭉쳐있는 돌이 없다면, 가장 가까이에 있는 돌 침
    else : 
        # 만약 내 돌 중 뭉쳐있는 돌이 있다면
        if my_min_length != MAX_NUMBER:
            message = "you x my o"
            # 내 뭉친 돌 중 상대방의 가장 가까운 돌을 선정
            # my_moong은 뭉친 돌 넘버가 들어있음
            for my in my_moong:
                for your in your_position:
                    x_distance = abs(my_position[my][0] - your[0])
                    y_distance = abs(my_position[my][1] - your[1])
                    current_distance = math.sqrt(x_distance * x_distance + y_distance * y_distance)

                    #기울기
                    inclination = (my_position[my][1] - your[1])/(my_position[my][0] - your[0])

                    for m in my_moong:
                        if my_position[m][0]==my_position[my][0] and my_position[m][1]==my_position[my][1]:
                            continue
                        if inclination + 1 > (my_position[m][1] - your[1])/(my_position[m][0] - your[0]) and inclination - 1 < (my_position[m][1] - your[1])/(my_position[m][0] - your[0]):
                            flag = False

                    if min_length > current_distance and flag==True:
                        current_stone_number = index
                        min_length = current_distance
                        x_length = your[0] - my_position[my][0]+random.randint(-10,10)
                        y_length = your[1] - my_position[my][1]+random.randint(-10,10)
                    flag=True
                index = index + 1
            
            if min_length==MAX_NUMBER:
                
                index=0
                for my in my_position:
                    for your in your_position:
                        x_distance = abs(my[0] - your[0])
                        y_distance = abs(my[1] - your[1])
                        current_distance = math.sqrt(x_distance * x_distance + y_distance * y_distance)
                        if min_length > current_distance:
                            current_stone_number = index
                            min_length = current_distance
                            x_length = your[0] - my[0]+random.randint(-10,10)
                            y_length = your[1] - my[1]+random.randint(-10,10)
                    index = index + 1

                    

                #     if min_length > current_distance:
                #         current_stone_number = index
                #         min_length = current_distance
                #         x_length = your[0] - my_position[my][0]+random.randint(-20,20)
                #         y_length = your[1] - my_position[my][1]+random.randint(-20,20)
                #         current_stone_number = my
                # index = index + 1

                
    
            


        # 아니면 그냥 가까운 돌 침
        else:
            message = "you x my x"
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
                        x_length = your[0] - my[0]+random.randint(-10,10)
                        y_length = your[1] - my[1]+random.randint(-10,10)
                    flag=True
                index = index + 1

            
            if min_length==MAX_NUMBER:
                
                index=0
                for my in my_position:
                    for your in your_position:
                        x_distance = abs(my[0] - your[0])
                        y_distance = abs(my[1] - your[1])
                        current_distance = math.sqrt(x_distance * x_distance + y_distance * y_distance)
                        if min_length > current_distance:
                            current_stone_number = index
                            min_length = current_distance
                            x_length = your[0] - my[0]+random.randint(-10,10)
                            y_length = your[1] - my[1]+random.randint(-10,10)
                    index = index + 1
            
        


#Return values

stone_number = current_stone_number
stone_x_strength = x_length * 10
stone_y_strength = y_length * 10
result = [stone_number, stone_x_strength, stone_y_strength, message]


print(str(result)[1:-1].replace("'", ""))