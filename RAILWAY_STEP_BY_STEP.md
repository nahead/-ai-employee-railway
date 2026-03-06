# 🚀 Railway Deployment - Step by Step Guide

## 📋 What We've Prepared
✅ `railway.json` - Railway configuration
✅ `Procfile` - Service definitions
✅ `railway_cloud_orchestrator.py` - Main orchestrator
✅ `requirements.txt` - Python dependencies
✅ All cloud deployment scripts ready

---

## 🎯 Step 1: Create GitHub Repository

### 1.1 Create New Repository
1. **Go to**: https://github.com
2. **Click**: "New repository"
3. **Repository name**: `ai-employee-railway`
4. **Visibility**: Public (for free Railway tier)
5. **Initialize**: ✅ Add README
6. **Click**: "Create repository"

### 1.2 Upload Your Files
```bash
# Clone the new repository
git clone https://github.com/YOUR-USERNAME/ai-employee-railway.git
cd ai-employee-railway

# Copy all your AI Employee files
# (Copy everything from your current directory)
```

**Or use GitHub web interface**:
1. **Click**: "uploading an existing file"
2. **Drag and drop** your entire project folder
3. **Commit**: "Initial AI Employee Railway deployment"

---

## 🚀 Step 2: Deploy to Railway

### 2.1 Create Railway Account
1. **Go to**: https://railway.app
2. **Click**: "Start a New Project"
3. **Sign up**: Use your GitHub account
4. **Verify**: Email verification
5. **Free $5 credit**: Automatically added

### 2.2 Create New Project
1. **Railway Dashboard** → "New Project"
2. **Select**: "Deploy from GitHub repo"
3. **Choose**: Your `ai-employee-railway` repository
4. **Click**: "Deploy Now"

Railway will automatically:
- ✅ Detect Python project
- ✅ Install dependencies from requirements.txt
- ✅ Build your application
- ✅ Start the web service

---

## ⚙️ Step 3: Configure Environment Variables

### 3.1 Essential Variables
**In Railway Dashboard** → Your Project → Variables tab:

```bash
# Core Configuration
AGENT_TYPE=cloud
NODE_ENV=production
RAILWAY_ENVIRONMENT=production
PORT=8080

# Vault Synchronization (IMPORTANT!)
VAULT_REPO_URL=https://github.com/YOUR-USERNAME/ai-employee-vault.git
GIT_USERNAME=your-github-username
GIT_TOKEN=your-github-personal-access-token

# Gmail Integration
GMAIL_CREDENTIALS_JSON={"type":"service_account","project_id":"your-project",...}

# Timing Configuration
SYNC_INTERVAL=60
GMAIL_CHECK_INTERVAL=300
HEALTH_CHECK_INTERVAL=300

# Security
MAX_MEMORY_RESTART=500M
MAX_RESTART_ATTEMPTS=3
```

### 3.2 Create GitHub Personal Access Token
1. **GitHub** → Settings → Developer settings → Personal access tokens
2. **Generate new token** (classic)
3. **Scopes**: Select `repo` (full repository access)
4. **Copy token** and paste in Railway variables

---

## 🔄 Step 4: Create Vault Repository

### 4.1 Create Vault Repository
1. **GitHub** → New Repository → `ai-employee-vault`
2. **Make it PRIVATE** (contains your data)
3. **Initialize with README**

### 4.2 Initialize Local Vault
```bash
cd "C:\\Users\\nahead\\Documents\\GitHub\\Hackathon0\\AI_Employee_Vault"

# Initialize git (if not already done)
git init
git remote add origin https://github.com/YOUR-USERNAME/ai-employee-vault.git

# Add all files
git add .
git commit -m "Initial vault for Railway deployment"
git push -u origin main
```

---

## 🧪 Step 5: Test Deployment

### 5.1 Check Railway Dashboard
1. **Go to**: Railway Dashboard → Your Project
2. **Check**: Service status should be "Active"
3. **View Logs**: Click on your service to see logs
4. **Health Check**: Visit your Railway URL + `/health`

### 5.2 Test Health Endpoint
Your Railway app will have a URL like: `https://your-app-name.railway.app`

**Test**: `https://your-app-name.railway.app/health`

Should return:
```json
{
  "status": "healthy",
  "timestamp": "2026-03-06T...",
  "environment": "production",
  "services": {
    "orchestrator": "running",
    "vault_sync": "active",
    "gmail_watcher": "monitoring",
    "file_watcher": "active"
  }
}
```

---

## 📊 Step 6: Monitor & Validate

### 6.1 Check Logs
**Railway Dashboard** → Your Project → Logs:
- Look for "Railway Cloud Orchestrator initialized"
- Check for "All services started successfully"
- Verify "AI Employee is now running 24/7 on Railway!"

### 6.2 Test Email Monitoring
1. **Send test email** to your monitored Gmail account
2. **Check Railway logs** for email detection
3. **Check vault repository** for new drafts

### 6.3 Verify Vault Sync
1. **Check your vault repository** on GitHub
2. **Look for new commits** from Railway
3. **Verify sync reports** in Reports/Cloud folder

---

## 🎉 Success Indicators

### ✅ Deployment Successful When:
- [ ] **Railway service**: Status shows "Active"
- [ ] **Health endpoint**: Returns healthy status
- [ ] **Logs show**: "AI Employee is now running 24/7"
- [ ] **Vault sync**: Repository shows recent commits
- [ ] **Email monitoring**: Logs show Gmail API connection
- [ ] **No errors**: All services running without crashes

---

## 🚨 Troubleshooting

### Common Issues:

**1. Build Fails**
- Check `requirements.txt` for compatibility
- Verify Python version (Railway uses Python 3.11)
- Check Railway build logs for specific errors

**2. Service Crashes**
- Check environment variables are set correctly
- Verify GitHub token has correct permissions
- Check Gmail credentials format

**3. Vault Sync Issues**
- Verify repository URL is correct
- Check GitHub token permissions
- Ensure vault repository exists and is accessible

---

## 💰 Cost Monitoring

### Railway Usage:
- **Free $5/month credit**
- **Expected usage**: $2-3/month
- **Monitor**: Railway Dashboard → Usage tab

---

## 🏆 Congratulations!

**Your AI Employee is now running 24/7 on Railway!**

- ✅ **Always-on monitoring**
- ✅ **Automatic deployments**
- ✅ **Built-in health checks**
- ✅ **Secure environment**
- ✅ **Zero server management**

**Ready to test the complete workflow?** 🎯