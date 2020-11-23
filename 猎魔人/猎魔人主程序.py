import pygame,time,random,sys,os,copy
from pygame.locals import *
import 函数 as hs
from dialog import dialog

pygame.init()
FPS = 30
screen_width = 900
screen_height = 700
bg_color = (70,70,70)
layer = 0
camerax = 0
cameray = 0
dialog_num = 0
yellow_key = 3
green_key = 1
purple_key = 1
red_key = 0
orange_key = 0
colors_key = 0
# 怪物属性值 名字 生命 攻击 防御 躲闪 暴击 击晕率 经验 金钱 装备掉落 装备爆率
monster_attribute = {
    'Z':['球球怪(白)',100,5,1,0,0,0,2,0,['i','a'],[4,1]],
    'X':['球球怪(绿)',150,6,1,0,0,0,3,1,['q','a'],[4,1]]
}
# 银魂属性 名字 生命 攻击 防御 躲闪率 暴击率 生命上限 击晕率
yh_attribute = ['银魂',100,5,1,0,0,100,0]

# 银魂等级及属性
attributes = {'yh_level':1,'money':0,'experience':0,'max_experience':10,'common_attribute':0,'special_attribute':0,'skill_attribute':10,'tizhi':0,'liliang':0,'naili':0,'minjie':0,'huixin':0,'zhongji':0}
mousex = 0
mousey = 0

# 技能
zhongjia_skill = {'1':False,'2':False,'3':False,'4':False,'5':False,'6':False,'7':False,'left1':False,'left2':False,'left3':False,'right1':False,'right2':False,'right3':False}
kongzhi_skill = {'1':False,'2':False,'3':False,'4':False,'5':False,'6':False,'7':False,'left1':False,'left2':False,'left3':False,'right1':False,'right2':False,'right3':False}
kuangzhan_skill = {'1':False,'2':False,'3':False,'4':False,'5':False,'6':False,'7':False,'left1':False,'left2':False,'left3':False,'right1':False,'right2':False,'right3':False}

# 地图图片
tiles_image = {
    '1':pygame.image.load('image/floor23.jpg'),
    '2':pygame.image.load('image/wall2.png'),
    '3':pygame.image.load('image/lt1.png'),
    '4':pygame.image.load('image/lt2.png'),
    '5':pygame.image.load('image/door1.png'),
    '6':pygame.image.load('image/door2.png'),
    '7':pygame.image.load('image/door3.png'),
    '8':pygame.image.load('image/door4.png'),
    '9':pygame.image.load('image/door5.png'),
    # 但在地图中'10'用'0'代替
    '10':pygame.image.load('image/door6.png'),
    'q':pygame.image.load('image/key1.png'),
    'w':pygame.image.load('image/key2.png'),
    'e':pygame.image.load('image/key3.png'),
    'r':pygame.image.load('image/key4.png'),
    't':pygame.image.load('image/key5.png'),
    'y':pygame.image.load('image/key6.png'),
    'smallq':pygame.image.load('image/smallkey1.png'),
    'smallw':pygame.image.load('image/smallkey2.png'),
    'smalle':pygame.image.load('image/smallkey3.png'),
    'smallr':pygame.image.load('image/smallkey4.png'),
    'smallt':pygame.image.load('image/smallkey5.png'),
    'smally':pygame.image.load('image/smallkey6.png'),
    'money':pygame.image.load('image/money.png'),
    'a':pygame.image.load('image/npc1.png'),
    's':pygame.image.load('image/npc2.png'),
    'z1':pygame.image.load('image/hero1.png'),
    'z2':pygame.image.load('image/hero2.png'),
    'z3': pygame.image.load('image/hero3.png'),
    'z4': pygame.image.load('image/hero4.png'),
    # 怪物
    'Z':pygame.image.load('image/ball_white.png'),
    'X':pygame.image.load('image/ball_green.png'),
    # 战斗图标
    'attack':pygame.image.load('image/attack.png')
}
#地图解析
map = hs.describemap()
floors = map[0]
walls = map[1]
movingup = False
movingdown = False
movingleft = False
movingright = False
dialog_TF = False
hero_direction = [True,False,False,False]

