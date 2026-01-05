"""
Script to merge tweet text from CSV into the merged_output.normalized.json file.

This script reads the source tweets CSV and adds the text_cleaned and text_original
fields to each tweet entry in the JSON, similar to how analogy_merged_output.normalized.json
already has the text_cleaned field.

Usage:
    python merge_csv_to_json.py <csv_file> <json_file> [output_file]

Example:
    python merge_csv_to_json.py "tw ny sample all topics basic columns.csv" merged_output.normalized.json merged_output.with_text.json
"""

import json
import csv
import sys
from pathlib import Path


def parse_csv(csv_path):
    """Parse CSV file and return a dictionary keyed by tweet_id."""
    tweets = {}
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            tweet_id = row.get('tweet_id', '')
            if tweet_id:
                tweets[str(tweet_id)] = {
                    'text_original': row.get('text_original', ''),
                    'text_cleaned': row.get('text_cleaned', ''),
                    'user_name': row.get('user_name', ''),
                    'screen_name': row.get('screen_name', ''),
                    'user_description': row.get('user_description', ''),
                    'topic_label': row.get('Topic_label_merged', ''),
                    'language': row.get('language', ''),
                }
    return tweets


def merge_json_with_csv(json_path, csv_tweets):
    """Load JSON and merge tweet text from CSV."""
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    merged_count = 0
    missing_count = 0

    # Handle both object format (keyed by tweet_id) and array format
    if isinstance(data, dict):
        for tweet_id, entry in data.items():
            csv_entry = csv_tweets.get(str(tweet_id))
            if csv_entry:
                entry['text_cleaned'] = csv_entry['text_cleaned']
                entry['text_original'] = csv_entry['text_original']
                entry['user_name'] = csv_entry['user_name']
                entry['screen_name'] = csv_entry['screen_name']
                entry['user_description'] = csv_entry['user_description']
                entry['topic_label'] = csv_entry['topic_label']
                entry['language'] = csv_entry['language']
                merged_count += 1
            else:
                missing_count += 1
    elif isinstance(data, list):
        for entry in data:
            tweet_id = entry.get('tweet_id', '')
            csv_entry = csv_tweets.get(str(tweet_id))
            if csv_entry:
                entry['text_cleaned'] = csv_entry['text_cleaned']
                entry['text_original'] = csv_entry['text_original']
                entry['user_name'] = csv_entry['user_name']
                entry['screen_name'] = csv_entry['screen_name']
                entry['user_description'] = csv_entry['user_description']
                entry['topic_label'] = csv_entry['topic_label']
                entry['language'] = csv_entry['language']
                merged_count += 1
            else:
                missing_count += 1

    return data, merged_count, missing_count


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    csv_path = sys.argv[1]
    json_path = sys.argv[2]
    output_path = sys.argv[3] if len(sys.argv) > 3 else json_path.replace('.json', '.with_text.json')

    print(f"Reading CSV: {csv_path}")
    csv_tweets = parse_csv(csv_path)
    print(f"  Found {len(csv_tweets)} tweets in CSV")

    print(f"Reading JSON: {json_path}")
    merged_data, merged_count, missing_count = merge_json_with_csv(json_path, csv_tweets)
    print(f"  Merged: {merged_count} tweets")
    print(f"  Missing from CSV: {missing_count} tweets")

    print(f"Writing output: {output_path}")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(merged_data, f, ensure_ascii=False)

    print("Done!")

    # Print file size
    output_size = Path(output_path).stat().st_size
    print(f"Output file size: {output_size / 1024 / 1024:.2f} MB")


if __name__ == '__main__':
    main()
