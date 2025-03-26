# AWS EC2 Instance Deployment using Pulumi

## Overview  
This project automates the deployment of an **EC2 instance** on **AWS** using **Pulumi**. It provisions a virtual machine, configures security groups, and ensures a streamlined infrastructure setup.

## Features  
- Creates an **AWS EC2 instance**  
- Configures **security groups** for access control  
- Uses **Pulumi stack outputs** for dynamic configuration  
- Automates infrastructure provisioning with **Pulumi**  

## Prerequisites  
- **AWS CLI** installed and configured  
- **Pulumi CLI** installed  
- **Python** (for Pulumi scripting)  
- **Git** for version control  

## Installation and Usage  

### 1️⃣ Clone the Repository  
```sh
git clone https://github.com/shashwatsharma-9/cloudrepopulumiEc2.git
cd cloudrepopulumiEc2
```
### 2️⃣ Install Dependencies
```sh
pip install pulumi pulumi-aws
```

### 3️⃣ Set Up Pulumi
#### Login to Pulumi
```sh
pulumi login
```
#### Initialize a New Stack
```sh
pulumi stack init dev
```
#### Set AWS Region
```sh
pulumi config set aws:region us-east-1
```

### 4️⃣ Deploy EC2 Instance
```sh
pulumi up
```

### 5️⃣ Get EC2 Instance Details
```sh
pulumi stack output instance_id
```

## 🔥 Cleanup
To destroy the infrastructure:
```sh
pulumi destroy
```
⚠️ **This action will delete the EC2 instance and associated resources.**

## 📂 Repository Structure
```
📂 cloudrepopulumiEc2  
 ├── 📄 __main__.py (Pulumi script)  
 ├── 📄 Pulumi.yaml  
 ├── 📄 Pulumi.dev.yaml  
 ├── 📄 README.md  
```

## 📜 License
This project is open-source and available under the MIT License.
