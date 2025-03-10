import requests, os

# Cloudflare API details
CLOUDFLARE_API_TOKEN = os.environ.get('TOKEN')
ZONE_ID = os.environ.get('ZONE')
DNS_RECORD_NAME = os.environ.get('DOMAIN')


# Get the DNS Zone ID from Cloudflare
def get_dns_record_id():
    url = f"https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records"
    headers = {
        "Authorization": f"Bearer {CLOUDFLARE_API_TOKEN}",
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    data = response.json()

    if data["success"]:
        for record in data["result"]:
            if record["name"] == DNS_RECORD_NAME:
                print(f"DNS Record ID for {DNS_RECORD_NAME}: {record['id']}")
                return record["id"]
        print(f"No DNS record found for {DNS_RECORD_NAME}.")
    else:
        print("Failed to fetch DNS records:", data)
    return None

DNS_RECORD_ID = get_dns_record_id()

# Get the current public IP address
def get_public_ip():
    response = requests.get("https://api64.ipify.org?format=json")
    return response.json().get("ip")

# Get the current IP on Cloudflare
def get_cloudflare_ip():
    url = f"https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records/{DNS_RECORD_ID}"
    headers = {
        "Authorization": f"Bearer {CLOUDFLARE_API_TOKEN}",
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    return response.json().get("result", {}).get("content")

# Update Cloudflare DNS if needed
def update_cloudflare_dns(new_ip):
    url = f"https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records/{DNS_RECORD_ID}"
    headers = {
        "Authorization": f"Bearer {CLOUDFLARE_API_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "type": "A",
        "name": DNS_RECORD_NAME,
        "content": new_ip,
        "ttl": 1,
        "proxied": True
    }
    response = requests.put(url, headers=headers, json=data)
    return response.json()

def main():
    public_ip = get_public_ip()
    cloudflare_ip = get_cloudflare_ip()
    
    print(f"Public IP: {public_ip}")
    print(f"Cloudflare IP: {cloudflare_ip}")
    
    if public_ip and cloudflare_ip and public_ip != cloudflare_ip:
        print("IP mismatch detected. Updating Cloudflare DNS...")
        update_response = update_cloudflare_dns(public_ip)
        print(update_response)
    else:
        print("No update needed.")

if __name__ == "__main__":
    print('running')
    main()
