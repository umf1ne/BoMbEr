"""
╔═════════════════════════════════════════════════════════════════════════════════╗
║                                                                                 ║
║                                    BoMbEr 2.0                                   ║
║  Authors:                                                                       ║
║  https://github.com/ebankoff                                                    ║
║  https://github.com/cludeex                                                     ║
║  https://github.com/ncorbuk                                                     ║
║  https://github.com/Nikait                                                      ║
║                                                                                 ║
║  The authors of this program are not responsible for its use!                   ║
║  When placing this code on third-party resources, please indicate the authors!  ║
║                                                                                 ║
║                               All rights reserved.                              ║
║                           Copyright (C) 2021 ebankoff                           ║
║                                                                                 ║
╚═════════════════════════════════════════════════════════════════════════════════╝
"""

#--------------------------------------(setup)--------------------------------------

import os
import time

os.system("cls")

def ex():
	param=input('Exit? yes/no: ')
	if param == 'yes':
		print("\033[36m{}" .format('''
╔═════════════════════════════════════════════════════════════════════════╗
║                                                                         ║
║                         Thanks for using BoMbEr!                        ║    
║      I would be grateful if you star on this repository on GitHub:      ║    
║                   https://github.com/ebankoff/BoMbEr                    ║
║                                                                         ║
║           You can support me by sending any amount to my Qiwi:          ║
║                           qiwi.com/n/HERAMANT                           ║
║                                                                         ║
║                       Copyright (C) 2021 ebankoff                       ║  
║                                                                         ║
╚═════════════════════════════════════════════════════════════════════════╝
			'''))
		print("Press Enter to exit")
		input()
		exit(0)
	elif param == 'no':
		main()
	else:
		print('ERROR: invalid value')
		ex()

def logo():
	print("\033[34m{}" .format('''╔══╗   ╔═╗╔═╦╗ ╔═══╗   ╔═══╦═══╦════╦╗ ╔╦═══╗
║╔╗║   ║ ╚╝ ║║ ║╔══╝   ║╔═╗║╔══╣╔╗╔╗║║ ║║╔═╗║
║╚╝╚╦══╣╔╗╔╗║╚═╣╚══╦═╗ ║╚══╣╚══╬╝║║╚╣║ ║║╚═╝║
║╔═╗║╔╗║║║║║║╔╗║╔══╣╔╝ ╚══╗║╔══╝ ║║ ║║ ║║╔══╝
║╚═╝║╚╝║║║║║║╚╝║╚══╣║  ║╚═╝║╚══╗ ║║ ║╚═╝║║
╚═══╩══╩╝╚╝╚╩══╩═══╩╝  ╚═══╩═══╝ ╚╝ ╚═══╩╝
	'''))

