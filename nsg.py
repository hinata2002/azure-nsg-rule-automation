from azure.identity import AzureCliCredential
from azure.mgmt.network import NetworkManagementClient

# Azure setup
subscription_id = "#"  # Replace with your actual subscription ID
resource_group = "RG-Network-Security-Demo"
location = "centralindia"

# Initialize client
credential = AzureCliCredential()
network_client = NetworkManagementClient(credential, subscription_id)

# Rule 1: Allow RDP from Internet to Public Subnet VM
network_client.security_rules.begin_create_or_update(
    resource_group,
    "nsg-public-subnet",
    "Allow-RDP",
    {
        "protocol": "Tcp",
        "source_port_range": "*",
        "destination_port_range": "3389",
        "source_address_prefix": "*",  # Anywhere
        "destination_address_prefix": "*",
        "access": "Allow",
        "priority": 100,
        "direction": "Inbound",
        "description": "Allow RDP from Internet"
    }
).result()
print("✅success Vimal RDP rule added to nsg-public-subnet")

# Rule 2: Allow SSH from public subnet to private subnet
network_client.security_rules.begin_create_or_update(
    resource_group,
    "nsg-private-subnet",
    "Allow-SSH",
    {
        "protocol": "Tcp",
        "source_port_range": "*",
        "destination_port_range": "22",
        "source_address_prefix": "10.0.1.0/24",  # Public subnet range
        "destination_address_prefix": "10.0.2.0/24",
        "access": "Allow",
        "priority": 100,
        "direction": "Inbound",
        "description": "Allow SSH from Public Subnet"
    }
).result()
print("✅ success Vimal SSH rule added to nsg-private-subnet")

