# Azure NSG Rule Automation 🚀

This project demonstrates how to automate **Network Security Group (NSG) rule creation** in Microsoft Azure using Python and Azure SDK. It helps quickly set up and manage security rules for public/private subnets in a cloud lab or test environment.

---

## 🔧 Features

- Create Inbound NSG Rules (e.g., RDP, SSH)
- Target specific subnets or VMs
- Authenticate using Azure CLI credentials
- Built with `azure-identity` and `azure-mgmt-network`

---

## 📁 Project Structure

azure-nsg-rule-automation \
-├── nsg_rules.py # Main automation script
-├── README.md # Project documentation
-├── requirements.txt # Python dependencies
-└── .gitignore # Git exclusions


---

## 🛠️ Prerequisites

- Python 3.7+
- Azure CLI installed and logged in:
  ```bash
  az login


## Dependencies

- azure-identity
- azure-mgmt-network


