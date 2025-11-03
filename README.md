# Azure Cloud Cost Planner

A Streamlit web application for estimating Azure Virtual Machine costs across different regions and configurations.

## Project Title
**Integrating Azure Pricing Calculator for Cloud Resource Planning and Cost Estimation**

## Features

- 💰 **Plan Cost**: Configure a single VM (region, size, OS, hours) and get instant cost estimates
- 🌍 **Compare Regions**: Compare the same VM configuration across multiple Azure regions with visual charts
- ℹ️ **About**: Project information and educational context

## Technology Stack

- **Framework**: Streamlit
- **Language**: Python 3.10+
- **Dependencies**: pandas
- **Hosting**: Azure App Service (Linux, Free F1 tier)

## Local Setup

### Prerequisites

- Python 3.10 or higher
- pip package manager

### Installation

1. Clone or download this repository

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running Locally

```bash
streamlit run app.py
```

The app will open in your default web browser at `http://localhost:8501`

## Project Structure

```
azure_cost_planner_streamlit/
├── app.py                 # Main Streamlit application
├── data/
│   ├── prices.py         # Internal price catalog and helper functions
│   └── azure_api.py      # Placeholder for future Azure API integration
├── assets/
│   └── styles.css        # Optional custom styling
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Usage

### Plan Cost Tab

1. Select Azure region from the dropdown
2. Choose VM size (e.g., Standard_D2s_v5)
3. Select operating system (Linux or Windows)
4. Enter hours per month (1-744, default: 730)
5. Click "Calculate Cost" to see hourly and monthly estimates

### Compare Regions Tab

1. Select VM size and operating system
2. Enter hours per month
3. Click "Compare Regions" to see a table and bar chart comparing costs across all available regions

## Important Notes

⚠️ **Educational Demo**: This application uses an internal price catalog with illustrative pricing data. Prices shown are **not official Azure prices** and may differ significantly from actual Azure retail pricing.

### Current Limitations

- Limited to 6-8 VM sizes across 4-5 regions
- Illustrative pricing data only
- Single service (Virtual Machines) in MVP

## Azure Deployment

### Target Platform
Azure App Service (Linux), Free F1 tier

### Deployment Steps

#### 1. Create Azure Web App

1. Log in to [Azure Portal](https://portal.azure.com)
2. Create a new **Web App**
3. Configure:
   - **Runtime stack**: Python
   - **Version**: Python 3.10 or higher (latest available: up to 3.14)
   - **Region**: South India (or your preferred region)
   - **App Service Plan**: Create new Free (F1) plan
   - **Name**: Choose a unique name (e.g., `yourname-azure-cost-planner`)

#### 2. Configure Application Settings

In Azure Portal → Your Web App → **Configuration** → **Application settings**, add:

| Name | Value |
|------|-------|
| `WEBSITES_PORT` | `8000` |

Save the configuration.

#### 3. Set Startup Command

In Azure Portal → Your Web App → **Configuration** → **General settings**, under **Startup Command**, enter:

```bash
python -m streamlit run app.py --server.port 8000 --server.address 0.0.0.0
```

Save the configuration.

#### 4. Deploy Code

**Option A: GitHub Deployment (Recommended)**

1. Push your code to a GitHub repository
2. In Azure Portal → Your Web App → **Deployment Center**
3. Select **GitHub** as source
4. Authorize and select your repository and branch
5. Azure will automatically deploy on every push

**Option B: Zip Deploy**

1. Install Azure CLI (if not already installed):
```bash
az --version
```

2. Login to Azure:
```bash
az login
```

3. Zip your project files (excluding venv, __pycache__, .git):
```bash
# On Linux/Mac
zip -r deploy.zip . -x "venv/*" "__pycache__/*" "*.pyc" ".git/*"

# On Windows (PowerShell)
Compress-Archive -Path * -DestinationPath deploy.zip -Exclude "venv","__pycache__","*.pyc",".git"
```

4. Deploy using Azure CLI:
```bash
az webapp deploy --resource-group <your-resource-group> --name <your-app-name> --src-path deploy.zip --type zip
```

Or use the Azure Portal:
- Go to **Advanced Tools (Kudu)** → **Go** → **Tools** → **Zip Push Deploy**
- Upload your zip file

#### 5. Verify Deployment

1. Visit `https://<your-app-name>.azurewebsites.net`
2. Verify all tabs/pages load correctly
3. Test the cost estimation features

### Troubleshooting

- **App doesn't load**: Check that `WEBSITES_PORT=8000` is set and startup command is correct
- **Import errors**: Ensure `requirements.txt` includes all dependencies
- **Timeout errors**: Free tier has resource limits; ensure app starts quickly

### Configuration Summary

```
Runtime: Python 3.10+
Port: 8000
Startup Command: python -m streamlit run app.py --server.port 8000 --server.address 0.0.0.0
```

## Future Enhancements

- [ ] Integrate Azure Retail Prices API for real-time pricing
- [ ] Add support for additional Azure services (Storage, Networking, Databases)
- [ ] Implement Reserved Instance pricing
- [ ] Add cost optimization recommendations
- [ ] Historical price tracking
- [ ] Export cost estimates (PDF/CSV)

## Testing Checklist

✅ **Estimator Tests**:
- D2s_v5 / southindia / Linux / 730h → shows hourly + monthly
- B1s / eastus / Windows / 100h → returns values or clean "not found"

✅ **Compare Tests**:
- E2s_v5 / Linux / 730h → table of ~5 regions + bar chart sorted by hourly price

✅ **General**:
- About page loads correctly
- Navigation between tabs works
- App renders in <2s locally
- Responsive on mobile devices

## License

Educational project - For academic use only.

## Disclaimer

**Educational demo. Prices are illustrative and may differ from Azure's live calculator.**

This application is created for educational purposes as part of a Cloud Computing academic project. The pricing data is illustrative and should not be used for actual cost planning. Always refer to the official [Azure Pricing Calculator](https://azure.microsoft.com/pricing/calculator/) for accurate pricing information.