def main():
	ans=input("Now the program will install the necessary pip libraries, continue? (y/n): ")
	if(ans.lower() == "y"):
		print("\nSetup...")

		try:
			os.system('pip uninstall colorama')
			os.system('pip install colorama')
			print("\033[34m{}" .format(now.strftime('%Y-%m-%d / %H:%M:%S')) + "\033[37m {}" .format('|') + "\033[33m {}" .format('Installed') + "\033[37m {}" .format('|') + "\033[32m {}" .format(f'SUCCESS') + "\033[37m {}" .format('|') + "\033[35m {}" .format('colorama'))

			os.system('pip uninstall about-time')
			os.system('pip install about-time')
			print("\033[34m{}" .format(now.strftime('%Y-%m-%d / %H:%M:%S')) + "\033[37m {}" .format('|') + "\033[33m {}" .format('Installed') + "\033[37m {}" .format('|') + "\033[32m {}" .format(f'SUCCESS') + "\033[37m {}" .format('|') + "\033[35m {}" .format('about-time'))

			os.system('pip uninstall progressbar')
			os.system('pip install progressbar')
			print("\033[34m{}" .format(now.strftime('%Y-%m-%d / %H:%M:%S')) + "\033[37m {}" .format('|') + "\033[33m {}" .format('Installed') + "\033[37m {}" .format('|') + "\033[32m {}" .format(f'SUCCESS') + "\033[37m {}" .format('|') + "\033[35m {}" .format('progressbar'))

			os.system('pip uninstall progress')
			os.system('pip install progress')
			print("\033[34m{}" .format(now.strftime('%Y-%m-%d / %H:%M:%S')) + "\033[37m {}" .format('|') + "\033[33m {}" .format('Installed') + "\033[37m {}" .format('|') + "\033[32m {}" .format(f'SUCCESS') + "\033[37m {}" .format('|') + "\033[35m {}" .format('progress'))

			os.system('pip uninstall datetime')
			os.system('pip install datetime')
			print("\033[34m{}" .format(now.strftime('%Y-%m-%d / %H:%M:%S')) + "\033[37m {}" .format('|') + "\033[33m {}" .format('Installed') + "\033[37m {}" .format('|') + "\033[32m {}" .format(f'SUCCESS') + "\033[37m {}" .format('|') + "\033[35m {}" .format('datetime'))

			os.system('pip uninstall requests')
			os.system('pip install requests')
			print("\033[34m{}" .format(now.strftime('%Y-%m-%d / %H:%M:%S')) + "\033[37m {}" .format('|') + "\033[33m {}" .format('Installed') + "\033[37m {}" .format('|') + "\033[32m {}" .format(f'SUCCESS') + "\033[37m {}" .format('|') + "\033[35m {}" .format('requests'))

			os.system('pip uninstall selenium')
			os.system('pip install selenium')
			print("\033[34m{}" .format(now.strftime('%Y-%m-%d / %H:%M:%S')) + "\033[37m {}" .format('|') + "\033[33m {}" .format('Installed') + "\033[37m {}" .format('|') + "\033[32m {}" .format(f'SUCCESS') + "\033[37m {}" .format('|') + "\033[35m {}" .format('selenium'))

			os.system('pip uninstall webdriver-manager')
			os.system('pip install webdriver-manager')
			print("\033[34m{}" .format(now.strftime('%Y-%m-%d / %H:%M:%S')) + "\033[37m {}" .format('|') + "\033[33m {}" .format('Installed') + "\033[37m {}" .format('|') + "\033[32m {}" .format(f'SUCCESS') + "\033[37m {}" .format('|') + "\033[35m {}" .format('webdriver-manager'))

			os.system('pip uninstall wheel')
			os.system('pip install wheel')
			print("\033[34m{}" .format(now.strftime('%Y-%m-%d / %H:%M:%S')) + "\033[37m {}" .format('|') + "\033[33m {}" .format('Installed') + "\033[37m {}" .format('|') + "\033[32m {}" .format(f'SUCCESS') + "\033[37m {}" .format('|') + "\033[35m {}" .format('wheel'))

			os.system('pip uninstall user-agent')
			os.system('pip install user-agent')
			print("\033[34m{}" .format(now.strftime('%Y-%m-%d / %H:%M:%S')) + "\033[37m {}" .format('|') + "\033[33m {}" .format('Installed') + "\033[37m {}" .format('|') + "\033[32m {}" .format(f'SUCCESS') + "\033[37m {}" .format('|') + "\033[35m {}" .format('user-agent'))

			os.system('pip uninstall asyncio')
			os.system('pip install asyncio')
			print("\033[34m{}" .format(now.strftime('%Y-%m-%d / %H:%M:%S')) + "\033[37m {}" .format('|') + "\033[33m {}" .format('Installed') + "\033[37m {}" .format('|') + "\033[32m {}" .format(f'SUCCESS') + "\033[37m {}" .format('|') + "\033[35m {}" .format('asyncio'))

			print("\033[32m{}" .format("\nSetup is COMPLETE!"))

		except:
			print("\033[31m{}" .format("\nSetup FAILED!"))

		ex()

	elif(ans.lower() == "n"):
		print("\033[32m{}" .format("\nSetup is COMPLETE!"))
		ex()

	else:
		print("\033[31m{}" .format("\nERROR: INVALID VALUE!"))
		ex()

if __name__=='__main__':
	logo()
	main()