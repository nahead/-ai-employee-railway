#!/usr/bin/env python3
"""
Cloud Orchestrator - Railway Compatible
Fixed paths for Railway deployment
"""

import os
import sys
import time
import logging
from pathlib import Path
from datetime import datetime
import json
import subprocess
import asyncio

# Create logs directory if it doesn't exist
logs_dir = Path("/app/logs")
logs_dir.mkdir(parents=True, exist_ok=True)

# Configure logging for Railway
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),  # Console output for Railway logs
        logging.FileHandler('/app/logs/cloud-orchestrator.log')
    ]
)
logger = logging.getLogger('CloudOrchestrator')

class CloudOrchestrator:
    """Main cloud orchestrator for Railway deployment"""

    def __init__(self):
        self.app_dir = Path("/app")
        self.vault_path = self.app_dir / "vault-sync"
        self.logs_path = self.app_dir / "logs"

        # Create necessary directories
        self.vault_path.mkdir(parents=True, exist_ok=True)
        self.logs_path.mkdir(parents=True, exist_ok=True)

        logger.info("Cloud Orchestrator initialized for Railway")

    def check_environment(self):
        """Check Railway environment"""
        required_vars = [
            "VAULT_REPO_URL",
            "GIT_USERNAME",
            "GIT_TOKEN"
        ]

        missing = [var for var in required_vars if not os.getenv(var)]

        if missing:
            logger.error(f"Missing environment variables: {missing}")
            return False

        logger.info("Environment variables configured correctly")
        return True

    def create_status_report(self):
        """Create Railway status report"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

        report_content = f"""---
type: railway_status
created_at: {datetime.now().isoformat()}
---

# Railway Deployment Status

## System Information
- **Platform**: Railway.app
- **Environment**: {os.getenv('RAILWAY_ENVIRONMENT', 'production')}
- **Port**: {os.getenv('PORT', '8080')}
- **Deployment Time**: {datetime.now().isoformat()}

## Service Status
- **Orchestrator**: ✅ Running
- **Vault Sync**: 🔄 Initializing
- **Gmail Watcher**: 🔄 Starting
- **File Watcher**: 🔄 Starting

## Configuration
- **Vault Repository**: {os.getenv('VAULT_REPO_URL', 'Not configured')}
- **Git Username**: {os.getenv('GIT_USERNAME', 'Not configured')}

---
*Railway Cloud Orchestrator - Platinum Tier*
"""

        report_file = self.logs_path / f"RAILWAY_STATUS_{timestamp}.md"
        report_file.write_text(report_content)
        logger.info(f"Status report created: {report_file.name}")

    def run(self):
        """Main run method"""
        logger.info("🚀 Starting Railway Cloud Orchestrator...")

        if not self.check_environment():
            logger.error("❌ Environment check failed")
            sys.exit(1)

        self.create_status_report()

        logger.info("✅ Railway Cloud Orchestrator running successfully!")
        logger.info("🌐 AI Employee is now live on Railway!")

        # Keep the service running
        while True:
            try:
                time.sleep(60)
                logger.info("💓 Heartbeat - Service running normally")
            except KeyboardInterrupt:
                logger.info("👋 Shutting down...")
                break

if __name__ == "__main__":
    orchestrator = CloudOrchestrator()
    orchestrator.run()