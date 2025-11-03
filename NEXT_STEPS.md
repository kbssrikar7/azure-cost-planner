# Next Steps for Azure Cloud Cost Planner Project

## ✅ Phase 1: Local Testing (Current)

### Immediate Actions:
1. **Test the App Features**
   - [ ] Open the app at `http://localhost:8501`
   - [ ] Test **Plan Cost** tab:
     - Try different VM sizes (Standard_D2s_v5, Standard_B1s, etc.)
     - Test different regions (South India, East US, etc.)
     - Test both Linux and Windows
     - Verify hours/month calculation (try 100, 730, 744)
     - Test invalid combinations (if any)
   
   - [ ] Test **Compare Regions** tab:
     - Select a VM size (e.g., Standard_E2s_v5)
     - Compare across all regions
     - Verify table displays correctly
     - Check bar chart visualization
     - Verify sorting by price
   
   - [ ] Test **About** tab:
     - Add your student details (name, ID, institution)
     - Review all content

2. **Verify Testing Checklist**
   - [ ] D2s_v5 / southindia / Linux / 730h → shows hourly + monthly ✓
   - [ ] B1s / eastus / Windows / 100h → returns values or clean "not found" ✓
   - [ ] E2s_v5 / Linux / 730h → table of ~5 regions + bar chart sorted by hourly price ✓
   - [ ] About page loads correctly ✓
   - [ ] Navigation between tabs works ✓
   - [ ] App renders in <2s locally ✓

3. **Fix Any Issues**
   - Address any bugs you find
   - Improve UX if needed
   - Update placeholders with real information

---

## 🚀 Phase 2: Prepare for Azure Deployment

### Step 1: Create GitHub Repository (Recommended)
```bash
# Initialize git (if not already done)
cd /Users/happy/Documents/Code/CloudComputing
git init
git add .
git commit -m "Initial commit: Azure Cloud Cost Planner MVP"

# Create a new repository on GitHub, then:
git remote add origin https://github.com/YOUR_USERNAME/azure-cost-planner.git
git branch -M main
git push -u origin main
```

**Why GitHub?** Azure App Service can auto-deploy from GitHub, making updates easier.

### Step 2: Prepare Deployment Files
- [ ] Verify `requirements.txt` has all dependencies
- [ ] Ensure no sensitive data (API keys, secrets) in code
- [ ] Add `.gitignore` if needed:
  ```
  venv/
  __pycache__/
  *.pyc
  .env
  .DS_Store
  ```

### Step 3: Update Student Information
- [ ] Edit `app.py` or `data/prices.py` to add your name/ID in the About section
- [ ] Update README.md with your details

---

## ☁️ Phase 3: Deploy to Azure App Service

