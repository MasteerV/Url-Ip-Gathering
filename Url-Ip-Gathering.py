import subprocess
import os

def ascii_art():
    os.system('clear')
    print("")
    print("""        .-'~"-.""")
    print("""       / `-    \\""")
    print("""      />  `.  -.|""")
    print("""     /_     '-.__)""")
    print("""      |-  _.' \ | """)
    print("""      `~~;     \\""")
    print("""         /      \\   Url-Ip-Gathering""")
    print("""        '.___.-'`     from MasteerV""")
    print("")
    print("")

#function to enter a valid url
def input_url_function():
    #while loop to check that url is valid
    while True:
        input_url = input('Enter URL to get Ips > > > ')
        if 'https://' in input_url or 'http://' in input_url:
            break
        else:
            print('Invalid URL, try again')
    #the function return input_url
    return input_url



#function to filter the source code
def filtered_source_code(input_url):
    #with 'wget' we copy the source code of web page
    subprocess.run(['wget', str(input_url)])
    #with 'grep' and 'cut' we will filter lines to only show the links
    os.system('grep "href=" index.html > source_code.txt')
    os.system('cut -d "/" -f3 source_code.txt > source_code1.txt')
    os.system('grep "\." source_code1.txt > source_code2.txt')
    os.system('cut -d \'"\' -f1 source_code2.txt > source_code3.txt')
    os.system('grep "\." source_code3.txt > source_code4.txt')
    os.system('sort -u source_code4.txt > source_code5.txt')

#function to discover ips with 'host'
def host_ip_discover():
    os.system('clear')
    #we will create a script in bash to make host each line and filter to take only ips
    os.system('echo \'for dom in $(cat source_code5.txt); do host $dom | grep \"has address\" | cut -d \" \" -f4; done\' > ip_discover.sh') 
    #we run the script
    os.system('bash ip_discover.sh')
    #and remove leftover files
    os.system('rm source_code*')
    os.remove('ip_discover.sh')
    os.remove('index.html')

ascii_art()
filtered_source_code(input_url_function())    
host_ip_discover()