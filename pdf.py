#srinuneelapala

import requests 
file_url = "http://10.11.4.25/2019-QPandKeys/Sem1/AT-1/CSE/QP's/E2/E2CSE-"
folder= 'C:\\Users\PYTHON\\Desktop\\OOPS-Weekend'
for i in range(1,9):
    sub='\\OOPS-AT'+str(i)+".pdf"
    url=file_url+sub
    r = requests.get(url) 

    with open(folder+sub,"wb") as pdf: 
        pdf.write(r.content)





