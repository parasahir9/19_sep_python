string=input("enter your string--")

if len(string) > 3:
    if string.endswith("ing"):
        new_string=string + "ly"
        print("new string is -",new_string)
    else:
        new_string=string+"ing"
        
        print("new string is-", new_string)
else:
    print("unchanged string ")            
    