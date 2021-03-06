#--------------------------------
# Open file via thinter
# read all sites saved in file.
# check response the site and time of response
#-------------------------------
import requests, time
from tkinter import filedialog as fd

def get_Adresses(file_path):
 with open(file_path, "r", encoding="UTF-8") as file:
# Read single line in file
   for line in file:
     file_line = line.strip()
# Check request and responese
     #Measure time of response
     try:
        start =time.time()
    # payload = {"id": "1' and if (ascii(substr(database(), 1, 1))=115,sleep(3),null) -- "}
        response = requests.get(file_line)#,#params=payload)
     # Compare last time and start
        trip_time =time.time() - start
        if (response.status_code == 200):
             print(file_line)
             print ("Response time",trip_time)
       # print(response.status_code)
        else:
             print(file_line,"-Site doesn't exist")
     except requests.exceptions.ConnectionError as e:
            print(e)

 # Close opened file
 file.close()
# Open filedialog
filename = fd.askopenfilename()
# run and print
print(get_Adresses(filename))
