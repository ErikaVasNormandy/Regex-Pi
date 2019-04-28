**A quick demo of Python and Regex**

**Input:** .txt or logfile with a list of IP addresses and ports that were pinged  
**Output:** Prints output and alerts when >3 ports were scanned on an IP  

### Primary Ingredients: 
&nbsp;&nbsp;&nbsp;+ **iplogs.txt:** An example file that the script ingests, consisting of the format <IP Address>:<Port       
&nbsp;&nbsp;&nbsp;+ **regex-pi.py:** The main script that ingests the logfile and identifies IP's   
&nbsp;&nbsp;&nbsp;+ **reg-pi.py:** Initial approach using an object approach  
&nbsp;&nbsp;&nbsp;+ **ipObject.py:** Object to contain IP addresses that reg-pi.py gleaned

 
### How to Run:

**python regex-pi.py**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IPAddress ----> 192.168.1.1  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Ports ----> ['18', '22', '21', '80']  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ALERT::: MORE THAN 3 PORTS WERE SCANNED AT THIS IP ----> 192.168.1.1  


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IPAddress ----> 192.1.1.4  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Ports ----> ['39']  
...

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ALERT::: MORE THAN 3 PORTS WERE SCANNED AT THIS IP ----> 10.2.14.13  



&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;At the Last Value  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IPAddress ---->  10.2.14.113  Ports::  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ['0']  

Example Screenshot:
![How to Run](https://raw.githubusercontent.com/ErikaVasNormandy/Regex-Pi/master/01HowToRun.png)


### Explanation:
