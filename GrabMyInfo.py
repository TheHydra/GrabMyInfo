'''

Created on (I don't remember xD)
@author: The-Hydra (aka Abdel-Rahman Mohamed Moez)

This script grabs lots of info about your PC. Info about Windows, 
Network, Memory, Drives, Proccessor, BIOS, Video Card, Printers (If installed)
and List you all the applications which start on Startup of windows (According to registry)

# Check importing modules part, and if you miss any module download it,
# and If you want to run the program without installing the modules,
# here's an executable version of the script: http://www.mediafire.com/?xojtjvri970z8k2
# and this is the virus scan: https://www.virustotal.com/en/file/9bf1702bb88a4e0f309131a48ef65a0da8e4fa97664dcdaf4490bfde52d08c41/analysis/1371231821/
#You will find 1 threat in the scan,I don't know why this One threat, the program is clean!
''''
#
from wmi import WMI
from re import search
from colorama import *
import os
from socket import gethostbyname, gethostname
import _winreg
from urllib import urlopen
init(autoreset=True)
os.system("cls")
os.system("title Grab My Info v 1.0                                                                                      ^|  Copyright (c) The-Hydra")
print Style.BRIGHT+Fore.GREEN+"*"*79
print Style.BRIGHT+Fore.WHITE+Back.RED+"\t\t\t\t Grab My Info\t\t\t\t       "
print Style.BRIGHT+Fore.GREEN+"*"*79
print Style.BRIGHT+Fore.YELLOW+"\t\t\t     Coded By: "+Fore.CYAN+"The-Hydra"
# Windows ---------------------- #
print Style.BRIGHT+Fore.RED+'\n\n[+] Windows:'
windows = {
  '\tWindows Name:':WMI().query('SELECT Caption FROM Win32_OperatingSystem')[0].Caption,
	'\tWindows Version:': WMI().query('SELECT Version FROM Win32_OperatingSystem')[0].Version,
	'\tOrganization:': WMI().query('SELECT Organization FROM Win32_OperatingSystem')[0].Organization,
	'\tOS Architecture': WMI().query('SELECT OSArchitecture FROM Win32_OperatingSystem')[0].OSArchitecture,
	'\tRegistered User:': WMI().query('SELECT RegisteredUser FROM Win32_OperatingSystem')[0].RegisteredUser,
	'\tSystem Dir:':WMI().query('SELECT SystemDirectory FROM Win32_OperatingSystem')[0].SystemDirectory,
	'\tSerialNumber:':WMI().query('SELECT SerialNumber FROM Win32_OperatingSystem')[0].SerialNumber,
	'\tManufacturer:': WMI().query('SELECT Manufacturer FROM Win32_OperatingSystem')[0].Manufacturer,
	'\tNumber Of Users:': WMI().query('SELECT NumberOfUsers FROM Win32_OperatingSystem')[0].NumberOfUsers}
for x,y in windows.items():
	print Fore.CYAN+x, Fore.WHITE+Style.BRIGHT+str(y)
# Network ---------------------- #
print Style.BRIGHT+Fore.RED+'[+] Network:'
try:
	address = "http://www.ipchicken.com"
	string = urlopen(address).read()
	EX_IP = search(r'\d+\.\d+\.\d+\.\d+', string).group()
except: EX_IP = Fore.RED+"No Internet Connection!"
print Fore.CYAN+'\tExternal IP:', Fore.WHITE+Style.BRIGHT+EX_IP
print Fore.CYAN+'\tInternal IP:', Fore.WHITE+Style.BRIGHT+gethostbyname(gethostname())
print Fore.CYAN+'\tHostname:', Fore.WHITE+Style.BRIGHT+gethostname()
for line in os.popen('ipconfig /all'):
	if line.lstrip().startswith('Physical Address'):
		mac = line.split(':')[1].strip()
		print Fore.CYAN+'\tMAC Address:'+ Fore.WHITE+Style.BRIGHT+mac
	if line.lstrip().startswith('Default Gateway'):
		gateway = line.split(':')[1].strip()
		print Fore.CYAN+'\tDefault Gateway:'+ Fore.WHITE+Style.BRIGHT+gateway
	if line.lstrip().startswith('Description'):
		NIC = line.split(':')[1].strip()	
		print Fore.CYAN+'\tNIC:'+ Fore.WHITE+Style.BRIGHT+NIC
	
