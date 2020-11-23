import pygame
import random
import math

def describemap():
    mapfile = open('地图.txt','r')
    content = mapfile.readlines()
    mapfile.close()
    maptextlines = []
    mapxy = []
    floors = []
    walls = []
    heros = []
    lts = []
    lts2 = []
    npcs = []
    monsters = []
    doors = []
    yellow_doors = []
    green_doors = []
    purple_doors = []
    red_doors = []
    orange_doors = []
    colors_doors = []
    keys = []
    yellow_keys = []
    green_keys = []
    purple_keys = []
    red_keys = []
    orange_keys = []
    colors_keys = []
    mapwidths = []
    mapheights = []
    for i in range(len(content)):
        line = content[i].rstrip('\n')
        if line != '':
            maptextlines.append(line)
        if len(maptextlines) > 0 and line == '':
            mapwidths.append(len(maptextlines[0]))
            mapheights.append(len(maptextlines))
            for x in range(len(maptextlines[0])):
                mapxy.append([])
            for y in range(len(maptextlines)):
                for x in range(len(maptextlines[0])):
                    mapxy[x].append(maptextlines[y][x])
            floor = []
            wall = []
            lt = []
            lt2 = []
            yellow_door = []
            green_door = []
            purple_door = []
            red_door = []
            orange_door = []
            colors_door = []
            yellow_key = []
            green_key = []
            purple_key = []
            red_key = []
            orange_key = []
            colors_key = []
            npc = {}
            # 怪物
            monster = {}
            Z_monster = []
            X_monster = []

            for x in range(len(mapxy)):
                for y in range(len(mapxy[0])):
                    if mapxy[x][y] in ('1','z','a','s','5','6','7','8','9','0','q','w','e','r','t','y','Z','X'):
                        floor.append([x,y])
                    if mapxy[x][y] == '2':
                        wall.append([x,y])
                    if mapxy[x][y] == 'z':
                        heros.append([x,y])
                    if mapxy[x][y] == '3':
                        lt.append([x,y])
                    if mapxy[x][y] == '4':
                        lt2.append([x,y])
                    # 6种颜色的门
                    if mapxy[x][y] == '5':
                        yellow_door.append([x,y])
                    if mapxy[x][y] == '6':
                        green_door.append([x,y])
                    if mapxy[x][y] == '7':
                        purple_door.append([x, y])
                    if mapxy[x][y] == '8':
                        red_door.append([x, y])
                    if mapxy[x][y] == '9':
                        orange_door.append([x, y])
                    if mapxy[x][y] == '0':
                        colors_door.append([x, y])
                    # 6种颜色的钥匙
                    if mapxy[x][y] == 'q':
                        red_key.append([x, y])
                    if mapxy[x][y] == 'w':
                        green_key.append([x, y])
                    if mapxy[x][y] == 'e':
                        purple_key.append([x, y])
                    if mapxy[x][y] == 'r':
                        red_key.append([x, y])
                    if mapxy[x][y] == 't':
                        orange_key.append([x, y])
                    if mapxy[x][y] == 'y':
                        colors_key.append([x, y])
                    # npc
                    if mapxy[x][y] == 'a':
                        npc['a'] = [x,y]
                    if mapxy[x][y] == 's':
                        npc['s'] = [x,y]
                    # 怪物
                    if mapxy[x][y] == 'Z':
                        Z_monster.append([x,y])
                    if mapxy[x][y] == 'X':
                        X_monster.append([x,y])

            floors.append(floor)
            walls.append(wall)
            lts.append(lt)
            lts2.append(lt2)
            yellow_doors.append(yellow_door)
            green_doors.append(green_door)
            purple_doors.append(purple_door)
            red_doors.append(red_door)
            orange_doors.append(orange_door)
            colors_doors.append(colors_door)
            yellow_keys.append(yellow_key)
            green_keys.append(green_key)
            purple_keys.append(purple_key)
            red_keys.append(red_key)
            orange_keys.append(orange_key)
            colors_keys.append(colors_key)
            npcs.append(npc)
            # 怪物
            monster['Z'] = Z_monster
            monster['X'] = X_monster
            monsters.append(monster)

            floor = []
            wall = []
            lt = []
            yellow_door = []
            green_door = []
            purple_door = []
            red_door = []
            orange_door = []
            colors_door = []
            yellow_key = []
            green_key = []
            purple_key = []
            red_key = []
            orange_key = []
            colors_key = []
            npc = {}
            Z_monster = []
            X_monster = []
            monster = {}
            maptextlines = []
            mapxy = []
    doors.append(yellow_doors)
    doors.append(green_doors)
    doors.append(purple_doors)
    doors.append(red_doors)
    doors.append(orange_doors)
    doors.append(colors_doors)
    keys.append(yellow_keys)
    keys.append(green_keys)
    keys.append(purple_keys)
    keys.append(red_keys)
    keys.append(orange_keys)
    keys.append(colors_keys)
    map = []
    map.append(floors)
    map.append(walls)
    map.append(mapwidths)
    map.append(mapheights)
    map.append(heros)
    map.append(lts)
    map.append(lts2)
    map.append(npcs)
    map.append(doors)
    map.append(keys)
    map.append(monsters)
    return(map)

def drawmap(map,layer,tiles_image,hero_direction):
    tile_width = 60
    tile_height = 60
    mapsurface_width = map[2][layer] * tile_width
    mapsurface_height = map[3][layer] * tile_height
    mapsurface = pygame.Surface((mapsurface_width,mapsurface_height))
    mapsurface.fill((100,100,100))
    # 遍历第layer个图的地板并绘制
    for i in range(len(map[0][layer])):
        x = map[0][layer][i][0] * tile_width
        y = map[0][layer][i][1] * tile_height
        tile_rect = pygame.Rect((x,y,tile_width,tile_height))
        mapsurface.blit(tiles_image['1'],tile_rect)
    # 遍历第layer个图的墙并绘制
    for i in range(len(map[1][layer])):
        x = map[1][layer][i][0] * tile_width
        y = map[1][layer][i][1] * tile_height
        tile_rect = pygame.Rect((x,y,tile_width,tile_height))
        mapsurface.blit(tiles_image['2'],tile_rect)
    # 楼梯绘制
    for i in range(len(map[5][layer])):
        x = map[5][layer][i][0] * tile_width
        y = map[5][layer][i][1] * tile_height
        tile_rect = pygame.Rect((x, y, tile_width, tile_height))
        mapsurface.blit(tiles_image['3'], tile_rect)
    for i in range(len(map[6][layer])):
        x = map[6][layer][i][0] * tile_width
        y = map[6][layer][i][1] * tile_height
        tile_rect = pygame.Rect((x, y, tile_width, tile_height))
        mapsurface.blit(tiles_image['4'], tile_rect)
    # 钥匙绘制
    for j in range(len(map[9])):
        for i in range(len(map[9][j][layer])):
            if j == 0:
                key_image = tiles_image['q']
            if j == 1:
                key_image = tiles_image['w']
            if j == 2:
                key_image = tiles_image['e']
            if j == 3:
                key_image = tiles_image['r']
            if j == 4:
                key_image = tiles_image['t']
            if j == 5:
                key_image = tiles_image['y']
            x = map[9][j][layer][i][0] * tile_width
            y = map[9][j][layer][i][1] * tile_height
            key_rect = pygame.Rect((x,y,tile_width,tile_height))
            mapsurface.blit(key_image,key_rect)
    # 地牢门绘制
    for j in range(len(map[8])):
        for i in range(len(map[8][j][layer])):
            if j == 0:
                door_image = tiles_image['5']
            if j == 1:
                door_image = tiles_image['6']
            if j == 2:
                door_image = tiles_image['7']
            if j == 3:
                door_image = tiles_image['8']
            if j == 4:
                door_image = tiles_image['9']
            if j == 5:
                door_image = tiles_image['10']
            if [map[8][j][layer][i][0] - 1,map[8][j][layer][i][1]] in map[1][layer]:
                x1 = map[8][j][layer][i][0] * tile_width
                y1 = map[8][j][layer][i][1] * tile_height
                tile_rect1 = pygame.Rect((x1, y1, tile_width/2, tile_height))
                x2 = x1 + tile_width/2
                y2 = y1
                tile_rect2 = pygame.Rect((x2, y2, tile_width/2, tile_height))
                image2 = pygame.transform.rotate(door_image,180)
                mapsurface.blit(door_image, tile_rect1)
                mapsurface.blit(image2, tile_rect2)
            if [map[8][j][layer][i][0],map[8][j][layer][i][1] - 1] in map[1][layer]:
                x1 = map[8][j][layer][i][0] * tile_width
                y1 = map[8][j][layer][i][1] * tile_height
                tile_rect1 = pygame.Rect((x1, y1, tile_width, tile_height/2))
                x2 = x1
                y2 = y1 + tile_height/2
                tile_rect2 = pygame.Rect((x2, y2, tile_width, tile_height/2))
                image1 = pygame.transform.rotate(door_image,270)
                image2 = pygame.transform.rotate(door_image,90)
                mapsurface.blit(image1, tile_rect1)
                mapsurface.blit(image2, tile_rect2)
    # 怪物绘制
    for key,value in map[10][layer].items():
        if value != []:
            for i in range(len(value)):
                rect = tiles_image[key].get_rect()
                rect.centerx = value[i][0] * tile_width + tile_width/2
                rect.centery = value[i][1] * tile_height + tile_height/2
                mapsurface.blit(tiles_image[key],rect)


    # 主人公绘制
    hero_x = map[4][layer][0] * tile_width
    hero_y = map[4][layer][1] * tile_height
    hero_rect = pygame.Rect((hero_x + (tile_width - 35)/2,hero_y + (tile_height - 47)/2,35,47))
    if hero_direction[0]:
        mapsurface.blit(tiles_image['z1'],hero_rect)
    if hero_direction[1]:
        mapsurface.blit(tiles_image['z2'],hero_rect)
    if hero_direction[2]:
        mapsurface.blit(tiles_image['z3'],hero_rect)
    if hero_direction[3]:
        mapsurface.blit(tiles_image['z4'],hero_rect)

    # npc绘制
    if map[7][layer] != {}:
        for key,value in map[7][layer].items():
            npc_x = value[0] * tile_width
            npc_y = value[1] * tile_height
            npc_rect = pygame.Rect((npc_x,npc_y,tile_width,tile_height))
            mapsurface.blit(tiles_image[key], npc_rect)
    return(mapsurface)

def opendoor(map,tiles_image,yellow_key,green_key,purple_key,red_key,orange_key,colors_key,FPSclock,layer,mapsurface,mapsurface_rect,screen,door_direction,i):

    if (yellow_key and i == 0) or (green_key and i == 1) or (purple_key and i == 2) or (red_key and i == 3) or (orange_key and i == 4) or (colors_key and i == 5):
        # 按上键或下键开门动画
        if door_direction == 'up' or door_direction == 'down':
            x = map[4][layer][0] * 60
            x2 = x
            if door_direction == 'up':
                y = (map[4][layer][1] - 1) * 60
            if door_direction == 'down':
                y = (map[4][layer][1] + 1) * 60
            while True:
                if x >= map[4][layer][0] * 60 - 30:
                    if door_direction == 'up':
                        floor_rect = pygame.Rect((map[4][layer][0] * 60, (map[4][layer][1] - 1) * 60, 60, 60))
                    if door_direction == 'down':
                        floor_rect = pygame.Rect((map[4][layer][0] * 60, (map[4][layer][1] + 1) * 60, 60, 60))
                    mapsurface.blit(tiles_image['1'], floor_rect)
                    door_rect1 = pygame.Rect((x, y, 30, 60))
                    door_rect2 = pygame.Rect((x2 + 30, y, 30, 60))
                    image2 = pygame.transform.rotate(tiles_image[str(i+5)],180)
                    mapsurface.blit(tiles_image[str(i+5)], door_rect1)
                    mapsurface.blit(image2, door_rect2)
                    x -= 1
                    x2 += 1
                    screen.blit(mapsurface, mapsurface_rect)
                    pygame.display.update()
                    FPSclock.tick(30)
                else:
                    if door_direction == 'up':
                        map[8][i][layer].remove([map[4][layer][0], map[4][layer][1] - 1])
                    if door_direction == 'down':
                        map[8][i][layer].remove([map[4][layer][0], map[4][layer][1] + 1])
                    if i == 0:
                        yellow_key -= 1
                    if i == 1:
                        green_key -= 1
                    if i == 2:
                        purple_key -= 1
                    if i == 3:
                        red_key -= 1
                    if i == 4:
                        orange_key -= 1
                    if i == 5:
                        colors_key -= 1
                    break
        # 按左键或右键开门动画
        if door_direction == 'left' or door_direction == 'right':
            y = map[4][layer][1] * 60
            y2 = y
            if door_direction == 'left':
                x = (map[4][layer][0] - 1) * 60
            if door_direction == 'right':
                x = (map[4][layer][0] + 1) * 60
            while True:
                if y >= map[4][layer][1] * 60 - 30:
                    if door_direction == 'left':
                        floor_rect = pygame.Rect(((map[4][layer][0] - 1) * 60, map[4][layer][1] * 60, 60, 60))
                    if door_direction == 'right':
                        floor_rect = pygame.Rect(((map[4][layer][0] + 1) * 60, map[4][layer][1] * 60, 60, 60))
                    mapsurface.blit(tiles_image['1'], floor_rect)
                    door_rect1 = pygame.Rect((x, y, 60, 30))
                    door_rect2 = pygame.Rect((x, y2 + 30, 60, 30))
                    image1 = pygame.transform.rotate(tiles_image[str(i+5)], 270)
                    image2 = pygame.transform.rotate(tiles_image[str(i+5)], 90)
                    mapsurface.blit(image1, door_rect1)
                    mapsurface.blit(image2, door_rect2)
                    y -= 1
                    y2 += 1
                    screen.blit(mapsurface, mapsurface_rect)
                    pygame.display.update()
                    FPSclock.tick(30)
                else:
                    if door_direction == 'left':
                        map[8][i][layer].remove([map[4][layer][0] - 1, map[4][layer][1]])
                    if door_direction == 'right':
                        map[8][i][layer].remove([map[4][layer][0] + 1, map[4][layer][1]])
                    if i == 0:
                        yellow_key -= 1
                    if i == 1:
                        green_key -= 1
                    if i == 2:
                        purple_key -= 1
                    if i == 3:
                        red_key -= 1
                    if i == 4:
                        orange_key -= 1
                    if i == 5:
                        colors_key -= 1
                    break
    return(yellow_key,green_key,purple_key,red_key,orange_key,colors_key)

