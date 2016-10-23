
import struct
import math
import pygame
import copy


bg_defaults = { "Coil Snake (306 / 307)": [306, 307],
  "Runaway Dog (260 / 0)": [260, 0],
  "Skate Punk, Pogo Punk (6 / 0)": [6, 0],
  "Skate Punk, Yes Man Junior (5 / 0)": [5, 0],
  "Skate Punk, Yes Man Junior, Pogo Punk (8 / 0)": [8, 0],
  "Pogo Punk, Yes Man Junior (7 / 0)": [7, 0],
  "Runaway Dog, Cop (1 / 0)": [1, 0],
  "Attack Slug (75 / 0)": [75, 0],
  "Rowdy Mouse, Attack Slug (72 / 0)": [72, 0],
  "Black Antoid, Attack Slug (81 / 0)": [81, 0],
  "Black Antoid, Rowdy Mouse (80 / 0)": [80, 0],
  "Frank (180 / 179)": [180, 179],
  "Rowdy Mouse (217 / 216)": [217, 216],
  "Starman Junior (219 / 218)": [219, 218],
  "Black Antoid (79 / 0)": [79, 0],
  "Black Antoid (9 / 0)": [9, 0],
  "Black Antoid, Ramblin' Evil Mushroom (10 / 0)": [10, 0],
  "Cop (184 / 183)": [184, 183],
  "Frankystein Mark II (182 / 181)": [182, 181],
  "Gruff Goat (122 / 0)": [122, 0],
  "Gruff Goat (127 / 0)": [127, 0],
  "Ramblin' Evil Mushroom (12 / 0)": [12, 0],
  "Worthless Protoplasm (156 / 0)": [156, 0],
  "Worthless Protoplasm (215 / 214)": [215, 214],
  "Cranky Lady (14 / 0)": [14, 0],
  "Mad Duck (213 / 212)": [213, 212],
  "Mad Duck (33 / 0)": [33, 0],
  "Mobile Sprout, Ramblin' Evil Mushroom (212 / 213)": [212, 213],
  "Unassuming Local Guy (269 / 270)": [269, 270],
  "Unassuming Local Guy (307 / 306)": [307, 306],
  "Titanic Ant, Black Antoid (170 / 169)": [170, 169],
  "Cave Boy (314 / 0)": [314, 0],
  "Mobile Sprout, Li'l UFO (21 / 0)": [21, 0],
  "Li'l UFO (20 / 0)": [20, 0],
  "Mobile Sprout, Territorial Oak (11 / 0)": [11, 0],
  "Insane Cultist (16 / 0)": [16, 0],
  "Red Antoid, Black Antoid (317 / 0)": [317, 0],
  "Mole Playing Rough (82 / 0)": [82, 0],
  "Spinning Robo (22 / 0)": [22, 0],
  "Everdred (273 / 272)": [273, 272],
  "Mr. Batty (89 / 0)": [89, 0],
  "Foppy (274 / 275)": [274, 275],
  "Foppy (276 / 277)": [276, 277],
  "Handsome Tom (25 / 0)": [25, 0],
  "Mighty Bear (76 / 0)": [76, 0],
  "Trick or Trick Kid, Handsome Tom (3 / 0)": [3, 0],
  "Zombie Possessor (152 / 0)": [152, 0],
  "Handsome Tom, Smilin' Sam (15 / 0)": [15, 0],
  "Mad Duck, Thirsty Coil Snake (137 / 0)": [137, 0],
  "No Good Fly, Putrid Moldyman (28 / 0)": [28, 0],
  "Violent Roach (186 / 185)": [186, 185],
  "Violent Roach (34 / 0)": [34, 0],
  "Zombie Dog, No Good Fly (154 / 0)": [154, 0],
  "Zombie Possessor, Urban Zombie (26 / 0)": [26, 0],
  "Farm Zombie (281 / 282)": [281, 282],
  "Mostly Bad Fly (280 / 0)": [280, 0],
  "Struttin' Evil Mushroom, Tough Mobile Sprout (134 / 0)": [134, 0],
  "Urban Zombie (27 / 0)": [27, 0],
  "Armored Frog, Farm Zombie (30 / 0)": [30, 0],
  "Red Antoid, Armored Frog, Farm Zombie (32 / 0)": [32, 0],
  "Urban Zombie, Zombie Dog (153 / 0)": [153, 0],
  "Mr. Carpainter (278 / 0)": [278, 0],
  "Armored Frog (316 / 0)": [316, 0],
  "Plain Crocodile, Red Antoid (31 / 0)": [31, 0],
  "Tough Mobile Sprout, Ranboob (133 / 0)": [133, 0],
  "Zombie Dog (29 / 0)": [29, 0],
  "Criminal Caterpillar (266 / 267)": [266, 267],
  "Mondo Mole (172 / 171)": [172, 171],
  "Scalding Coffee Cup, Mystical Record, Worthless Protoplasm (159 / 0)": [159, 0],
  "Ranboob (132 / 0)": [132, 0],
  "Ranboob (135 / 0)": [135, 0],
  "Slimy Little Pile (192 / 191)": [192, 191],
  "Boogey Tent (293 / 292)": [293, 292],
  "Skelpion, Cute Li'l UFO (259 / 0)": [259, 0],
  "Skelpion, Smilin' Sphere (318 / 0)": [318, 0],
  "Trillionage Sprout, Tough Mobile Sprout (174 / 173)": [174, 173],
  "Cave Boy, Mighty Bear Seven (131 / 0)": [131, 0],
  "Crested Booka, Cute Li'l UFO, Smilin' Sphere (319 / 0)": [319, 0],
  "Cute Li'l UFO (155 / 0)": [155, 0],
  "Extra Cranky Lady (39 / 0)": [39, 0],
  "Master Belch (194 / 193)": [194, 193],
  "Spiteful Crow (123 / 0)": [123, 0],
  "Spiteful Crow (126 / 0)": [126, 0],
  "Spiteful Crow (262 / 0)": [262, 0],
  "Mad Taxi (203 / 202)": [203, 202],
  "Mad Taxi (41 / 0)": [41, 0],
  "Mad Taxi (83 / 0)": [83, 0],
  "Thirsty Coil Snake (136 / 0)": [136, 0],
  "Desert Wolf (38 / 0)": [38, 0],
  "Gigantic Ant (138 / 0)": [138, 0],
  "Gigantic Ant (139 / 0)": [139, 0],
  "Annoying Reveler (42 / 0)": [42, 0],
  "Crested Booka, Bad Buffalo (36 / 0)": [36, 0],
  "Scalding Coffee Cup, Mystical Record (84 / 0)": [84, 0],
  "Scalding Coffee Cup, Mystical Record (87 / 0)": [87, 0],
  "Arachnid! (78 / 0)": [78, 0],
  "Bad Buffalo, Desert Wolf (35 / 0)": [35, 0],
  "Enraged Fire Plug (162 / 0)": [162, 0],
  "Enraged Fire Plug (189 / 0)": [189, 0],
  "Enraged Fire Plug (320 / 0)": [320, 0],
  "Guardian Digger (196 / 0)": [196, 0],
  "Elder Batty, Arachnid! (73 / 0)": [73, 0],
  "Crazed Sign (40 / 0)": [40, 0],
  "Crazed Sign (48 / 0)": [48, 0],
  "Dali's Clock (158 / 0)": [158, 0],
  "Dali's Clock (43 / 0)": [43, 0],
  "Musica, Mystical Record (85 / 0)": [85, 0],
  "Musica, Mystical Record (86 / 0)": [86, 0],
  "Robo-pump, Enraged Fire Plug (288 / 0)": [288, 0],
  "Robo-pump, Enraged Fire Plug (45 / 258)": [45, 258],
  "Abstract Art (44 / 0)": [44, 0],
  "Over Zealous Cop, Tough Guy (49 / 0)": [49, 0],
  "Robo-pump (157 / 0)": [157, 0],
  "Master Criminal Worm (190 / 326)": [190, 326],
  "Strong Crocodile, Arachnid! (74 / 0)": [74, 0],
  "Tough Guy (46 / 0)": [46, 0],
  "Lesser Mook (161 / 0)": [161, 0],
  "Lesser Mook, Whirling Robo (125 / 0)": [125, 0],
  "Lesser Mook, Whirling Robo (315 / 0)": [315, 0],
  "Lesser Mook, Wooly Shambler (313 / 0)": [313, 0],
  "Pit Bull Slug (61 / 0)": [61, 0],
  "Sentry Robot (284 / 0)": [284, 0],
  "Wooly Shambler, Whirling Robo (130 / 0)": [130, 0],
  "Deadly Mouse, Stinky Ghost (143 / 0)": [143, 0],
  "Dept. Store Spook (197 / 0)": [197, 0],
  "Filthy Attack Roach (140 / 0)": [140, 0],
  "Filthy Attack Roach (141 / 0)": [141, 0],
  "Thunder Mite (51 / 0)": [51, 0],
  "Beautiful UFO (54 / 0)": [54, 0],
  "Arachnid!!! (95 / 0)": [95, 0],
  "Dread Skelpion, Great Crested Booka (56 / 0)": [56, 0],
  "Evil Mani-Mani (302 / 0)": [302, 0],
  "High-class UFO, Beautiful UFO (53 / 0)": [53, 0],
  "Thunder Mite, Tangoo (304 / 0)": [304, 0],
  "Clumsy Robot (285 / 0)": [285, 0],
  "Kiss of Death (144 / 0)": [144, 0],
  "Lethal Asp Hieroglyph (99 / 0)": [99, 0],
  "Stinky Ghost (142 / 0)": [142, 0],
  "Fierce Shattered Man, Arachnid!!! (96 / 0)": [96, 0],
  "High-class UFO (321 / 0)": [321, 0],
  "Plague Rat of Doom (178 / 177)": [178, 177],
  "Even Slimier Little Pile, Zap Eel (62 / 0)": [62, 0],
  "Fobby (289 / 0)": [289, 0],
  "Fobby (290 / 0)": [290, 0],
  "Fobby (291 / 0)": [291, 0],
  "Fobby (312 / 0)": [312, 0],
  "Manly Fish, Hard Crocodile (63 / 0)": [63, 0],
  "Shrooom! (168 / 167)": [168, 167],
  "Tangoo (146 / 0)": [146, 0],
  "Tangoo (305 / 0)": [305, 0],
  "Great Crested Booka (52 / 0)": [52, 0],
  "Marauder Octobot (55 / 0)": [55, 0],
  "Demonic Petunia (59 / 0)": [59, 0],
  "Fierce Shattered Man (294 / 0)": [294, 0],
  "Fierce Shattered Man (98 / 0)": [98, 0],
  "Fierce Shattered Man, Petrified Royal Guard (97 / 0)": [97, 0],
  "Shattered Man (195 / 0)": [195, 0],
  "Zap Eel, Hard Crocodile (60 / 0)": [60, 0],
  "Conducting Menace (145 / 0)": [145, 0],
  "Hyper Spinning Robo, Fobby (102 / 0)": [102, 0],
  "Uncontrollable Sphere, Fobby (100 / 0)": [100, 0],
  "Kraken (201 / 200)": [201, 200],
  "Mook Senior (151 / 0)": [151, 0],
  "Mook Senior (160 / 0)": [160, 0],
  "Mook Senior (198 / 0)": [198, 0],
  "Mook Senior (324 / 0)": [324, 0],
  "Atomic Power Robot, Starman (243 / 0)": [243, 0],
  "Guardian General (208 / 0)": [208, 0],
  "Starman (271 / 0)": [271, 0],
  "Starman (283 / 0)": [283, 0],
  "Starman, Starman Super (148 / 0)": [148, 0],
  "Mr. Molecule (68 / 0)": [68, 0],
  "Starman Super, Atomic Power Robot (286 / 0)": [286, 0],
  "Thunder and Storm (176 / 175)": [176, 175],
  "Uncontrollable Sphere (311 / 0)": [311, 0],
  "Big Pile of Puke (58 / 0)": [58, 0],
  "Evil Elemental (104 / 0)": [104, 0],
  "Evil Elemental, Psychic Psycho (325 / 0)": [325, 0],
  "Hyper Spinning Robo, Conducting Spirit (310 / 0)": [310, 0],
  "Uncontrollable Sphere, Conducting Spirit (309 / 0)": [309, 0],
  "Atomic Power Robot, Military Octobot (287 / 0)": [287, 0],
  "Care Free Bomb, Mr. Molecule (71 / 0)": [71, 0],
  "Ego Orb (66 / 0)": [66, 0],
  "Evil Elemental, Soul Consuming Flame (299 / 0)": [299, 0],
  "Psychic Psycho (303 / 0)": [303, 0],
  "Conducting Spirit (103 / 0)": [103, 0],
  "Hostile Elder Oak (57 / 0)": [57, 0],
  "Loaded Dice (323 / 0)": [323, 0],
  "Loaded Dice (67 / 0)": [67, 0],
  "Soul Consuming Flame (106 / 0)": [106, 0],
  "Wetnosaur (64 / 0)": [64, 0],
  "Care Free Bomb (322 / 0)": [322, 0],
  "Master Barf (211 / 210)": [211, 210],
  "Psychic Psycho, Major Psychic Psycho (105 / 0)": [105, 0],
  "Chomposaur (65 / 0)": [65, 0],
  "Electro Swoosh (268 / 0)": [268, 0],
  "Evil Eye, Mechanical Octobot (116 / 0)": [116, 0],
  "Ghost of Starman, Evil Eye (114 / 0)": [114, 0],
  "Ghost of Starman, Mechanical Octobot, Evil Eye (117 / 0)": [117, 0],
  "Starman Deluxe (199 / 0)": [199, 0],
  "Ghost of Starman, Nuclear Reactor Robot (107 / 0)": [107, 0],
  "Ghost of Starman, Nuclear Reactor Robot (297 / 0)": [297, 0],
  "Electro Specter (164 / 163)": [164, 163],
  "Ghost of Starman, Final Starman, Nuclear Reactor Robot (301 / 0)": [301, 0],
  "Ghost of Starman, Mechanical Octobot (115 / 0)": [115, 0],
  "Nuclear Reactor Robot, Final Starman (110 / 0)": [110, 0],
  "Ultimate Octobot, Nuclear Reactor Robot (209 / 0)": [209, 0],
  "Wild 'n Wooly Shambler, Ultimate Octobot (111 / 0)": [111, 0],
  "Ghost of Starman, Final Starman (300 / 0)": [300, 0],
  "Squatter Demon (296 / 0)": [296, 0],
  "Bionic Kraken (109 / 0)": [109, 0],
  "Carbon Dog (166 / 165)": [166, 165],
  "French Kiss of Death (70 / 0)": [70, 0],
  "Ness's Nightmare (298 / 0)": [298, 0],
  "Giygas, Heavily Armed Pokey (220 / 0)": [220, 0],
  "Giygas, Heavily Armed Pokey (222 / 221)": [222, 221],
  "Giygas (224 / 223)": [224, 223],
  "Giygas (225 / 0)": [225, 0],
  "Giygas (226 / 0)": [226, 0],
  "Giygas (227 / 0)": [227, 0],
  "Giygas (265 / 0)": [265, 0]
}

