###### A quick demo of Python and Regex 

**Input:** .txt or logfile with a list of IP addresses and ports that were pinged  
**Output:** Prints output and alerts when >3 ports were scanned on an IP  

#### Primary Ingredients: 
&nbsp;&nbsp;&nbsp;+ **iplogs.txt:** An example file that the script ingests, consisting of the format <IP Address>:<Port       
&nbsp;&nbsp;&nbsp;+ **regex-pi.py:** The main script that ingests the logfile and identifies IP's   
&nbsp;&nbsp;&nbsp;+ **reg-pi.py:** Initial approach using an object approach  
&nbsp;&nbsp;&nbsp;+ **ipObject.py:** Object to contain IP addresses that reg-pi.py gleaned
        -  
 
 
 
 
 
 
 
##### How to Run:
````
&nbsp;> python regex-pi.py

&nbsp;IPAddress ----> 192.168.1.1
&nbsp; Ports ----> ['18', '22', '21', '80']

&nbsp;ALERT::: MORE THAN 3 PORTS WERE SCANNED AT THIS IP ----> 192.168.1.1


&nbsp;IPAddress ----> 192.1.1.4
&nbsp; Ports ----> ['39']

&nbsp;IPAddress ----> 192.1.5.6
&nbsp; Ports ----> ['20', '21']

&nbsp;IPAddress ----> 192.1.5.4
&nbsp; Ports ----> ['22']

&nbsp;IPAddress ----> 10.0.0.1
&nbsp; Ports ----> ['190', '45160']

&nbsp;IPAddress ----> 10.2.14.13
&nbsp; Ports ----> ['0', '1', '2']

&nbsp;ALERT::: MORE THAN 3 PORTS WERE SCANNED AT THIS IP ----> 10.2.14.13



&nbsp;At the Last Value

&nbsp;IPAddress ---->  10.2.14.113  Ports::
&nbsp; ['0']

````
