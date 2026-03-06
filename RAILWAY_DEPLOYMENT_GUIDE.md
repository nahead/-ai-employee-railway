# 🚀 Railway Deployment Guide - AI Employee
## Platinum Tier - Easiest Cloud Deployment Ever!

### 🎯 Why Railway is Perfect
- **5 minutes setup** - Fastest deployment
- **GitHub integration** - Direct from your repo
- **$5/month free credit** - More than enough
- **No VM management** - Just deploy and run
- **Automatic scaling** - Handles everything
- **Simple environment variables** - Easy configuration

---

## 📋 Phase 1: Railway Account Setup

### Step 1: Create Railway Account
1. **Go to**: https://railway.app
2. **Click**: "Start a New Project"
3. **Sign up** with GitHub account (recommended)
4. **Verify** your email
5. **Free $5 credit** automatically added

### Step 2: Connect GitHub Repository
1. **Create new GitHub repository**: `ai-employee-cloud`
2. **Make it public** (for free tier) or private (with paid plan)
3. **Upload your deployment files**

---

## 📦 Phase 2: Prepare Deployment Files

### Step 3: Create Railway-Specific Files

**Create `railway.json`**:
```json
{
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "python cloud_orchestrator.py",
    "healthcheckPath": "/health",
    "healthcheckTimeout": 100,
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 3
  }
}
```

**Create `requirements.txt`**:
```txt
requests>=2.31.0
google-auth>=2.23.0
google-auth-oauthlib>=1.0.0
google-auth-httplib2>=0.1.0
google-api-python-client>=2.100.0
pathlib2>=2.3.7
python-dotenv>=1.0.0
asyncio-mqtt>=0.13.0
```

**Create `Procfile`**:
```
web: python cloud-deployment/scripts/cloud_orchestrator.py
worker: python cloud-deployment/scripts/vault_sync_daemon.py
gmail: python cloud-deployment/scripts/cloud_gmail_watcher.py
files: python cloud-deployment/scripts/cloud_file_watcher.py
```

### Step 4: Upload to GitHub
```bash
# In your project directory
git add .
git commit -m "Railway deployment setup"
git push origin main
```

---

## 🚀 Phase 3: Deploy to Railway

### Step 5: Create Railway Project
1. **Railway Dashboard** → "New Project"
2. **Select**: "Deploy from GitHub repo"
3. **Choose**: Your `ai-employee-cloud` repository
4. **Click**: "Deploy Now"

### Step 6: Configure Environment Variables
**In Railway Dashboard** → Your Project → Variables:

```bash
# Essential Variables
AGENT_TYPE=cloud
NODE_ENV=production
RAILWAY_ENVIRONMENT=production

# Vault Sync (Create GitHub repo first)
VAULT_REPO_URL=https://github.com/YOUR-USERNAME/ai-employee-vault.git
GIT_USERNAME=your-github-username
GIT_TOKEN=your-github-personal-access-token

# Gmail Integration
GMAIL_CREDENTIALS_JSON={"paste your credentials.json content here"}

# Intervals
SYNC_INTERVAL=60
GMAIL_CHECK_INTERVAL=300
HEALTH_CHECK_INTERVAL=300

# Railway-specific
PORT=8080
RAILWAY_STATIC_URL=your-app-url.railway.app
```

### Step 7: Deploy Services
**Railway automatically**:
- ✅ Builds your application
- ✅ Installs dependencies
- ✅ Starts your services
- ✅ Provides HTTPS URL
- ✅ Monitors health

---

## 🔄 Phase 4: Setup Vault Synchronization

### Step 8: Create Vault Repository
1. **GitHub** → New Repository → `ai-employee-vault`
2. **Make it private**
3. **Initialize with README**

### Step 9: Initialize Local Vault
```bash
cd "C:\\Users\\nahead\\Documents\\GitHub\\Hackathon0\\AI_Employee_Vault"

git init
git remote add origin https://github.com/YOUR-USERNAME/ai-employee-vault.git
git add .
git commit -m "Initial vault for Railway deployment"
git push -u origin main
```

---

## 🧪 Phase 5: Testing & Validation

### Step 10: Check Deployment
1. **Railway Dashboard** → Your Project
2. **Check**: All services are "Active"
3. **View Logs**: Click on each service to see logs
4. **Test URL**: Visit your Railway app URL

### Step 11: Test Email Monitoring
1. **Send test email** to monitored Gmail
2. **Check Railway logs** for email detection
3. **Verify vault sync** in GitHub repository

---

## 📊 Phase 6: Monitoring

### Step 12: Railway Monitoring
**Built-in features**:
- ✅ **Real-time logs**
- ✅ **Resource usage graphs**
- ✅ **Automatic restarts**
- ✅ **Health checks**
- ✅ **Deployment history**

### Step 13: Custom Monitoring
**Add to your main script**:
```python
import os
import requests

def railway_health_check():
    """Health check endpoint for Railway"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "services": {
            "orchestrator": "running",
            "gmail_watcher": "running",
            "vault_sync": "running",
            "file_watcher": "running"
        }
    }

# Add this to your main script
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    # Your main application logic
```

---

## 💰 Cost & Limits

### Railway Free Tier:
- **$5 free credit per month**
- **500 hours execution time**
- **1GB RAM per service**
- **1GB disk space**
- **100GB bandwidth**

### Expected Usage:
- **AI Employee**: ~$2-3/month
- **Well within free limits**
- **Automatic scaling**

---

## 🎯 Success Checklist

### ✅ Deployment Complete When:
- [ ] **Railway project deployed**
- [ ] **All 4 services running**
- [ ] **Environment variables configured**
- [ ] **Vault repository syncing**
- [ ] **Gmail monitoring active**
- [ ] **Health checks passing**

---

## 🚨 Troubleshooting

### Common Issues:

**1. Build Fails**
```bash
# Check requirements.txt
# Verify Python version compatibility
# Check Railway build logs
```

**2. Environment Variables**
```bash
# Double-check all required variables
# Verify GitHub token permissions
# Test Gmail credentials format
```

**3. Service Crashes**
```bash
# Check Railway logs
# Verify memory limits
# Check for missing dependencies
```

---

## 🏆 Railway Deployment Complete!

**Your AI Employee is now running 24/7 on Railway with**:

- ✅ **Automatic deployments** from GitHub
- ✅ **Built-in monitoring** and health checks
- ✅ **Secure environment** variables
- ✅ **HTTPS endpoint** included
- ✅ **Zero server management**
- ✅ **Cost-effective** operation

**Total setup time: ~15 minutes!** 🎉

---

## 📞 Next Steps

1. **Test the complete workflow**
2. **Monitor Railway dashboard**
3. **Check vault synchronization**
4. **Send test emails**
5. **Verify 24/7 operations**

**Welcome to effortless AI Employee hosting!** 🚀