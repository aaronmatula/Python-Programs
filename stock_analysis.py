from pandas_datareader import data
import datetime
from bokeh.plotting import figure, show, output_file


    # Enter your date ranges here
sdate=datetime.datetime(2015,6,1)
edate=datetime.datetime(2017,6,30)

    #Enter the company ticker symbol here
df=data.DataReader(name="GOOG",data_source="google",start=sdate,end=edate)
df.index[df.Close > df.Open]
p=figure(x_axis_type='datetime', width=1000, height=300, responsive=True, title="Candlestick Chart")
    #p.title.text="Candlestick Chart"
p.grid.grid_line_alpha=0.3

def inc_dec(c, o):
	if c > o:
		value="Increase"
	elif c < o:
		value="Decrease"
	else:
		value="Equal"
	return value

df["Status"]=[inc_dec(c, o) for c, o in zip(df.Close, df.Open)]

df["Middle"]=(df.Open+df.Close)/2
df["Height"] = abs(df.Close-df.Open)

hours_12 = 12*60*60*1000

p.segment(df.index, df.High, df.index, df.Low, color="Black")

p.rect(df.index[df.Status=="Increase"], df.Middle[df.Status=="Increase"],
           hours_12,df.Height[df.Status=="Increase"],fill_color="#CCFFFF",line_color="black")

p.rect(df.index[df.Status=="Decrease"], df.Middle[df.Status=="Decrease"],
           hours_12,df.Height[df.Status=="Decrease"],fill_color="#FF3333",line_color="black")


output_file("CS.html")
show(p)
    