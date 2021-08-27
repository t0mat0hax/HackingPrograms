from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import 
from colorama import init, Fore, Back, Style


def banner():
    print(Style.DIM + Fore.RED + """
    
                                       .:-.                              
                                      /mmhyys                              
                                      /mmdyyh.                             
                             .+sys:    +mmdyy+                             
                             smdhyh.    -mmhyh`                            
                             -mmdhys     /mdhy/     `-.                    
                              /mmmdy/     hmdyy    :hhs/                   
                               smmmyh`   .dmdhy:  .mmhyy                   
                               +mmdyh-  .hmNmhy-  ommdyh-                  
                               /mmdyh  -dmdddy.   ymmdhy:                  
                               +mmhys :mmdhhy`  -ymmmds.  ``               
                     .oo/      ymmyyo+mmdhhs` -ymmmmh-  `ohh:              
                     shhmh`   -mmmhdmmmdhyy`.smmmmd/    ymmy/              
                    .y+dmmh   hmmmhhyyyyhhsommmddy`    :mmdyo              
                  .+s+shmms  smmddhhyyyyyyyyyyhhd-.:+ymmNmdhs              
                `yhhddddd/` +mmdhhhmhyyyyyyyyyyyyddmmmdddy+.               
                 hmdhhmh`  :mmmmmdddmmmdhhyyyyyyyhddddyo.`                 
                 -hhhdmm/osyhhhdmmmdddmmmmddhyyyyhdho-`                    
                  hhhdddyyyyyyyyydmmdhhdhdddddyyyh/.                       
                  +hmddhhhhhhhhyyydmdhddhyyhdhyyy.                         
                   .sdmdddhhhhhhhyymdhmmdhyyyyyd-                          
                     .odmmydhhhhhhhhhhdmmdhyyydy                           
                       -ydmmmdddddmddddmmmdhyhd.                           
                         ./oyddNNmmmNmmmmmmmmm+                            
                               hmmmmNmNNNNmmNs                             
                               :mmmmNmNNmmdhh-                             
                                +mmmMmNNmmhyy+                             
                                ydmmMmNNmmhhyy                             
                               .dhmmNmNNmmhhyh.                            
                               ohhmmmmNNmmhhyyo                            
                              `dhhmmmmNNmdhhhyh`                           
                         -++. sddddmmmNmmdhhyyy+                           
                         ``+dyMMmdmmmmNmNdddosyy    `.-..``....-.--`       
          ..--------:::::os/oh+oosydmmNNmddddmmNyyydhs+oo+//:-.....`   

                    ┏━━━┳┓╋╋╋╋╋╋╋╋╋╋╋┏━━━┓╋╋╋╋┏┓╋┏┓
                    ┃┏━┓┃┃╋╋╋╋╋╋╋╋╋╋╋┃┏━┓┃╋╋╋╋┃┃╋┃┃ v 1.00
                    ┃┗━┛┃┗━┳━━┳━┓┏━━┓┃┃╋┗╋━┳━━┫┗━┫┗━┳━━┳━┓
                    ┃┏━━┫┏┓┃┏┓┃┏┓┫┃━┫┃┃┏━┫┏┫┏┓┃┏┓┃┏┓┃┃━┫┏┛
                    ┃┃╋╋┃┃┃┃┗┛┃┃┃┃┃━┫┃┗┻━┃┃┃┏┓┃┗┛┃┗┛┃┃━┫┃ 
                    ┗┛╋╋┗┛┗┻━━┻┛┗┻━━┛┗━━━┻┛┗┛┗┻━━┻━━┻━━┻┛  
                                            by Parrothax
  
    """)

def phone_info():
    number = input(Style.BRIGHT + Fore.GREEN + "[+]Please enter number to identify starting with country code as + | eg. (+19999999999) [+] >> ")
    ch_number = phonenumbers.parse(number, "CH")
    service_n = phonenumbers.parse(number, "RO")
    print(Style.BRIGHT + Fore.GREEN + geocoder.description_for_number(ch_number, "en"))
    print(Style.BRIGHT + Fore.GREEN + carrier.name_for_number(service_n, "en"))

banner()
phone_info()