# 绘制钥匙计数板
def drawkeyscoreboard(yellow_key,green_key,purple_key,red_key,orange_key,colors_key,basic_FONT,screen,tiles_image,yellow_rect,green_rect,purple_rect,red_rect,orange_rect,colors_rect,y_rect,g_rect,p_rect,r_rect,o_rect,c_rect):
    if yellow_key:
        y_surf = basic_FONT.render('× ' + str(yellow_key), 1, (200, 150, 50))
        screen.blit(tiles_image['smallq'],yellow_rect)
        screen.blit(y_surf,y_rect)
    if green_key:
        g_surf = basic_FONT.render('× ' + str(green_key), 1, (200, 150, 50))
        screen.blit(tiles_image['smallw'],green_rect)
        screen.blit(g_surf,g_rect)
    if purple_key:
        p_surf = basic_FONT.render('× ' + str(purple_key), 1, (200, 150, 50))
        screen.blit(tiles_image['smalle'],purple_rect)
        screen.blit(p_surf,p_rect)
    if red_key:
        r_surf = basic_FONT.render('× ' + str(red_key), 1, (200, 150, 50))
        screen.blit(tiles_image['smallr'],red_rect)
        screen.blit(r_surf,r_rect)
    if orange_key:
        o_surf = basic_FONT.render('× ' + str(orange_key), 1, (200, 150, 50))
        screen.blit(tiles_image['smallt'],orange_rect)
        screen.blit(o_surf,o_rect)
    if colors_key:
        c_surf = basic_FONT.render('× ' + str(colors_key), 1, (200, 150, 50))
        screen.blit(tiles_image['smally'],colors_rect)
        screen.blit(c_surf,c_rect)