### Prerequisites:
- [ ] Azure account (free tier available: https://azure.microsoft.com/free/)
- [ ] Azure Portal access

### Deployment Steps:

#### Option A: GitHub Deployment (Easiest)

1. **Create Azure Web App**
   - Go to https://portal.azure.com
   - Click "Create a resource" → "Web App"
   - Fill in:
     - **Name**: `yourname-azure-cost-planner` (must be unique)
     - **Runtime stack**: Python
     - **Version**: Python 3.10 or higher (up to 3.14 available)
     - **Region**: South India (or closest to you)
     - **App Service Plan**: Create new → **Free (F1)** tier
   - Click "Review + create" → "Create"

2. **Configure Application Settings**
   - After creation, go to your Web App
   - Navigate to **Configuration** → **Application settings**
   - Click **+ New application setting**
   - Add: `WEBSITES_PORT` = `8000`
   - Click **Save**

3. **Set Startup Command**
   - Go to **Configuration** → **General settings**
   - Under **Startup Command**, enter:
     ```
     python -m streamlit run app.py --server.port 8000 --server.address 0.0.0.0
     ```
   - Click **Save**

4. **Deploy from GitHub**
   - Go to **Deployment Center**
   - Select **GitHub** as source
   - Authorize Azure to access your GitHub
   - Select:
     - **Organization**: Your GitHub username
     - **Repository**: `azure-cost-planner` (or your repo name)
     - **Branch**: `main`
   - Click **Save**
   - Azure will start deploying automatically (takes 2-5 minutes)

5. **Verify Deployment**
   - Go to **Overview** → Your app URL: `https://yourname-azure-cost-planner.azurewebsites.net`
   - Test all features
   - Check logs if there are errors: **Log stream** or **Logs**

#### Option B: Zip Deploy (Alternative)

1. **Install Azure CLI** (if not installed)
   ```bash
   brew install azure-cli  # macOS
   # or visit: https://aka.ms/installazurecliwindows
   ```

2. **Login to Azure**
   ```bash
   az login
   ```

3. **Create Deployment Package**
   ```bash
   # Exclude venv and other unnecessary files
   zip -r deploy.zip . -x "venv/*" "__pycache__/*" "*.pyc" ".git/*" "*.md" "*.DS_Store"
   ```

4. **Deploy**
   ```bash
   az webapp deploy --resource-group <your-resource-group> \
                    --name <your-app-name> \
                    --src-path deploy.zip \
                    --type zip
   ```

---

## 📝 Phase 4: Documentation & Submission

### Update Documentation:
- [ ] Take screenshots of the deployed app
- [ ] Update README.md with:
  - Screenshot of working app
  - Your deployment URL
  - Any deployment challenges/solutions
- [ ] Document any customizations made

### Prepare Submission:
- [ ] Code repository (GitHub link)
- [ ] Deployed app URL (Azure App Service)
- [ ] README with setup instructions
- [ ] Screenshots/video demo (optional)
- [ ] Project report/documentation (if required by your course)

---

## 🔮 Phase 5: Future Enhancements (Optional)

### Short-term Improvements:
- [ ] Add more VM sizes to the price catalog
- [ ] Add more Azure regions
- [ ] Improve error messages
- [ ] Add cost savings suggestions (e.g., "You could save X% by using reserved instances")

### Integration with Azure Retail Prices API:
- [ ] Study Azure Retail Prices API documentation
- [ ] Get API credentials/endpoints
- [ ] Implement `data/azure_api.py` with real API calls
- [ ] Add caching to reduce API calls
- [ ] Handle API rate limits
- [ ] Add fallback to local catalog if API fails

### Advanced Features:
- [ ] Support for Reserved Instances pricing
- [ ] Spot pricing options
- [ ] Multi-VM cost estimation
- [ ] Cost optimization recommendations
- [ ] Export estimates to PDF/CSV
- [ ] Historical price tracking
- [ ] Support for additional Azure services (Storage, Networking, etc.)

---

## 🐛 Troubleshooting Common Issues

### Local Issues:
- **Port already in use**: Change port with `streamlit run app.py --server.port 8502`
- **Import errors**: Make sure virtual environment is activated and dependencies installed

### Azure Deployment Issues:
- **App not loading**: Check `WEBSITES_PORT=8000` is set correctly
- **Import errors**: Verify `requirements.txt` has all packages
- **Timeout**: Free tier has resource limits; ensure app starts quickly
- **502 errors**: Check startup command is correct
- **View logs**: Go to **Log stream** or **Logs** in Azure Portal

---

## 📋 Quick Reference Commands

### Local Development:
```bash
# Activate virtual environment
source venv/bin/activate

# Run app
streamlit run app.py

# Install new dependency
pip install package-name
pip freeze > requirements.txt
```

### Azure CLI:
```bash
# Login
az login

# List web apps
az webapp list

# View logs
az webapp log tail --name <app-name> --resource-group <resource-group>

# Restart app
az webapp restart --name <app-name> --resource-group <resource-group>
```

---

## ✅ Deployment Checklist

Before deploying, ensure:
- [ ] All code is committed to Git
- [ ] `requirements.txt` is up to date
- [ ] No hardcoded secrets or API keys
- [ ] Student information is filled in
- [ ] App works perfectly locally
- [ ] All tests pass
- [ ] README is complete and accurate

---

## 📞 Need Help?

- **Azure Documentation**: https://docs.microsoft.com/azure/app-service/
- **Streamlit Documentation**: https://docs.streamlit.io/
- **Azure Support**: Free tier includes community support

---

**Good luck with your Cloud Computing project!** 🎓☁️


