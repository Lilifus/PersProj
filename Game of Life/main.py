from Monde import *
import time


width=600
height=480
cellPerRaw = 60

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
    time.sleep(0.05)













# World_map = Monde(5)




# World_map.checkAllNeighborhoods()
# print(World_map.getCell(1,2).getNeighborhood())
# print(World_map.getCell(4,2).getNeighborhood())

# print(-1%10)

# World_map.display_map_shell()
# print('------------------')

# World_map.updateAll()

# World_map.display_map_shell()
