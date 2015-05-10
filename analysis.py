#!/bin/python
import math

underlyers = ["FSL", "CTRX", "HSP", "PCYC" , "BHI",  "DTV", "TWC", "ALTR", "SLXP",  "MWV", "PETM", "INFA", "CNQR", "MCRS" , "BEAM"]

benchmark = [-172, -123]

pre_ann = [ -10,-1]

pre_rumour = [-30, -1]

params = [1, 2, 3] 		## 1=Call, 2=Put, 3=Stock
for param in params:
	for underlyer in underlyers:
		with open( "final-" + underlyer + ".csv" ) as f:
	    		lines = f.read().splitlines()
	
		benchmark_vol = 0
		for i in range( benchmark[0], benchmark[1] + 1 ):
			benchmark_vol += math.log( 1 + int( lines[ -i ].split(",")[param] ) )
	
		pre_ann_vol = 0
		for i in range( pre_ann[0], pre_ann[1] + 1 ):
			pre_ann_vol += math.log( 1 + int( lines[ -i ].split(",")[param] ) )
	
		pre_rumour_vol = 0
		for i in range( pre_rumour[0], pre_rumour[1] + 1 ):
			pre_rumour_vol += math.log( 1 + int( lines[ -i ].split(",")[param] ) )
	
		print underlyer + "," + str(benchmark_vol/50) + "," + str(pre_ann_vol/10) + "," + str(pre_rumour_vol/30)

	print "----------------------------------------------\n"
	
