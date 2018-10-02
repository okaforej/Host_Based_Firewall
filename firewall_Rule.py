import pandas as pd
columns_header= ['direction', 'protocol', 'port', 'ip_address']

def load_data():
    ## Change the file path to include the link to the input file.
    filepath = "testfile.csv" 
    ## Read the input file using pandas and store the column new header to easily access them
    dfi = pd.read_csv(filepath,  header=None, names=columns_header)
    # iterated over each row in pandas data structure and checked that all rules are met.
    for row in dfi.itertuples():
        if row.direction in ('inbound', 'outbound') and row.protocol in ('tcp', 'udp') and portChecker(row.port) == True and DashSplit(row.ip_address) == True:
            print(True, row)
        else: print(False, row)


# Function to validate port range
def validPort(port): # check if the port number is within the range 1 - 65535 (65536)
    return False if not int(port) in range(1, 65536) else  True

#function to analyse port number/range provided. This function split port range and calls validport function to validate the port number.
# Check port range
#split port range with hyphen
def portChecker(port):
    port = str(port).strip()
    dash = port.count('-')
    if dash == 0:
        return False if validPort(port) == False else True
    elif dash > 0:
        val=port.split('-')
        if not val[0]<val[len(val)-1]: return False
        for i in range(len(val)):
            if validPort(val[i]) == False: return False
        return True
def validIP(IP_add):
    IP_add= str(IP_add).split(".")
    if len(IP_add) != 4: return False
    for item in IP_add:
        if not 0 <= int(item) <= 255: return False
    return True

#Function to split IP address.
def DashSplit(IP_add):
    IP_add = IP_add.strip()
    dash = IP_add.count("-")
    if dash == 0:
        if validIP(IP_add) is True: return True 
        else: return False
    elif dash > 0:
        ip=IP_add.split("-")
        #if not ip[0]<ip[len(ip)-1]: return False
        for i in range(len(ip)-1):
            if validIP(ip[i]) == False: return False
        return True
print(load_data())