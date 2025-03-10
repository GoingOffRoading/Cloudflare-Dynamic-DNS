# Use a lightweight Python image
FROM python:3.9-alpine

# Set working directory
WORKDIR /app

# Copy script to container
COPY cloudflare_dns_updater.py /app/

# Install dependencies
RUN pip install --no-cache-dir requests

# Run the script
CMD ["python", "cloudflare_dns_updater.py"]