from socket import *
import optparse
from threading import *

def scan(tgtHost,tgtPort):
  try:
    sock = socket(AF_INET,SOCK_STREAM)
    print(f"<> {tgtPort} Porti ochiq ekan !")
  except:
    print(f'<> {tgtPort} Porti yopiq ekan ')
  finally:
    sock.close()

def portscanner(tgtHost,tgtPorts):
  try:
    tgtIP = gethostbyname(tgtHost)
  except:
    print(f'{tgtHost} IP manzili topilmadi yoki domen xato')
  try:
    tgtName = gethostbyaddr(tgtIP)
    print(f'{tgtName} - ga tegishli')
  except:
    print(f"{tgtIP} uchun scanner natijalari ")
    setdefaulttimeout(10)
    for tgtPort in tgtPorts:
      t = Thread(target=scan,args=(tgtHost,int(tgtPort)))
      t.start()

def main():
    parser = optparse.OptionParser("Dasturdan Foydalanish  Tartibi : "+"--H <IP> --P <Port> ")
    parser.add_option('--H',dest='tgtHost',type='string',help='Nishonning IP manzilini kiriting')
    parser.add_option('--P',dest='tgtPort',type='string',help='Nishonning Portini kiriting')
    (options,args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPort = str(options.tgtPort).split(',')
    if (tgtHost == None) | (tgtPort[0] == None):
        print(parser.usage)
        exit()
    else:
        portscanner(tgtHost,tgtPort)
if __name__=='__main__':
    main()