# z = 'Z','X' ......代表怪的种类
def fighting(z,map,layer,monster_attribute,yh_attribute,screen_width,screen_height,screen,tiles_image,basic_FONT,sys,attributes,equipment,equipment_imformation2,zhongjia_skill,kongzhi_skill,kuangzhan_skill):
    if map[4][layer] in map[10][layer][str(z)]:
        # 怪物属性值
        monster_name = monster_attribute[z][0]
        monster_life = monster_attribute[z][1]
        monster_attack = monster_attribute[z][2]
        monster_defend = monster_attribute[z][3]
        monster_dodge = monster_attribute[z][4]
        monster_crit = monster_attribute[z][5]
        monster_dizziness = monster_attribute[z][6]

        # 战斗表参数
        fighting_width = screen_width/2
        fighting_height = 300
        fighting_surf = pygame.Surface((fighting_width,fighting_height))
        fighting_rect = fighting_surf.get_rect()
        fighting_rect.right = screen_width
        yh_dizzinessed = 0
        monster_dizzinessed = 0
        fighting_end = False
        upgrade = False
        fall_equipment = []
        full_equipment = False
        equipment_name = ''
        poison = 0

        # 怪
        monster_rect = tiles_image[z].get_rect()
        monster_rect.x = 10
        monster_rect.centery = 80/2
        monstername_surf = basic_FONT.render(monster_name, 1, (0, 0, 0))
        monstername_rect = monstername_surf.get_rect()
        monstername_rect.x = 70
        monstername_rect.centery = 80/2
        monsterattack_surf = basic_FONT.render('攻击 ：' + str(monster_attack), 1, (0, 0, 0))
        monsterattack_rect = monsterattack_surf.get_rect()
        monsterattack_rect.x = 5
        monsterattack_rect.y = 115
        monsterdefend_surf = basic_FONT.render('防御 ：' + str(monster_defend), 1, (0, 0, 0))
        monsterdefend_rect = monsterdefend_surf.get_rect()
        monsterdefend_rect.x = 5
        monsterdefend_rect.y = 140
        monsterdodge_surf = basic_FONT.render('躲闪率 ：' + str(monster_dodge), 1, (0, 0, 0))
        monsterdodge_rect = monsterdodge_surf.get_rect()
        monsterdodge_rect.x = 5
        monsterdodge_rect.y = 165
        monstercrit_surf = basic_FONT.render('暴击率 ：' + str(monster_crit), 1, (0, 0, 0))
        monstercrit_rect = monstercrit_surf.get_rect()
        monstercrit_rect.x = 5
        monstercrit_rect.y = 190
        monsterdizziness_surf = basic_FONT.render('击晕率 ：' + str(monster_dizziness), 1, (0, 0, 0))
        monsterdizziness_rect = monsterdizziness_surf.get_rect()
        monsterdizziness_rect.x = 5
        monsterdizziness_rect.y = 215


        # hero
        hero_rect = tiles_image['z2'].get_rect()
        hero_rect.x = 10 + fighting_width/2
        hero_rect.centery = 80 / 2
        heroname_surf = basic_FONT.render(yh_attribute[0], 1, (0, 0, 0))
        heroname_rect = heroname_surf.get_rect()
        heroname_rect.x = 70 + fighting_width/2
        heroname_rect.centery = 80 / 2
        # 攻击力可能变化，因此在循环内绘制
        hero_attack = yh_attribute[2]
        herodefend_surf = basic_FONT.render('防御 ：' + str(yh_attribute[3]), 1, (0, 0, 0))
        herodefend_rect = herodefend_surf.get_rect()
        herodefend_rect.x = 5 + fighting_width/2
        herodefend_rect.y = 140
        herododge_surf = basic_FONT.render('躲闪率 ：' + str(yh_attribute[4]),1,(0,0,0))
        herododge_rect = herododge_surf.get_rect()
        herododge_rect.x = 5 + fighting_width/2
        herododge_rect.y = 165
        herocrit_surf = basic_FONT.render('暴击率 ：' + str(yh_attribute[5]), 1, (0, 0, 0))
        herocrit_rect = herocrit_surf.get_rect()
        herocrit_rect.x = 5 + fighting_width / 2
        herocrit_rect.y = 190
        herodizziness_surf = basic_FONT.render('击晕率 ：' + str(yh_attribute[7]), 1, (0, 0, 0))
        herodizziness_rect = herodizziness_surf.get_rect()
        herodizziness_rect.x = 5 + fighting_width / 2
        herodizziness_rect.y = 215


        # 战斗特效
        attack_image = tiles_image['attack']
        attack_rect = attack_image.get_rect()
        dodge_surf = basic_FONT.render('躲闪！', 1, (250, 200, 55))
        dodge_rect = dodge_surf.get_rect()
        crit_surf = basic_FONT.render('暴击！', 1, (255, 0, 0))
        crit_rect = dodge_surf.get_rect()
        dizziness_surf = basic_FONT.render('击晕！', 1, (50, 100, 255))
        dizziness_rect = dizziness_surf.get_rect()
        dizziness_surf2 = basic_FONT.render('~眩晕~', 1, (50, 100, 255))
        dizziness_rect2 = dizziness_surf2.get_rect()
        zhongjia_surf = basic_FONT.render('反弹伤害', 1, (200, 200, 100))
        zhongjia_rect = zhongjia_surf.get_rect()
        kuangzhan_surf = basic_FONT.render('致命一击',1,(200,0,0))
        kuangzhan_rect = kuangzhan_surf.get_rect()


        # 战斗循环
        i = 0
        while True:
            fighting_surf.fill((200, 100, 200))
            # 人物死亡
            if yh_attribute[1] == 0:
                # 狂战士技能1 回复原本攻击力
                yh_attribute[2] = hero_attack

                pygame.quit()
                sys.exit()
            # 怪物死亡
            if monster_life == 0:
                # 狂战士技能1 回复原本攻击力
                yh_attribute[2] = hero_attack

                fighting_end = True
                map[10][layer][z].remove(map[4][layer])

                # 掉经验
                if attributes['experience'] + monster_attribute[z][7] < attributes['max_experience']:
                    attributes['experience'] += monster_attribute[z][7]
                else:
                    attributes['yh_level'] += 1
                    # 等级上升自动加点（攻击+1，防御+1，生命上限+10)
                    attributes['tizhi'] += 1
                    yh_attribute[6] += 10
                    attributes['liliang'] += 1
                    yh_attribute[2] += 1
                    attributes['naili'] += 1
                    yh_attribute[3] += 1

                    upgrade = True
                    yh_attribute[1] = yh_attribute[6]
                    attributes['common_attribute'] += 2
                    if (attributes['yh_level'] + 1) % 5 == 0:
                        attributes['special_attribute'] += 2
                        attributes['skill_attribute'] += 1
                    attributes['experience'] = attributes['experience'] + monster_attribute[z][7] - attributes['max_experience']
                    # 每级经验上限增加5
                    attributes['max_experience'] += 5
                # 掉金币
                attributes['money'] += monster_attribute[z][8]
                # 掉装备
                for i in range(len(monster_attribute[z][9])):
                    if random.randint(1,100) <= monster_attribute[z][10][i]:
                        # 背包已满无法获得装备
                        if len(equipment) < 16:
                            equipment.append(monster_attribute[z][9][i])
                            fall_equipment.append(monster_attribute[z][9][i])
                        else:
                            full_equipment = True
                break

            # 怪物先手攻击
            if (i%2) == 1:
                # 绘制战斗图标
                attack_rect.centerx = 190
                attack_rect.centery = 40
                fighting_surf.blit(attack_image,attack_rect)

                # 控制流魔法师技能2--对怪物造成的伤害
                if poison:
                    if monster_life - poison >= 0:
                        monster_life -= poison
                    else:
                        monster_life = 0


                # 判断是否被击晕
                if monster_dizzinessed:
                    dizziness_rect2.x = 10 + 110
                    dizziness_rect2.y = 215
                    fighting_surf.blit(dizziness_surf2, dizziness_rect2)
                    monster_dizzinessed -= 1
                else:
                    # 闪避率
                    if random.randint(1,100) > yh_attribute[4]:
                        # 重甲骑士技能2--敌方攻击时有几率反弹敌方攻击力一半的伤害
                        if zhongjia_skill['7']:
                            if random.randint(1, 100) <= 20:
                                if (monster_life - int(monster_attack/2)) >= 0:
                                    monster_life -= int(monster_attack/2)
                                else:
                                    monster_life = 0
                                zhongjia_rect.x = 10 + fighting_width / 2
                                zhongjia_rect.y = 265
                                fighting_surf.blit(zhongjia_surf,zhongjia_rect)

                        # 击晕率
                        if random.randint(1,100) <= monster_dizziness:
                            yh_dizzinessed += 1
                            dizziness_rect.x = 10 + 110
                            dizziness_rect.y = 215
                            fighting_surf.blit(dizziness_surf, dizziness_rect)

                        # 暴击率
                        if random.randint(1,100) > monster_crit:
                            # 应对防御大于攻击时的保底伤害
                            if yh_attribute[3] < monster_attack:
                                # 重甲骑士技能1--减免所受伤害的30%
                                if zhongjia_skill['4']:
                                    yh_attribute[1] -= int((monster_attack - yh_attribute[3])*0.7)
                                else:
                                    yh_attribute[1] -= (monster_attack - yh_attribute[3])
                            else:
                                yh_attribute[1] -= 1
                        else:
                            if yh_attribute[3] < monster_attack*2:
                                # 重甲骑士技能1--减免所受伤害的30%
                                if zhongjia_skill['4']:
                                    yh_attribute[1] -= int((monster_attack*2 - yh_attribute[3])*0.7)
                                else:
                                    yh_attribute[1] -= (monster_attack*2 - yh_attribute[3])
                            else:
                                yh_attribute[1] -= 1
                            crit_rect.x = 10 + 110
                            crit_rect.y = 190
                            fighting_surf.blit(crit_surf,crit_rect)
                        if yh_attribute[1] < 0:
                            yh_attribute[1] = 0
                    else:
                        dodge_rect.x = 10 + fighting_width / 2 + 110
                        dodge_rect.y = 165
                        fighting_surf.blit(dodge_surf,dodge_rect)
            # 人物后手攻击
            if (i%2) == 0 and i != 0:
                # 绘制战斗图标
                attack_rect.centerx = 190 + fighting_width/2
                attack_rect.centery = 40
                fighting_surf.blit(attack_image, attack_rect)

                # 控制流魔法师技能2--攻击时使敌方附带（等级/3）点中毒状态
                if kongzhi_skill['7']:
                    poison += (int(attributes['yh_level']/3))

                # 判断是否被击晕
                if yh_dizzinessed:
                    dizziness_rect2.x = 10 + fighting_width / 2 + 110
                    dizziness_rect2.y = 215
                    fighting_surf.blit(dizziness_surf2, dizziness_rect2)
                    yh_dizzinessed -= 1
                else:
                    # 闪避率
                    if random.randint(1,100) > monster_dodge:
                        # 击晕率
                        if random.randint(1, 100) <= yh_attribute[7]:
                            # 控制魔法师的技能1--击晕敌方增至两回合
                            if kongzhi_skill['4']:
                                monster_dizzinessed += 2
                            else:
                                monster_dizzinessed += 1
                            dizziness_rect.x = 10 + fighting_width / 2 + 110
                            dizziness_rect.y = 215
                            fighting_surf.blit(dizziness_surf, dizziness_rect)

                        # 暴击率
                        if random.randint(1,100) > yh_attribute[5]:
                            # 狂战士技能2--第三次攻击造成1.5倍伤害
                            if kuangzhan_skill['7'] and i%6 == 0:
                                # 绘制狂战技能特效
                                kuangzhan_rect.x = 120 + fighting_width / 2
                                kuangzhan_rect.y = 265
                                fighting_surf.blit(kuangzhan_surf,kuangzhan_rect)
                                if monster_defend < int(yh_attribute[2]*1.5):
                                    monster_life -= (int(yh_attribute[2]*1.5) - monster_defend)
                                else:
                                    monster_life -= 1
                            else:
                            # 应对防御大于攻击时的保底伤害
                                if monster_defend < yh_attribute[2]:
                                    monster_life -= (yh_attribute[2] - monster_defend)
                                else:
                                    monster_life -= 1
                        else:
                            if kuangzhan_skill['7'] and i%6 == 0:
                                # 绘制狂战技能特效
                                kuangzhan_rect.x = 120 + fighting_width / 2
                                kuangzhan_rect.y = 265
                                fighting_surf.blit(kuangzhan_surf, kuangzhan_rect)
                                if monster_defend < int(yh_attribute[2] * 2 * 1.5):
                                    monster_life -= (int(yh_attribute[2] * 2 * 1.5) - monster_defend)
                                else:
                                    monster_life -= 1
                            else:
                                if monster_defend < yh_attribute[2]*2:
                                    monster_life -= (yh_attribute[2]*2 - monster_defend)
                                else:
                                    monster_life -= 1
                            crit_rect.x = 10 + fighting_width / 2 + 110
                            crit_rect.y = 190
                            fighting_surf.blit(crit_surf,crit_rect)
                        if monster_life < 0:
                            monster_life = 0
                    else:
                        dodge_rect.x = 10 + 110
                        dodge_rect.y = 165
                        fighting_surf.blit(dodge_surf, dodge_rect)

            # 控制流魔法师技能2的绘制特效
            if poison:
                kongzhi_surf = basic_FONT.render('中毒--' + str(poison), 1, (0, 0, 150))
                kongzhi_rect = kongzhi_surf.get_rect()
                kongzhi_rect.x = 10
                kongzhi_rect.y = 265
                fighting_surf.blit(kongzhi_surf, kongzhi_rect)

            i = i + 1
            # 绘制
            pygame.draw.rect(fighting_surf, (0, 0, 0), (0, 0, fighting_width, fighting_height), 5)
            pygame.draw.line(fighting_surf, (0, 0, 0), (fighting_width / 2, 0), (fighting_width / 2, fighting_height),2)
            pygame.draw.line(fighting_surf, (0, 0, 0), (0, 80), (fighting_width, 80), 2)
            fighting_surf.blit(tiles_image[z], monster_rect)
            fighting_surf.blit(monstername_surf, monstername_rect)
            monsterlife_surf = basic_FONT.render('生命 ：' + str(monster_life), 1, (0, 0, 0))
            monsterlife_rect = monsterlife_surf.get_rect()
            monsterlife_rect.x = 5
            monsterlife_rect.y = 90
            fighting_surf.blit(monsterlife_surf, monsterlife_rect)
            fighting_surf.blit(monsterattack_surf, monsterattack_rect)
            fighting_surf.blit(monsterdefend_surf, monsterdefend_rect)
            if monster_dodge > 0:
                fighting_surf.blit(monsterdodge_surf, monsterdodge_rect)
            if monster_crit > 0:
                fighting_surf.blit(monstercrit_surf, monstercrit_rect)
            if monster_dizziness > 0:
                fighting_surf.blit(monsterdizziness_surf, monsterdizziness_rect)

            fighting_surf.blit(tiles_image['z2'], hero_rect)
            fighting_surf.blit(heroname_surf, heroname_rect)
            herolife_surf = basic_FONT.render('生命/上限 ：' + str(yh_attribute[1]) + '/' + str(yh_attribute[6]), 1, (0, 0, 0))
            herolife_rect = herolife_surf.get_rect()
            herolife_rect.x = 5 + fighting_width / 2
            herolife_rect.y = 90
            fighting_surf.blit(herolife_surf, herolife_rect)
            # 攻击力绘制
            if kuangzhan_skill['4']:
                if yh_attribute[1] > int(yh_attribute[6] * 0.7):
                    heroattack_surf = basic_FONT.render('攻击 ：' + str(yh_attribute[2]), 1, (0, 0, 0))
                elif yh_attribute[1] <= int(yh_attribute[6] * 0.3):
                    yh_attribute[2] = int(hero_attack * 1.6)
                    heroattack_surf = basic_FONT.render('攻击 ：' + str(yh_attribute[2]), 1, (200, 0, 0))
                elif yh_attribute[1] <= int(yh_attribute[6] * 0.5):
                    yh_attribute[2] = int(hero_attack * 1.4)
                    heroattack_surf = basic_FONT.render('攻击 ：' + str(yh_attribute[2]), 1, (150, 0, 0))
                elif yh_attribute[1] <= int(yh_attribute[6] * 0.7):
                    yh_attribute[2] = int(hero_attack * 1.2)
                    heroattack_surf = basic_FONT.render('攻击 ：' + str(yh_attribute[2]), 1, (100, 0, 0))
            else:
                heroattack_surf = basic_FONT.render('攻击 ：' + str(yh_attribute[2]), 1, (0, 0, 0))
            heroattack_rect = heroattack_surf.get_rect()
            heroattack_rect.x = 5 + fighting_width / 2
            heroattack_rect.y = 115
            fighting_surf.blit(heroattack_surf, heroattack_rect)

            fighting_surf.blit(herodefend_surf, herodefend_rect)
            if yh_attribute[4] > 0:
                fighting_surf.blit(herododge_surf, herododge_rect)
            if yh_attribute[5] > 0:
                fighting_surf.blit(herocrit_surf, herocrit_rect)
            if yh_attribute[7] > 0:
                fighting_surf.blit(herodizziness_surf, herodizziness_rect)

            screen.blit(fighting_surf, fighting_rect)
            pygame.display.update()
            pygame.time.wait(900)
        pygame.event.clear()
        if fighting_end:
            # 经验与金币
            tishi_surf = basic_FONT.render('经验+' + str(monster_attribute[z][7]) + ' 金币+' + str(monster_attribute[z][8]),1,(200,150,50))
            tishi_rect = tishi_surf.get_rect()
            tishi_rect.centerx = screen_width/2
            tishi_rect.bottom = screen_height
            screen.blit(tishi_surf,tishi_rect)
            # 升级
            if upgrade:
                tishi_surf2 = basic_FONT.render('恭喜升级', 1, (200, 150, 200))
                tishi_rect2 = tishi_surf2.get_rect()
                tishi_rect2.centerx = screen_width / 2
                tishi_rect2.bottom = screen_height - 30
                screen.blit(tishi_surf2, tishi_rect2)
            # 掉装备
            if fall_equipment:
                for i in range(len(fall_equipment)):
                    equipment_name = equipment_name + equipment_imformation2[fall_equipment[i]] + ' '
                tishi_surf3 = basic_FONT.render('获得' + equipment_name, 1, (255, 100, 50))
                tishi_rect3 = tishi_surf3.get_rect()
                tishi_rect3.centerx = screen_width / 2
                tishi_rect3.bottom = screen_height - 60
                screen.blit(tishi_surf3, tishi_rect3)
            # 背包已满无法获得装备
            if full_equipment:
                tishi_surf4 = basic_FONT.render('背包已满无法获得道具', 1, (255, 100, 50))
                tishi_rect4 = tishi_surf4.get_rect()
                tishi_rect4.centerx = screen_width / 2
                tishi_rect4.bottom = screen_height - 90
                screen.blit(tishi_surf4, tishi_rect4)

            pygame.display.update()
            pygame.time.wait(1800)
            pygame.event.clear()



def decorate_rect(equipment_surf,mouse_position):
    j1 = int(mouse_position / 4)
    j2 = mouse_position % 4
    rect = pygame.Rect((0, 0, 70, 70))
    rect.centerx = 300 + 100 * j2 + 50
    rect.centery = 0 + 100 * j1 + 50
    pygame.draw.rect(equipment_surf,(0,0,255),rect,4)

