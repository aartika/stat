#!/bin/python

import matplotlib.pyplot as plt
import datetime
from datetime import timedelta
import urllib2
#http://www.theocc.com/webapps/volume-query?reportDate=20100212&format=csv&volumeQueryType=O&symbolType=O&symbol=IBM&reportType=D&accountType=ALL&productKind=OSTK&porc=C

firm = ["FSL", "CTRX", "HSP", "PCYC" , "BHI", "COV", "AGN", "DTV", "TWC", "ALTR", "SLXP", "AXS" ,  "MWV", "ANS", "PETM", "INFA", "CNQR", "MCRS" , "SWY", "BEAM"] 
ann_dates  = ["2015/03/02", "2015/03/30" , "2015/02/05", "2015/03/04", "2014/11/17", "2014/06/16", "2014/11/17", "2014/05/18", "2014/02/13", "2015/03/27", "2015/02/22", "2015/01/25", "2015/01/26", "2014/12/08", "2014/12/14", "2015/04/07", "2014/09/18", "2014/06/23", "2014/03/06", "2014/01/13"]

url_format = 'http://www.theocc.com/webapps/volume-query?reportDate={}&format=csv&volumeQueryType=O&symbolType=O&symbol={}&reportType=D&accountType=ALL&productKind=OSTK&porc={}'

daily_data_call = []
daily_data_put = []
for i in range(18, len(firm)):
	f = open(firm[i] + '.csv', 'w')
	d = ann_dates[i].split("/")
	#print d
	ann_date = datetime.date( int(d[0]), int(d[1]), int(d[2]))
	firm_data_call = []
	firm_data_put = []
	working_days = 0
	for delta in range (0, 400):	
		date = ann_date + timedelta(days=-delta)	
		if( date.weekday() == 5 or date.weekday() == 6 ):	#saturday or sunday
			continue
		call_url = url_format.format(date.strftime('%Y%m%d'), firm[i], 'C')
		call_data = urllib2.urlopen(call_url).read() 
		call_rows = call_data.splitlines()
		if ( len(call_rows) == 1 ): # seems like a holiday
			continue
		call_sum = 0;
		for call_row in call_rows[1:]:
			call_sum += int(call_row.split(',')[0])

		firm_data_call.append( call_sum )
		put_url = url_format.format(date.strftime('%Y%m%d'), firm[i], 'P')
		put_data = urllib2.urlopen(put_url).read() 
		put_rows = put_data.splitlines()
		put_sum = 0;
		for put_row in put_rows[1:]:
			put_sum += int(put_row.split(',')[0])

		firm_data_put.append( put_sum )
		#print str( date )
		f.write( str( date ) + "," + str( call_sum ) + "," + str( put_sum ) + "\n" )
		working_days += 1
		if ( working_days == 201 ):
			break
	
	daily_data_call.append(firm_data_call)
	daily_data_put.append(firm_data_put)	