# Memory ----------------------- #
print Style.BRIGHT+Fore.RED+'[+] Memory:'
memory = {
	'\tTotal Memory(RAM):':'%.2f' % (float(WMI().query('SELECT TotalVisibleMemorySize FROM Win32_OperatingSystem')[0].TotalVisibleMemorySize)/1024)+ str(" MB"),
	'\tFree Memory(RAM):':'%.2f' % (float(WMI().query('SELECT FreePhysicalMemory  FROM Win32_OperatingSystem')[0].FreePhysicalMemory)/1024)+ str(" MB")}
for x,y in memory.items():
	print Fore.CYAN+x,Fore.WHITE+Style.BRIGHT+y
# Drives ------------------------#
NumOfDrives = 0
x = 0
for one in WMI().query("SELECT * FROM Win32_LogicalDisk"): NumOfDrives+=1
print Style.BRIGHT+Fore.RED+"[+] Drives"
for x in xrange(NumOfDrives):
	total_ = str(WMI().query("SELECT Size FROM Win32_LogicalDisk")[x].Size)
	free_ = str(WMI().query("SELECT FreeSpace FROM Win32_LogicalDisk")[x].FreeSpace)
	try:
		used_ = (float(total_)/float(1024**3))-(float(free_)/float(1024**3))
	except: pass
	print Style.BRIGHT+Fore.YELLOW+"\t\bDrive no. "+Style.BRIGHT+Fore.YELLOW+str(x+1)
	dic = {
	'\tDevice ID:':WMI().query("SELECT DeviceID FROM Win32_LogicalDisk")[x].DeviceID,
	'\tVolume Name:':WMI().query("SELECT VolumeName FROM Win32_LogicalDisk")[x].VolumeName,
	'\tFile System:':WMI().query("SELECT FileSystem FROM Win32_LogicalDisk")[x].FileSystem,
	'\tTotal Space:': str(total_) + "GB",
	'\tFree Space:': str(free_)+ "GB",
	'\tUsed Space:': str(used_)+ "GB",
	'\tVolume Serial Number: ': WMI().query("SELECT VolumeSerialNumber FROM Win32_LogicalDisk")[x].VolumeSerialNumber
	}
	for y,z in dic.items():
		print Fore.CYAN+str(y), Style.BRIGHT+Fore.WHITE+str(z)
	x =+ 1
# Processors ------------------ #
print Style.BRIGHT+Fore.RED+"[+] Processor(s):"
processors = {
	'\tNumber Of Processor(s):':WMI().query("SELECT NumberOfCores FROM Win32_Processor")[0].NumberOfCores,
	'\tName:':WMI().query("SELECT Name FROM Win32_Processor")[0].Name,
	'\tDescription:':WMI().query("SELECT Description FROM Win32_Processor")[0].Description,
	'\tManufacturer:':WMI().query("SELECT Manufacturer FROM Win32_Processor")[0].Manufacturer}
for x,y in processors.items():
	print Fore.CYAN+x,Fore.WHITE+Style.BRIGHT+str(y)
