import os
import zipfile
import shutil

#This line finds all the files in the current dir ending with ".app"
files = [f for f in os.listdir('.') if os.path.isfile(f) and f.split(".")[1] == "app"]

#Iterating throught all the pertinent files
for f in files:
    #Change the extension from .app to .zip
    nameWithoutExt = f.split(".")[0]
    nameWithZipExt = nameWithoutExt + ".zip"
    os.rename(f, nameWithZipExt)
    #Extract the file
    with zipfile.ZipFile(nameWithZipExt, 'r') as zip_ref:
        zip_ref.extractall(nameWithoutExt)
    #Copy Runner.app to Payload
    shutil.copytree('Runner\\', 'temp\\')
    #Zip the Payload folder
    shutil.make_archive("Payload", 'zip', "temp")
    #Rename the file from zip to ipa
    os.rename("Payload.zip", "Payload.ipa")
    #Clean up
    os.remove(nameWithZipExt)
    shutil.rmtree("Runner")
    shutil.rmtree("temp")