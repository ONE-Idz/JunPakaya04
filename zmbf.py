#-----------------------[ MASUK & INSTALL MODUL ]--------------------#
if __name__=='__main__':
	try:os.system('clear')
	except:pass
	
	try:os.system('touch .prox.txt')
	except:pass
	
	try:
		import npyscreen
	except ImportError:
		os.system('clear')
		prints(Panel(f"""{H2}• {P2}Modul npyscreen Proses {H2}•""",width=55,padding=(0,15),style=f"{color_panel}"))
		os.system('pip install npyscreen && git pull')
		
	try:
		import rich
	except ImportError:
		prints(Panel(f"""{H2}• {P2}Modul rich Proses {H2}•""",width=55,padding=(0,15),style=f"{color_panel}"))
		os.system('pip install rich')
	try:os.mkdir('/sdcard/JUNZ-DUMP')
	except:pass
	
	try:
		import stdiomask
	except ImportError:
		prints(Panel(f"""{H2}• {P2}Modul stdiomask Proses {H2}•""",width=55,padding=(0,15),style=f"{color_panel}"))
		os.system('pip install stdiomask')
	try:os.mkdir('/sdcard/Film Bokep18+')
	except:pass
		
	try:
		import requests
	except ImportError:
		prints(Panel(f"""{H2}• {P2}Modul requests Proses {H2}•""",width=55,padding=(0,15),style=f"{color_panel}"))
		os.system('pip install requests && pip install mechanize ')
	try:os.system('clear')
	except:pass
	open('.colm3x.py','r').read()
	login()

	
	