def draw_attribute(tiles_image,yh_attribute,screen_width,screen_height,screen,FPSclock,FPS,basic_FONT,big_FONT,attributes,mousex,mousey):
    while True:
        # 一些常量
        close = False
        distance = 30
        mouse_click = False

        # 装备栏和道具栏的初始界面
        attribute_width = 700
        attribute_height = 500
        attribute_surf = pygame.Surface((attribute_width, attribute_height))
        attribute_rect = attribute_surf.get_rect()
        attribute_rect.centerx = screen_width / 2
        attribute_rect.centery = screen_height / 2
        attribute_surf.fill((100, 100, 100))
        pygame.draw.lines(attribute_surf, (0, 0, 0), True,[(0, 0), (0, attribute_height), (attribute_width, attribute_height),(attribute_width, 0)], 16)
        pygame.draw.line(attribute_surf, (0, 0, 0),(0, 70), (73, 70),8)
        pygame.draw.line(attribute_surf, (0, 0, 0), (69, 70), (69, 0), 8)
        pygame.draw.line(attribute_surf, (0, 0, 0), (170, 0), (170, attribute_height), 3)
        pygame.draw.line(attribute_surf, (100, 100, 50), (180, 8), (180, attribute_height - 8), 16)
        pygame.draw.line(attribute_surf, (0, 0, 0), (190, 0), (190, attribute_height), 3)
        pygame.draw.line(attribute_surf, (0, 0, 0), (0, 405), (170, 405), 3)
        pygame.draw.line(attribute_surf, (0, 0, 0), (190, 405), (attribute_width, 405), 3)
        yh_image = tiles_image['z2']
        yh_rect = yh_image.get_rect()
        yh_rect.x = 20
        yh_rect.y = 15
        attribute_surf.blit(yh_image,yh_rect)
        # 银魂
        yhfont_surf = basic_FONT.render('银魂', 1, (0, 0, 0))
        yhfont_rect = yhfont_surf.get_rect()
        yhfont_rect.x = 20
        yhfont_rect.y = 80
        attribute_surf.blit(yhfont_surf, yhfont_rect)
        # 等级
        level_surf = basic_FONT.render('等级：' + str(attributes['yh_level']), 1, (0, 0, 0))
        level_rect = level_surf.get_rect()
        level_rect.x = 20
        level_rect.y = 120
        attribute_surf.blit(level_surf, level_rect)
        # 经验和经验上限
        experience_surf = basic_FONT.render('经验：' + str(attributes['experience']) + '/' + str(attributes['max_experience']), 1, (0, 0, 0))
        experience_rect = experience_surf.get_rect()
        experience_rect.x = 20
        experience_rect.y = 120 + distance
        attribute_surf.blit(experience_surf, experience_rect)
        # 生命上限
        life_surf = basic_FONT.render('生命上限：' + str(yh_attribute[6]), 1, (0, 0, 0))
        life_rect = life_surf.get_rect()
        life_rect.x = 20
        life_rect.y = 120 + distance*2
        attribute_surf.blit(life_surf, life_rect)
        # 攻击
        attack_surf = basic_FONT.render('攻击：' + str(yh_attribute[2]), 1, (0, 0, 0))
        attack_rect = attack_surf.get_rect()
        attack_rect.x = 20
        attack_rect.y = 120 + distance*3
        attribute_surf.blit(attack_surf, attack_rect)
        # 防御
        defend_surf = basic_FONT.render('防御：' + str(yh_attribute[3]), 1, (0, 0, 0))
        defend_rect = defend_surf.get_rect()
        defend_rect.x = 20
        defend_rect.y = 120 + distance*4
        attribute_surf.blit(defend_surf, defend_rect)
        # 躲闪
        dodge_surf = basic_FONT.render('躲闪率：' + str(yh_attribute[4]), 1, (0, 0, 0))
        dodge_rect = dodge_surf.get_rect()
        dodge_rect.x = 20
        dodge_rect.y = 120 + distance*5
        attribute_surf.blit(dodge_surf, dodge_rect)
        # 暴击
        crit_surf = basic_FONT.render('暴击率：' + str(yh_attribute[5]), 1, (0, 0, 0))
        crit_rect = crit_surf.get_rect()
        crit_rect.x = 20
        crit_rect.y = 120 + distance*6
        attribute_surf.blit(crit_surf, crit_rect)
        # 击晕率
        dizziness_surf = basic_FONT.render('击晕率：' + str(yh_attribute[7]), 1, (0, 0, 0))
        dizziness_rect = dizziness_surf.get_rect()
        dizziness_rect.x = 20
        dizziness_rect.y = 120 + distance*7
        attribute_surf.blit(dizziness_surf,dizziness_rect)

        # 潜能值
        # 体质
        tizhi_surf = big_FONT.render(' +  ' + '体质：' + str(attributes['tizhi']), 1, (0, 0, 0))
        tizhi_rect = tizhi_surf.get_rect()
        tizhi_rect.x = 200
        tizhi_rect.y = 30
        attribute_surf.blit(tizhi_surf, tizhi_rect)
        # 力量
        liliang_surf = big_FONT.render(' +  ' + '力量：' + str(attributes['liliang']), 1, (0, 0, 0))
        liliang_rect = liliang_surf.get_rect()
        liliang_rect.x = 200
        liliang_rect.y = 30 + distance*2
        attribute_surf.blit(liliang_surf, liliang_rect)
        # 耐力
        naili_surf = big_FONT.render(' +  ' + '耐力：' + str(attributes['naili']), 1, (0, 0, 0))
        naili_rect = naili_surf.get_rect()
        naili_rect.x = 200
        naili_rect.y = 30 + distance*4
        attribute_surf.blit(naili_surf, naili_rect)
        # 敏捷
        minjie_surf = big_FONT.render(' +  ' + '敏捷：' + str(attributes['minjie']), 1, (0, 0, 0))
        minjie_rect = minjie_surf.get_rect()
        minjie_rect.x = 200
        minjie_rect.y = 30 + distance*6
        attribute_surf.blit(minjie_surf, minjie_rect)
        # 会心
        huixin_surf = big_FONT.render(' +  ' + '会心：' + str(attributes['huixin']), 1, (0, 0, 0))
        huixin_rect = huixin_surf.get_rect()
        huixin_rect.x = 200
        huixin_rect.y = 30 + distance*8
        attribute_surf.blit(huixin_surf, huixin_rect)
        # 重击
        zhongji_surf = big_FONT.render(' +  ' + '重击：' + str(attributes['zhongji']), 1, (0, 0, 0))
        zhongji_rect = zhongji_surf.get_rect()
        zhongji_rect.x = 200
        zhongji_rect.y = 30 + distance*10
        attribute_surf.blit(zhongji_surf, zhongji_rect)
        # 普通潜能值
        commonattribute_surf = basic_FONT.render('普通潜能值：' + str(attributes['common_attribute']), 1, (0, 0, 0))
        commonattribute_rect = commonattribute_surf.get_rect()
        commonattribute_rect.x = 20
        commonattribute_rect.y = 30 + distance*13
        attribute_surf.blit(commonattribute_surf, commonattribute_rect)
        # 特殊潜能值
        specialattribute_surf = basic_FONT.render('特殊潜能值：' + str(attributes['special_attribute']), 1, (0, 0, 0))
        specialattribute_rect = specialattribute_surf.get_rect()
        specialattribute_rect.x = 20
        specialattribute_rect.y = 30 + distance*14
        attribute_surf.blit(specialattribute_surf, specialattribute_rect)

        # 提示信息
        tstizhi_surf = basic_FONT.render('生命上限+10（消耗普通潜能值）', 1, (200, 150, 50))
        tsliliang_surf = basic_FONT.render('攻击+1（消耗普通潜能值）', 1, (200, 150, 50))
        tsnaili_surf = basic_FONT.render('防御+1（消耗普通潜能值）', 1, (200, 150, 50))
        tsminjie_surf = basic_FONT.render('躲闪率+1（消耗特殊潜能值）', 1, (200, 150, 50))
        tshuixin_surf = basic_FONT.render('暴击率+1（消耗特殊潜能值）', 1, (200, 150, 50))
        tszhongji_surf = basic_FONT.render('击晕率+1（消耗特殊潜能值）', 1, (200, 150, 50))
        tsrect = pygame.Rect((210,440,10,10))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # 再按o关闭
                if event.key == pygame.K_o:
                    close = True
            if event.type == pygame.MOUSEMOTION:
                mousex,mousey = event.pos
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_click = True

        if close == True:
            break
        # 绘制高亮框，显示加点详细解释
        if mousex >= 313 and mousex <= 331 and mousey >= 136 and mousey <= 154:
            pygame.draw.rect(attribute_surf, (0, 0, 255), (213, 36, 18, 18), 1)
            attribute_surf.blit(tstizhi_surf,tsrect)
            if attributes['common_attribute'] != 0:
                if mouse_click:
                    attributes['tizhi'] += 1
                    yh_attribute[6] += 10
                    yh_attribute[1] += 10
                    attributes['common_attribute'] -= 1

        elif mousex >= 313 and mousex <= 331 and mousey >= 136 + 60 and mousey <= 154 + 60:
            pygame.draw.rect(attribute_surf, (0, 0, 255), (213, 36 + 60, 18, 18), 1)
            attribute_surf.blit(tsliliang_surf,tsrect)
            if attributes['common_attribute'] != 0:
                if mouse_click:
                    attributes['liliang'] += 1
                    yh_attribute[2] += 1
                    attributes['common_attribute'] -= 1

        elif mousex >= 313 and mousex <= 331 and mousey >= 136 + 120 and mousey <= 154 + 120:
            pygame.draw.rect(attribute_surf, (0, 0, 255), (213, 36 + 120, 18, 18), 1)
            attribute_surf.blit(tsnaili_surf, tsrect)
            if attributes['common_attribute'] != 0:
                if mouse_click:
                    attributes['naili'] += 1
                    yh_attribute[3] += 1
                    attributes['common_attribute'] -= 1

        elif mousex >= 313 and mousex <= 331 and mousey >= 136 + 180 and mousey <= 154 + 180:
            pygame.draw.rect(attribute_surf, (0, 0, 255), (213, 36 + 180, 18, 18), 1)
            attribute_surf.blit(tsminjie_surf, tsrect)
            if attributes['special_attribute'] != 0:
                if mouse_click:
                    attributes['minjie'] += 1
                    yh_attribute[4] += 1
                    attributes['special_attribute'] -= 1

        elif mousex >= 313 and mousex <= 331 and mousey >= 136 + 240 and mousey <= 154 + 240:
            pygame.draw.rect(attribute_surf, (0, 0, 255), (213, 36 + 240, 18, 18), 1)
            attribute_surf.blit(tshuixin_surf, tsrect)
            if attributes['special_attribute'] != 0:
                if mouse_click:
                    attributes['huixin'] += 1
                    yh_attribute[5] += 1
                    attributes['special_attribute'] -= 1

        elif mousex >= 313 and mousex <= 331 and mousey >= 136 + 300 and mousey <= 154 + 300:
            pygame.draw.rect(attribute_surf, (0, 0, 255), (213, 36 + 300, 18, 18), 1)
            attribute_surf.blit(tszhongji_surf, tsrect)
            if attributes['special_attribute'] != 0:
                if mouse_click:
                    attributes['zhongji'] += 1
                    yh_attribute[7] += 1
                    attributes['special_attribute'] -= 1

        screen.blit(attribute_surf,attribute_rect)
        pygame.display.update()
        FPSclock.tick(FPS)