class Distorter:
	def __init__(self):
		self.src = None
		self.dist = [{ 'ampl':0,
					's_freq':0,
					'ampl_acc':0,
					's_freq_acc':0,
					'start':0,
					'speed':0,
					'comp':0,
					'comp_acc':0,
					'type':0 }]*4 # 0=invalid, 1=horiz, 2=horiz-interlaced, 3=vert
					
		self.dist_cur=0
		
		self.c1 = float('%.6f' % (1/512.0))
		self.c2 = float('%.6f' % (8.0 * math.pi / (1024 * 256)))
		self.c3 = float('%.6f' % (math.pi / 60.0))
		
		
		
	def compute_frame(self, dst,src,effect,letterbox,ticks,alpha,erase,ampl,ampl_acc,freq,freqacc,comp,compacc,speed):
		
		bdst = dst
		bsrc = src
		
		bdst=''

		#// TODO: hardcoding is bad.
		stride = 1024

		#/*
			#Given the list of 4 distortions and the tick count, decide which
			#effect to use:

			#Basically, we have 4 effects, each possibly with a duration.

			#Evaluation order is: 1, 2, 3, 0

			#If the first effect is null, control transitions to the second effect.
			#If the first and second effects are null, no effect occurs.
			#If any other effect is null, the sequence is truncated.
			#If a non-null effect has a zero duration, it will not be switched
			#away from.

			#Essentially, this configuration sets up a precise and repeating
			#sequence of between 0 and 4 different distortion effects. Once we
			#compute the sequence, computing the particular frame of which distortion
			#to use becomes easy; simply mod the tick count by the total duration
			#of the effects that are used in the sequence, then check the remainder
			#against the cumulative durations of each effect.

			#I guess the trick is to be sure that my description above is correct.

			#Heh.
		#*/

		x = 0
		y = 0

		while y < 256:
			s = self.get_applied_offset(y, ticks, effect, ampl, ampl_acc, freq, freqacc, comp, compacc, speed);
			l=y

			if effect==3:
				l=s
				
			if letterbox!=0 and (y<letterbox or y>224-letterbox):
			
				x=0
				while x < 256:
					bdst += '\x00\x00\x00\x00'
					x+=1
			
			else:
				
				xto=256
				xfro=0
				
				
				if effect == 1 or effect == 2:
					dx = (x + s) % 256;
					if (dx < 0):
						dx = 256 + dx
					if (dx > 255):
						dx = 256 - dx
					x=xfro
					while x < xto:
						t=(256*l)+(dx)
						bdst += bsrc[t]
						#bdst += bsrc[t+1]
						#bdst += bsrc[t+2]
						#bdst += bsrc[t+3]#'\x00\x00\x00\x00'
						
						dx=(dx+1)%256
						x+=1
				else:
					x=xfro
					while x < xto:
						t=(256*l)+(x)
						bdst += bsrc[t]
						#t=(256*l*4)+(x*4)
						#bdst += bsrc[t]
						#bdst += bsrc[t+1]
						#bdst += bsrc[t+2]
						#bdst += bsrc[t+3]#'\x00\x00\x00\x00'
						
						x+=1
			y+=1
			continue
		
		return bdst
			
			#x=0
			#while x < 256:
				##bpos = x * 4 + y * stride;
				#if y < letterbox or y > 224 - letterbox:
					##bdst[bpos + 2 ] = 0;
					##bdst[bpos + 1 ] = 0;
					##bdst[bpos + 0 ] = 0;
					#bdst[x][y] = [0,0,0]
					#x+=1
					#continue
				
				#dx = x

				#if effect == 1 or effect==2:
					#dx = (x + s) % 256;
					#if (dx < 0):
						#dx = 256 + dx
					#if (dx > 255):
						#dx = 256 - dx
				
				##spos = dx * 4 + l * stride

				##// Either copy or add to the destination bitmap
				#if erase:
					##bdst[bpos + 3 ] = 255;
					##bdst[bpos + 2 ] = int(alpha * bsrc[spos + 2 ])
					##bdst[bpos + 1 ] = int(alpha * bsrc[spos + 1 ])
					##bdst[bpos + 0 ] = int(alpha * bsrc[spos + 0 ])
					
					##bdst[x][y][0] = int(alpha*bsrc[dx][l][0])
					##bdst[x][y][1] = int(alpha*bsrc[dx][l][1])
					##bdst[x][y][2] = int(alpha*bsrc[dx][l][2])
					
					
					#bdst[x][y] = bsrc[dx][l]
				#else:
					##bdst[bpos + 3 ] = 255;
					##bdst[bpos + 2 ] += int(alpha * bsrc[spos + 2 ])
					##bdst[bpos + 1 ] += int(alpha * bsrc[spos + 1 ])
					##bdst[bpos + 0 ] += int(alpha * bsrc[spos + 0 ])
					
					##bdst[x][y][0] += int(alpha*bsrc[dx][l][0])
					##bdst[x][y][1] += int(alpha*bsrc[dx][l][1])
					##bdst[x][y][2] += int(alpha*bsrc[dx][l][2])
					
					#bdst[x][y] = bsrc[dx][l]
					
				#x+=1
			#y+=1
					
					#if bdst[bpos + 2 ] > 255:
						#bdst[bpos + 2 ] = 255
					#if bdst[bpos + 2 ] < 0:
						#bdst[bpos + 2 ] = 0
					
					#if bdst[bpos + 1 ] > 255:
						#bdst[bpos + 1 ] = 255
					#if bdst[bpos + 1 ] < 0:
						#bdst[bpos + 1 ] = 0
					
					#if bdst[bpos + 0 ] > 255:
						#bdst[bpos + 0 ] = 255
					#if bdst[bpos + 0 ] < 0:
						#bdst[bpos + 0 ] = 0

		#return bdst;
		
		#public void OverlayFrame(Bitmap dst, int letterbox, int ticks, float alpha,
				#boolean erase) {
			#final int e = erase ? 1 : 0;
			#ComputeFrame(dst, src, getEffectAsInt(), letterbox, ticks, alpha, e,
					#effect.getAmplitude(), effect.getAmplitudeAcceleration(),
					#effect.getFrequency(), effect.getFrequencyAcceleration(),
					#effect.getCompression(), effect.getCompressionAcceleration(),
					#effect.getSpeed());
		#}
	
		
		
	def get_cur_type(self):
		return self.dist[self.dist_cur]['type']
	def get_cur_s_freq(self):
		return self.dist[self.dist_cur]['s_freq']
	def get_cur_ampl(self):
		return self.dist[self.dist_cur]['ampl']
	def get_cur_ampl_acc(self):
		return self.dist[self.dist_cur]['ampl_acc']
	def get_cur_s_freq_acc(self):
		return self.dist[self.dist_cur]['s_freq_acc']
	def get_cur_start(self):
		return self.dist[self.dist_cur]['start']
	def get_cur_speed(self):
		return self.dist[self.dist_cur]['speed']
	def get_cur_comp(self):
		return self.dist[self.dist_cur]['comp']
	def get_cur_comp_acc(self):
		return self.dist[self.dist_cur]['comp_acc']
	
	def set_cur_type(self,t):
		self.dist[self.dist_cur]['type'] = t
	def set_cur_s_freq(self,t):
		self.dist[self.dist_cur]['s_freq'] = t
	def set_cur_ampl(self,t):
		self.dist[self.dist_cur]['ampl'] = t
	def set_cur_ampl_acc(self,t):
		self.dist[self.dist_cur]['ampl_acc'] = t
	def set_cur_s_freq_acc(self,t):
		self.dist[self.dist_cur]['s_freq_acc'] = t
	def set_cur_start(self,t):
		self.dist[self.dist_cur]['start'] = t
	def set_cur_speed(self,t):
		self.dist[self.dist_cur]['speed'] = t
	def set_cur_comp(self,t):
		self.dist[self.dist_cur]['comp'] = t
	def set_cur_comp_acc(self,t):
		self.dist[self.dist_cur]['comp_acc'] = t
	
	def overlay_frame(self, dst, letterbox, ticks, alpha, erase):
		return self.compute_frame(dst,self.src,self.get_cur_type(), letterbox, ticks, alpha, erase, self.get_cur_ampl(), self.get_cur_ampl_acc(), self.get_cur_s_freq(),  self.get_cur_s_freq_acc(), self.get_cur_comp(), self.get_cur_comp_acc(), self.get_cur_speed())
	
	def get_applied_offset(self,y,t,effect,ampl, ampl_acc,freq,freq_acc,comp,comp_acc,speed):
		
		 #// N.B. another discrepancy from Java--these values should be "short," and
    #// must have a specific precision. this seems to effect backgrounds with
    #// distortEffect == 1
    #var C1 = (1 / 512.0).toFixed(6);
    #var C2 = (8.0 * Math.PI / (1024 * 256)).toFixed(6);
    #var C3 = (Math.PI / 60.0).toFixed(6);

    #// Compute "current" values of amplitude, frequency, and compression
    #var amplitude = (ampl + ampl_accel * t * 2);
    #var frequency = (s_freq + s_freq_accel * t * 2);
    #var compression = (compr + compr_accel * t * 2);

    #// Compute the value of the sinusoidal line offset function
    #var S = Math.round(C1 * amplitude * Math.sin((C2 * frequency * y + C3 * speed * t).toFixed(6)));

    #if (distortEffect == 1)
		
		
		
		amplitude = int(ampl + ampl_acc * t * 2)
		frequency = int(freq + freq_acc * t * 2)
		compression = int(comp + comp_acc * t * 2)
		
		s = int(round(self.c1 * amplitude * math.sin(float('%.6f'%(self.c2 * frequency * y + self.c3 * speed * t)))  ))
		
		if effect == 1:
			return s
			
		elif effect == 2:
			if (y%2)==0:
				return -s
			return s
			
		elif effect == 3:
			l=int(math.floor(y*(1 + compression / 256.0) + s))%256
			
			if l < 0:
				l=256+l
				
			if l > 255:
				l=256-l
				
			return l
		
		return 0
	
	def set_original(self, s):
		self.src = s
	
	


