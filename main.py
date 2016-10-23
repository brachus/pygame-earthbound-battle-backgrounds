

import kraken
import pygame
import random
import numpy
import cProfile
import textwrap


#56 9   72 43


pygame.display.init()
pygame.font.init()

font = pygame.font.Font('ttf/gohufont-11.ttf', 11)

smul=1
fps=30
ssiz=[256,224]

i = pygame.display.Info()
sc_size = [i.current_w, i.current_h]

fsiz=(sc_size[0],sc_size[1])




a=kraken.Rom()
a.open('bg/bgs.dat')


def get_rand_default():
	tmp = random.choice(kraken.bg_defaults.keys())
	return kraken.bg_defaults[tmp]

def get_sel_default(idx):
	idx%=len(kraken.bg_defaults.keys())
	tmp = kraken.bg_defaults.keys()[idx]
	return kraken.bg_defaults[tmp]

def get_sel_default_name(idx):
	idx%=len(kraken.bg_defaults.keys())
	tmp = kraken.bg_defaults.keys()[idx]
	return tmp

winsurf = pygame.display.set_mode((256*smul,224*smul))
s = pygame.Surface((256,224))
s_b = pygame.Surface((256,224))

			
tmp = get_sel_default(0)
layer_a = kraken.BGLayer(a, tmp[0])
layer_b = kraken.BGLayer(a, tmp[1])

letterbox=32

def kraken_frame(s,tick,blendmd='add'):
	
	s.fill((0,0,0,0))
	
	
	if get_sel_default(sel)[1] != 0:
	
		bmp = layer_a.overlay_frame(None, letterbox, tick, 1, True)
		bmp1 = layer_b.overlay_frame(None, letterbox, tick, 1, False	)
		
		
		s.get_buffer().write(numpy.array(bmp),0	)
		s_b.get_buffer().write(numpy.array(bmp1),0)

		s_b.set_alpha(128)
		
		s.unlock()
		s_b.unlock()
		
		if blendmd=='add':
			s.blit(s_b,(0,0),None,pygame.BLEND_RGB_ADD)
		else:
			s.blit(s_b,(0,0),None)
	
	else:
		bmp = layer_a.overlay_frame(None, letterbox, tick, 1, True)
		s.get_buffer().write(numpy.array(bmp),0	)
	
	
		
	


sel=0
sw='def'
tmp=[0,0]

isfull=False

clock = pygame.time.Clock()

tick=0
tmsg='''<- ->  Choose preset/change layer 1.

a, d   Change layer 2.

r      Random preset

p      Preset Mode

s      Separate Mode

l      Toggle letterbox

f      Fullscreen

b      Toggle blend mode
         (alpha/add)

Esc    Quit

(Preset Mode)'''
tcnt=fps*8

bmd='reg'

pygame.key.set_repeat(200,fps/2)

run=True

while (run):
	
	switch=False
	
	for e in pygame.event.get():
		if   e.type == pygame.QUIT:
			run=False
		elif e.type == pygame.KEYDOWN:
			
			if e.key == pygame.K_LEFT:
				if sw=='def':
					sel-=1
				else:
					tmp[0]-=1
				switch=True
				
			if e.key == pygame.K_RIGHT:
				if sw=='def':
					sel+=1
				else:
					tmp[0]+=1
				switch=True
			
			if e.key==pygame.K_a:
				if sw=='sep':
					tmp[1]-=1
				switch=True
				
			
				
			if e.key==pygame.K_d:
				if sw=='sep':
					tmp[1]+=1
				switch=True
			
			if e.key == pygame.K_r:
				if sw=='def':
					sel = random.randint(0,len(kraken.bg_defaults.keys())-1)
					switch=True
				
			if e.key == pygame.K_p:
				sw='def'
				tmsg='Preset mode'
				tcnt=fps*1
				
			if e.key == pygame.K_s:
				sw='sep'
				tmsg='Separate mode'
				tcnt=fps*1
			
			if e.key==pygame.K_f:
				if isfull:
					winsurf = pygame.display.set_mode((ssiz[0]*smul,ssiz[1]*smul))
					isfull=False
				else:
					winsurf = pygame.display.set_mode(fsiz,pygame.FULLSCREEN)
					isfull=True
			
			if e.key==pygame.K_l:
				if letterbox==0:
					letterbox=16
				elif letterbox==16:
					letterbox=24
				elif letterbox==24:
					letterbox=32
				elif letterbox==32:
					letterbox=48
				else:
					letterbox=0
			
			if e.key==pygame.K_b:
				if bmd=='reg':
					bmd='add'
					tmsg='Blend add'
					tcnt=fps*1
				else:
					bmd='reg'
					tmsg='Blend alpha'
					tcnt=fps*1

			
			if sw=='def':
				if sel<0:sel=len(kraken.bg_defaults.keys())-1
				sel%=len(kraken.bg_defaults.keys())
				tmp = get_sel_default(sel)
			elif sw=='sep':
				if tmp[0]<0:tmp[0]=326
				tmp[0]%=327
				
				if tmp[1]<0:tmp[1]=326
				tmp[1]%=327
			
			if e.key == pygame.K_ESCAPE:
				run=False
	
	if switch:
		tick=0
		layer_a.load(tmp[0])
		layer_b.load(tmp[1])
		if sw=='def':
			print get_sel_default_name(sel)
			tmsg=get_sel_default_name(sel)
			tcnt=fps*3
		else:
			print tmp[0],tmp[1]
			tmsg='layer 1 %d, layer 2 %d' % (tmp[0] , tmp[1])
			tcnt=fps*3
	
	#cProfile.run("kraken_frame(s, tick)")
	kraken_frame(s, tick, bmd)
	
	
	
	
	
	if tcnt>0:
		if tmsg.count('\n')==0:
			tmsg = textwrap.fill(tmsg,35)+'\n'
		s.fill((128,128,128),((4,4),(248,tmsg.count('\n') * 11 + 4)),pygame.BLEND_MULT)
		tmpy=4
		for x in tmsg.split('\n'):
			ttmp = font.render(x, True, (0,0,255))
			s.blit(ttmp, [9,tmpy])
			ttmp = font.render(x, True, (255,255,255))
			s.blit(ttmp, [10,tmpy])
			mp = font.render(x, True, (255,255,255))
			s.blit(ttmp, [11,tmpy])
			tmpy+=10
	
	if isfull:
		winsurf.blit( pygame.transform.scale(s, fsiz), [0,0] )
	else:
		winsurf.blit( pygame.transform.scale(s, (ssiz[0]*smul, ssiz[1]*smul)), [0,0] )
	
	pygame.display.flip()
	clock.tick(fps)
	tick+=1
	tcnt-=1
