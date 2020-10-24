import re
import pandas as pd
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

    print(len(IPreport))
    print(IPreport)
    Ncatreport = re.findall(r'(?<=Ncat: )(.*?[.](?=\n)|(?:\s*[\d.,])+)', report)
    FinalNcatreport=[]
    for string in Ncatreport:
        resultNcat= string.replace(".", "")
        FinalNcatreport.append(resultNcat)
    print(FinalNcatreport)

    # Ncatreport = re.findall(r'(?<=Ncat: )(.*?host|.*?out|(?:\s*[\d.,])+)', report)

    df1 = pd.DataFrame(IpPort)
    df2 = pd.DataFrame(FinalNcatreport)
    df1.rename(columns={0:"IP address", 1:"Port"},inplace=True)
    df1['Result']= df2
    print(df1)
    df1.to_excel(r'C:\Users\MIRACLE\Documents\2020.08.19 - 172.17.251.114 Tests\result.xlsx', index=False )


extraction('Batch 6.txt')