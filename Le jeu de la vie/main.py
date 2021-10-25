from Monde import *
import time


width=1200
height=960
cellPerRaw = 120

World_map = Monde(cellPerRaw,width,height)


World_map.randomStart()

pygame.display.flip()

# Event loop

time.sleep(0.5)

continuer = 1
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
    World_map.updateAll()
    World_map.display_map()
    # World_map.display_map_shell()
    # print('----------------------------')
    # time.sleep(0.0005)













# World_map = Monde(5)




# World_map.checkAllNeighborhoods()
# print(World_map.getCell(1,2).getNeighborhood())
# print(World_map.getCell(4,2).getNeighborhood())

# print(-1%10)

# World_map.display_map_shell()
# print('------------------')

# World_map.updateAll()

# World_map.display_map_shell()
