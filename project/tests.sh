#!/bin/bash

# Test: Run the data pipeline
echo "Running data pipeline..."

# Run your pipeline
python pipeline.ipynb

# List of output files to check
OUTPUT_FILES=("final_dataset.csv")

# Check if each output file exists
for file in "${OUTPUT_FILES[@]}"; do
    if [ -f "$file" ]; then
        echo "Test Passed: $file exists."
    else
        echo "Test Failed: $file does not exist."
        exit 1
    fi
done

# Optionally, check if the file size is reasonable (non-zero)
for file in "${OUTPUT_FILES[@]}"; do
    if [ -s "$file" ]; then
        echo "Test Passed: $file is not empty."
    else
        echo "Test Failed: $file is empty."
        exit 1
    fi
done

# Test successful completion
echo "All tests passed!"