class BGLayer:
	def __init__(self, rom, entry):
		self.src=rom
		self.gfx_dat = None
		self.arr_dat = None
		self.bbg_dat = None
		self.distort=Distorter()
		self.bmp=None
		self.h=256
		self.w=256
		self.cycle={'type':0,'start1':0,'end1':0,'start2':0,'end2':0,'speed':0}
		
		self.bmp = '\x00'*256*256*4
		
		self.arr_bmp=['\x00\x00\x00\x00']*256*256
		
		self.load(entry)
		
	def do_cycle(self):
		if self.cycle['speed'] == 0:
			return False
		self.cycle['cntdown'] -=1
		if self.cycle['cntdown'] <= 0:
			
			if self.cycle['type'] == 1 or self.cycle['type'] == 2:
				clen = self.cycle['end1'] - self.cycle['start1'] + 1
				cpos = self.cycle['cnt'] % clen
				
				for sp in range(len(self.cycle['col_orig'])):
					for i in range(self.cycle['start1'], self.cycle['end1']+1):
						nc = i - cpos
						if nc < self.cycle['start1']:
							nc += clen
						self.cycle['col_now'][sp][i] = self.cycle['col_orig'][sp][nc]
			
			if self.cycle['type'] == 2:
				clen = self.cycle['end2'] - self.cycle['start2'] + 1
				cpos = self.cycle['cnt'] % clen
				
				for sp in range(len(self.cycle['col_orig'])):
					for i in range(self.cycle['start2'], self.cycle['end2']+1):
						nc = i - cpos
						if nc < self.cycle['start2']:
							nc += clen
						self.cycle['col_now'][sp][i] = self.cycle['col_orig'][sp][nc]
			
			if self.cycle['type'] == 3:
				clen = self.cycle['end1'] - self.cycle['start1'] + 1
				cpos = self.cycle['cnt'] % (clen*2)
				
				for sp in range(len(self.cycle['col_orig'])):
					for i in range(self.cycle['start1'], self.cycle['end1']+1):
						nc = i + cpos
						dif = 0
						
						if nc > self.cycle['end1']:
							dif = nc-self.cycle['end1']-1
							nc = self.cycle['end1']-dif
							
							if nc < self.cycle['start1']:
								dif = self.cycle['start1']-nc-1
								nc = self.cycle['start1']+dif
								
						self.cycle['col_now'][sp][i] = self.cycle['col_orig'][sp][nc]
							
			
			self.cycle['cnt'] += 1
			self.cycle['cntdown']  = self.cycle['speed']
			return True
		return False

          #if (newcolor > this.end1) {
            #difference = newcolor-this.end1-1;
            #newcolor = this.end1 - difference;

            #if (newcolor < this.start1) {
              #difference = this.start1 - newcolor - 1;
              #newcolor = this.start1 + difference
            #}
          #}

          #// if (i == 14 && this.debug) {
          #//   console.log("difference: "+difference+"newcolor: "+newcolor+" cycle1Position: "+cycle1Position+ "cycleLength: " + cycleLength + "cycleCount: "+this.cycleCount)
          #// }
          #this.now_colors[subpalnum][i] = this.original_colors[subpalnum][newcolor];

        #};
      #};
      #//console.log(this.now_colors)
	
	def load(self, entry):
		self.idx=entry
		
		bbg = self.src.bbg_dat[self.idx]
		self.bbg=bbg
		
		self.gfx_dat = self.src.bbg_gfx_dat[bbg['gfx_idx']]
		self.pal_dat = self.src.bbg_pal_dat[bbg['pal_idx']]
		
		self.cycle['type'] = bbg['cycle_type']
		self.cycle['start1'] = bbg['cycle_1_start']
		self.cycle['end1'] = bbg['cycle_1_end']
		self.cycle['start2'] = bbg['cycle_2_start']
		self.cycle['end2'] = bbg['cycle_2_end']
		self.cycle['speed'] = bbg['cycle_speed'] / 2

		self.cycle['cntdown'] = self.cycle['speed']
		self.cycle['cnt'] = 0
		self.cycle['col_orig']=copy.deepcopy(self.pal_dat['colors'])
		self.cycle['col_now']=copy.deepcopy(self.pal_dat['colors'])
		
		
		e=bbg['animation']
		
		e1 = (( (e >> 24)) & 0xFF);
		e2 = (( (e >> 16)) & 0xFF);
		e3 = (( (e >> 8)) & 0xFF);
		e4 = (( (e)) & 0xFF);
		
		
		if (e2 != 0):
			eff = e2
		else:
			eff = e1
		
		
		self.distort.set_cur_s_freq( self.src.bbge_get_freq(eff) )
		self.distort.set_cur_s_freq_acc( self.src.bbge_get_freq_acc(eff) )
		self.distort.set_cur_comp( self.src.bbge_get_comp(eff) )
		self.distort.set_cur_comp_acc( self.src.bbge_get_comp_acc(eff) )
		self.distort.set_cur_ampl( self.src.bbge_get_amp(eff) )
		self.distort.set_cur_ampl_acc( self.src.bbge_get_amp_acc(eff) )
		self.distort.set_cur_speed( self.src.bbge_get_speed(eff) )
		self.distort.set_cur_start(0)
	
		if self.src.bbge_get_type(eff)==0:
			self.distort.set_cur_type(0)
		else:
			self.distort.set_cur_type(self.src.bbge_get_type(eff))
		
		
		self.load_bmp()
	
	def load_bmp(self):
		#self.bmp = [0]*self.h*self.w*4
		#self.bmp = [ [[0,0,0]]*self.h ] *self.w
		self.gfx_draw(self.bmp, self.cycle['col_now'])
		self.distort.set_original(self.arr_bmp);
	
	def overlay_frame(self, dst, letterbox, ticks, alpha, erase):
		if self.do_cycle():
			self.load_bmp()
			
		return self.distort.overlay_frame(dst, letterbox, ticks, alpha, erase);
	
	def gfx_draw(self, bmp, pal):
		bmp
		block = 0
		tile = 0
		subpal = 0
		i = 0
		j = 0
		n = 0
		b1 = 0
		b2 = 0
		vflip = False
		hflip = False
		
		arr = self.gfx_dat['arr']

		#// TODO: hardcoding is bad; how do I get the stride normally?
		stride = 1024;
		
		
		

		#// for each pixel in the 256x256 grid, we need to render the image found in the .dat file
		for i in xrange(32):

			for j in xrange(32):

				n = j * 32 + i

				b1 = arr[n * 2]
				b2 = arr[n * 2 + 1] << 8
				block = b1 + b2

				tile = block & 0x3FF
				vflip = (block & 0x8000) != 0
				hflip = (block & 0x4000) != 0
				subpal = (block >> 10) & 7

				self.gfx_draw_tile(self.arr_bmp, stride, i * 8, j * 8, pal, tile, subpal, vflip, hflip)
				
		bmp = ''
		
		#for x in self.arr_bmp:
		#	bmp+=x
		
		self.bmp=bmp
	
	def get_rgb_pal(self, pal, tile, subpal, i, j):
		pos = self.gfx_dat['tiles'][tile][i][j]
		
		return pal[subpal][pos]
	
	def gfx_draw_tile(self, pixels, stride, x,y,pal,tile,subpal,vflip,hflip):
		i=0
		while i < 8:
			
			
			if hflip and vflip==False:
				
				j=0
				while j < 8:
					rgb = self.get_rgb_pal(pal,tile,subpal,i,j)
					
					px=x+7-i
						
					py=y+j
						
					pixels[px + (py*256)] = rgb
					j+=1
				i+=1
			
			elif hflip==False and vflip==False:
				j=0
				while j < 8:
					rgb = self.get_rgb_pal(pal,tile,subpal,i,j)
					
					px=x+i
						
					py=y+j
						
					pixels[px + (py*256)] = rgb
					j+=1
				i+=1
				
			elif hflip==False and vflip:
				j=0
				while j < 8:
					rgb = self.get_rgb_pal(pal,tile,subpal,i,j)
					
					px=x+i
						
					py=y+7-j
						
					pixels[px + (py*256)] = rgb
					j+=1
				i+=1
				
			else:
				
				j=0
				while j < 8:
					rgb = self.get_rgb_pal(pal,tile,subpal,i,j)
					
					px=x+7-i
						
					py=y+7-j
						
					pixels[px + (py*256)] = rgb
					j+=1
				i+=1
			
			j=0
			while j < 8:
				rgb = self.get_rgb_pal(pal,tile,subpal,i,j)
				
				px=x+i
				if hflip:
					px=x+7-i
					
				py=y+j
				if vflip:
					py=y+7-j
					
				pixels[px + (py*256)] = rgb
				j+=1
			i+=1
			
			continue
			
			
			
			j=0
			while j < 8:
				
				rgb_arr = self.get_rgb_pal(pal,tile,subpal,i,j)
				
				#rgb_arr = struct.pack('i',rgb_arr[2] + (rgb_arr[1] << 8) + (rgb_arr[0]<< 16))
				
				
				px=x+i
				if hflip:
					px=x+7-i
					
				
				py=y+j
				if vflip:
					py=y+7-j
					
				
				#pos=(px*4) + (py*stride)
				pos=px + (py*256)
				
				#pixels[pos+0] = rgb_arr[0]
				#pixels[pos+1] = rgb_arr[1]
				#pixels[pos+2] = rgb_arr[2]
				pixels[pos] = rgb_arr
				#pixels[px][py][0] = rgb_arr[0]
				#pixels[px][py][1] = rgb_arr[1]
				#pixels[px][py][2] = rgb_arr[2]
				
				j+=1
			i+=1
        

		

