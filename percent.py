#!/usr/bin/env python3
"""
Simple CSV Filter: AI Tutor = 2 AND Education Setting = 2:CS
Just two options:
1. Show statistics
2. Generate filtered CSV
"""

import csv
from datetime import datetime


def filter_data(file_path):
    """
    Find all entries where:
    - AI Tutor Category contains "2"
    - Education Setting contains "2" and "cs"
    """
    matching_entries = []
    total_entries = 0
    
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames
        
        for row in reader:
            total_entries += 1
            
            # Get values
            ai_tutor = (row.get('AI Tutor Category', '') or '').lower()
            edu_setting = (row.get('Education Setting', '') or '').lower()
            
            # Check if both contain "2" and education contains "cs"
            if '2' in ai_tutor and '2' in edu_setting and 'cs' in edu_setting:
                matching_entries.append(row)
    
    return matching_entries, total_entries, fieldnames


def main():
    file_path = 'AI Literature/AI-Literature/IEEE_papersCombinedAndCategorized - Ieee_papersCombined.csv'
    ## what is pandas
    print("\n" + "="*60)
    print("  Filter: AI Tutor = 2 AND Education Setting = 2:CS")
    print("="*60)
    
    while True:
        print("\nOptions:")
        print("  1 - Show statistics")
        print("  2 - Generate CSV with filtered results")
        print("  3 - Exit")
        print("-"*60)
        
        choice = input("\nEnter your choice (1, 2, or 3): ").strip()
        
        if choice == '1':
            # Show statistics
            print("\n" + "="*60)
            print("📊 Analyzing data...")
            print("-"*60)
            
            matching, total, _ = filter_data(file_path)
            percentage = (len(matching) / total * 100) if total > 0 else 0
            
            print(f"Total entries: {total}")
            print(f"Matching entries (AI Tutor = 2 AND Education = 2:CS): {len(matching)}")
            print(f"Percentage: {percentage:.2f}%")
            print("="*60)
        
        elif choice == '2':
            # Generate CSV
            print("\n" + "="*60)
            print("📄 Generating CSV...")
            print("-"*60)
            
            matching, total, fieldnames = filter_data(file_path)
            
            # Create output filename in current directory
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = f'ai_tutor_2_education_2cs_{timestamp}.csv'
            
            # Write to CSV
            with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(matching)
            
            print(f"✓ CSV file created successfully!")
            print(f"  File: {output_file}")
            print(f"  Entries: {len(matching)}")
            print("="*60)
        
        elif choice == '3':
            print("\n👋 Goodbye!")
            break
        
        else:
            print("\n❌ Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()