#!/bin/bash

PYTHON_SCRIPT="main.py"

# Check if the Python script exists
if [ -f "$PYTHON_SCRIPT" ]; then
    echo "Found $PYTHON_SCRIPT"

    python3 "$PYTHON_SCRIPT"

    # Check if the program executed successfully
    if [ $? -eq 0 ]; then
        echo "Program executed successfully."
    else
        echo "Error: Program execution failed."
        exit 1
    fi

else
    echo "Error: $PYTHON_SCRIPT not found."
    exit 1
fi
