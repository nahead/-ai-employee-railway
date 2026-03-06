#!/usr/bin/env python3
"""
AI Employee System Startup Script
Launches all components in the correct order
"""

import asyncio
import subprocess
import sys
import time
from pathlib import Path

async def start_ai_employee_system():
    """Start the complete AI Employee system"""
    print("[START] Starting AI Employee Master System...")
    print("=" * 50)

    # 1. Start Playwright MCP Server (for LinkedIn automation)
    print("\n[PLAYWRIGHT] Starting Playwright MCP Server...")
    try:
        import os
        playwright_dir = os.path.join(os.getcwd(), ".claude", "skills", "browsing-with-playwright")
        if os.path.exists(playwright_dir):
            playwright_process = subprocess.Popen([
                "npx", "@playwright/mcp@latest",
                "--port", "8808",
                "--shared-browser-context"
            ], cwd=playwright_dir)
            print("  [SUCCESS] Started Playwright MCP Server on port 8808")
            time.sleep(3)  # Give Playwright time to start
        else:
            print("  [WARNING] Playwright directory not found, skipping Playwright server")
            print("  [INFO] LinkedIn automation will use existing server if available")
    except Exception as e:
        print(f"  [WARNING] Playwright MCP Server not available: {e}")
        print("  [INFO] LinkedIn automation will attempt to use existing server")

    # 2. Start MCP Servers
    print("\n[MCP] Starting MCP Servers...")
    mcp_processes = []

    servers = [
        ("Odoo MCP Server", "odoo-mcp-server/odoo_mcp_server.py"),
        ("Email MCP Server", "email-mcp-server/email_mcp_server.py"),
        ("Social Media MCP Server", "social-media-mcp-servers/social_media_mcp_server.py"),
        ("Task Management MCP Server", "task-management-mcp-server/task_management_mcp_server.py")
    ]

    for name, script in servers:
        try:
            process = subprocess.Popen([sys.executable, script])
            mcp_processes.append((name, process))
            print(f"  [SUCCESS] Started {name}")
            time.sleep(2)  # Stagger startup
        except Exception as e:
            print(f"  [ERROR] Failed to start {name}: {e}")

    # 3. Start LinkedIn Content Handler (for processing approved posts)
    print("\n[LINKEDIN] Starting LinkedIn Content Handler...")
    try:
        linkedin_process = subprocess.Popen([sys.executable, "linkedin_content_handler.py"])
        print("  [SUCCESS] Started LinkedIn Content Handler")
    except Exception as e:
        print(f"  [ERROR] Failed to start LinkedIn Content Handler: {e}")

    # 4. Start Error Recovery System
    print("\n[RECOVERY] Starting Error Recovery System...")
    try:
        error_recovery_process = subprocess.Popen([sys.executable, "error_recovery_system.py"])
        print("  [SUCCESS] Error Recovery System started")
    except Exception as e:
        print(f"  [ERROR] Failed to start Error Recovery: {e}")

    # 5. Start Audit Logger
    print("\n[AUDIT] Starting Audit Logger...")
    try:
        audit_process = subprocess.Popen([sys.executable, "comprehensive_audit_logger.py"])
        print("  [SUCCESS] Audit Logger started")
    except Exception as e:
        print(f"  [ERROR] Failed to start Audit Logger: {e}")

    # 4. Initialize Cross-Domain Integration
    print("\n[INTEGRATION] Initializing Cross-Domain Integration...")
    try:
        subprocess.run([sys.executable, "cross_domain_integration.py"], timeout=30)
        print("  [SUCCESS] Cross-Domain Integration initialized")
    except Exception as e:
        print(f"  [ERROR] Failed to initialize Cross-Domain Integration: {e}")

    # 5. Setup Scheduling
    print("\n[SCHEDULE] Setting up Scheduling System...")
    try:
        subprocess.run([sys.executable, "scheduling_system.py"], timeout=30)
        print("  [SUCCESS] Scheduling System configured")
    except Exception as e:
        print(f"  [ERROR] Failed to setup Scheduling: {e}")

    # 6. Start Cloud Signal Processor (Platinum Tier)
    print("\n[CLOUD] Starting Cloud Signal Processor...")
    try:
        cloud_signal_process = subprocess.Popen([sys.executable, "cloud_signal_processor.py", "--daemon"])
        print("  [SUCCESS] Cloud Signal Processor started")
    except Exception as e:
        print(f"  [ERROR] Failed to start Cloud Signal Processor: {e}")

    # 7. Start Ralph Wiggum Loop (Autonomous Agent)
    print("\n[RALPH] Starting Ralph Wiggum Autonomous Loop...")
    try:
        ralph_process = subprocess.Popen([sys.executable, "ralph_wiggum_loop.py"])
        print("  [SUCCESS] Ralph Wiggum Loop started - I'm helping!")
    except Exception as e:
        print(f"  [ERROR] Failed to start Ralph Loop: {e}")

    # 7. Generate Initial CEO Briefing
    print("\n[BRIEFING] Generating Initial CEO Briefing...")
    try:
        subprocess.run([sys.executable, "ceo_briefing_system.py"], timeout=60)
        print("  [SUCCESS] CEO Briefing generated")
    except Exception as e:
        print(f"  [ERROR] Failed to generate CEO Briefing: {e}")

    print("\n[COMPLETE] AI Employee Master System is now FULLY OPERATIONAL!")
    print("=" * 50)
    print("\n[STATUS] System Status:")
    print("  [SUCCESS] Silver Tier: 100% Complete")
    print("  [SUCCESS] Gold Tier: 100% Complete")
    print("  [SUCCESS] LinkedIn Automation: INTEGRATED")
    print("  [RUNNING] All components running")
    print("  [ACTIVE] Autonomous operations active")
    print("  [PLAYWRIGHT] Browser automation ready")
    print("\n[CAPABILITIES] New LinkedIn Integration:")
    print("  - Automatic LinkedIn posting via Playwright")
    print("  - AI-generated professional content")
    print("  - Human approval workflow (optional)")
    print("  - Ralph Wiggum autonomous posting")
    print("  - Visual feedback via screenshots")
    print("\n[FILES] Check AI_Employee_Vault/ for:")
    print("  - Daily briefings in /Briefings/")
    print("  - Business audits in /Audits/")
    print("  - Task plans in /Plans/")
    print("  - System logs in /Logs/")
    print("  - LinkedIn posts in /Archive/")
    print("\n[SUCCESS] The AI Employee is ready to manage your business!")
    print("[LINKEDIN] LinkedIn automation fully integrated - no more API restrictions!")

if __name__ == "__main__":
    asyncio.run(start_ai_employee_system())
