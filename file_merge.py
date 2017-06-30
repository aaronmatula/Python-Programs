import glob2
import datetime

filenames=glob2.glob("Downloads/"+ "*.txt")

with open("Downloads/" + str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f"))+".txt", 'w') as file:
    file.seek(0)
    for filename in filenames:
        with open(filename,"r") as f:
            file.write(f.read()+"\n")