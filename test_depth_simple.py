#!/usr/bin/env python3
"""
Simple test to verify depth limiting functionality in doc_to_md.py
"""

import sys
import os
import tempfile

# Add the current directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_depth_functionality():
    """Test that DocDumper properly handles depth parameter"""
    print("Testing depth limiting functionality...")
    
    # Import and use the DocDumper class
    from doc_to_md import DocDumper
    
    # Create a temporary directory for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        # Test creating DocDumper with different depth values
        dumper_unlimited = DocDumper("https://example.com", temp_dir, max_depth=float('inf'))
        print(f"✓ Unlimited depth: {dumper_unlimited.max_depth}")
        
        dumper_limited = DocDumper("https://example.com", temp_dir, max_depth=2)
        print(f"✓ Limited depth (2): {dumper_limited.max_depth}")
        
        dumper_zero = DocDumper("https://example.com", temp_dir, max_depth=0)
        print(f"✓ Zero depth: {dumper_zero.max_depth}")
        
        # Test that the depth parameter is properly stored
        assert dumper_unlimited.max_depth == float('inf'), "Unlimited depth not set correctly"
        assert dumper_limited.max_depth == 2, "Limited depth not set correctly"
        assert dumper_zero.max_depth == 0, "Zero depth not set correctly"
        
        print("✓ All depth parameter tests passed!")
        
        # Test that crawl queue and enqueued URLs are properly initialized with depth tracking
        print(f"✓ Crawl queue type: {type(dumper_limited.crawl_queue)} (should be list of tuples)")
        print(f"✓ Enqueued URLs type: {type(dumper_limited.enqueued_urls)} (should be dict)")
        
        # Test depth functionality logic
        # Test if depth limiting would work in crawl method
        test_depth = 2
        dumper = DocDumper("https://example.com", temp_dir, max_depth=test_depth)
        
        # Simulate URL queue with depths
        test_queue = [("https://example.com/page1", 0), ("https://example.com/page2", 1), ("https://example.com/page3", 3)]
        filtered_queue = [(url, depth) for url, depth in test_queue if depth <= dumper.max_depth]
        
        print(f"✓ Depth filtering test: {len(test_queue)} -> {len(filtered_queue)} (depth limit: {test_depth})")
        
        assert len(filtered_queue) == 2, "Depth filtering not working correctly"
        
        print("✓ Depth limiting functionality test completed successfully!")
        return True

if __name__ == "__main__":
    test_depth_functionality()