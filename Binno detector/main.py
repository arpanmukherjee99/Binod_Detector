import os

def isBinod(filename):
    with open(filename, "r") as f:
        fileContent = f.read()
    #detect all forms of binod like biNOd    
    if "binod" in fileContent.lower():
        return True
    else:
        return False

if __name__=="__main__":
    #listing the contents of this folder
    dir_contents = os.listdir()
    nBinod=0
    #for each text file, run isBiod for them
    for item in dir_contents:        
        if item.endswith('txt'):    
            print(f"Detecting Binod in {item}")  
            flag = isBinod(item)
            if (flag):
                print(f"*****WARNING*******Binod found in {item}")
                nBinod+=1
            else:
                print(f"Binod not found in {item}")
print("____________Binod detector summery____________")
print(f"{nBinod} files found with Binod into them")
  