import Myro
import math
from Myro import *
from Graphics import *
from Queue import PriorityQueue
from heapq import *
pque={}
pathcost = {}
parent={}
heap=[]
path=[]
explored={"oradea":0,"arad":0,"sibiu":0,"eforie":0,"fagaras":0,"lugoj":0,"rimnicuvilecea":0,
"pitesti":0,"bucharest":0,"neamt":0,"vaslui":0,"hirsova":0,"mehadia":0,"urziceni":0,"iasi":0,
"giurgiu":0,"zerind":0,"craiova":0,"drobeta":0,"timisoara":0}
citiesco_ord = {"oradea": [134,31],"arad":[69,160],"sibiu":[260,215],"eforie":[847,488],
"fagaras":[425,229],"lugoj":[190,346],"rimnicuvilecea":[304,295],"pitesti":[448,366],"bucharest":[579,430],
"neamt":[588,87],"vaslui":[761,236],"hirsova":[798,394],"mehadia":[196,411],
"urziceni":[672,392],"iasi":[702,135],"giurgiu":[535,523],"zerind":[98,93],"craiova":[337,498],
"drobeta":[191,478],"timisoara":[73,295]}

maps ={"arad":{"zerind":75,"timisoara":118,"sibiu":140},"zerind":{"oradea":71,"arad":75},"oradea":{"zerind":71,"sibiu":151},
"timisoara":{"arad":118,"lugoj":111},"sibiu":{"arad":140,"oradea":151,"rimnicuvilecea":80,"fagaras":99},
"lugoj":{"timisoara":111,"mehadia":70},"mehadia":{"lugoj":70,"drobeta":75},"craiova":{"drobeta":120,"rimnicuvilecea":146,"pitesti":138},
"rimnicuvilecea":{"sibiu":80,"craiova":146,"pitesti":97},"fagaras":{"sibiu":99,"bucharest":211},"pitesti":{"rimnicuvilecea":97,"craiova":138,"bucharest":101},
"bucharest":{"fagaras":211,"pitesti":101,"urziceni":85,"giurgiu":90},"urziceni":{"bucharest":85,"hirsova":98,"vaslui":142},
"hirsova":{"eforie":86,"urziceni":98},"vaslui":{"urziceni":142,"iasi":92},"iasi":{"vaslui":92,"neamt":87},"neamt":{"iasi":87},"giurgiu":{"bucharest":90},
"drobeta":{"mehadia":75,"craiova":120},"eforie":{"hirsova":86}}


flag = 1
startcity = raw_input("Enter the starting location")
start_X,start_Y = citiesco_ord[startcity]




endcity = raw_input("Enter the destination location")
goal_X,goal_Y = citiesco_ord[endcity]


#heuristic for each city
def getheur(a,b):
    start_heu_x,start_heu_y= citiesco_ord[a]
    end_heu_x,end_heu_y= citiesco_ord[b]
    distance = math.sqrt((math.pow((end_heu_x - start_heu_x),2)) + (math.pow((end_heu_y - start_heu_y),2)))
    distance = math.ceil(distance)
    return distance

def astar():


    heurcost={}
    heuristic = getheur(startcity,endcity)
    heurcost[startcity]=heuristic
    parent[startcity]="none"
    pathcost[startcity]=0
    explored[startcity]=1
    print("start city:",startcity)
    heappush(heap,0)
    pque[0]=startcity
    #pq.put(startcity,heuristic)
    #while not pq.empty():
    while heap:
        #element=pq.get()
        x=heappop(heap)
        element=pque[x]
        print("\n")
        print("next city selected:",element)
        if element == endcity:
            print("Goal city found!!!!\n")
            break
        else:
            adjacent=maps[element]
            for edges in adjacent:

                if explored[edges] !=1:
                    cost=adjacent[edges]
                    pathcost[edges]=cost+pathcost[element]
                    parent[edges]=element
                    totalcost= pathcost[edges]+getheur(edges,endcity)
                    print("adding edge:",edges," pathcost:",pathcost[edges],"totalcost:",totalcost)
                    #pq.put(edges,totalcost)
                    heappush(heap,totalcost)
                    pque[totalcost]=edges
                    explored[edges]=1
    previous=endcity
    path.append(previous)

    while  parent[previous] != "none":

        temp=parent[previous]
        previous=temp

        path.append(previous)

width, height = 900, 656




#win = Window('Video Stream', 427, 266)

#sim = Simulation("map", width, height, Color("white"))
sim=Simulation("Maze",width,height, Color("lightgreen"))

picture = makePicture("E:\AI\extra_project\RomaniaMap.PNG")
picture.draw(sim.window)
#sim.addWall([wallwidth*1,wallheight*1],[wallwidth*(1+2),wallheight*3 +thickness],Color("green"))
#sim.addWall([wallwidth*2,wallheight*2],[wallwidth*(1+2),wallheight*2 +thickness],Color("green"))
# Set up simulation
sim.setup()
robot = makeRobot("SimScribbler", sim)

robot.setPose(start_X, start_Y, 0)

astar()
path.reverse()
print("path",path)
print("total path cost:",pathcost[endcity])
for value in path:
    wait(1)
    value_x,value_y=citiesco_ord[value]
    robot.setPose(value_x,value_y,0)





