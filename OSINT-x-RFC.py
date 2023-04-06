import argparse
import json
import requests

# Print Banner
print("")     
print("                                ╓▄▓▌▀▓▓▓▓@▄▄,                              ")
print("                             .▄█▓▓▓▀╜└└╙╙▀▀▓▓▄¿                            ")
print("                           `Å╙      ,▄▄▓▓▀▀▓█▀▀▄                           ")
print("                       ,         █▀▓▓▓▀▓▀Ñ▄▄▄▓▓▌   ,▓▓▓█▓▓▄,               ")
print("                  ,▄▓▓▀▀▀▓▓▓     █▀╫╫╫╫╫╫╫▓╩╨███   J█╫▓▓▓█▓╫▀▓▄            ")
print("                ╥▓▌Ñ██▓█▓▓╫╫▌   █▀▓▓▓▓▓▓▓▌  ▄█▀█    ▌╫▓█▓▓▓▓▓▓▓█▄¿         ")
print("              ╥▓█▓▓▓▓▓▓▓▓▓▒▓L  ▐▓▓▓█▓▓▓▌▓▌ ▄█▌█    ,▌╫▀█▓▓▀▓▓█▓█▓▀▄        ")
print("             ▓▌▀▓▓▀████▀╫█▀█   █▓▓▓▓█▓▓▌▓▓█▓▀█    ▄▓╫╫▌▓▓▀▀█▓▓█╫▓▓▓█▄      ")
print("           ▄█▓▓▓█▓█▓█▓█▓▓▓▓▓▓▄▓▓▓▓▓▓▓▓▓▓▓▀▓▓█▓▓▓▓▓▓▓█▀█▄▒██▓▓▌█╫█╫█▓▓▄     ")
print("          ╥███▓╫▓╫▓╫█▀▓▓▓▓▓▀█▓▓█▓▓▓▓▓▓▓█▄▌▓█▌▀▓▓▀▓▀▓▓▓▓▓▓▓█▓█▓▀▌▀▌▓▓▓▓▌    ")
print("         ,█▓╫█╫█▀▓▓▓▌▓▓▓▓╫▓▓▀▒█▓▓▓╫█▀▀█▀▌▓█╫▓▓▓█▓▓▓▓▓▓▓▀▓▓▓▓▓█╫█▓█▓▓█▓▓█   ")
print("         █▓▓█▓█▓██▓▌██▓█▓█▓▒█▀█▓▓▓╫▌╫█▌▓▓██╫█╫▓▓▌▓▓▓▓▒▓█▓█▀██▓████▓██▓██▄  ")
print("        ▄█▓╫█▀█▀█▓█╫█▓▓╫▓╫█▓█▓█▓▓█▓█▓▌╫▌█▓█╫▓▓▓▓█▓▓▓█▓▓▓▓▓▓╫█╫█▓█▓▓█▓▓▓▓█  ")
print("       ╒██╫▓▓▓▌╫▓╫▌▓▌▓╫█▓▓▓╫▓╫▓██▓▓▓▓▀▀▌█▓▓▀▓▀▓▀▓╫▓▓▌╫▓╫▓╫▓╫█▓▓▓█▓█╫█▓▓█▓▄ ")
print("       █▓▀╫▓╫█▀█▓▓▓▓▓▌╫▌╫█▓▓▓╫█▓█▓▓▓▓▀▓▓█╫▓╫▌╫▌╫▓╫█╫▌╫█▓▓╫▓╫█▓╫█▀█▓▓╫▓█▓▓█ ")
print("       █▓╫▓▀╫▌╫█╫▌╫▌▓▌╫▌╫█╫╫█╫▓▓▓█▓█▓▓▄▌██▓▓▓▓▓▓▓╫▌╫▌╫▌╫▌╫█▓▀▀▓▓▓▀██▓▀▓█▓█ ")
print("      ▄▓▒▓▓▓█╫▓▓▓▓▀▀`▀▀█▓▓▓╫█▓▓▀███▓▀█▀▓▓█▒╫▒▓▓█▀▀▀▀▓▓▓▀▀▀`   `▀█▓█▓▓▌▓▓▓█ ")
print("      █╫▓▓╫▓▀▓▌▓▀       `└`▀  ▄▌▀▓█▓▓▓▌█╫█▓█▓▓▓▓█▄               ▀▀▀▓╫▓▀▓█ ")
print("      █▓▓╫▓▌▓█▌`              █▓▓██▓▓▓▌▄▓█▓███▓▓▓█▓▄                  ▀▀▓╫▌")
print("      ▀▓╫▓█▓Ö                 ▀▓▓▒▓▓▓█▌█╫█▓▓▓▓▓▓█▓█▓▌        ▓█▓ ▄▄,    ▀▓▌")
print("       █▀╜       ▄µ            ╨▀▓▓▓▓██▌██▀█▓▓▓▓▓▓▌▀▓▓       ▀▓▓█▓▓█▌      ")
print("              ▀▀▄▄▄▀▓▓▄▄        ╥▄▀█▓▓█▓▓▌█▓▓██▓█▓██▓▀▓▓        ▓▓▓▓█      ")
print("            ╥,▄█▓▓▓▓▌ ╙▓▓▄,╥╥æ▓█▀▀└ ▄█▓▓╙▓▓█╫▓▓▀█▓█▓▓▓▓▓▌     ▄▄▓▓█▌ ▄▄▄   ")
print("           ╨█▓▓██▓▓▓▓▌▄▄▓▓▀▀▌╫▓█▄▄▓█▓▀▀   ╙ ╙╙└▀██▀▀╙▀▀└ ,  ,▄▓▓▓▓▓█▓▓▓█F  ")
print("              `  ╙▀▀█▓▓▓▓██▓▌▀█▓█▓▓█▓▌     ,▄▄▄▄▓█     ▄▓▓█▄▄▓▓▓▓▓▓█▓▓▀╙   ")
print("              ⁿ▄▄▓▓▓█▓▓▓▓▓▓█µ -█▓▓▓▓▓▓▓▄   ▓▓▓██▒▀█▓▓ ▄▓▓▓▓▌█▓▓▓▓▓▀        ")
print("              ▀▓▓▓▓▓▓▓▓▓▓▓▓▓█  Å█▓▓▓▓▓▓▓▌ ▄█▓▓▓▓█▓▓██ █▓▓▓█▄█▓██▀          ")
print("                ▀▀█▓█▓▌▀█▓▓▓█▄▄▄▓██▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓█▄███▓▓▓▓▓▓▓▌          ")
print("                         ▄█▓▓▓▓▓▓▓▓▓▓█▓▓▓█▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓█▀          ")
print("                         █▓▓▓▓▓▓▓▓▓▓▓▀,. █▓▓▓▓▓▓▓▓█▀▀▀▓█▓▓▓▓█▌▀            ")
print("                          ▐▌▀█▀▓▀▀██▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓█▓Γ `                 ")
print("                                  ▀▓█▓▓█▓▀▓▓▓▓▀╙▀▀▓█▀▀                     ")
print("           =============================================================   ")                                       
print("                                    OSINT MX                               ")  
print("           =============================================================   ")
print("                                  osint x rfc                              ")
print("                              ======================                       ")
print("                               Author: Edgar Medina                        ")
print("                              ======================                       ")  
print("")

# Define constants
URL = "https://rfc1.p.rapidapi.com/validate-rfc"
CONFIG_FILE = "config.json"

# Define functions
def get_api_key():
    """Retrieve the API key from the config file."""
    with open(CONFIG_FILE) as f:
        config = json.load(f)
    return config["api_key"]

def validate_rfc(rfc):
    """Validate an RFC number using the RapidAPI endpoint."""
    payload = {"rfc": rfc}
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": get_api_key(),
        "X-RapidAPI-Host": "rfc1.p.rapidapi.com"
    }
    response = requests.post(URL, json=payload, headers=headers)
    return response.text

def main():
    """Parse command-line arguments and validate the RFC."""
    parser = argparse.ArgumentParser(description="Validate an RFC number using the Mexico's SAT API")
    parser.add_argument("rfc", help="the RFC number to validate")
    args = parser.parse_args()
    result = validate_rfc(args.rfc)
    print(result)

# Call the main function
if __name__ == "__main__":
    main()
