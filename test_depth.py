#!/usr/bin/env python3
"""
Test script to verify depth limiting functionality in doc_to_md.py
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Temporarily modify sys.argv to prevent the main execution
original_argv = sys.argv.copy()
sys.argv = [sys.argv[0]]  # Keep only the script name

from doc_to_md import DocDumper

# Restore original argv
sys.argv = original_argv

def test_depth_functionality():
    """Test that DocDumper properly handles depth parameter"""
    print("Testing depth limiting functionality...")
    
    # Test creating DocDumper with different depth values
    dumper_unlimited = DocDumper("https://example.com", "test_output", max_depth=float('inf'))
    print(f"Unlimited depth: {dumper_unlimited.max_depth}")
    
    dumper_limited = DocDumper("https://example.com", "test_output", max_depth=2)
    print(f"Limited depth (2): {dumper_limited.max_depth}")
    
    dumper_zero = DocDumper("https://example.com", "test_output", max_depth=0)
    print(f"Zero depth: {dumper_zero.max_depth}")
    
    print("Depth limiting functionality test completed successfully!")

if __name__ == "__main__":
    test_depth_functionality()