#!/bin/python

import matplotlib.pyplot as plt
import datetime
from datetime import timedelta
import urllib2
#http://www.theocc.com/webapps/volume-query?reportDate=20100212&format=csv&volumeQueryType=O&symbolType=O&symbol=IBM&reportType=D&accountType=ALL&productKind=OSTK&porc=C

firm = ["BHI", "COV", "AGN", "DTV", "TWC", "ALTR", "SLXP", "AXS"] 
date  = ["2014/11/17", "2014/06/16", "2014/11/17", "2014/05/18", "2014/02/13", "2015/03/27", "2015/02/22" "2015/01/25" ]

days = 300
url_format = 'http://www.theocc.com/webapps/volume-query?reportDate={}&format=csv&volumeQueryType=O&symbolType=O&symbol={}&reportType=D&accountType=ALL&productKind=OSTK&porc={}'

total_benchmark_call = [ ]
total_benchmark_put = [ ]
total_preann_call = [ ]
total_preann_put = [ ]
for i in range(0, len(firm)):
	f = open(firm[i] + '.csv', 'w')
	d = date[i].split("/")
	ann_date = datetime.date( int(d[0]), int(d[1]), int(d[2]))
	daily_data_call = []
	daily_data_put = []
	delta = -201
	while delta < 1:
		if( delta == -100 ):
			dela = -31
		date = ann_date + timedelta(days=delta)	
		if( date.weekday() == 5 or date.weekday() == 6 ):	#saturday or sunday
			continue
		call_url = url_format.format(date.strftime('%Y%m%d'), firm[i], 'C')
		call_data = urllib2.urlopen(call_url).read() 
		call_rows = call_data.splitlines()
		call_sum = 0;
		for call_row in call_rows[1:]:
			call_sum += int(call_row.split(',')[0])

		daily_data_call.append( call_sum )
		put_url = url_format.format(date.strftime('%Y%m%d'), firm[i], 'P')
		put_data = urllib2.urlopen(put_url).read() 
		put_rows = put_data.splitlines()
		put_sum = 0;
		for put_row in put_rows[1:]:
			put_sum += int(put_row.split(',')[0])

		daily_data_put.append( put_sum )
		if( call_sum == 0 and put_sum == 0):
			continue		## seems like a holiday
		f.write( str( date ) +"," + str( call_sum ) + "," + str( put_sum ))
		delta += 1
	
	benchmark_call = benchmark_put = 0
	preann_call = preann_put = 0
	for i in range(0,100):
		benchmark_call += call_sum[i]
		benchmark_put +=  put_sum[i]
	for i in range(101,131):
		preann_call += call_sum[i]
		preann_put += put_sum[i]
	
	total_benchmark_call.append( benchmark_call/100 )
	total_benchmark_put.append( benchmark_put/100 )
	total_preann_call.append( preann_call/30 )
	total_preann_put.append( preann_put/30 )

print( total_benchmark_call )
print( total_benchmark_put )
print( total_preann_call )
print( total_reann_put )

plt.plot( call_sum )
plt.ylabel('some numbers')
plt.show()
		
	


