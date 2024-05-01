import random
from math import sqrt
from math import inf
#these lines read the file
the_particle=[]
with open("points.txt") as primary_points:
    for it in primary_points.readlines():
        the_particle.append(it[:-1].split(","))
#---------------------------------------------------------
#these lines delete unuseful datas
the_particle2=[]
for point in the_particle.copy():
    my_list=[]
    for coordinate in point:
        try:
            x=float(coordinate)
            my_list.append(x)
        except:
            the_particle.remove(point)
            continue
    if len(my_list)==3:
        the_particle2.append(my_list)
#---------------------------------------------------------
number_of_k=int(input("enter the number of k: "))
center_points_before = [random.choice(the_particle2) for _ in range(number_of_k)]
center_points_now = []
groups = []
#---------------------------------------------------------
def calculate_distance(list1,list2):
    return sqrt((list1[0]-list2[0])**2 + (list1[1]-list2[1])**2 + (list1[2]-list2[2])**2)
#---------------------------------------------------------
def choose_group(point):
    temp = inf
    result = 0
    for index,item in enumerate(center_points_before):
        temp2 = calculate_distance(item,point)
        if temp2<temp:
            temp = temp2
            result = index
    return result
#---------------------------------------------------------
def calculate_mean(list):
    X = 0
    Y = 0
    Z = 0
    for x,y,z in list:
        X+=x
        Y+=y
        Z+=z
    return [X/len(list),Y/len(list),Z/len(list)]
#----------------------------------------------------------

while True:
    print(center_points_before == center_points_now)
    groups.clear()
    for it in range(number_of_k):
        groups.append([])

    for item in the_particle2:
        (groups[choose_group(item)]).append(item)

    center_points_now.clear()
    for item in groups:
        means=calculate_mean(item)
        center_points_now.append(means)


    if center_points_before==center_points_now:
        break
    else:
        center_points_before=center_points_now
    


print(groups)

for item in groups:
    print(len(item))

