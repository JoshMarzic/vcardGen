import csv

#program to import CSV -> translate to Vcard 3.0 format
#https://en.wikipedia.org/wiki/VCard#vCard_3.0 if needed in the future!
#author - Josh Marzic

#Open Book2.csv (note name hard coded, could be changed in future)
with open('ContactCSV.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    fnames = []
    lnames = []
    titles = []
    numbers = []
    locations = []
    extensions = []
    emails = []
    
    for row in readCSV:
        #read in each bit of data, store into a variable (called dataType)
        fname = row[0]
        lname = row[1]
        title = row[2]
        location = row[3]
        number = row[4]
        extension = row[5]
        email = row[6]
        
        #add each item to its coresponding array
        fnames.append(fname)
        lnames.append(lname)
        numbers.append(number)
        titles.append(title)
        locations.append(location)
        extensions.append(extension)
        emails.append(email)
        

    #print(fnames)
    #print(lnames)
    #print(numbers)

f = open("vcard3.txt","w+")
i = 0
for i in range(len(fnames)):
    f.write("BEGIN:VCARD\n")
    f.write("VERSION:3.0\n")
    f.write("N:" + lnames[i] + ";" + fnames[i] + ";;;\n")
    f.write("FN:" + fnames[i] + " " + lnames[i] +"\n")
    f.write("ORG: J. Ranck Electric, Inc. (Ext." + extensions[i] + ")\n") #ORG includes person's extension at end
    f.write("TITLE:" + titles[i] +"\n")
    f.write("TEL;TYPE=WORK,VOICE:" +  numbers[i] + "\n")

    #determine the person's location, and write out the specific address / field for that location  
    if locations[i] == "MP":
        f.write("ADR;TYPE=WORK,PREF:;1993 Gover Pkwy;Mt. Pleasant;MI;48858;United States of America\n")
    elif locations[i] == "FNT":
        f.write("ADR;TYPE=WORK,PREF:;3015 Airpark Drive N.;Flint;MI;48507;United States of America\n")
    elif locations[i] == "MPMECH":
        f.write("ADR;TYPE=WORK,PREF:;1993 Gover Pkwy;Mt. Pleasant;MI;48858;United States of America\n")
    elif locations[i] == "JOBSITE":
        f.write("ADR;TYPE=WORK,PREF:Job Site;Unkown;MI;;United States of America\n")
    elif locations[i] == "MPWH":
        f.write("ADR;TYPE=WORK,PREF:;1993 Gover Pkwy;Mt. Pleasant;MI;48858;United States of America\n")
    elif locations[i] == "SSM":
        f.write("ADR;TYPE=WORK,PREF:;3137 South Baker Side Rd;Sault Ste. Marie;MI;49783;United States of America\n")
    elif locations[i] == "SSMWH":
        f.write("ADR;TYPE=WORK,PREF:;3137 South Baker Side Rd;Sault Ste. Marie;MI;49783;United States of America\n")
    elif locations[i] == "CLWH":
        f.write("ADR;TYPE=WORK,PREF:;23862 Sherwood Ave;Center Line;MI;48015;United States of America\n")

    #email
    f.write("EMAIL:" + emails[i] + "\n")
 
    
    f.write("END:VCARD\n")
    
f.close()