class Rom:
	def __init__(self):
		self.fn=''
		self.rom_dat=[]
		self.loaded=False
		self.rom_dat_loc=0
		
		self.bbg_palbits=[0]*114
		self.bbg_gfxbits=[0]*103
		
		self.bbg_dat=[None]*327
		self.bbg_pal_dat=[None]*114
		self.bbg_gfx_dat=[None]*103
		
		self.bbg_pal=0
		
		self.bgp_bbp=0
		self.bgp_palettes=[]
		
	
		self.bitrevs = [0, 128, 64, 192, 32, 160, 96,
			224, 16, 144, 80, 208, 48, 176, 112, 240, 8, 136, 72, 200, 40, 168,
			104, 232, 24, 152, 88, 216, 56, 184, 120, 248, 4, 132, 68, 196, 36,
			164, 100, 228, 20, 148, 84, 212, 52, 180, 116, 244, 12, 140, 76,
			204, 44, 172, 108, 236, 28, 156, 92, 220, 60, 188, 124, 252, 2,
			130, 66, 194, 34, 162, 98, 226, 18, 146, 82, 210, 50, 178, 114,
			242, 10, 138, 74, 202, 42, 170, 106, 234, 26, 154, 90, 218, 58,
			186, 122, 250, 6, 134, 70, 198, 38, 166, 102, 230, 22, 150, 86,
			214, 54, 182, 118, 246, 14, 142, 78, 206, 46, 174, 110, 238, 30,
			158, 94, 222, 62, 190, 126, 254, 1, 129, 65, 193, 33, 161, 97, 225,
			17, 145, 81, 209, 49, 177, 113, 241, 9, 137, 73, 201, 41, 169, 105,
			233, 25, 153, 89, 217, 57, 185, 121, 249, 5, 133, 69, 197, 37, 165,
			101, 229, 21, 149, 85, 213, 53, 181, 117, 245, 13, 141, 77, 205,
			45, 173, 109, 237, 29, 157, 93, 221, 61, 189, 125, 253, 3, 131, 67,
			195, 35, 163, 99, 227, 19, 147, 83, 211, 51, 179, 115, 243, 11,
			139, 75, 203, 43, 171, 107, 235, 27, 155, 91, 219, 59, 187, 123,
			251, 7, 135, 71, 199, 39, 167, 103, 231, 23, 151, 87, 215, 55, 183,
			119, 247, 15, 143, 79, 207, 47, 175, 111, 239, 31, 159, 95, 223,
			63, 191, 127, 255]
		
		self.loc=0
	
	def snes2hex(self,addr,header=True):
		if addr >= 0x400000 and addr < 0x600000:
			addr -= 0x0
		elif addr >= 0xC00000 and addr < 0x1000000:
			addr -= 0xC00000
		else:
			print "snes address out of range: %d " % address
			exit(1)

		if header:
			addr += 0x200
		
		return addr
	
	def rom_read_byte(self):
		val=self.rom_dat[self.loc]
		self.loc += 1
		
		return val
	
	def rom_read_short(self):
		return self.rom_read_byte()
	
	def rom_read_dbl_short(self):
		return self.rom_read_byte() + (self.rom_read_byte() << 8)
	
	def rom_read_int(self):		
		return self.rom_read_byte() + (self.rom_read_byte() << 8) + (self.rom_read_byte() << 16) + (self.rom_read_byte() << 24)
	
	def bbg_read_idx(self, idx):
		self.loc = 0xADEA1 + idx * 17
		
		for i in range(17):
			self.bbg_dat[i] = self.rom_read_byte()
	
	def bbg_get_gfx_idx(self):
		return self.bbg_dat[0]
	
	def bbg_get_pal_idx(self):
		return self.bbg_dat[1]
	
	def bbg_get_bits_per_pixel(self):
		return self.bbg_dat[2]
	
	def bbg_get_animation(self):
		return (self.bbg_dat[13] << 24) + (self.bbg_dat[14] << 16) + (self.bbg_dat[15] << 8) + (self.bbg_dat[16])
	
	def bgp_set_bits_per_pixel(self,val):
		self.bgp_bbp=val
	
	def bgp_load_palette(self,idx):
		self.loc = 0xADCD9 + idx * 4
		self.loc = self.snes2hex(self.rom_read_int())
		
		#self.bgp_bbp=0
		#self.bgp_palettes=[]
		
		if self.bgp_bbp != 2 and  self.bgp_bbp != 4:
			print "palette error : incorrect color depth specified"
			exit(1)
			
		cnt=1
		bbp = self.bgp_bbp
			
		self.bgp_palettes.append([ [[]]*cnt ])
		
		colors = self.bgp_palettes[-1][0]
		
		#for (int pal = 0; pal < count; pal++) {
			#colors[pal] = new int[(int) Math.pow(2, bpp)];
			#for (int i = 0; i < (int) Math.pow(2, bpp); i++) {
				#int clr16 = block.ReadDoubleShort();

				#short b = (short) (((clr16 >> 10) & 31) * 8);
				#short g = (short) (((clr16 >> 5) & 31) * 8);
				#short r = (short) ((clr16 & 31) * 8);
				#colors[pal][i] = Color.rgb(r, g, b);
			#}
		#}
		
		for pal in range(cnt):
			colors[pal] = [None]*(bbp**2)
			for i in range( bbp**2 ):
				clr16 = self.rom_read_dbl_short()
				
				b = (((clr16 >> 10) & 31) * 8);
				g = (((clr16 >> 5) & 31) * 8);
				r = ((clr16 & 31) * 8);
				
				#colors[pal][i] = [r,g,b]
				
				colors[pal][i] = struct.pack('i',b + (g << 8) + (r<< 16))
	
	def rom_dat_decomp(self):
		size = self.rom_dat_get_comp_size()
		
		if size < 1:
			print 'invalid compressed data'
			exit(1)
		
		bout = [0]*size
		
		bout = self.rom_dat_decomp_block(bout) # uses self.loc for pointer
		
		
		if (bout == None):
			print "compression error : Computed and actual decompressed sizes do not match. Please reinstall universe and reboot."
			exit(1)
		
		return bout
	
	def rom_dat_decomp_block(self, output):
		start = self.loc
		data = self.rom_dat
		read = 0
		
		pos=start
		maxlen = len(output)
		bpos,bpos2=0,0
		tmp=0
		
		while data[pos] != 0xff:
			if pos >= len(data):
				read = pos - start + 1
				return None
				# -8
			
			cmdtype = (data[pos]) >> 5
			tlen = ((data[pos]) & 0x1F) + 1;

			if (cmdtype == 7):
				cmdtype = ((data[pos]) & 0x1C) >> 2;
				tlen = (((data[pos]) & 3) << 8) + (data[pos + 1]) + 1;
				pos+=1

			#// Error: block length would overflow maxlen, or block endpos
			#// negative?
			if (bpos + tlen > maxlen or bpos + tlen < 0):
				read = pos - start + 1;
				return None;
				# -1;

			pos+=1

			if (cmdtype >= 4):
				bpos2 = ((data[pos]) << 8) + (data[pos + 1]);
				if (bpos2 >= maxlen or bpos2 < 0):
					read = pos - start + 1;
					return None
					#// return -2;
				pos += 2
			
			
			
			if cmdtype==0: # Uncompressed block
				while (tlen != 0):
					output[bpos] = data[pos];#output[bpos++] = data[pos++];
					pos += 1
					bpos += 1
					tlen -= 1
				#// Array.Copy(data, pos, output, bpos, tlen);
				#// bpos += tlen;
				#// pos += tlen;

			if cmdtype==1: # RLE
				while (tlen != 0):
					output[bpos] = data[pos];
					bpos+=1
					tlen-=1
				pos+=1;

			if cmdtype==2: # 2-byte RLE
				if (bpos + (2 * tlen) > maxlen or bpos < 0): #if (bpos + 2 * len > maxlen || bpos < 0) {
					read = pos - start + 1;
					return None;
					#// return -3;
					
				while (tlen != 0):
					output[bpos] = data[pos];
					bpos += 1
					output[bpos] = data[pos + 1];
					bpos += 1
					tlen-=1
				
				pos += 2;

			if cmdtype==3: # Incremental sequence
				tmp = data[pos];
				pos+=1
				while (tlen != 0):
					output[bpos] = tmp;
					bpos+=1
					tmp+=1
					tlen-=1
				#break;

			if cmdtype==4: # Repeat previous data
				if (bpos2 + tlen > maxlen or bpos2 < 0):
					read = pos - start + 1;
					return None;
					#// return -4;
				
				for i in range(tlen):
					output[bpos] = output[bpos2 + i];
					bpos += 1
				

			if cmdtype==5: # Output with bits reversed
				if (bpos2 + tlen > maxlen or bpos2 < 0):
					read = pos - start + 1;
					return None;
					#// return -5;
				
				while (tlen != 0):
					output[bpos] = self.bitrevs[output[bpos2] & 0xff];
					bpos+=1
					bpos2+=1
					tlen-=1
				

			if cmdtype==6:
				if (bpos2 - tlen + 1 < 0):
					read = pos - start + 1;
					return None
					#// return -6;
				
				while (tlen != 0):
					output[bpos] = output[bpos2];
					bpos+=1
					bpos2-=1
					tlen-=1

			if cmdtype==7:
				read = pos - start + 1;
				return None;
				#// return -7;
			

		read = pos - start + 1;
		
		
		return output
		
		
	
	
	
	
	
	def rom_dat_get_comp_size(self):
		# self.loc
		# self.rom_dat
		
		pos = self.loc
		data = self.rom_dat
		bpos = 0
		bpos2 = 0

		while data[pos] != 0xff:
			# data overflow before end of compressed data
			if pos >= len(self.rom_dat):
				return -8

			cmdtype = (data[pos]) >> 5;
			tlen = ((data[pos]) & 0x1F) + 1;

			if cmdtype == 7:
				cmdtype = ((data[pos]) & 0x1C) >> 2;
				tlen = (((data[pos]) & 3) << 8) + (data[pos + 1]) + 1;
				pos+=1

			if (bpos + tlen < 0):
				return -1
			pos+=1

			if (cmdtype >= 4):
				bpos2 = ((data[pos]) << 8) + (data[pos + 1]);
				if (bpos2 < 0):
					return -2;
				pos += 2;
				
			if   cmdtype==0: # uncompressed block
				bpos += tlen
				pos += tlen
				
			elif cmdtype==1: # rle
				bpos+=tlen
				pos += 1
				
			elif cmdtype==2: # 2-byte rle
				if (bpos < 0):
					return -3;
				bpos += 2 * tlen;
				pos += 2;
				

			elif cmdtype==3: # incremental sequence
				bpos += tlen;
				pos += 1;
				

			elif cmdtype==4: # repeat previous data
				if (bpos2 < 0):
					return -4;
				bpos += tlen;
				

			elif cmdtype==5: # output with bits reversed
				if (bpos2 < 0):
					return -5;
				bpos += tlen;
				

			elif cmdtype==6:
				if (bpos2 - tlen + 1 < 0):
					return -6;
				bpos += tlen;
				

			elif cmdtype== 7:
				return -7;
				
		return bpos
	
	def bbgg_build_tiles(self,idx):
		
		
		n = len(self.bbg_gfx_dat[idx]['gfx']) / (8 * self.bbg_gfx_dat[idx]['bpp']);

		self.bbg_gfx_dat[idx]['tiles'] = [] #new ArrayList<short[][]>();
		
		tiles = self.bbg_gfx_dat[idx]['tiles']

		for i in range(n):
			tiles.append( [None]*8 );

			o = i * 8 * self.bbg_gfx_dat[idx]['bpp']

			for x in range(8):
				tiles[-1][x] = [0] * 8
				for y in range(8):
					c = 0;
					
					for bp in range(self.bbg_gfx_dat[idx]['bpp']):
						half_bp = int(math.floor(bp/2))
						
						gfx = self.bbg_gfx_dat[idx]['gfx'][o + y * 2 + (half_bp * 16 + (bp & 1))];
						

						c += ((gfx & (1 << 7 - x)) >> 7 - x) << bp;

					tiles[-1][x][y] = c; # (byte)
	
	def bbge_get_type(self,idx):
		return self.bbge_dats[idx][2]
	
	def bbge_get_dur(self,idx):
		return self.bbge_dats[idx][0] + (self.bbge_dats[idx][1] << 8) & 0xffff
	
	def bbge_get_freq(self,idx):
		return self.bbge_dats[idx][3] + (self.bbge_dats[idx][4] << 8) & 0xffff
	
	def bbge_get_amp(self,idx):
		return self.bbge_dats[idx][5] + (self.bbge_dats[idx][6] << 8) & 0xffff
	
	def bbge_get_comp(self,idx):
		return (self.bbge_dats[idx][8] + (self.bbge_dats[idx][9] << 8)) & 0xffff
		
	def bbge_get_freq_acc(self,idx):
		return self.bbge_dats[idx][10] + (self.bbge_dats[idx][11] << 8) & 0xffff
	
	def bbge_get_amp_acc(self,idx):
		return self.bbge_dats[idx][12] + (self.bbge_dats[idx][13] << 8) & 0xffff
	
	def bbge_get_speed(self,idx):
		return self.bbge_dats[idx][14]
	
	def bbge_get_comp_acc(self,idx):
		return (self.bbge_dats[idx][15] + (self.bbge_dats[idx][16] << 8)) & 0xffff
	
	
	def read_gfx_dat(self,idx):
		self.bbg_gfx_dat[idx] = {'width':32,'height':32, 'bpp' : self.bbg_gfxbits[idx]}
		
		
		# graphics pointer table entry
		self.loc = 0xAD9A1 + idx * 4
		self.loc = self.snes2hex(self.rom_read_int())
		self.bbg_gfx_dat[idx]['gfx'] = self.rom_dat_decomp()
		self.bbgg_build_tiles(idx)
		
		# arrangement pointer table entry
		self.loc = 0xADB3D + idx * 4
		self.loc = self.snes2hex(self.rom_read_int())
		self.bbg_gfx_dat[idx]['arr'] = self.rom_dat_decomp();
	
	
	# bbg dat table:
	# 17 bytes per entry:
	#
	# 0  Graphics/Arrangement index
	# 1  Palette
	# 2  Bits per pixel
	# 3  Palette cycle type
	# 4  Palette cycle #1 start
	# 5  Palette cycle #1 end
	# 6  Palette cycle #2 start
	# 7  Palette cycle #2 end
	# 8  Palette cycle speed
	# 9  Mov
	# 10 Mov
	# 11 Mov
	# 12 Mov
	# 13 Effects
	# 14 Effects
	# 15 Effects
	# 16 Effects
	#
	
	def read_bbg_dat(self,idx):
		self.bbg_dat[idx] = {}
		
		self.loc = 0xADEA1 + idx * 17
		
		tmp=[0]*17
		
		for i in range(17):
			tmp[i] = self.rom_read_byte()
		
		self.bbg_dat[idx]['gfx_idx'] = tmp[0]
		self.bbg_dat[idx]['pal_idx'] = tmp[1]
		self.bbg_dat[idx]['bpp'] = tmp[2]
		self.bbg_dat[idx]['cycle_type'] = tmp[3]
		self.bbg_dat[idx]['cycle_1_start'] = tmp[4]
		self.bbg_dat[idx]['cycle_1_end'] = tmp[5]
		self.bbg_dat[idx]['cycle_2_start'] = tmp[6]
		self.bbg_dat[idx]['cycle_2_end'] = tmp[7]
		self.bbg_dat[idx]['cycle_speed'] = tmp[8]
		self.bbg_dat[idx]['animation'] = (tmp[13]<<24) + (tmp[13]<<16) + (tmp[15]<<8) + (tmp[16])
		
	
	def read_pal_dat(self,idx):
		self.bbg_pal_dat[idx] = {}
		
		self.bbg_pal_dat[idx]['bpp'] = self.bbg_palbits[idx]
		
		self.loc = 0xADCD9 + idx * 4
		self.loc = self.snes2hex(self.rom_read_int())
		
		#self.bgp_bbp=0
		#self.bgp_palettes=[]
		
		if self.bbg_pal_dat[idx]['bpp'] != 2 and  self.bbg_pal_dat[idx]['bpp'] != 4:
			print "palette error : incorrect color depth specified"
			exit(1)
			
		cnt=1
		bbp = self.bbg_pal_dat[idx]['bpp']
			
		self.bbg_pal_dat[idx]['colors'] = [[[]]*cnt ]
		
		colors = self.bbg_pal_dat[idx]['colors']
		
		#for (int pal = 0; pal < count; pal++) {
			#colors[pal] = new int[(int) Math.pow(2, bpp)];
			#for (int i = 0; i < (int) Math.pow(2, bpp); i++) {
				#int clr16 = block.ReadDoubleShort();

				#short b = (short) (((clr16 >> 10) & 31) * 8);
				#short g = (short) (((clr16 >> 5) & 31) * 8);
				#short r = (short) ((clr16 & 31) * 8);
				#colors[pal][i] = Color.rgb(r, g, b);
			#}
		#}
		
		for pal in range(cnt):
			colors[pal] = [None]*(bbp**2)
			for i in range( bbp**2 ):
				clr16 = self.rom_read_dbl_short()
				
				b = (((clr16 >> 10) & 31) * 8);
				g = (((clr16 >> 5) & 31) * 8);
				r = ((clr16 & 31) * 8);
				
				#colors[pal][i] = [r,g,b]
				
				colors[pal][i] = struct.pack('i',b + (g << 8) + (r<< 16))
	
	## TODO: implement bbg_gfx_dat

	def open(self, binfn):
		
		f=open(binfn, 'rb')
		raw=f.read()
		f.close()
		
		for x in raw:
			self.rom_dat.append(struct.unpack('<h', x+'\x00')[0])
		
		# gather background data, while checking consistency in bpp values across pallettes.
		for i in range(327):
			self.read_bbg_dat(i)
			
			pal = self.bbg_dat[i]['pal_idx']
			
			if self.bbg_palbits[pal] != 0:
				if self.bbg_palbits[pal] != self.bbg_dat[i]['bpp']:
					print ' battle background : inconsistent bit depth'
					exit(1)
			
			self.bbg_palbits[pal] = self.bbg_dat[i]['bpp']
			
			self.bbg_gfxbits[self.bbg_dat[i]['gfx_idx']] = self.bbg_dat[i]['bpp']
		
		# load palettes
		for i in range(114):
			self.read_pal_dat(i)
			
		
		# load bg graphics
		for i in range(103):
			self.read_gfx_dat(i)
			
		
		self.bbge_dats = [None]*135
		# load bg effects
		for i in range(135):
			self.bbge_dats[i] = [0]*17
			self.loc = 0x0AF908 + i * 17
			for x in range(17):
				self.bbge_dats[i][x] = self.rom_read_short();
		
		
		
		self.loaded=True
	

