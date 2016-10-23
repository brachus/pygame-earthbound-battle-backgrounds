

import main
import pygame
import random
import numpy
import cProfile


#56 9   72 43


pygame.display.init()
pygame.font.init()

font = pygame.font.Font('ttf/determinationmonoweb-webfont.ttf', 12)

smul=2
fps=30
i = pygame.display.Info()
sc_size = [i.current_w, i.current_h]

fsiz=(sc_size[0],sc_size[1])




a=main.Rom()
a.open('bgs.dat')

#tmp = vars(a)
#for x in tmp:
	#if x!='rom_dat':
		#print x,':', tmp[x]


layer_a = main.BGLayer(a, 2)
layer_b = main.BGLayer(a, 4)


def get_rand_default():
	tmp = random.choice(main.bg_defaults.keys())
	return main.bg_defaults[tmp]

def get_sel_default(idx):
	idx%=len(main.bg_defaults.keys())
	tmp = main.bg_defaults.keys()[idx]
	return main.bg_defaults[tmp]

def get_sel_default_name(idx):
	idx%=len(main.bg_defaults.keys())
	tmp = main.bg_defaults.keys()[idx]
	return tmp

winsurf = pygame.display.set_mode((256*smul,256*smul))
s = pygame.Surface((256,256))
s_b = pygame.Surface((256,256))

bmp2=numpy.array([100]*256*256*4,dtype=int)

			
tmp = get_sel_default(0)
layer_a = main.BGLayer(a, tmp[0])
layer_b = main.BGLayer(a, tmp[1])

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
tmsg='r-random s/p separate/predef mode\nuse left/right (a & \nd for layer 2 in separate) to change'
tcnt=fps*3

bmd='reg'

pygame.key.set_repeat(400,fps/2)

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
					sel = random.randint(0,len(main.bg_defaults.keys())-1)
					switch=True
				
			if e.key == pygame.K_p:
				sw='def'
				tmsg='predefines'
				tcnt=fps*1
				
			if e.key == pygame.K_s:
				sw='sep'
				tmsg='separate'
				tcnt=fps*1
			
			if e.key==pygame.K_f:
				if isfull:
					winsurf = pygame.display.set_mode((256*smul,256*smul))
					isfull=False
				else:
					winsurf = pygame.display.set_mode(fsiz,pygame.FULLSCREEN)
					isfull=True
			
			if e.key==pygame.K_l:
				if letterbox==0:
					letterbox=16
				elif letterbox==16:
					letterbox=24
				else:
					letterbox=0
			
			if e.key==pygame.K_b:
				if bmd=='reg':
					bmd='add'
				else:
					bmd='reg'

			
			if sw=='def':
				if sel<0:sel=len(main.bg_defaults.keys())-1
				sel%=len(main.bg_defaults.keys())
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
		tmpy=200
		for x in tmsg.split('\n'):
			ttmp = font.render(x, True, (255,255,255))
			s.blit(ttmp, [10,tmpy])
			tmpy+=16
	
	if isfull:
		winsurf.blit( pygame.transform.scale(s, fsiz), [0,0] )
	else:
		winsurf.blit( pygame.transform.scale(s, (256*smul, 256*smul)), [0,0] )
	
	pygame.display.flip()
	clock.tick(fps)
	tick+=1
	tcnt-=1
