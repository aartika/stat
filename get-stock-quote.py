#!/bin/python

import matplotlib.pyplot as plt
import datetime
from datetime import timedelta
import urllib2

#http://ichart.yahoo.com/table.csv?s=BAS.DE&a=0&b=1&c=2000 &d=0&e=31&f=2010&g=w&ignore=.csv

url_format = 'http://ichart.yahoo.com/table.csv?s={}&a={}&b={}&c={}&d={}&e={}&f={}&g=d&ignore.csv'

underlyers = ["FSL", "CTRX", "HSP", "PCYC" , "BHI", "COV", "AGN", "DTV", "TWC", "ALTR", "SLXP", "AXS" ,  "MWV", "PETM", "INFA", "CNQR", "MCRS" , "SWY", "BEAM"]
ann_dates  = ["2015/03/02", "2015/03/30" , "2015/02/05", "2015/03/04", "2014/11/17", "2014/06/16", "2014/11/17", "2014/05/18", "2014/02/13", "2015/03/27", "2015/02/22", "2015/01/25", "2015/01/26", "2014/12/14", "2015/04/07", "2014/09/18", "2014/06/23", "2014/03/06", "2014/01/13"]

#underlyers = ["FSL"]
#ann_dates = ["2015/03/02"]

delta = 400
for i in range(18, len( underlyers ) ):
	underlyer = underlyers[ i ]
	d = ann_dates[i].split("/")
	#print d
	fw = open( 'final-' + underlyer + '.csv', 'w')
	to_date = datetime.date( int(d[0]), int(d[1]), int(d[2]))	
	from_date = to_date + timedelta(days=-delta)	
	
	# >>>> https://code.google.com/p/yahoo-finance-managed/wiki/csvHistQuotesDownload
	a = from_date.month - 1
	b = from_date.day
	c = from_date.year

	d = to_date.month - 1
	e = to_date.day
	f = to_date.year
	
	stock_url = url_format.format( underlyer, a, b, c, d, e, f )
	data = urllib2.urlopen(stock_url).read()
	rows = data.splitlines()
	#print( data )
	with open( underlyer + ".csv" ) as f:
    		lines = f.read().splitlines()
	p = 0
	q = 1
	while 1:
		if( p == len( lines ) ):
			break
		option = lines[p]
		stock = rows[q]
		option_date = option.split(",")[0]
		stock_date = stock.split(",")[0]
		d1 = option_date.split("-")
		od = datetime.date( int(d1[0]), int(d1[1]), int(d1[2])) 			
		d2 = stock_date.split("-")
		sd = datetime.date( int(d2[0]), int(d2[1]), int(d2[2]))
		
		if ( od - sd == timedelta(0) ):
			fw.write( option + "," + str( stock.split(",")[5] ) + "\n" )
			p += 1
			q += 1
		else:
			q += 1


						
	
	
