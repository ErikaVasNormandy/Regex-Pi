###### A quick demo of Python and Regex 

**Input:** .txt or logfile with a list of IP addresses and ports that were pinged  
**Output:** Prints output and alerts when >3 ports were scanned on an IP  

##### Primary Ingredients: 
    + Python 3
    + IP file in .txt format
        -  <IP Address>:<Port>
 
##### How to Run:
````
> python regex-pi.py

IPAddress ----> 192.168.1.1
 Ports ----> ['18', '22', '21', '80']

ALERT::: MORE THAN 3 PORTS WERE SCANNED AT THIS IP ----> 192.168.1.1


IPAddress ----> 192.1.1.4
 Ports ----> ['39']

IPAddress ----> 192.1.5.6
 Ports ----> ['20', '21']

IPAddress ----> 192.1.5.4
 Ports ----> ['22']

IPAddress ----> 10.0.0.1
 Ports ----> ['190', '45160']

IPAddress ----> 10.2.14.13
 Ports ----> ['0', '1', '2']

ALERT::: MORE THAN 3 PORTS WERE SCANNED AT THIS IP ----> 10.2.14.13



At the Last Value

IPAddress ---->  10.2.14.113  Ports::
 ['0']

````
