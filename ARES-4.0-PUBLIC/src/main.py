#!/usr/bin/env python3
"""
ARES 4.0 - AI Trading Platform
Main Entry Point
"""

import os
import sys
import time
import logging
from pathlib import Path

# Add src to path
sys.path.append(str(Path(__file__).parent))

# Setup basic logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('ARES')

def main():
    """Main entry point - simple version"""
    print(" ARES 4.0 Trading Bot Starting...")
    print(" Make sure all configuration files exist")
    
    counter = 0
    try:
        while True:
            counter += 1
            logger.info(f"Strategy check #{counter}")
            print(f" Cycle #{counter} - Bot is running...")
            time.sleep(5)  # Check every 5 seconds
            
    except KeyboardInterrupt:
        print("\n Bot stopped by user")
    except Exception as e:
        logger.error(f"Bot error: {e}")

if __name__ == "__main__":
    main()
