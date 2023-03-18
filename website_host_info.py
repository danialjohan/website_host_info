import socket
import whois

# Specify the website URL
url = input("Enter url: ")
print("Please wait...")

# Retrieve the IP address of the website
ip_address = socket.gethostbyname(url)

# Query the WHOIS database for information about the IP address
domain_info = whois.whois(ip_address)

# Print the results
print(f'Website URL: {url}')
print(f'IP address: {ip_address}')
print(f'WHOIS information: {domain_info}')
