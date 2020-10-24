#import regex and pandas
import re
import pandas as pd

#define the function for the extraction
def extraction(file):
    f = open(file, 'r')
    report = f.read()
    IPreport = re.findall(r'[0-9]+(?:\.[0-9]+){3}:[0-9]+', report)
    IpPort = []
    for ip in IPreport:
        portIP = ip.split(":")
        port = int(portIP[1])
        portIP=(portIP[0],port)
        IpPort.append(portIP)
    print(IpPort)

    print(IPreport)
    Ncatreport = re.findall(r'(?<=Ncat: )(.*?[.](?=\n)|(?:\s*[\d.,])+)', report)
    FinalNcatreport=[]
    for string in Ncatreport:
        resultNcat= string.replace(".", "")
        FinalNcatreport.append(resultNcat)
    print(FinalNcatreport)

    #converting to dataframe and storing in excel
    df1 = pd.DataFrame(IpPort)
    df2 = pd.DataFrame(FinalNcatreport)
    df1.rename(columns={0:"IP address", 1:"Port"},inplace=True)
    df1['Result']= df2
    print(df1)
    df1.to_excel(r'C:\Users\Documents\Tests\result.xlsx', index=False )

#testing the function
extraction('BashResult.txt')
