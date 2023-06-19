import os, sys, re, time, requests, calendar, random, bs4, uuid, json, subprocess, base64
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from datetime import date,datetime
from requests.exceptions import ConnectionError
###----------[ RANDOM WARNA RICH ]---------- ###
try:
	file_color = open("data/theme_color","r").read()
	color_text = file_color.split("|")[0]
	color_panel = file_color.split("|")[1,2]
	
except:
	junWik = "#00C8FF"
	stenly = "#FFFF00"
	mat = "#FFFFFF"
	fikri = "#00FF00"
	sabi = "#FF0000"
	color_panel = random.choice([junWik,sabi,stenly,mat,fikri])
	
###----------[ WARNA PRINT RICH ]---------- ###
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH
###----------[ INSTALING MODUL ]---------- ###
try:
        import npyscreen
except ImportError:
        os.system('clear')
        prints(Panel(f"""{H2}• {P2}Modul Requests Proses {H2}•""",width=55,padding=(0,15),style=f"{color_panel}")
        os.system('pip install npyscreen')
try:
        import rich
except ImportError:
        cetak(nel('\t• Modul Rich Proses •'))
        os.system('pip install rich')
try:
        import stdiomask
except ImportError:
        cetak(nel('\t• Modul Stdiomask Proses •'))
        os.system('pip install stdiomask')
try:
	import requests
except ImportError:
	cetak(nel('\t• Modul Requests Proses •'))
	os.system('pip install requests && pip install mechanize ')
	
	
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('/sdcard/Film Bokep18+')
	except:pass
	try:os.mkdir('/sdcard/JUNZ-DUMP')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.system('clear')
	except:pass
	login()