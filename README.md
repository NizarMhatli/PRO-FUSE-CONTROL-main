# PRO-FUSE-CONTROL
Package to control the Vanguard PRO-FUSE digital industrial screw driver  
hardware : https://www.hp-vanguard.com/products/2015101425/

# Introduction: 

Package to control the PRO-FUSE screw driver.
This package contains different commands to control the screw driver remotely


# Set-up: 
1- First power on the PRO-FUSE 
2- Enter Setting menu 
3- Enter the Network menu 
4- In the Network menu set up the IP address , Subnet and Gateway in our case we are using: 

[Gateway : 192.168.20.254]

[IP : 192.168.20.99]

[Subnet : 255.255.255.0]


5- Use the setup network to create TCP/IP communication on the PC you will use for remote control:
- In ubuntu OS : 



![ubuntu-os](https://user-images.githubusercontent.com/47193436/146130947-4e1c476d-ce18-4f0e-bcc4-b2184f0c0150.png)




- In Windows OS : 



![Capture_250](https://user-images.githubusercontent.com/47193436/146131158-23a69923-8c53-4e13-a90a-2f88aad73770.PNG)



#   Functions: 



1-  UUID_get() : used to get working UUID 

2-  Z_Homing () : used to set Z-axsis home point 

3-  PRO_SCREW_pik() : used to pick up screw 

4-  PRO_SCREW_in() : used to intiate screw in 

5-  PRO_SCREW_out() : used to intiate un-screw motion 

6-  PRO_SCREW_pik_RE() : used to pick up screw and return response from device

7-  PRO_SCREW_in_RE() : used to intiate screw in and return response from device

8-  PRO_SCREW_out_RE() : used to intiate un-screw motion and return response from device

9-  PRO_PARA_IN() : used to get the current device parameters 

10- PRO_CANCEL_C() : used to cancel current command

11- PRO_DATA_IN() : used to get result data in remote device as json file (currently not working on relay PC update needed) 



# Usage

-To test the program just run the SCrew_pa_test.py program 

-To  use on different programs just import PRO-FUSE-SOFT and import the command you need to run 