#提示语言
tishi = False
basic_FONT = pygame.font.SysFont('SimHei',20)
big_FONT = pygame.font.SysFont('SimHei',30)
tishi_surf = basic_FONT.render('按下空格键与人物对话', 1, (200, 150, 50))
tishi_rect = tishi_surf.get_rect()
tishi_rect.centerx = screen_width/2
tishi_rect.bottom = screen_height

# 钥匙计数板
distance = 40
yellow_rect = pygame.Rect((0,screen_height - 2*distance,30,30))
green_rect = pygame.Rect((0,screen_height - 3*distance,30,30))
purple_rect = pygame.Rect((0,screen_height - 4*distance,30,30))
red_rect = pygame.Rect((0,screen_height - 5*distance,30,30))
orange_rect = pygame.Rect((0,screen_height - 6*distance,30,30))
colors_rect = pygame.Rect((0,screen_height - 7*distance,30,30))
y_rect = pygame.Rect((35,screen_height - 2*distance,30,30))
g_rect = pygame.Rect((35,screen_height - 3*distance,30,30))
p_rect = pygame.Rect((35,screen_height - 4*distance,30,30))
r_rect = pygame.Rect((35,screen_height - 5*distance,30,30))
o_rect = pygame.Rect((35,screen_height - 6*distance,30,30))
c_rect = pygame.Rect((35,screen_height - 7*distance,30,30))

# 金钱计数板
image_rect = pygame.Rect((6,screen_height - distance,20,20))
font_rect = pygame.Rect((35,screen_height - distance,20,20))

# 道具与装备
drawstate_1 = False
drawstate_2 = False
drawstate_3 = False
drawstate_4 = False
drawstate_5 = False
drawstate_6 = False
draw_1 = ''
draw_2 = ''
draw_3 = ''
draw_4 = ''
draw_5 = ''
draw_6 = ''
mousex = 0
mousey = 0
equipment = ['1','2']
equipment_image = {'a':pygame.image.load('image/wuqi1.png'),
                   'b':pygame.image.load('image/wuqi2.png'),
                   'c':pygame.image.load('image/wuqi3.png'),
                   'd':pygame.image.load('image/wuqi4.png'),
                   'e':pygame.image.load('image/toukui1.png'),
                   'f':pygame.image.load('image/toukui2.png'),
                   #'g':pygame.image.load('image/toukui3.png'),
                   #'h':pygame.image.load('image/toukui4.png'),
                   'i':pygame.image.load('image/hujia1.png'),
                   'j':pygame.image.load('image/hujia2.png'),
                   #'k':pygame.image.load('image/hujia3.png'),
                   #'l':pygame.image.load('image/hujia4.png'),
                   'm':pygame.image.load('image/jiezhi1.png'),
                   'n':pygame.image.load('image/jiezhi2.png'),
                   #'o':pygame.image.load('image/jiezhi3.png'),
                   #'p':pygame.image.load('image/jiezhi4.png'),
                   'q':pygame.image.load('image/xiezi1.png'),
                   'r':pygame.image.load('image/xiezi2.png'),
                   's':pygame.image.load('image/xiezi3.png'),
                   #'t':pygame.image.load('image/xiezi4.png'),
                   'u':pygame.image.load('image/xianglian1.png'),
                   'v':pygame.image.load('image/xianglian2.png'),
                   #'w':pygame.image.load('image/xianglian3.png'),
                   #'x':pygame.image.load('image/xianglian4.png'),


                   '1':pygame.image.load('image/blood1.png'),
                   '2':pygame.image.load('image/blood2.png'),
                   #'3':pygame.image.load('image/blood3.png')
                   }
