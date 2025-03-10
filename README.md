# Cloudflare Dynamic DNS
If your IP provisioning is dynamic and you use Cloudflare for DNS/etc services, then a service is needed to keep Cloudflare's records of your dynamic IP up to date.

I.E. You're like me and too lazy to pay for static IP provisioning

# How to use

Pull the image like any other container:

```
docker pull ghcr.io/goingoffroading/cloudflare-dynamic-dns:latest
```

Run it with the following variables:

| ENV | Type | Notes |
|-----|-----|-------|
|     TOKEN     |   String    | Your Cloudflare API token
|     ZONE     |   String    | The Zone of the website
|     DOMAIN     |   String    | Which Domain is being updated

Kubernetes cronjob example attached as Kub-DNS.yml

## Where to get Cloudflare API Token

- Go to [Cloudflare.com](https://dash.cloudflare.com)
- Log in
- In the top right, click on your account, then click profile
- On page load, click on API Tokens on the far right
- Click 'Create Token' and:
    - Click 'Get Started' under Create Custom Token
    - Give the Token a name (any name works)
    - Under Permissions, click on 'Select item...' and select DNS Settings
    - To the field on the right, click 'Edit'
    - Click 'Continie to summary' at the bottom
    - When the next screen loads, click 'Create Token'
    - When the final screen loads, note the Token

## Where to get Zone ID

- Go to [Cloudflare.com](https://dash.cloudflare.com)
- Log in
- Click on the Domain you're looking to push DNS updates to
- Zone ID will be on the far right, near the bottom of the page, under 'API'

## Where to get the Domain:

- Go to [Cloudflare.com](https://dash.cloudflare.com)
- Log in
- Click on the Domain you're looking to push DNS updates to
- Click on 'DNS' on the far right
- The 'Name' field in the DNS management for the Domain being managed is the correct field

Yes, I could have named this variable better.
