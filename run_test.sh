#!/bin/bash

TEST_FILE="test_main.py"

# Run the tests
echo "Running tests..."
pytest $TEST_FILE -v

if [ $? -eq 0 ]; then
    echo "All tests passed successfully!"
else
    echo "Some tests failed"
fi
