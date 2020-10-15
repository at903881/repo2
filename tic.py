import pygame
pygame.init()
def line(winh,winw):
     for j in range(0,winw,int(winh/3)):
        pygame.draw.line(win,(0,0,0),[0,j],[300,j],1)
     for i in range(0, winh, int(winh / 3)):
        pygame.draw.line(win,(0,0,0),[i,0],[i,300],1)
def drawo(x,y):
    x1=x-int(x%100)
    y1=y-int(y%100)
    cx=x1+50
    cy=y1+50
    pygame.draw.circle(win,(60,78,100),[cx,cy],40,5)
def drawx(x,y):
    x1 = x - int(x % 100)
    y1 = y - int(y % 100)
    cx = x1 + 50
    cy = y1 + 50
    pygame.draw.line(win,(0,90,70),[cx-40,cy+40],[cx+40,cy-40],5)
    pygame.draw.line(win,(0,90,70),[cx-40,cy-40],[cx+40,cy+40],5)
r=True
winh=301
winw=301
mouse=0
pos=[]
win=pygame.display.set_mode((winw,winh+20))
pygame.display.set_caption("TicTacToe")
while r:
    t=False
    do = []
    dx = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            r = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos.append(pygame.mouse.get_pos())
            mouse+=1


    win.fill((255,255,255))
    line(winh,winw)
    for i in range(0,mouse):
        #print(pos[i][0],pos[i][1])
        if i%2==0:
            drawx(pos[i][0],pos[i][1])
            if pos[i][0]<int(winw/3) and pos[i][0]>0:
                if pos[i][1]>0 and pos[i][1]<int(winh/3):
                    dx.append(1)
                if pos[i][1]>int(winh/3) and pos[i][1]<2*int(winh/3):
                    dx.append(2)
                if pos[i][1]>2*int(winh/3) and pos[i][1]<3*int(winh/3):
                    dx.append(3)
            if pos[i][0]<2*int(winw/3) and pos[i][0]>int(winh/3):
                if pos[i][1]>0 and pos[i][1]<int(winh/3):
                    dx.append(4)
                if pos[i][1]>int(winh/3) and pos[i][1]<2*int(winh/3):
                    dx.append(5)
                if pos[i][1]>2*int(winh/3) and pos[i][1]<3*int(winh/3):
                    dx.append(6)
            if pos[i][0]<3*int(winw/3) and pos[i][0]>2*int(winh/3):
                if pos[i][1]>0 and pos[i][1]<int(winh/3):
                    dx.append(7)
                if pos[i][1]>int(winh/3) and pos[i][1]<2*int(winh/3):
                    dx.append(8)
                if pos[i][1]>2*int(winh/3) and pos[i][1]<3*int(winh/3):
                    dx.append(9)
           # print(dx)
        else:
            drawo(pos[i][0],pos[i][1])
            if pos[i][0]<int(winw/3) and pos[i][0]>0:
                if pos[i][1]>0 and pos[i][1]<int(winh/3):
                    do.append(1)
                if pos[i][1]>int(winh/3) and pos[i][1]<2*int(winh/3):
                    do.append(2)
                if pos[i][1]>2*int(winh/3) and pos[i][1]<3*int(winh/3):
                    do.append(3)
            if pos[i][0]<2*int(winw/3) and pos[i][0]>int(winh/3):
                if pos[i][1]>0 and pos[i][1]<int(winh/3):
                    do.append(4)
                if pos[i][1]>int(winh/3) and pos[i][1]<2*int(winh/3):
                    do.append(5)
                if pos[i][1]>2*int(winh/3) and pos[i][1]<3*int(winh/3):
                    do.append(6)
            if pos[i][0]<3*int(winw/3) and pos[i][0]>2*int(winh/3):
                if pos[i][1]>0 and pos[i][1]<int(winh/3):
                    do.append(7)
                if pos[i][1]>int(winh/3) and pos[i][1]<2*int(winh/3):
                    do.append(8)
                if pos[i][1]>2*int(winh/3) and pos[i][1]<3*int(winh/3):
                    do.append(9)
    if ((1 in do) and (4 in do) and (7 in do)) or ((1 in do) and (2 in do) and (3 in do)) or ((3 in do) and (6 in do) and (9 in do)) or ((7 in do) and (8 in do) and (9 in do)) or ((1 in do) and (5 in do) and (9 in do)) or ((3 in do) and (5 in do) and (7 in do)) or ((4 in do) and (5 in do) and (6 in do)) or ((2 in do) and (5 in do) and (8 in do)):
        win.fill((150,40,70))
        pygame.draw.circle(win, (60, 78, 100), [int(winw/2), int(winw/2)], 100, 20)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            pos.clear()
            mouse=0
    elif ((1 in dx) and (4 in dx) and (7 in dx)) or ((1 in dx) and (2 in dx) and (3 in dx)) or ((3 in dx) and (6 in dx) and (9 in dx)) or ((7 in dx) and (8 in dx) and (9 in dx)) or ((1 in dx) and (5 in dx) and (9 in dx)) or ((3 in dx) and (5 in dx) and (7 in dx)) or ((4 in dx) and (5 in dx) and (6 in dx)) or ((2 in dx) and (5 in dx) and (8 in dx)):
        win.fill((200,40,70))
        pygame.draw.line(win, (0, 90, 70), [20, 20], [280, 280], 20)
        pygame.draw.line(win, (0, 90, 70), [20,280], [280, 20], 20)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            pos.clear()
            mouse=0
    pygame.display.update()
pygame.quit()
