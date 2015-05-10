#!/bin/python

import matplotlib.pyplot as plt
import datetime
from datetime import timedelta
import urllib2
import csv
#http://www.theocc.com/webapps/volume-query?reportDate=20100212&format=csv&volumeQueryType=O&symbolType=O&symbol=IBM&reportType=D&accountType=ALL&productKind=OSTK&porc=C

firms = {"FSL"  :    "2015/03/02",
         "CTRX" :    "2015/03/30",
         "HSP"  :    "2015/02/05",
         "PCYC" :    "2015/03/04",
         "BHI"  :    "2014/11/17",
         "COV"  :    "2014/06/16",
         "AGN"  :    "2014/11/17",
         "DTV"  :    "2014/05/18",
         "TWC"  :    "2014/02/13",
         "ALTR" :    "2015/03/27",
         "SLXP" :    "2015/02/22",
       #  "AXS"  :    "2015/01/25",
         "MWV"  :    "2015/01/26",
       #  "ANS"  :    "2014/12/08",
         "PETM" :    "2014/12/14",
         "INFA" :    "2015/04/07",
         "CNQR" :    "2014/09/18",
         "MCRS" :    "2014/06/23",
         "SWY"  :    "2014/03/06",
         "BEAM" :    "2014/01/13"
        }

url_format = 'http://www.theocc.com/webapps/volume-query?reportDate={}&format=csv&volumeQueryType=O&symbolType=O&symbol={}&reportType=D&accountType=ALL&productKind=OSTK&porc={}'

for firm in firms.keys():
	f = open(firm + '.csv', 'w')
	d = firms[firm].split("/")
	#print d
	ann_date = datetime.date( int(d[0]), int(d[1]), int(d[2]))
	firm_data_call = []
	firm_data_put = []
	working_days = 0
	for delta in range (0, 400):	
		date = ann_date + timedelta(days=-delta)	
		if( date.weekday() == 5 or date.weekday() == 6 ):	#saturday or sunday
			continue
		call_url = url_format.format(date.strftime('%Y%m%d'), firm, 'C')
		call_data = urllib2.urlopen(call_url).read() 
		call_rows = call_data.splitlines()
		if ( len(call_rows) == 1 ): # seems like a holiday
			continue
		call_sum = 0;
		for call_row in call_rows[1:]:
			call_sum += int(call_row.split(',')[0])

		put_url = url_format.format(date.strftime('%Y%m%d'), firm, 'P')
		put_data = urllib2.urlopen(put_url).read() 
		put_rows = put_data.splitlines()
		put_sum = 0;
		for put_row in put_rows[1:]:
			put_sum += int(put_row.split(',')[0])

		#print str( date )
		f.write( str( date ) + "," + str( call_sum ) + "," + str( put_sum ) + "\n" )
		working_days += 1
		if ( working_days == 201 ):
			break

daily_data = []
for firm in firms.keys():
        firm_data = []
        f = open(firm + '.csv')
        reader = csv.reader(f)
        for row in reader:
                firm_data.append(row)

        daily_data.append(firm_data)

f = open('average_call_volume', 'w')
for i in range (0, 173):
        call_sum = 0;
        for j in range (0, len(firms.keys())):
                call_sum += int(daily_data[j][i][1])
        f.write(str(call_sum/len(firms.keys())) + "\n")