equipment_information2 = {'a':'漆木棍','b':'青铜剑','c':'佩剑','d':'血剑','e':'布帽','f':'官人帽','i':'红布衣','j':'锦衣','m':'碧水戒','n':'红宝石戒指','q':'木屐','r':'雨靴','s':'铁靴','u':'铃铛链','v':'翡翠链','1':'止血散','2':'胶囊'}
equipment_information = {'a':'漆木棍(武器)：攻击+1','b':'青铜剑(武器)：攻击+2','c':'佩剑(武器)：攻击+10','d':'血剑(武器)：攻击+40',
                         'e':'布帽(头盔)：防御+1','f':'官人帽(头盔)：防御+2',
                         'i':'红布衣(护甲)：防御+3','j':'锦衣(护甲)：防御+4',
                         'm':'碧水戒(戒指)：防御+5','n':'红宝石戒指(戒指)：防御+6',
                         'q':'木屐(鞋子)：防御+7','r':'雨靴(鞋子)：防御+8','s':'铁靴(鞋子)：防御+7',
                         'u':'铃铛链(项链)：防御+9','v':'翡翠链(项链)：防御+10',
                         '1':'止血散：气血+10','2':'胶囊：气血+30'}

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('猎魔人')
FPSclock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                hero_direction[0] = True
                hero_direction[1] = False
                hero_direction[2] = False
                hero_direction[3] = False
                # 如果角色与墙不碰撞即可移动
                if [map[4][layer][0],map[4][layer][1] - 1] not in map[1][layer]:
                    if [map[4][layer][0], map[4][layer][1] - 1] not in map[7][layer].values():
                        nodoors = 0
                        for i in range(len(map[8])):
                            if [map[4][layer][0], map[4][layer][1] - 1] not in map[8][i][layer]:
                                nodoors = nodoors + 1
                                if nodoors == len(map[8]):
                                    map[4][layer][1] -= 1
                            else:
                                #开门
                                door_direction = 'up'
                                key = hs.opendoor(map,tiles_image,yellow_key,green_key,purple_key,red_key,orange_key,colors_key,FPSclock,layer,mapsurface,mapsurface_rect,screen,door_direction,i)
                                yellow_key = key[0]
                                green_key = key[1]
                                purple_key = key[2]
                                red_key = key[3]
                                orange_key = key[4]
                                colors_key = key[5]
                                pygame.event.clear()
            if event.key == K_DOWN:
                hero_direction[0] = False
                hero_direction[1] = True
                hero_direction[2] = False
                hero_direction[3] = False
                if [map[4][layer][0],map[4][layer][1] + 1] not in map[1][layer]:
                    if [map[4][layer][0], map[4][layer][1] + 1] not in map[7][layer].values():
                        nodoors = 0
                        for i in range(len(map[8])):
                            if [map[4][layer][0], map[4][layer][1] + 1] not in map[8][i][layer]:
                                nodoors = nodoors + 1
                                if nodoors == len(map[8]):
                                    map[4][layer][1] += 1
                            else:
                                door_direction = 'down'
                                key = hs.opendoor(map, tiles_image, yellow_key, green_key, purple_key, red_key, orange_key, colors_key,FPSclock, layer, mapsurface, mapsurface_rect, screen, door_direction,i)
                                yellow_key = key[0]
                                green_key = key[1]
                                purple_key = key[2]
                                red_key = key[3]
                                orange_key = key[4]
                                colors_key = key[5]
                                pygame.event.clear()
            if event.key == K_LEFT:
                hero_direction[0] = False
                hero_direction[1] = False
                hero_direction[2] = True
                hero_direction[3] = False
                if [map[4][layer][0] - 1,map[4][layer][1]] not in map[1][layer]:
                    if [map[4][layer][0] - 1, map[4][layer][1]] not in map[7][layer].values():
                        nodoors = 0
                        for i in range(len(map[8])):
                            if [map[4][layer][0] - 1, map[4][layer][1]] not in map[8][i][layer]:
                                nodoors = nodoors + 1
                                if nodoors == len(map[8]):
                                    map[4][layer][0] -= 1
                            else:
                                door_direction = 'left'
                                key = hs.opendoor(map, tiles_image, yellow_key, green_key, purple_key, red_key, orange_key, colors_key, FPSclock, layer, mapsurface, mapsurface_rect, screen, door_direction,i)
                                yellow_key = key[0]
                                green_key = key[1]
                                purple_key = key[2]
                                red_key = key[3]
                                orange_key = key[4]
                                colors_key = key[5]
                                pygame.event.clear()
            if event.key == K_RIGHT:
                hero_direction[0] = False
                hero_direction[1] = False
                hero_direction[2] = False
                hero_direction[3] = True
                if [map[4][layer][0] + 1,map[4][layer][1]] not in map[1][layer]:
                    if [map[4][layer][0] + 1, map[4][layer][1]] not in map[7][layer].values():
                        nodoors = 0
                        for i in range(len(map[8])):
                            if [map[4][layer][0] + 1, map[4][layer][1]] not in map[8][i][layer]:
                                nodoors = nodoors + 1
                                if nodoors == len(map[8]):
                                    map[4][layer][0] += 1
                            else:
                                door_direction = 'right'
                                key = hs.opendoor(map, tiles_image, yellow_key, green_key, purple_key, red_key, orange_key, colors_key,FPSclock, layer, mapsurface, mapsurface_rect, screen, door_direction,i)
                                yellow_key = key[0]
                                green_key = key[1]
                                purple_key = key[2]
                                red_key = key[3]
                                orange_key = key[4]
                                colors_key = key[5]
                                pygame.event.clear()

            if tishi:
                if event.key == K_SPACE:
                    if dialog_TF:
                        dialog_num += 1
                    dialog_TF = True
            # 捡钥匙
            for i in range(len(map[9])):
                if map[4][layer] in map[9][i][layer]:
                    map[9][i][layer].remove(map[4][layer])
                    if i == 0:
                        yellow_key += 1
                    if i == 1:
                        green_key += 1
                    if i == 2:
                        purple_key += 1
                    if i == 3:
                        red_key += 1
                    if i == 4:
                        orange_key += 1
                    if i == 5:
                        colors_key += 1
            # 相机
            if event.key == K_w:
                cameray -= 30
            if event.key == K_s:
                cameray += 30
            if event.key == K_a:
                camerax -= 30
            if event.key == K_d:
                camerax += 30

            # 按I绘制技能表
            if event.key == K_i:
                hs.draw_skill(screen_width, screen_height, screen, FPS, FPSclock,basic_FONT,big_FONT,mousex,mousey,attributes,zhongjia_skill,kongzhi_skill,kuangzhan_skill,yh_attribute)


            # 按O绘制潜能分配表
            if event.key == K_o:
                hs.draw_attribute(tiles_image,yh_attribute,screen_width,screen_height,screen,FPSclock,FPS,basic_FONT,big_FONT,attributes,mousex,mousey)

            # 按P绘制装备栏和道具栏
            if event.key == K_p:
                while True:
                    # 装备栏和道具栏的初始界面
                    equipment_width = 700
                    equipment_height = 500
                    equipment_surf = pygame.Surface((equipment_width, equipment_height))
                    equipment_rect = equipment_surf.get_rect()
                    equipment_rect.centerx = screen_width / 2
                    equipment_rect.centery = screen_height / 2
                    equipment_surf.fill((100, 100, 100))
                    pygame.draw.lines(equipment_surf, (0, 0, 0), True,
                                      [(0, 0), (0, equipment_height), (equipment_width, equipment_height),
                                       (equipment_width, 0)], 16)
                    pygame.draw.line(equipment_surf, (0, 0, 0), (0, 100), (200, 100), 8)
                    pygame.draw.line(equipment_surf, (0, 0, 0), (0, 200), (200, 200), 8)
                    pygame.draw.line(equipment_surf, (0, 0, 0), (0, 300), (200, 300), 8)
                    pygame.draw.line(equipment_surf, (0, 0, 0), (200, 0), (200, 500), 8)
                    pygame.draw.line(equipment_surf, (0, 0, 0), (100, 0), (100, 300), 8)
                    pygame.draw.rect(equipment_surf, (100, 100, 50), (204, 8, 92, 484))
                    pygame.draw.line(equipment_surf, (0, 0, 0), (300, 0), (300, 500), 8)
                    pygame.draw.line(equipment_surf, (0, 0, 0), (400, 0), (400, 400), 8)
                    pygame.draw.line(equipment_surf, (0, 0, 0), (500, 0), (500, 400), 8)
                    pygame.draw.line(equipment_surf, (0, 0, 0), (600, 0), (600, 400), 8)
                    pygame.draw.line(equipment_surf, (0, 0, 0), (300, 100), (700, 100), 8)
                    pygame.draw.line(equipment_surf, (0, 0, 0), (300, 200), (700, 200), 8)
                    pygame.draw.line(equipment_surf, (0, 0, 0), (300, 300), (700, 300), 8)
                    pygame.draw.line(equipment_surf, (0, 0, 0), (300, 400), (700, 400), 8)

                    # 一些常量
                    close = False
                    mouseClicked = False
                    mouse_position = -1
                    draws = [draw_1,draw_2,draw_3,draw_4,draw_5,draw_6]
                    sell_state = False

                    if len(equipment) > 0:
                        i = 0
                        for equip in equipment:
                            j1 = int(i/4)
                            j2 = i%4
                            rect = pygame.Rect((0,0,60,60))
                            rect.centerx = 300 + 100*j2 + 50
                            rect.centery = 0 + 100*j1 + 50
                            equipment_surf.blit(equipment_image[equip],rect)
                            i += 1


                    for event in pygame.event.get():
                        if event.type == KEYDOWN:
                            if event.key == K_p:
                                close = True
                            if event.key == K_s:
                                sell_state = True



                        if event.type == MOUSEMOTION:
                            mousex, mousey = event.pos
                        elif event.type == MOUSEBUTTONUP:
                            click_mousex, click_mousey = event.pos
                            mouseClicked = True

                    if close == True:
                        break

                    # 绘制装备栏的装饰蓝色边框和物品信息
                    if draw_1 != '' or draw_2 != '' or draw_3 != '' or draw_4 != '' or draw_5 != '' or draw_6 != '':
                        for i in range(6):
                            j1 = int(i / 2)
                            j2 = i%2
                            if (mousex > 100 + 100*j2) and (mousex < 200 + 100*j2) and (mousey > 100 + 100*j1) and (mousey < 200 + 100*j1):
                                if draws[i] != '':
                                    rect = pygame.Rect((0, 0, 70, 70))
                                    rect.centerx = 100 * j2 + 50
                                    rect.centery = 100 * j1 + 50
                                    pygame.draw.rect(equipment_surf, (0, 0, 255), rect, 4)
                                    imformation_surf = basic_FONT.render(equipment_information[draws[i]], 1, (200, 150, 50))
                                    imformation_rect = tishi_surf.get_rect()
                                    imformation_rect.x = 320
                                    imformation_rect.centery = 450
                                    equipment_surf.blit(imformation_surf, imformation_rect)

                    # 绘制物品栏的装饰蓝色边框和物品信息
                    for i in range(len(equipment)):
                        j1 = int(i / 4)
                        j2 = i % 4
                        if (mousex > 400 + 100*j2) and (mousex < 500 + 100*j2) and (mousey > 100 + 100*j1) and (mousey < 200 + 100*j1):
                            # 物品出售金钱
                            if sell_state:
                                if equipment[i] == 'a':
                                    attributes['money'] += 1
                                del equipment[i]
                                continue

                            mouse_position = i
                            hs.decorate_rect(equipment_surf, mouse_position)
                            imformation_surf = basic_FONT.render(equipment_information[equipment[mouse_position]], 1, (200, 150, 50))
                            imformation_rect = tishi_surf.get_rect()
                            imformation_rect.x = 320
                            imformation_rect.centery = 450
                            equipment_surf.blit(imformation_surf,imformation_rect)
                            # 鼠标点击
                            if mouseClicked == True:
                                # 物品如果是装备(6种)
                                # 武器
                                if equipment[mouse_position] in ['a','b','c','d']:
                                    if equipment[mouse_position] == 'a':
                                        yh_attribute[2] += 5
                                    if equipment[mouse_position] == 'b':
                                        yh_attribute[2] += 10
                                    if equipment[mouse_position] == 'c':
                                        yh_attribute[2] += 20
                                    if equipment[mouse_position] == 'd':
                                        yh_attribute[2] += 35
                                    if drawstate_1 == True:
                                        equipment.append(draw_1)
                                        if draw_1 == 'a':
                                            yh_attribute[2] -= 5
                                        if draw_1 == 'b':
                                            yh_attribute[2] -= 10
                                        if draw_1 == 'c':
                                            yh_attribute[2] -= 20
                                        if draw_1 == 'd':
                                            yh_attribute[2] -= 35
                                    if drawstate_1 == False:
                                        drawstate_1 = True
                                    draw_1 = equipment[mouse_position]
                                    del equipment[mouse_position]
                                # 头盔
                                elif equipment[mouse_position] in ['e','f','g','h']:

                                    if equipment[mouse_position] == 'e':
                                        yh_attribute[3] += 1
                                    if equipment[mouse_position] == 'f':
                                        yh_attribute[3] += 2
                                    if equipment[mouse_position] == 'g':
                                        yh_attribute[3] += 10
                                    if drawstate_2 == True:
                                        equipment.append(draw_2)
                                        if draw_2 == 'e':
                                            yh_attribute[3] -= 1
                                        if draw_2 == 'f':
                                            yh_attribute[3] -= 2
                                        if draw_2 == 'g':
                                            yh_attribute[3] -= 10
                                    if drawstate_2 == False:
                                        drawstate_2 = True
                                    draw_2 = equipment[mouse_position]
                                    del equipment[mouse_position]
                                # 护甲
                                elif equipment[mouse_position] in ['i', 'j', 'k', 'l']:
                                    if equipment[mouse_position] == 'i':
                                        yh_attribute[3] += 1
                                    if equipment[mouse_position] == 'j':
                                        yh_attribute[3] += 2
                                    if equipment[mouse_position] == 'k':
                                        yh_attribute[3] += 10
                                    if drawstate_3 == True:
                                        equipment.append(draw_3)
                                        if draw_3 == 'i':
                                            yh_attribute[3] -= 1
                                        if draw_3 == 'j':
                                            yh_attribute[3] -= 2
                                        if draw_3 == 'k':
                                            yh_attribute[3] -= 10
                                    if drawstate_3 == False:
                                        drawstate_3 = True
                                    draw_3 = equipment[mouse_position]
                                    del equipment[mouse_position]
                                # 腰带
                                elif equipment[mouse_position] in ['m', 'n', 'o', 'p']:
                                    if equipment[mouse_position] == 'm':
                                        yh_attribute[3] += 1
                                    if equipment[mouse_position] == 'n':
                                        yh_attribute[3] += 2
                                    if equipment[mouse_position] == 'o':
                                        yh_attribute[3] += 10
                                    if drawstate_4 == True:
                                        equipment.append(draw_4)
                                        if draw_4 == 'm':
                                            yh_attribute[3] -= 1
                                        if draw_4 == 'n':
                                            yh_attribute[3] -= 2
                                        if draw_4 == 'o':
                                            yh_attribute[3] -= 10
                                    if drawstate_4 == False:
                                        drawstate_4 = True
                                    draw_4 = equipment[mouse_position]
                                    del equipment[mouse_position]
                                # 鞋子
                                elif equipment[mouse_position] in ['q', 'r', 's', 't']:
                                    if equipment[mouse_position] == 'q':
                                        yh_attribute[3] += 1
                                    if equipment[mouse_position] == 'r':
                                        yh_attribute[3] += 2
                                    if equipment[mouse_position] == 's':
                                        yh_attribute[3] += 10
                                    if drawstate_5 == True:
                                        equipment.append(draw_5)
                                        if draw_5 == 'q':
                                            yh_attribute[3] -= 1
                                        if draw_5 == 'r':
                                            yh_attribute[3] -= 2
                                        if draw_5 == 's':
                                            yh_attribute[3] -= 10
                                    if drawstate_5 == False:
                                        drawstate_5 = True
                                    draw_5 = equipment[mouse_position]
                                    del equipment[mouse_position]
                                # 项链
                                elif equipment[mouse_position] in ['u', 'v', 'w', 'x']:
                                    if equipment[mouse_position] == 'u':
                                        yh_attribute[3] += 1
                                    if equipment[mouse_position] == 'v':
                                        yh_attribute[3] += 2
                                    if equipment[mouse_position] == 'w':
                                        yh_attribute[3] += 10
                                    if drawstate_6 == True:
                                        equipment.append(draw_6)
                                        if draw_6 == 'u':
                                            yh_attribute[3] -= 1
                                        if draw_6 == 'v':
                                            yh_attribute[3] -= 2
                                        if draw_6 == 'w':
                                            yh_attribute[3] -= 10
                                    if drawstate_6 == False:
                                        drawstate_6 = True
                                    draw_6 = equipment[mouse_position]
                                    del equipment[mouse_position]

                                # 物品如果是道具（消耗品）
                                elif equipment[mouse_position] in ['1', '2', '3', '4','5','6','7']:
                                    # 小血瓶
                                    if equipment[mouse_position] == '1':
                                        if (yh_attribute[1] + 10) <= yh_attribute[6]:
                                            yh_attribute[1] += 10
                                        else:
                                            yh_attribute[1] = yh_attribute[6]
                                    # 中血瓶
                                    if equipment[mouse_position] == '2':
                                        if (yh_attribute[1] + 30) <= yh_attribute[6]:
                                            yh_attribute[1] += 30
                                        else:
                                            yh_attribute[1] = yh_attribute[6]

                                    del equipment[mouse_position]


                    # 穿装备
                    if drawstate_1 == True:
                        rect = pygame.Rect((0, 0, 60, 60))
                        rect.centerx = 50
                        rect.centery = 50
                        equipment_surf.blit(equipment_image[draw_1], rect)
                    if drawstate_2 == True:
                        rect = pygame.Rect((0, 0, 60, 60))
                        rect.centerx = 150
                        rect.centery = 50
                        equipment_surf.blit(equipment_image[draw_2], rect)
                    if drawstate_3 == True:
                        rect = pygame.Rect((0, 0, 60, 60))
                        rect.centerx = 50
                        rect.centery = 150
                        equipment_surf.blit(equipment_image[draw_3], rect)
                    if drawstate_4 == True:
                        rect = pygame.Rect((0, 0, 60, 60))
                        rect.centerx = 150
                        rect.centery = 150
                        equipment_surf.blit(equipment_image[draw_4], rect)
                    if drawstate_5 == True:
                        rect = pygame.Rect((0, 0, 60, 60))
                        rect.centerx = 50
                        rect.centery = 250
                        equipment_surf.blit(equipment_image[draw_5], rect)
                    if drawstate_6 == True:
                        rect = pygame.Rect((0, 0, 60, 60))
                        rect.centerx = 150
                        rect.centery = 250
                        equipment_surf.blit(equipment_image[draw_6], rect)


                    screen.blit(equipment_surf, equipment_rect)
                    pygame.display.update()
                    FPSclock.tick(FPS)



    # 显示“按下空格与人物对话”
    if map[7][layer] != {}:
        for key,value in map[7][layer].items():
            if map[4][layer] not in [[value[0] - 1,value[1]],[value[0] + 1,value[1]],[value[0],value[1] - 1],[value[0],value[1] + 1]]:
                tishi = False
            else:
                tishi = True
                if dialog_TF:
                    if dialog_num < len(dialog[key]):
                        if dialog_num % 2 == 0:
                            dialog_surf = basic_FONT.render(dialog[key][dialog_num],1,(0,0,0))
                            dialog_rect = dialog_surf.get_rect()
                        if dialog_num % 2 == 1:
                            dialog_surf = basic_FONT.render(dialog[key][dialog_num], 1, (255,255,255))
                            dialog_rect = dialog_surf.get_rect()
                            dialog_rect.y = 40
                    else:
                        dialog_TF = False
                        dialog_num = 0
                break


    # 上下楼梯
    if map[4][layer] in map[5][layer]:
        map[4][layer][0] -= 1
        layer += 1
    if map[4][layer] in map[6][layer]:
        map[4][layer][0] += 1
        layer -= 1

    mapsurface = hs.drawmap(map, layer, tiles_image,hero_direction)
    mapsurface_rect = mapsurface.get_rect()
    mapsurface_rect.centerx = screen_width/2 - camerax
    mapsurface_rect.centery = screen_height/2 - cameray
    screen.fill(bg_color)
    screen.blit(mapsurface,mapsurface_rect)
    # 绘制提示语
    if tishi:
        screen.blit(tishi_surf,tishi_rect)
        if dialog_TF:
            screen.blit(dialog_surf,dialog_rect)
    hs.fighting('Z', map, layer, monster_attribute,yh_attribute, screen_width,screen_height, screen,tiles_image,basic_FONT,sys,attributes,equipment,equipment_information2,zhongjia_skill,kongzhi_skill,kuangzhan_skill)
    hs.fighting('X', map, layer, monster_attribute,yh_attribute, screen_width,screen_height, screen, tiles_image, basic_FONT,sys,attributes,equipment,equipment_information2,zhongjia_skill,kongzhi_skill,kuangzhan_skill)
    # 绘制钥匙计数板
    hs.drawkeyscoreboard(yellow_key,green_key,purple_key,red_key,orange_key,colors_key,basic_FONT,screen,tiles_image,yellow_rect,green_rect,purple_rect,red_rect,orange_rect,colors_rect,y_rect,g_rect,p_rect,r_rect,o_rect,c_rect)
    # 绘制金钱计数板
    money_surf = basic_FONT.render('× ' + str(attributes['money']), 1, (200, 150, 50))
    screen.blit(tiles_image['money'],image_rect)
    screen.blit(money_surf,font_rect)

    pygame.display.update()
    FPSclock.tick(FPS)