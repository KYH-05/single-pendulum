import pygame
import numpy as np
import sympy as sy
import time
#----------------------------------------------------
pygame.init()
screen_width = 600
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("P")
clock = pygame.time.Clock()
#----------------------------------------------------
m=float(input("공의 질량(kg):"))
g=9.80665#중력가속도
r=float(input("줄의 길이(m):"))
#r=3.6#부채꼴 반지름(#단위m)
w0=(g/r)**(1/2)
θ0=np.pi/4#최대각이자 처음 시작각
x0=r*θ0
x=sy.symbols('x')
v_t=w0*x0*sy.sin(w0*x)
#print(v_t)
θ=0#이동각
l=0#이동 호 길이
ft=0#시작시간
t=0#현재시간
#----------------------------------------------------
pen_s_x=300
pen_s_y=0
pen_e_x = 0
pen_e_y =0
def draw_line():
  pygame.draw.line(screen, (0, 0, 0), (pen_s_x, pen_s_y), (int(pen_e_x), int(pen_e_y)), 2)
def draw_circle():
  pygame.draw.circle(screen, (0, 0, 0), (int(pen_e_x), int(pen_e_y)), 10, 0)
wall= pygame.Rect(0, 0,600,20)
def draw():
  screen.fill((255,255,255))
  draw_line()
  draw_circle()
#----------------------------------------------------
running = True
ft=time.time()
while running:
  # ----------------------------------------------------
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  # ----------------------------------------------------
  draw()
  draw_circle()
  draw_line()
  # ----------------------------------------------------
  t = time.time() - ft
  l=sy.integrate(v_t, (x, 0, t))
  θ=l/r
  pen_e_x=pen_s_x+sy.sin(θ0-θ)*r*(360/r)#pygame에서 길이 360으로 나타내기 위해
  pen_e_y=pen_s_y + sy.cos(θ0-θ) *r*(360/r)
  # ----------------------------------------------------
  v=v_t.subs({x:t})
  font = pygame.font.SysFont("arialrounded",10)
  text=font.render("V:"+str(round(v,3)),True,(0,0,0))
  screen.blit(text,(550,480))
  # ----------------------------------------------------
  Ek=(1/2)*m*(v**2)
  font = pygame.font.SysFont("arialrounded",10)
  text1=font.render("Ek:"+str(round(Ek,3)),True,(0,0,0))
  screen.blit(text1,(480,480))
  # ----------------------------------------------------
  Ep = m * g * abs((r) - (pen_e_y * r / 360))
  font = pygame.font.SysFont("arialrounded",10)
  text2=font.render("Ep:"+str(round(Ep,3)),True,(0,0,0))
  screen.blit(text2,(410,480))
  # ----------------------------------------------------
  Et=Ep+Ek
  font = pygame.font.SysFont("arialrounded",10)
  text3=font.render("Et:"+str(round(Ep+Ek,3)),True,(0,0,0))
  screen.blit(text3,(340,480))
  # ----------------------------------------------------
  pygame.display.update()
  clock.tick(60)
#----------------------------------------------------
