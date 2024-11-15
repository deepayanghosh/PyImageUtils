#!/usr/bin/env python3

"""
Main script to execute the program.
"""

import sys
from resize import resize_images
from paths import *

def main():
    """Main function to execute the script."""
    
    resize_images( source_dir, resize_dest_dir, crop_dest_dir)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)