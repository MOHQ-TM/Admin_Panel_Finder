import requests as r
import os


class color:
	GREEN = '\033[92m'
	GREEN1 = '\033[32m'
	WHITE = '\033[0m'
	RED = '\033[91m'
	BLUE = '\033[96m'


try:

	os.system('clear')
	
	
	print(color.GREEN1 + '')
	
	print('███╗   ███╗ ██████╗ ██╗  ██╗ ██████╗     ████████╗███╗   ███╗')
	print('████╗ ████║██╔═══██╗██║  ██║██╔═══██╗    ╚══██╔══╝████╗ ████║')
	print('██╔████╔██║██║   ██║███████║██║   ██║       ██║   ██╔████╔██║')
	print('██║╚██╔╝██║██║   ██║██╔══██║██║▄▄ ██║       ██║   ██║╚██╔╝██║')
	print('██║ ╚═╝ ██║╚██████╔╝██║  ██║╚██████╔╝       ██║   ██║ ╚═╝ ██║')
	print('╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚══▀▀═╝        ╚═╝   ╚═╝     ╚═╝')
	print(color.GREEN + '                            ************************************')
	print('                            ** Telegram : @MOHQ_Team **')
	print('                            **     Email : mohq@gmail.com     **')
	print('                            ************************************')
	print('ctrl+c for exit!')


	#url
	url = str(input (color.BLUE+"Enter your target address (Example: www.google.com) : "))
    
	#admin_list
	ad_list=open("admin.txt","r")
    
	#range
	if "http://" in url :
    
		ulr = (url + "/")
        
	elif "https://" in url :
    
		url = (url + "/")
        
	else :
    
		url = ("https://" + url + "/")




	for i in ad_list:
    
		req=r.post(url+i.strip())
        
	if req.status_code == 200:
        
		print("{} Admin Panel {} => {} {} {} Found".format(color.GREEN,color.RED,color.GREEN1,url+i,color.GREEN))
            
		f=open("result.txt","a+")
            
		f.write(str(url+i))
            

	else:
        
		print("{} Not Found {} {}".format(color.RED,color.WHITE,url+i))
            
            
except :
	os.system('clear')
	print (color.BLUE + "\nOK goodbye !!!")