# 绘制技能表
def draw_skill(screen_width,screen_height,screen,FPS,FPSclock,basic_FONT,big_FONT,mousex,mousey,attributes,zhongjia_skill,kongzhi_skill,kuangzhan_skill,yh_attribute):

    while True:
        # 一些常量
        close = False
        distance = 50
        mouse_click = False
        zhongjia_click = False
        kongzhi_click = False
        kuangzhan_click = False

        # 各种职业介绍面板
        skill_width = 700
        skill_height = 500
        skill_surf = pygame.Surface((skill_width,skill_height))
        skill_rect = skill_surf.get_rect()
        skill_rect.centerx = screen_width / 2
        skill_rect.centery = screen_height / 2
        skill_surf.fill((100,100,100))
        pygame.draw.lines(skill_surf, (0, 0, 0), True,[(0, 0), (0, skill_height), (skill_width, skill_height), (skill_width, 0)],16)
        pygame.draw.line(skill_surf,(0,0,0),(0,440),(skill_width,440),8)
        pygame.draw.line(skill_surf, (100, 0, 0), (113, 8), (113, 436), 210)
        pygame.draw.line(skill_surf, (0, 0, 0), (222, 0), (222, 436), 8)
        pygame.draw.line(skill_surf, (100, 0, 0), (587, 8), (587, 436), 210)
        pygame.draw.line(skill_surf, (0, 0, 0), (478, 0), (478, 436), 8)

        zhongjia_surf = big_FONT.render('重甲战士',1,(0,0,0))
        zhongjia_rect = zhongjia_surf.get_rect()
        zhongjia_rect.centerx = skill_width/2
        zhongjia_rect.centery = 50
        skill_surf.blit(zhongjia_surf,zhongjia_rect)

        kongzhi_surf = big_FONT.render('控制流魔法师', 1, (0, 0, 0))
        kongzhi_rect = kongzhi_surf.get_rect()
        kongzhi_rect.centerx = skill_width / 2
        kongzhi_rect.centery = 50 + distance
        skill_surf.blit(kongzhi_surf, kongzhi_rect)

        kuangzhan_surf = big_FONT.render('狂战士', 1, (0, 0, 0))
        kuangzhan_rect = kuangzhan_surf.get_rect()
        kuangzhan_rect.centerx = skill_width / 2
        kuangzhan_rect.centery = 50 + distance*2
        skill_surf.blit(kuangzhan_surf, kuangzhan_rect)




        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # 再按i关闭
                if event.key == pygame.K_i:
                    close = True
            if event.type == pygame.MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_click = True

        if close:
            break

        # 鼠标落在字体上
        if mousex >=388 and mousex <= 511 and mousey >= 135 and mousey <= 164:
            pygame.draw.rect(skill_surf,(200,150,50),(268,42,16,16))
            pygame.draw.rect(skill_surf, (200, 150, 50), (416, 42, 16, 16))
            # 提示信息
            tszhongjia_surf = basic_FONT.render('防御、生命上限较高，反弹伤害', 1, (0, 0, 0))
            tszhongjia_rect = tszhongjia_surf.get_rect()
            tszhongjia_rect.centerx = skill_width / 2
            tszhongjia_rect.centery = 470
            skill_surf.blit(tszhongjia_surf, tszhongjia_rect)
            if mouse_click:
                zhongjia_click = True

        if mousex >=359 and mousex <= 541 and mousey >= 186 and mousey <= 216:
            pygame.draw.rect(skill_surf,(200,150,50),(238,93,16,16))
            pygame.draw.rect(skill_surf, (200, 150, 50), (446, 93, 16, 16))
            # 提示信息
            tskongzhi_surf = basic_FONT.render('擅长控制和持续输出', 1, (0, 0, 0))
            tskongzhi_rect = tskongzhi_surf.get_rect()
            tskongzhi_rect.centerx = skill_width / 2
            tskongzhi_rect.centery = 470
            skill_surf.blit(tskongzhi_surf, tskongzhi_rect)
            if mouse_click:
                kongzhi_click = True
        if mousex >=405 and mousex <= 494 and mousey >= 235 and mousey <= 264:
            pygame.draw.rect(skill_surf,(200,150,50),(283,142,16,16))
            pygame.draw.rect(skill_surf, (200, 150, 50), (400, 142, 16, 16))
            # 提示信息
            tskuangzhan_surf = basic_FONT.render('伤害较高，爆发力强，速战速决', 1, (0, 0, 0))
            tskuangzhan_rect = tskuangzhan_surf.get_rect()
            tskuangzhan_rect.centerx = skill_width / 2
            tskuangzhan_rect.centery = 470
            skill_surf.blit(tskuangzhan_surf, tskuangzhan_rect)
            if mouse_click:
                kuangzhan_click = True

        # 进入重甲技能树
        if zhongjia_click:
            while True:
                # 一些常量
                close = False
                mouse_click = False


                # 各种职业介绍面板
                skill_width = 700
                skill_height = 500
                skill_surf = pygame.Surface((skill_width, skill_height))
                skill_rect = skill_surf.get_rect()
                skill_rect.centerx = screen_width / 2
                skill_rect.centery = screen_height / 2
                skill_surf.fill((100, 100, 100))
                pygame.draw.lines(skill_surf, (0, 0, 0), True,[(0, 0), (0, skill_height), (skill_width, skill_height), (skill_width, 0)], 16)
                pygame.draw.line(skill_surf, (0, 0, 0), (0, 440), (skill_width, 440), 8)

                zhongjia_surf = big_FONT.render('重甲战士', 1, (0, 0, 0))
                zhongjia_rect = zhongjia_surf.get_rect()
                zhongjia_rect.centerx = skill_width / 2
                zhongjia_rect.centery = 50
                skill_surf.blit(zhongjia_surf, zhongjia_rect)

                pygame.draw.line(skill_surf, (0, 0, 0), (skill_width / 2 - 150, 250), (skill_width / 2 + 150, 250), 2)
                pygame.draw.line(skill_surf, (0, 0, 0), (skill_width / 2, 100), (skill_width / 2, 400), 2)
                if zhongjia_skill['1']:
                    pygame.draw.circle(skill_surf, (200, 150, 50), (skill_width // 2, 100), 10)
                else:
                    pygame.draw.circle(skill_surf,(0,0,0),(skill_width//2,100),10)
                if zhongjia_skill['2']:
                    pygame.draw.circle(skill_surf, (200, 150, 50), (skill_width // 2, 150), 10)
                else:
                    pygame.draw.circle(skill_surf, (0, 0, 0), (skill_width // 2, 150), 10)
                if zhongjia_skill['3']:
                    pygame.draw.circle(skill_surf, (200, 150, 50), (skill_width // 2, 200), 10)
                else:
                    pygame.draw.circle(skill_surf, (0, 0, 0), (skill_width // 2, 200), 10)
                if zhongjia_skill['4']:
                    pygame.draw.circle(skill_surf, (200, 150, 50), (skill_width // 2, 250), 10)
                else:
                    pygame.draw.circle(skill_surf, (0, 0, 0), (skill_width // 2, 250), 10)
                if zhongjia_skill['5']:
                    pygame.draw.circle(skill_surf, (200, 150, 50), (skill_width // 2, 300), 10)
                else:
                    pygame.draw.circle(skill_surf, (0, 0, 0), (skill_width // 2, 300), 10)
                if zhongjia_skill['6']:
                    pygame.draw.circle(skill_surf, (200, 150, 50), (skill_width // 2, 350), 10)
                else:
                    pygame.draw.circle(skill_surf, (0, 0, 0), (skill_width // 2, 350), 10)
                if zhongjia_skill['7']:
                    pygame.draw.circle(skill_surf, (200, 150, 50), (skill_width // 2, 400), 10)
                else:
                    pygame.draw.circle(skill_surf, (0, 0, 0), (skill_width // 2, 400), 10)
                if zhongjia_skill['left1']:
                    pygame.draw.circle(skill_surf, (200, 150, 50), (skill_width // 2 - 50, 250), 10)
                else:
                    pygame.draw.circle(skill_surf, (0, 0, 0), (skill_width // 2 - 50, 250), 10)
                if zhongjia_skill['left2']:
                    pygame.draw.circle(skill_surf, (200, 150, 50), (skill_width // 2 - 100, 250), 10)
                else:
                    pygame.draw.circle(skill_surf, (0, 0, 0), (skill_width // 2 - 100, 250), 10)
                if zhongjia_skill['left3']:
                    pygame.draw.circle(skill_surf, (200, 150, 50), (skill_width // 2 - 150, 250), 10)
                else:
                    pygame.draw.circle(skill_surf, (0, 0, 0), (skill_width // 2 - 150, 250), 10)
                if zhongjia_skill['right1']:
                    pygame.draw.circle(skill_surf, (200, 150, 50), (skill_width // 2 + 50, 250), 10)
                else:
                    pygame.draw.circle(skill_surf, (0, 0, 0), (skill_width // 2 + 50, 250), 10)
                if zhongjia_skill['right2']:
                    pygame.draw.circle(skill_surf, (200, 150, 50), (skill_width // 2 + 100, 250), 10)
                else:
                    pygame.draw.circle(skill_surf, (0, 0, 0), (skill_width // 2 + 100, 250), 10)
                if zhongjia_skill['right3']:
                    pygame.draw.circle(skill_surf, (200, 150, 50), (skill_width // 2 + 150, 250), 10)
                else:
                    pygame.draw.circle(skill_surf, (0, 0, 0), (skill_width // 2 + 150, 250), 10)



                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        # 再按i关闭
                        if event.key == pygame.K_i:
                            close = True
                    if event.type == pygame.MOUSEMOTION:
                        mousex, mousey = event.pos
                    elif event.type == pygame.MOUSEBUTTONUP:
                        mouse_click = True

                if close:
                    break

                if math.sqrt(pow((mousex - 100 - skill_width/2),2) + pow((mousey - 100 - 100),2)) <= 10:
                    pygame.draw.circle(skill_surf,(200,150,50),(skill_width//2,100),13,3)
                    # 提示信息
                    ts_surf1 = basic_FONT.render(('防御 + 5'),1,(200,150,50))
                    ts_rect1 = ts_surf1.get_rect()
                    ts_rect1.centerx = skill_width/2
                    ts_rect1.centery = 470
                    skill_surf.blit(ts_surf1,ts_rect1)
                    if mouse_click and zhongjia_skill['1'] == False:
                        if attributes['skill_attribute']:
                            yh_attribute[3] += 5
                            attributes['skill_attribute'] -= 1
                            zhongjia_skill['1'] = True


                if math.sqrt(pow((mousex - 100 - skill_width/2),2) + pow((mousey - 100 - 150),2)) <= 10:
                    pygame.draw.circle(skill_surf,(200,150,50),(skill_width//2,150),13,3)
                    # 提示信息
                    ts_surf1 = basic_FONT.render(('生命上限 + 50'), 1, (200, 150, 50))
                    ts_rect1 = ts_surf1.get_rect()
                    ts_rect1.centerx = skill_width / 2
                    ts_rect1.centery = 470
                    skill_surf.blit(ts_surf1, ts_rect1)
                    if zhongjia_skill['1'] and mouse_click and zhongjia_skill['2'] == False:
                        if attributes['skill_attribute']:
                            yh_attribute[6] += 50
                            yh_attribute[1] += 50
                            attributes['skill_attribute'] -= 1
                            zhongjia_skill['2'] = True

                if math.sqrt(pow((mousex - 100 - skill_width/2),2) + pow((mousey - 100 - 200),2)) <= 10:
                    pygame.draw.circle(skill_surf,(200,150,50),(skill_width//2,200),13,3)
                    # 提示信息
                    ts_surf1 = basic_FONT.render(('防御 + 5'), 1, (200, 150, 50))
                    ts_rect1 = ts_surf1.get_rect()
                    ts_rect1.centerx = skill_width / 2
                    ts_rect1.centery = 470
                    skill_surf.blit(ts_surf1, ts_rect1)
                    if zhongjia_skill['2'] and mouse_click and zhongjia_skill['3'] == False:
                        if attributes['skill_attribute']:
                            yh_attribute[3] += 5
                            attributes['skill_attribute'] -= 1
                            zhongjia_skill['3'] = True

                if math.sqrt(pow((mousex - 100 - skill_width/2),2) + pow((mousey - 100 - 250),2)) <= 10:
                    pygame.draw.circle(skill_surf,(200,150,50),(skill_width//2,250),13,3)
                    # 提示信息
                    ts_surf1 = basic_FONT.render(('减免所受伤害的30%'), 1, (200, 150, 50))
                    ts_rect1 = ts_surf1.get_rect()
                    ts_rect1.centerx = skill_width / 2
                    ts_rect1.centery = 470
                    skill_surf.blit(ts_surf1, ts_rect1)
                    if zhongjia_skill['3'] and mouse_click and zhongjia_skill['4'] == False:
                        if attributes['skill_attribute']:
                            attributes['skill_attribute'] -= 1
                            zhongjia_skill['4'] = True

                if math.sqrt(pow((mousex - 100 - skill_width/2),2) + pow((mousey - 100 - 300),2)) <= 10:
                    pygame.draw.circle(skill_surf,(200,150,50),(skill_width//2,300),13,3)
                    # 提示信息
                    ts_surf1 = basic_FONT.render(('生命上限 + 70'), 1, (200, 150, 50))
                    ts_rect1 = ts_surf1.get_rect()
                    ts_rect1.centerx = skill_width / 2
                    ts_rect1.centery = 470
                    skill_surf.blit(ts_surf1, ts_rect1)
                    if zhongjia_skill['4'] and mouse_click and zhongjia_skill['5'] == False:
                        if attributes['skill_attribute']:
                            yh_attribute[6] += 70
                            yh_attribute[1] += 70
                            attributes['skill_attribute'] -= 1
                            zhongjia_skill['5'] = True

                if math.sqrt(pow((mousex - 100 - skill_width/2),2) + pow((mousey - 100 - 350),2)) <= 10:
                    pygame.draw.circle(skill_surf,(200,150,50),(skill_width//2,350),13,3)
                    # 提示信息
                    ts_surf1 = basic_FONT.render(('防御 + 7'), 1, (200, 150, 50))
                    ts_rect1 = ts_surf1.get_rect()
                    ts_rect1.centerx = skill_width / 2
                    ts_rect1.centery = 470
                    skill_surf.blit(ts_surf1, ts_rect1)
                    if zhongjia_skill['5'] and mouse_click and zhongjia_skill['6'] == False:
                        if attributes['skill_attribute']:
                            yh_attribute[3] += 7
                            attributes['skill_attribute'] -= 1
                            zhongjia_skill['6'] = True

                if math.sqrt(pow((mousex - 100 - skill_width/2),2) + pow((mousey - 100 - 400),2)) <= 10:
                    pygame.draw.circle(skill_surf,(200,150,50),(skill_width//2,400),13,3)
                    # 提示信息
                    ts_surf1 = basic_FONT.render(('敌方攻击时有30%几率反弹敌方攻击力一半的伤害'), 1, (200, 150, 50))
                    ts_rect1 = ts_surf1.get_rect()
                    ts_rect1.centerx = skill_width / 2
                    ts_rect1.centery = 470
                    skill_surf.blit(ts_surf1, ts_rect1)
                    if zhongjia_skill['6'] and mouse_click and zhongjia_skill['7'] == False:
                        if attributes['skill_attribute']:
                            attributes['skill_attribute'] -= 1
                            zhongjia_skill['7'] = True

                if math.sqrt(pow((mousex - 100 - skill_width/2 - 50),2) + pow((mousey - 100 - 250),2)) <= 10:
                    pygame.draw.circle(skill_surf,(200,150,50),(skill_width//2 + 50,250),13,3)
                    # 提示信息
                    ts_surf1 = basic_FONT.render(('不详'), 1, (200, 150, 50))
                    ts_rect1 = ts_surf1.get_rect()
                    ts_rect1.centerx = skill_width / 2
                    ts_rect1.centery = 470
                    skill_surf.blit(ts_surf1, ts_rect1)
                    if zhongjia_skill['4'] and mouse_click and zhongjia_skill['right1'] == False:
                        if attributes['skill_attribute']:
                            attributes['skill_attribute'] -= 1
                            zhongjia_skill['right1'] = True

                if math.sqrt(pow((mousex - 100 - skill_width/2 - 100),2) + pow((mousey - 100 - 250),2)) <= 10:
                    pygame.draw.circle(skill_surf,(200,150,50),(skill_width//2 + 100,250),13,3)
                    # 提示信息
                    ts_surf1 = basic_FONT.render(('不详'), 1, (200, 150, 50))
                    ts_rect1 = ts_surf1.get_rect()
                    ts_rect1.centerx = skill_width / 2
                    ts_rect1.centery = 470
                    skill_surf.blit(ts_surf1, ts_rect1)
                    if zhongjia_skill['right1'] and mouse_click and zhongjia_skill['right2'] == False:
                        if attributes['skill_attribute']:
                            attributes['skill_attribute'] -= 1
                            zhongjia_skill['right2'] = True

                if math.sqrt(pow((mousex - 100 - skill_width/2 - 150),2) + pow((mousey - 100 - 250),2)) <= 10:
                    pygame.draw.circle(skill_surf,(200,150,50),(skill_width//2 + 150,250),13,3)
                    # 提示信息
                    ts_surf1 = basic_FONT.render(('不详'), 1, (200,150, 50))
                    ts_rect1 = ts_surf1.get_rect()
                    ts_rect1.centerx = skill_width / 2
                    ts_rect1.centery = 470
                    skill_surf.blit(ts_surf1, ts_rect1)
                    if zhongjia_skill['right2'] and mouse_click and zhongjia_skill['right3'] == False:
                        if attributes['skill_attribute']:
                            attributes['skill_attribute'] -= 1
                            zhongjia_skill['right3'] = True

                if math.sqrt(pow((mousex - 100 - skill_width/2 + 50),2) + pow((mousey - 100 - 250),2)) <= 10:
                    pygame.draw.circle(skill_surf,(200,150,50),(skill_width//2 - 50,250),13,3)
                    # 提示信息
                    ts_surf1 = basic_FONT.render(('不详'), 1, (200, 150, 50))
                    ts_rect1 = ts_surf1.get_rect()
                    ts_rect1.centerx = skill_width / 2
                    ts_rect1.centery = 470
                    skill_surf.blit(ts_surf1, ts_rect1)
                    if zhongjia_skill['4'] and mouse_click and zhongjia_skill['left1'] == False:
                        if attributes['skill_attribute']:
                            attributes['skill_attribute'] -= 1
                            zhongjia_skill['left1'] = True

                if math.sqrt(pow((mousex - 100 - skill_width/2 + 100),2) + pow((mousey - 100 - 250),2)) <= 10:
                    pygame.draw.circle(skill_surf,(200,150,50),(skill_width//2 - 100,250),13,3)
                    # 提示信息
                    ts_surf1 = basic_FONT.render(('不详'), 1, (200, 150, 50))
                    ts_rect1 = ts_surf1.get_rect()
                    ts_rect1.centerx = skill_width / 2
                    ts_rect1.centery = 470
                    skill_surf.blit(ts_surf1, ts_rect1)
                    if zhongjia_skill['left1'] and mouse_click and zhongjia_skill['left2'] == False:
                        if attributes['skill_attribute']:
                            attributes['skill_attribute'] -= 1
                            zhongjia_skill['left2'] = True

                if math.sqrt(pow((mousex - 100 - skill_width/2 + 150),2) + pow((mousey - 100 - 250),2)) <= 10:
                    pygame.draw.circle(skill_surf,(200,150,50),(skill_width//2 - 150,250),13,3)
                    # 提示信息
                    ts_surf1 = basic_FONT.render(('不详'), 1, (200, 150, 50))
                    ts_rect1 = ts_surf1.get_rect()
                    ts_rect1.centerx = skill_width / 2
                    ts_rect1.centery = 470
                    skill_surf.blit(ts_surf1, ts_rect1)
                    if zhongjia_skill['left2'] and mouse_click and zhongjia_skill['left3'] == False:
                        if attributes['skill_attribute']:
                            attributes['skill_attribute'] -= 1
                            zhongjia_skill['left3'] = True

                screen.blit(skill_surf, skill_rect)
                pygame.display.update()
                FPSclock.tick(FPS)

        # 进入控制技能树
        if kongzhi_click:
            while True:
                # 一些常量
                close = False
                mouse_click = False
                # 各种职业介绍面板
                skill_width = 700
                skill_height = 500
                skill_surf = pygame.Surface((skill_width, skill_height))
                skill_rect = skill_surf.get_rect()
                skill_rect.centerx = screen_width / 2
                skill_rect.centery = screen_height / 2
                skill_surf.fill((100, 100, 100))
                pygame.draw.lines(skill_surf, (0, 0, 0), True,[(0, 0), (0, skill_height), (skill_width, skill_height), (skill_width, 0)],16)
                pygame.draw.line(skill_surf, (0, 0, 0), (0, 440), (skill_width, 440), 8)

                zhongjia_surf = big_FONT.render('控制流魔法师', 1, (0, 0, 0))
                zhongjia_rect = zhongjia_surf.get_rect()
                zhongjia_rect.centerx = skill_width / 2
                zhongjia_rect.centery = 50
                skill_surf.blit(zhongjia_surf, zhongjia_rect)

                pygame.draw.line(skill_surf, (0, 0, 0), (skill_width / 2 - 150, 250),(skill_width / 2 + 150, 250), 2)
                pygame.draw.line(skill_surf, (0, 0, 0), (skill_width / 2, 100), (skill_width / 2, 400), 2)

                if kongzhi_skill['1']:
                    pygame.draw.circle(skill_surf, (0, 0, 150), (skill_width // 2, 100), 10)
                else:
                    pygame.draw.circle(skill_surf, (0, 0, 0), (skill_width // 2, 100), 10)
                if kongzhi_skill['2']:
                    pygame.draw.circle(skill_surf, (0, 0, 150), (skill_width // 2, 150), 10)
                else:
                    pygame.draw.circle(skill_surf, (0, 0, 0), (skill_width // 2, 150), 10)
                if kongzhi_skill['3']:
                    pygame.draw.circle(skill_surf, (0, 0, 150), (skill_width // 2, 200), 10)
                else:
                    pygame.draw.circle(skill_surf, (0, 0, 0), (skill_width // 2, 200), 10)
                if kongzhi_skill['4']:
                    pygame.draw.circle(skill_surf, (0, 0, 150), (skill_width // 2, 250), 10)
                else:
                    pygame.draw.circle(skill_surf, (0, 0, 0), (skill_width // 2, 250), 10)
                if kongzhi_skill['5']:
                    pygame.draw.circle(skill_surf, (0, 0, 150), (skill_width // 2, 300), 10)
                else:
                    pygame.draw.circle(skill_surf, (0, 0, 0), (skill_width // 2, 300), 10)
                if kongzhi_skill['6']:
                    pygame.draw.circle(skill_surf, (0, 0, 150), (skill_width // 2, 350), 10)
                else:
                    pygame.draw.circle(skill_surf, (0, 0, 0), (skill_width // 2, 350), 10)
                if kongzhi_skill['7']:
                    pygame.draw.circle(skill_surf, (0, 0, 150), (skill_width // 2, 400), 10)
                else:
                    pygame.draw.circle(skill_surf, (0, 0, 0), (skill_width // 2, 400), 10)
                if kongzhi_skill['left1']:
                    pygame.draw.circle(skill_surf, (0, 0, 150), (skill_width // 2 - 50, 250), 10)
                else:
                    pygame.draw.circle(skill_surf, (0, 0, 0), (skill_width // 2 - 50, 250), 10)
                if kongzhi_skill['left2']:
                    pygame.draw.circle(skill_surf, (0, 0, 150), (skill_width // 2 - 100, 250), 10)
                else:
                    pygame.draw.circle(skill_surf, (0, 0, 0), (skill_width // 2 - 100, 250), 10)
                if kongzhi_skill['left3']:
                    pygame.draw.circle(skill_surf, (0, 0, 150), (skill_width // 2 - 150, 250), 10)
                else:
                    pygame.draw.circle(skill_surf, (0, 0, 0), (skill_width // 2 - 150, 250), 10)
                if kongzhi_skill['right1']:
                    pygame.draw.circle(skill_surf, (0, 0, 150), (skill_width // 2 + 50, 250), 10)
                else:
                    pygame.draw.circle(skill_surf, (0, 0, 0), (skill_width // 2 + 50, 250), 10)
                if kongzhi_skill['right2']:
                    pygame.draw.circle(skill_surf, (0, 0, 150), (skill_width // 2 + 100, 250), 10)
                else:
                    pygame.draw.circle(skill_surf, (0, 0, 0), (skill_width // 2 + 100, 250), 10)
                if kongzhi_skill['right3']:
                    pygame.draw.circle(skill_surf, (0, 0, 150), (skill_width // 2 + 150, 250), 10)
                else:
                    pygame.draw.circle(skill_surf, (0, 0, 0), (skill_width // 2 + 150, 250), 10)


                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        # 再按i关闭
                        if event.key == pygame.K_i:
                            close = True
                    if event.type == pygame.MOUSEMOTION:
                        mousex, mousey = event.pos
                    elif event.type == pygame.MOUSEBUTTONUP:
                        mouse_click = True

                if close:
                    break

                if math.sqrt(pow((mousex - 100 - skill_width / 2), 2) + pow((mousey - 100 - 100), 2)) <= 10:
                    pygame.draw.circle(skill_surf, (0, 0, 150), (skill_width // 2, 100), 13, 3)
                    # 提示信息
                    ts_surf1 = basic_FONT.render(('击晕率 + 1'), 1, (0, 0, 150))
                    ts_rect1 = ts_surf1.get_rect()
                    ts_rect1.centerx = skill_width / 2
                    ts_rect1.centery = 470
                    skill_surf.blit(ts_surf1, ts_rect1)
                    if mouse_click and kongzhi_skill['1'] == False:
                        if attributes['skill_attribute']:
                            yh_attribute[7] += 1
                            attributes['skill_attribute'] -= 1
                            kongzhi_skill['1'] = True

                if math.sqrt(pow((mousex - 100 - skill_width / 2), 2) + pow((mousey - 100 - 150), 2)) <= 10:
                    pygame.draw.circle(skill_surf, (0, 0, 150), (skill_width // 2, 150), 13, 3)
                    # 提示信息
                    ts_surf1 = basic_FONT.render(('躲闪率 + 1'), 1, (0, 0, 150))
                    ts_rect1 = ts_surf1.get_rect()
                    ts_rect1.centerx = skill_width / 2
                    ts_rect1.centery = 470
                    skill_surf.blit(ts_surf1, ts_rect1)
                    if kongzhi_skill['1'] and mouse_click and kongzhi_skill['2'] == False:
                        if attributes['skill_attribute']:
                            yh_attribute[4] += 1
                            attributes['skill_attribute'] -= 1
                            kongzhi_skill['2'] = True

                if math.sqrt(pow((mousex - 100 - skill_width / 2), 2) + pow((mousey - 100 - 200), 2)) <= 10:
                    pygame.draw.circle(skill_surf, (0, 0, 150), (skill_width // 2, 200), 13, 3)
                    # 提示信息
                    ts_surf1 = basic_FONT.render(('击晕率 + 1'), 1, (0, 0, 150))
                    ts_rect1 = ts_surf1.get_rect()
                    ts_rect1.centerx = skill_width / 2
                    ts_rect1.centery = 470
                    skill_surf.blit(ts_surf1, ts_rect1)
                    if kongzhi_skill['2'] and mouse_click and kongzhi_skill['3'] == False:
                        if attributes['skill_attribute']:
                            yh_attribute[7] += 1
                            attributes['skill_attribute'] -= 1
                            kongzhi_skill['3'] = True

                if math.sqrt(pow((mousex - 100 - skill_width / 2), 2) + pow((mousey - 100 - 250), 2)) <= 10:
                    pygame.draw.circle(skill_surf, (0, 0, 150), (skill_width // 2, 250), 13, 3)
                    # 提示信息
                    ts_surf1 = basic_FONT.render(('击晕敌方增至两回合'), 1, (0, 0, 150))
                    ts_rect1 = ts_surf1.get_rect()
                    ts_rect1.centerx = skill_width / 2
                    ts_rect1.centery = 470
                    skill_surf.blit(ts_surf1, ts_rect1)
                    if kongzhi_skill['3'] and mouse_click and kongzhi_skill['4'] == False:
                        if attributes['skill_attribute']:
                            attributes['skill_attribute'] -= 1
                            kongzhi_skill['4'] = True

                if math.sqrt(pow((mousex - 100 - skill_width / 2), 2) + pow((mousey - 100 - 300), 2)) <= 10:
                    pygame.draw.circle(skill_surf, (0, 0, 150), (skill_width // 2, 300), 13, 3)
                    # 提示信息
                    ts_surf1 = basic_FONT.render(('击晕率 + 2'), 1, (0, 0, 150))
                    ts_rect1 = ts_surf1.get_rect()
                    ts_rect1.centerx = skill_width / 2
                    ts_rect1.centery = 470
                    skill_surf.blit(ts_surf1, ts_rect1)
                    if kongzhi_skill['4'] and mouse_click and kongzhi_skill['5'] == False:
                        if attributes['skill_attribute']:
                            yh_attribute[7] += 2
                            attributes['skill_attribute'] -= 1
                            kongzhi_skill['5'] = True

                if math.sqrt(pow((mousex - 100 - skill_width / 2), 2) + pow((mousey - 100 - 350), 2)) <= 10:
                    pygame.draw.circle(skill_surf, (0, 0, 150), (skill_width // 2, 350), 13, 3)
                    # 提示信息
                    ts_surf1 = basic_FONT.render(('击晕率 + 2'), 1, (0, 0, 150))
                    ts_rect1 = ts_surf1.get_rect()
                    ts_rect1.centerx = skill_width / 2
                    ts_rect1.centery = 470
                    skill_surf.blit(ts_surf1, ts_rect1)
                    if kongzhi_skill['5'] and mouse_click and kongzhi_skill['6'] == False:
                        if attributes['skill_attribute']:
                            yh_attribute[7] += 2
                            attributes['skill_attribute'] -= 1
                            kongzhi_skill['6'] = True

                if math.sqrt(pow((mousex - 100 - skill_width / 2), 2) + pow((mousey - 100 - 400), 2)) <= 10:
                    pygame.draw.circle(skill_surf, (0, 0, 150), (skill_width // 2, 400), 13, 3)
                    # 提示信息
                    ts_surf1 = basic_FONT.render(('攻击时使敌方附带(等级/3)点中毒状态'), 1, (0, 0, 150))
                    ts_rect1 = ts_surf1.get_rect()
                    ts_rect1.centerx = skill_width / 2
                    ts_rect1.centery = 470
                    skill_surf.blit(ts_surf1, ts_rect1)
                    if kongzhi_skill['6'] and mouse_click and kongzhi_skill['7'] == False:
                        if attributes['skill_attribute']:
                            attributes['skill_attribute'] -= 1
                            kongzhi_skill['7'] = True

                if math.sqrt( pow((mousex - 100 - skill_width / 2 - 50), 2) + pow((mousey - 100 - 250), 2)) <= 10:
                    pygame.draw.circle(skill_surf, (0, 0, 150), (skill_width // 2 + 50, 250), 13, 3)
                    # 提示信息
                    ts_surf1 = basic_FONT.render(('不详'), 1, (0, 0, 150))
                    ts_rect1 = ts_surf1.get_rect()
                    ts_rect1.centerx = skill_width / 2
                    ts_rect1.centery = 470
                    skill_surf.blit(ts_surf1, ts_rect1)
                    if kongzhi_skill['4'] and mouse_click and kongzhi_skill['right1'] == False:
                        if attributes['skill_attribute']:
                            attributes['skill_attribute'] -= 1
                        kongzhi_skill['right1'] = True

                if math.sqrt(
                        pow((mousex - 100 - skill_width / 2 - 100), 2) + pow((mousey - 100 - 250), 2)) <= 10:
                    pygame.draw.circle(skill_surf, (0, 0, 150), (skill_width // 2 + 100, 250), 13, 3)
                    # 提示信息
                    ts_surf1 = basic_FONT.render(('不详'), 1, (0, 0, 150))
                    ts_rect1 = ts_surf1.get_rect()
                    ts_rect1.centerx = skill_width / 2
                    ts_rect1.centery = 470
                    skill_surf.blit(ts_surf1, ts_rect1)
                    if kongzhi_skill['right1'] and mouse_click and kongzhi_skill['right2'] == False:
                        if attributes['skill_attribute']:
                            attributes['skill_attribute'] -= 1
                            kongzhi_skill['right2'] = True

                if math.sqrt(
                        pow((mousex - 100 - skill_width / 2 - 150), 2) + pow((mousey - 100 - 250), 2)) <= 10:
                    pygame.draw.circle(skill_surf, (0, 0, 150), (skill_width // 2 + 150, 250), 13, 3)
                    # 提示信息
                    ts_surf1 = basic_FONT.render(('不详'), 1, (0, 0, 150))
                    ts_rect1 = ts_surf1.get_rect()
                    ts_rect1.centerx = skill_width / 2
                    ts_rect1.centery = 470
                    skill_surf.blit(ts_surf1, ts_rect1)
                    if kongzhi_skill['right2'] and mouse_click and kongzhi_skill['right3'] == False:
                        if attributes['skill_attribute']:
                            attributes['skill_attribute'] -= 1
                            kongzhi_skill['right3'] = True

                if math.sqrt(
                        pow((mousex - 100 - skill_width / 2 + 50), 2) + pow((mousey - 100 - 250), 2)) <= 10:
                    pygame.draw.circle(skill_surf, (0, 0, 150), (skill_width // 2 - 50, 250), 13, 3)
                    # 提示信息
                    ts_surf1 = basic_FONT.render(('不详'), 1, (0, 0, 150))
                    ts_rect1 = ts_surf1.get_rect()
                    ts_rect1.centerx = skill_width / 2
                    ts_rect1.centery = 470
                    skill_surf.blit(ts_surf1, ts_rect1)
                    if kongzhi_skill['4'] and mouse_click and kongzhi_skill['left1'] == False:
                        if attributes['skill_attribute']:
                            attributes['skill_attribute'] -= 1
                            kongzhi_skill['left1'] = True

                if math.sqrt(
                        pow((mousex - 100 - skill_width / 2 + 100), 2) + pow((mousey - 100 - 250), 2)) <= 10:
                    pygame.draw.circle(skill_surf, (0, 0, 150), (skill_width // 2 - 100, 250), 13, 3)
                    # 提示信息
                    ts_surf1 = basic_FONT.render(('不详'), 1, (0, 0, 150))
                    ts_rect1 = ts_surf1.get_rect()
                    ts_rect1.centerx = skill_width / 2
                    ts_rect1.centery = 470
                    skill_surf.blit(ts_surf1, ts_rect1)
                    if kongzhi_skill['left1'] and mouse_click and kongzhi_skill['left2'] == False:
                        if attributes['skill_attribute']:
                            attributes['skill_attribute'] -= 1
                            kongzhi_skill['left2'] = True

                if math.sqrt(
                        pow((mousex - 100 - skill_width / 2 + 150), 2) + pow((mousey - 100 - 250), 2)) <= 10:
                    pygame.draw.circle(skill_surf, (0, 0, 150), (skill_width // 2 - 150, 250), 13, 3)
                    # 提示信息
                    ts_surf1 = basic_FONT.render(('不详'), 1, (0, 0, 150))
                    ts_rect1 = ts_surf1.get_rect()
                    ts_rect1.centerx = skill_width / 2
                    ts_rect1.centery = 470
                    skill_surf.blit(ts_surf1, ts_rect1)
                    if kongzhi_skill['left2'] and mouse_click and kongzhi_skill['left3'] == False:
                        if attributes['skill_attribute']:
                            attributes['skill_attribute'] -= 1
                            kongzhi_skill['left3'] = True

                screen.blit(skill_surf, skill_rect)
                pygame.display.update()
                FPSclock.tick(FPS)

        # 进入狂战技能树
        if kuangzhan_click:
            while True:
                # 一些常量
                close = False
                mouse_click = False

                # 各种职业介绍面板
                skill_width = 700
                skill_height = 500
                skill_surf = pygame.Surface((skill_width, skill_height))
                skill_rect = skill_surf.get_rect()
                skill_rect.centerx = screen_width / 2
                skill_rect.centery = screen_height / 2
                skill_surf.fill((100, 100, 100))
                pygame.draw.lines(skill_surf, (0, 0, 0), True,
                                  [(0, 0), (0, skill_height), (skill_width, skill_height), (skill_width, 0)],
                                  16)
                pygame.draw.line(skill_surf, (0, 0, 0), (0, 440), (skill_width, 440), 8)

                zhongjia_surf = big_FONT.render('狂战士', 1, (0, 0, 0))
                zhongjia_rect = zhongjia_surf.get_rect()
                zhongjia_rect.centerx = skill_width / 2
                zhongjia_rect.centery = 50
                skill_surf.blit(zhongjia_surf, zhongjia_rect)

                pygame.draw.line(skill_surf, (0, 0, 0), (skill_width / 2 - 150, 250),(skill_width / 2 + 150, 250), 2)
                pygame.draw.line(skill_surf, (0, 0, 0), (skill_width / 2, 100), (skill_width / 2, 400), 2)

                if kuangzhan_skill['1']:
                    pygame.draw.circle(skill_surf, (150, 0, 0), (skill_width // 2, 100), 10)
                else:
                    pygame.draw.circle(skill_surf, (0, 0, 0), (skill_width // 2, 100), 10)
                if kuangzhan_skill['2']:
                    pygame.draw.circle(skill_surf, (150, 0, 0), (skill_width // 2, 150), 10)
                else:
                    pygame.draw.circle(skill_surf, (0, 0, 0), (skill_width // 2, 150), 10)
                if kuangzhan_skill['3']:
                    pygame.draw.circle(skill_surf, (150, 0, 0), (skill_width // 2, 200), 10)
                else:
                    pygame.draw.circle(skill_surf, (0, 0, 0), (skill_width // 2, 200), 10)
                if kuangzhan_skill['4']:
                    pygame.draw.circle(skill_surf, (150, 0, 0), (skill_width // 2, 250), 10)
                else:
                    pygame.draw.circle(skill_surf, (0, 0, 0), (skill_width // 2, 250), 10)
                if kuangzhan_skill['5']:
                    pygame.draw.circle(skill_surf, (150, 0, 0), (skill_width // 2, 300), 10)
                else:
                    pygame.draw.circle(skill_surf, (0, 0, 0), (skill_width // 2, 300), 10)
                if kuangzhan_skill['6']:
                    pygame.draw.circle(skill_surf, (150, 0, 0), (skill_width // 2, 350), 10)
                else:
                    pygame.draw.circle(skill_surf, (0, 0, 0), (skill_width // 2, 350), 10)
                if kuangzhan_skill['7']:
                    pygame.draw.circle(skill_surf, (150, 0, 0), (skill_width // 2, 400), 10)
                else:
                    pygame.draw.circle(skill_surf, (0, 0, 0), (skill_width // 2, 400), 10)
                if kuangzhan_skill['left1']:
                    pygame.draw.circle(skill_surf, (150, 0, 0), (skill_width // 2 - 50, 250), 10)
                else:
                    pygame.draw.circle(skill_surf, (0, 0, 0), (skill_width // 2 - 50, 250), 10)
                if kuangzhan_skill['left2']:
                    pygame.draw.circle(skill_surf, (150, 0, 0), (skill_width // 2 - 100, 250), 10)
                else:
                    pygame.draw.circle(skill_surf, (0, 0, 0), (skill_width // 2 - 100, 250), 10)
                if kuangzhan_skill['left3']:
                    pygame.draw.circle(skill_surf, (150, 0, 0), (skill_width // 2 - 150, 250), 10)
                else:
                    pygame.draw.circle(skill_surf, (0, 0, 0), (skill_width // 2 - 150, 250), 10)
                if kuangzhan_skill['right1']:
                    pygame.draw.circle(skill_surf, (150, 0, 0), (skill_width // 2 + 50, 250), 10)
                else:
                    pygame.draw.circle(skill_surf, (0, 0, 0), (skill_width // 2 + 50, 250), 10)
                if kuangzhan_skill['right2']:
                    pygame.draw.circle(skill_surf, (150, 0, 0), (skill_width // 2 + 100, 250), 10)
                else:
                    pygame.draw.circle(skill_surf, (0, 0, 0), (skill_width // 2 + 100, 250), 10)
                if kuangzhan_skill['right3']:
                    pygame.draw.circle(skill_surf, (150, 0, 0), (skill_width // 2 + 150, 250), 10)
                else:
                    pygame.draw.circle(skill_surf, (0, 0, 0), (skill_width // 2 + 150, 250), 10)



                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        # 再按i关闭
                        if event.key == pygame.K_i:
                            close = True
                    if event.type == pygame.MOUSEMOTION:
                        mousex, mousey = event.pos
                    elif event.type == pygame.MOUSEBUTTONUP:
                        mouse_click = True

                if close:
                    break

                if math.sqrt(pow((mousex - 100 - skill_width / 2), 2) + pow((mousey - 100 - 100), 2)) <= 10:
                    pygame.draw.circle(skill_surf, (150, 0, 0), (skill_width // 2, 100), 13, 3)
                    # 提示信息
                    ts_surf1 = basic_FONT.render(('攻击 + 5'), 1, (150, 0, 0))
                    ts_rect1 = ts_surf1.get_rect()
                    ts_rect1.centerx = skill_width / 2
                    ts_rect1.centery = 470
                    skill_surf.blit(ts_surf1, ts_rect1)
                    if mouse_click and kuangzhan_skill['1'] == False:
                        if attributes['skill_attribute']:
                            yh_attribute[2] += 5
                            attributes['skill_attribute'] -= 1
                            kuangzhan_skill['1'] = True

                if math.sqrt(pow((mousex - 100 - skill_width / 2), 2) + pow((mousey - 100 - 150), 2)) <= 10:
                    pygame.draw.circle(skill_surf, (150, 0, 0), (skill_width // 2, 150), 13, 3)
                    # 提示信息
                    ts_surf1 = basic_FONT.render(('暴击率 + 1'), 1, (150, 0, 0))
                    ts_rect1 = ts_surf1.get_rect()
                    ts_rect1.centerx = skill_width / 2
                    ts_rect1.centery = 470
                    skill_surf.blit(ts_surf1, ts_rect1)
                    if kuangzhan_skill['1'] and mouse_click and kuangzhan_skill['2'] == False:
                        if attributes['skill_attribute']:
                            yh_attribute[5] += 1
                            attributes['skill_attribute'] -= 1
                            kuangzhan_skill['2'] = True

                if math.sqrt(pow((mousex - 100 - skill_width / 2), 2) + pow((mousey - 100 - 200), 2)) <= 10:
                    pygame.draw.circle(skill_surf, (150, 0, 0), (skill_width // 2, 200), 13, 3)
                    # 提示信息
                    ts_surf1 = basic_FONT.render(('攻击 + 5'), 1, (150, 0, 0))
                    ts_rect1 = ts_surf1.get_rect()
                    ts_rect1.centerx = skill_width / 2
                    ts_rect1.centery = 470
                    skill_surf.blit(ts_surf1, ts_rect1)
                    if kuangzhan_skill['2'] and mouse_click and kuangzhan_skill['3'] == False:
                        if attributes['skill_attribute']:
                            yh_attribute[2] += 5
                            attributes['skill_attribute'] -= 1
                            kuangzhan_skill['3'] = True

                if math.sqrt(pow((mousex - 100 - skill_width / 2), 2) + pow((mousey - 100 - 250), 2)) <= 10:
                    pygame.draw.circle(skill_surf, (150, 0, 0), (skill_width // 2, 250), 13, 3)
                    # 提示信息
                    ts_surf1 = basic_FONT.render(('生命 < 70%/50%/30%时：攻击 * 1.2/1.4/1.6 '), 1, (150, 0, 0))
                    ts_rect1 = ts_surf1.get_rect()
                    ts_rect1.centerx = skill_width / 2
                    ts_rect1.centery = 470
                    skill_surf.blit(ts_surf1, ts_rect1)
                    if kuangzhan_skill['3'] and mouse_click and kuangzhan_skill['4'] == False:
                        if attributes['skill_attribute']:
                            attributes['skill_attribute'] -= 1
                            kuangzhan_skill['4'] = True

                if math.sqrt(pow((mousex - 100 - skill_width / 2), 2) + pow((mousey - 100 - 300), 2)) <= 10:
                    pygame.draw.circle(skill_surf, (150, 0, 0), (skill_width // 2, 300), 13, 3)
                    # 提示信息
                    ts_surf1 = basic_FONT.render(('暴击率 + 2'), 1, (150, 0, 0))
                    ts_rect1 = ts_surf1.get_rect()
                    ts_rect1.centerx = skill_width / 2
                    ts_rect1.centery = 470
                    skill_surf.blit(ts_surf1, ts_rect1)
                    if kuangzhan_skill['4'] and mouse_click and kuangzhan_skill['5'] == False:
                        if attributes['skill_attribute']:
                            yh_attribute[5] += 2
                            attributes['skill_attribute'] -= 1
                            kuangzhan_skill['5'] = True

                if math.sqrt(pow((mousex - 100 - skill_width / 2), 2) + pow((mousey - 100 - 350), 2)) <= 10:
                    pygame.draw.circle(skill_surf, (150, 0, 0), (skill_width // 2, 350), 13, 3)
                    # 提示信息
                    ts_surf1 = basic_FONT.render(('暴击率 + 2'), 1, (150, 0, 0))
                    ts_rect1 = ts_surf1.get_rect()
                    ts_rect1.centerx = skill_width / 2
                    ts_rect1.centery = 470
                    skill_surf.blit(ts_surf1, ts_rect1)
                    if kuangzhan_skill['5'] and mouse_click and kuangzhan_skill['6'] == False:
                        if attributes['skill_attribute']:
                            yh_attribute[5] += 2
                            attributes['skill_attribute'] -= 1
                            kuangzhan_skill['6'] = True

                if math.sqrt(pow((mousex - 100 - skill_width / 2), 2) + pow((mousey - 100 - 400), 2)) <= 10:
                    pygame.draw.circle(skill_surf, (150, 0, 0), (skill_width // 2, 400), 13, 3)
                    # 提示信息
                    ts_surf1 = basic_FONT.render(('致命一击：第三次攻击造成1.5倍伤害（如果暴击则为3倍）'), 1, (150, 0, 0))
                    ts_rect1 = ts_surf1.get_rect()
                    ts_rect1.centerx = skill_width / 2
                    ts_rect1.centery = 470
                    skill_surf.blit(ts_surf1, ts_rect1)
                    if kuangzhan_skill['6'] and mouse_click and kuangzhan_skill['7'] == False:
                        if attributes['skill_attribute']:
                            attributes['skill_attribute'] -= 1
                            kuangzhan_skill['7'] = True

                if math.sqrt(
                        pow((mousex - 100 - skill_width / 2 - 50), 2) + pow((mousey - 100 - 250), 2)) <= 10:
                    pygame.draw.circle(skill_surf, (150, 0, 0), (skill_width // 2 + 50, 250), 13, 3)
                    # 提示信息
                    ts_surf1 = basic_FONT.render(('不详'), 1, (150, 0, 0))
                    ts_rect1 = ts_surf1.get_rect()
                    ts_rect1.centerx = skill_width / 2
                    ts_rect1.centery = 470
                    skill_surf.blit(ts_surf1, ts_rect1)
                    if kuangzhan_skill['4'] and mouse_click and kuangzhan_skill['right1'] == False:
                        if attributes['skill_attribute']:
                            attributes['skill_attribute'] -= 1
                            kuangzhan_skill['right1'] = True

                if math.sqrt(
                        pow((mousex - 100 - skill_width / 2 - 100), 2) + pow((mousey - 100 - 250), 2)) <= 10:
                    pygame.draw.circle(skill_surf, (150, 0, 0), (skill_width // 2 + 100, 250), 13, 3)
                    # 提示信息
                    ts_surf1 = basic_FONT.render(('不详'), 1, (150, 0, 0))
                    ts_rect1 = ts_surf1.get_rect()
                    ts_rect1.centerx = skill_width / 2
                    ts_rect1.centery = 470
                    skill_surf.blit(ts_surf1, ts_rect1)
                    if kuangzhan_skill['right1'] and mouse_click and kuangzhan_skill['right2'] == False:
                        if attributes['skill_attribute']:
                            attributes['skill_attribute'] -= 1
                            kuangzhan_skill['right2'] = True

                if math.sqrt(
                        pow((mousex - 100 - skill_width / 2 - 150), 2) + pow((mousey - 100 - 250), 2)) <= 10:
                    pygame.draw.circle(skill_surf, (150, 0, 0), (skill_width // 2 + 150, 250), 13, 3)
                    # 提示信息
                    ts_surf1 = basic_FONT.render(('不详'), 1, (150, 0, 0))
                    ts_rect1 = ts_surf1.get_rect()
                    ts_rect1.centerx = skill_width / 2
                    ts_rect1.centery = 470
                    skill_surf.blit(ts_surf1, ts_rect1)
                    if kuangzhan_skill['right2'] and mouse_click and kuangzhan_skill['right3'] == False:
                        if attributes['skill_attribute']:
                            attributes['skill_attribute'] -= 1
                            kuangzhan_skill['right3'] = True

                if math.sqrt(
                        pow((mousex - 100 - skill_width / 2 + 50), 2) + pow((mousey - 100 - 250), 2)) <= 10:
                    pygame.draw.circle(skill_surf, (150, 0, 0), (skill_width // 2 - 50, 250), 13, 3)
                    # 提示信息
                    ts_surf1 = basic_FONT.render(('不详'), 1, (150, 0, 0))
                    ts_rect1 = ts_surf1.get_rect()
                    ts_rect1.centerx = skill_width / 2
                    ts_rect1.centery = 470
                    skill_surf.blit(ts_surf1, ts_rect1)
                    if kuangzhan_skill['4'] and mouse_click and kuangzhan_skill['left1'] == False:
                        if attributes['skill_attribute']:
                            attributes['skill_attribute'] -= 1
                            kuangzhan_skill['left1'] = True

                if math.sqrt(
                        pow((mousex - 100 - skill_width / 2 + 100), 2) + pow((mousey - 100 - 250), 2)) <= 10:
                    pygame.draw.circle(skill_surf, (150, 0, 0), (skill_width // 2 - 100, 250), 13, 3)
                    # 提示信息
                    ts_surf1 = basic_FONT.render(('不详'), 1, (150, 0, 0))
                    ts_rect1 = ts_surf1.get_rect()
                    ts_rect1.centerx = skill_width / 2
                    ts_rect1.centery = 470
                    skill_surf.blit(ts_surf1, ts_rect1)
                    if kuangzhan_skill['left1'] and mouse_click and kuangzhan_skill['left2'] == False:
                        if attributes['skill_attribute']:
                            attributes['skill_attribute'] -= 1
                            kuangzhan_skill['left2'] = True

                if math.sqrt(
                        pow((mousex - 100 - skill_width / 2 + 150), 2) + pow((mousey - 100 - 250), 2)) <= 10:
                    pygame.draw.circle(skill_surf, (150, 0, 0), (skill_width // 2 - 150, 250), 13, 3)
                    # 提示信息
                    ts_surf1 = basic_FONT.render(('不详'), 1, (150, 0, 0))
                    ts_rect1 = ts_surf1.get_rect()
                    ts_rect1.centerx = skill_width / 2
                    ts_rect1.centery = 470
                    skill_surf.blit(ts_surf1, ts_rect1)
                    if kuangzhan_skill['left2'] and mouse_click and kuangzhan_skill['left3'] == False:
                        if attributes['skill_attribute']:
                            attributes['skill_attribute'] -= 1
                            kuangzhan_skill['left3'] = True

                screen.blit(skill_surf, skill_rect)
                pygame.display.update()
                FPSclock.tick(FPS)





        screen.blit(skill_surf,skill_rect)
        pygame.display.update()
        FPSclock.tick(FPS)























