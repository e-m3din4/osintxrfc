# OSINT MX
## OSINT x RFC
This tool retrieves data from the SAT API, a mexican goverment dependency which deals with taxes in Mexican territory. This script is part of the OSNT MX Toolkit and is one of the few OSINT tools designed to retrieve and verify data in the OSINT investigations context in Mexico. Uses python's requests library and a config.json file containing your API keys managed by RFC SAT API available at RapidAPI.com, data points obtained aid to validate a Mexican citizen identity for OSINT research purposes, applied to missing person cases, fraud prevention and identity theft investigations.

### Prerequisites
Python 3.x requests library (pip3 install requests) A valid suscrisption to SAT API and its API key.

### Installation
Clone this repository to your local machine. Install the requests library by running pip install requests in your terminal.

### Configuration
Open the config.json file in the root directory of the repository. Replace "your_api_key_here" with your actual SAT API's RapidAPI key.

### Usage
In your terminal, navigate to the root directory of the repository. Run the following command:

python3 OSINT-x-RFC.py -h

					╓▄▓▌▀▓▓▓▓@▄▄,                              
			             .▄█▓▓▓▀╜└└╙╙▀▀▓▓▄¿                            
			            Å╙      ,▄▄▓▓▀▀▓█▀▀▄                           
			       ,         █▀▓▓▓▀▓▀Ñ▄▄▄▓▓▌   ,▓▓▓█▓▓▄,               
			  ,▄▓▓▀▀▀▓▓▓     █▀╫╫╫╫╫╫╫▓╩╨███   J█╫▓▓▓█▓╫▀▓▄            
			╥▓▌Ñ██▓█▓▓╫╫▌   █▀▓▓▓▓▓▓▓▌  ▄█▀█    ▌╫▓█▓▓▓▓▓▓▓█▄¿         
		      ╥▓█▓▓▓▓▓▓▓▓▓▒▓L  ▐▓▓▓█▓▓▓▌▓▌ ▄█▌█    ,▌╫▀█▓▓▀▓▓█▓█▓▀▄        
		     ▓▌▀▓▓▀████▀╫█▀█   █▓▓▓▓█▓▓▌▓▓█▓▀█    ▄▓╫╫▌▓▓▀▀█▓▓█╫▓▓▓█▄      
		   ▄█▓▓▓█▓█▓█▓█▓▓▓▓▓▓▄▓▓▓▓▓▓▓▓▓▓▓▀▓▓█▓▓▓▓▓▓▓█▀█▄▒██▓▓▌█╫█╫█▓▓▄     
		  ╥███▓╫▓╫▓╫█▀▓▓▓▓▓▀█▓▓█▓▓▓▓▓▓▓█▄▌▓█▌▀▓▓▀▓▀▓▓▓▓▓▓▓█▓█▓▀▌▀▌▓▓▓▓▌    
		 ,█▓╫█╫█▀▓▓▓▌▓▓▓▓╫▓▓▀▒█▓▓▓╫█▀▀█▀▌▓█╫▓▓▓█▓▓▓▓▓▓▓▀▓▓▓▓▓█╫█▓█▓▓█▓▓█   
		 █▓▓█▓█▓██▓▌██▓█▓█▓▒█▀█▓▓▓╫▌╫█▌▓▓██╫█╫▓▓▌▓▓▓▓▒▓█▓█▀██▓████▓██▓██▄  
		▄█▓╫█▀█▀█▓█╫█▓▓╫▓╫█▓█▓█▓▓█▓█▓▌╫▌█▓█╫▓▓▓▓█▓▓▓█▓▓▓▓▓▓╫█╫█▓█▓▓█▓▓▓▓█  
	       ╒██╫▓▓▓▌╫▓╫▌▓▌▓╫█▓▓▓╫▓╫▓██▓▓▓▓▀▀▌█▓▓▀▓▀▓▀▓╫▓▓▌╫▓╫▓╫▓╫█▓▓▓█▓█╫█▓▓█▓▄ 
	       █▓▀╫▓╫█▀█▓▓▓▓▓▌╫▌╫█▓▓▓╫█▓█▓▓▓▓▀▓▓█╫▓╫▌╫▌╫▓╫█╫▌╫█▓▓╫▓╫█▓╫█▀█▓▓╫▓█▓▓█ 
	       █▓╫▓▀╫▌╫█╫▌╫▌▓▌╫▌╫█╫╫█╫▓▓▓█▓█▓▓▄▌██▓▓▓▓▓▓▓╫▌╫▌╫▌╫▌╫█▓▀▀▓▓▓▀██▓▀▓█▓█ 
	      ▄▓▒▓▓▓█╫▓▓▓▓▀▀`▀▀█▓▓▓╫█▓▓▀███▓▀█▀▓▓█▒╫▒▓▓█▀▀▀▀▓▓▓▀▀▀`   `▀█▓█▓▓▌▓▓▓█ 
	      █╫▓▓╫▓▀▓▌▓▀        └ ▀  ▄▌▀▓█▓▓▓▌█╫█▓█▓▓▓▓█▄               ▀▀▀▓╫▓▀▓█ 
	      █▓▓╫▓▌▓█▌               █▓▓██▓▓▓▌▄▓█▓███▓▓▓█▓▄                  ▀▀▓╫▌
	      ▀▓╫▓█▓Ö                 ▀▓▓▒▓▓▓█▌█╫█▓▓▓▓▓▓█▓█▓▌        ▓█▓ ▄▄,    ▀▓▌
	       █▀╜       ▄µ            ╨▀▓▓▓▓██▌██▀█▓▓▓▓▓▓▌▀▓▓       ▀▓▓█▓▓█▌      
		      ▀▀▄▄▄▀▓▓▄▄        ╥▄▀█▓▓█▓▓▌█▓▓██▓█▓██▓▀▓▓        ▓▓▓▓█      
		    ╥,▄█▓▓▓▓▌ ╙▓▓▄,╥╥æ▓█▀▀└ ▄█▓▓╙▓▓█╫▓▓▀█▓█▓▓▓▓▓▌     ▄▄▓▓█▌ ▄▄▄   
		   ╨█▓▓██▓▓▓▓▌▄▄▓▓▀▀▌╫▓█▄▄▓█▓▀▀   ╙ ╙╙└▀██▀▀╙▀▀└ ,  ,▄▓▓▓▓▓█▓▓▓█F  
		         ╙▀▀█▓▓▓▓██▓▌▀█▓█▓▓█▓▌     ,▄▄▄▄▓█     ▄▓▓█▄▄▓▓▓▓▓▓█▓▓▀╙   
		      ⁿ▄▄▓▓▓█▓▓▓▓▓▓█µ -█▓▓▓▓▓▓▓▄   ▓▓▓██▒▀█▓▓ ▄▓▓▓▓▌█▓▓▓▓▓▀        
		      ▀▓▓▓▓▓▓▓▓▓▓▓▓▓█  Å█▓▓▓▓▓▓▓▌ ▄█▓▓▓▓█▓▓██ █▓▓▓█▄█▓██▀          
			▀▀█▓█▓▌▀█▓▓▓█▄▄▄▓██▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓█▄███▓▓▓▓▓▓▓▌          
			         ▄█▓▓▓▓▓▓▓▓▓▓█▓▓▓█▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓█▀          
			         █▓▓▓▓▓▓▓▓▓▓▓▀,. █▓▓▓▓▓▓▓▓█▀▀▀▓█▓▓▓▓█▌▀            
			          ▐▌▀█▀▓▀▀██▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓█▓Γ                  
			                  ▀▓█▓▓█▓▀▓▓▓▓▀╙▀▀▓█▀▀                     
		   =============================================================   
			                   OSINT MX                                
		   =============================================================   
			                 osint x rfc                             
			             ======================                        
			              Author: Edgar Medina                         
			             ======================                        

	                 usage: OSINT-x-RFC.py [-h] rfc

	                 Validate an RFC number using the Mexico's SAT API

	                 positional arguments:
	                 rfc       The RFC to validate

	                 options:
	                  -h, --help  show this help message and exit
                    
The results print the data returned in json format. The data points retrieved are the following: birthdate,entity_birth, homonimo, mothers_maiden_name, names, coorporate name (if it is an organization), status, email contact and / or phone number.
