#!/usr/bin/python

import sys
import pandas as pd
from tabula import read_pdf

keyword = {"S/C", "W/P", "T/S", "SUBPOENA", "GREENBACK", "SCIF", "TRAFFIC"}
clear = ["CLEAR LAST", "I/S"]
section_1 = {"BOWLING", "ARMS", "POST", "LIBRARY"}
file_name = sys.argv[1]

# df = read_pdf("PAGE3.pdf", multiple_tables=True, pages='all')
df = read_pdf(file_name, multiple_tables=True, pages='all')

def wrangle(raw_data):
	date = raw_data[3].iloc[0,1][-8:]
	page_1, page_2 = raw_data[3], raw_data[4]
	page_1.drop([i for i in range(0, 5)], axis=0, inplace=True)
	try:
		page_2.drop([3, 5], axis=1, inplace=True)
	except:
		page_2.drop([3], axis=1, inplace=True)
	for i in range(2, 29, 2):
		page_2.iat[i, 0] = page_2.iat[i+1, 0]
	page_2.dropna(inplace=True); page_2.columns = [i for i in range(0, 4)]
	page_1.drop(1, axis=1, inplace=True); page_2.drop(1, axis=1, inplace=True) 
	page_1.index = [i for i in range(0, 11)]; page_2.index = [i for i in range(11, 25)]
	frame = pd.concat([page_1, page_2])
	frame.columns = ["Call Time", "Unit", "Remarks"]
	frame["Date"] = date[4:6] + "/" + date[6:] + "/" + date[0:4]
	return frame

def arrange(df):
	for row in df.itertuples():
		desc = set(str(df.iat[row.Index, 2]).split(" "))
		if desc.isdisjoint(keyword):
			df.iat[row.Index, 2] = pd.NaT
		else:
			temp = str(row[1])
			df.iat[row.Index, 0] = temp[:2] + ":" + temp[2:]
	df.dropna(inplace=True)
	df["Name"] = df.apply(activity, axis=1)
	df["Location"] = df.apply(sector, axis=1)
	df["Shift"] = df.apply(shift, axis=1)
	df["Type"], df["Action"] = "Service", "Checked for security AIO"
	df["Dispatched"], df["Arrive"] = df["Call Time"], df["Call Time"]
	df["Clear"], df["Close"], df["Time"] = pd.NaT, pd.NaT, pd.NaT
	df = df[["Type", "Name", "Date", "Shift", "Call Time", "Unit", "Location", "Dispatched", "Arrive", "Clear", "Close", "Time", "Action", "Remarks"]]
	return df

def activity(row):
	short = (keyword & set(row[2].split(" "))).pop()
	if short == "S/C":
		result = "security check"
	elif short == "W/P":
		result = "walking patrol"
	elif short == "T/S" or "Traffic":
		result = "traffic stop"
	elif short == "SUBPOENA":
		result = "subpoena"
	elif short == "SCIF":
		result = "scif alarm"
	else:
		result == "greenback"
	return result

def sector(row):
	dash = row[1][2]
	location = row[2].split()
	if "KNP" in location:
		if "YONGSAN" in location:
			loc = "Off Post (Yongsan-Gu)"
		elif "ITAEWON" in location:
			loc = "Off Post (Itaewon)"
		elif "HONGDAE" in location:
			loc = "Off Post (Hongdae)"
		else:
			loc = "Off Post (Other)"
	elif dash == 3:
		loc = "K-16"
	elif not set(location).isdisjoint(section_1):
		loc = "Sector 1"
	else:
		loc = "Sector 2"
	return loc

def shift(row):
	dash = int(row[1][0])
	if dash == 1:
		time = "Days"
	elif dash == 2:
		time = "Swings"
	else:
		time = "Mids"
	return time

arrange(wrangle(df)).to_excel("{}.xlsx".format(file_name), index=False)
# arrange(wrangle(df)).to_excel("Test.xlsx", index=False)
# print(arrange(wrangle(df)))