# BIOS ------------------------ #
print Style.BRIGHT+Fore.RED+"[+] BIOS:"
regConnect = _winreg.ConnectRegistry(None, _winreg.HKEY_LOCAL_MACHINE)
winReg = _winreg.OpenKey(regConnect, r"HARDWARE\DESCRIPTION\System\BIOS")
try:
	for i in range(1024):
		subkey  = _winreg.EnumValue(winReg,i)
		if subkey[0] == '\tBaseBoardManufacturer':
			print Fore.CYAN+'\tBase Board Manufacturer:', Fore.WHITE+Style.BRIGHT+subkey[1]
		if subkey[0] == 'BIOSReleaseDate':
			print Fore.CYAN+'\tBIOS Release Date:', Fore.WHITE+Style.BRIGHT+subkey[1]
		if subkey[0] == 'BIOSVendor':
			print Fore.CYAN+'\tBIOS Vendor:', Fore.WHITE+Style.BRIGHT+subkey[1]
		if subkey[0] == 'BIOSVersion':
			print Fore.CYAN+'\tBIOS Version:', Fore.WHITE+Style.BRIGHT+subkey[1]
		if subkey[0] == 'SystemManufacturer':
			print Fore.CYAN+'\tSystem Manufacturer:', Fore.WHITE+Style.BRIGHT+subkey[1]
except: pass
# Video Card ------------------ #
print Style.BRIGHT+Fore.RED+"[+] Video Card:"
date = WMI().query("SELECT DriverDate FROM Win32_VideoController")[0].DriverDate
AdapterRAM = float(WMI().query("SELECT AdapterRAM FROM Win32_VideoController")[0].AdapterRAM)
video = {
	'\tAdapter Compatibility:':WMI().query("SELECT AdapterCompatibility FROM Win32_VideoController")[0].AdapterCompatibility,
	'\tAdapter DAC Type:': WMI().query("SELECT AdapterDACType FROM Win32_VideoController")[0].AdapterDACType,
	'\tAdapter RAM:': str(AdapterRAM/(1024**2))+ ' MB == '+ str(AdapterRAM/(1024**3))+ ' GB',
	'\tName:':WMI().query("SELECT Name FROM Win32_VideoController")[0].Name,
	'\tDriver Date:': date[0:4]+'-'+date[4:6]+'-'+date[6:8],
	'\tDriver Version:':WMI().query("SELECT DriverVersion FROM Win32_VideoController")[0].DriverVersion,
	'\tVideo Processor:':WMI().query("SELECT VideoProcessor FROM Win32_VideoController")[0].VideoProcessor}
for x,y in video.items():
	print Fore.CYAN+x,Fore.WHITE+Style.BRIGHT+y
# Installed Printers ---------- #
print Style.BRIGHT+Fore.RED+"[+] Printers:"
try:
	for x in WMI().query('SELECT * FROM Win32_Printer'):
		print Fore.CYAN+"\tName:" ,Style.BRIGHT+ str(x.Name)
		print Fore.CYAN+"\tPort Name:",Style.BRIGHT+str(x.PortName)
		print Fore.CYAN+"\tShared:",Style.BRIGHT+str(x.Shared)
		print 
except: print Fore.RED+"\t No printers are installed on your Machine!"
# Start Up:
print Style.BRIGHT+Fore.RED+"[+] Start Up Applications:"
regConnect = _winreg.ConnectRegistry(None, _winreg.HKEY_LOCAL_MACHINE)
winReg = _winreg.OpenKey(regConnect, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run")
print Style.BRIGHT+Fore.YELLOW+"\t[-] Local Machine:"
try:
	for i in range(1024):
		subkey = _winreg.EnumValue(winReg, i)
		print Fore.CYAN+"\t Name:",Fore.WHITE+Style.BRIGHT+subkey[0]
		print Fore.CYAN+"\t Path:",Fore.WHITE+Style.BRIGHT+subkey[1]+'\n'
except: pass
######################
print Style.BRIGHT+Fore.YELLOW+"\t[-] Current User:"
regConnect = _winreg.ConnectRegistry(None, _winreg.HKEY_CURRENT_USER)
winReg = _winreg.OpenKey(regConnect, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run")
try:
	for i in range(1024):
		subkey = _winreg.EnumValue(winReg, i)
		print Fore.CYAN+"\t Name:",Fore.WHITE+Style.BRIGHT+subkey[0]
		print Fore.CYAN+"\t Path:",Fore.WHITE+Style.BRIGHT+subkey[1]+'\n'
except: pass
raw_input('\n\\')
