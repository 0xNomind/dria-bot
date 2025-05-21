#!/bin/bash

# Function to run a Python script
run_script() {
  script_name="$1"
  echo "Running script: $script_name"

  # Try running with python3 first
  command -v python3 >/dev/null 2>&1 && {
    echo "Trying python3..."
    python3 "$script_name"
    if [ $? -eq 0 ]; then
      echo "Script '$script_name' executed successfully with python3."
      return 0 # Return success
    fi
    echo "Script '$script_name' failed with python3. Trying python..."
  } || echo "python3 not found. Trying python..."

  # Try running with python
  python "$script_name"
  if [ $? -eq 0 ]; then
    echo "Script '$script_name' executed successfully with python."
    return 0 # Return success
  else
    echo "Script '$script_name' failed with both python3 and python."
    echo "Check the script for errors."
    return 1 # Explicitly return 1 for failure
  fi
}

# Main loop
while true
do
  # Run generate_prompt.py
  run_script "generate_prompt.py"

  # Run send_dria.py
  run_script "send_dria.py"

  # Wait for 1 hour (3600 seconds)
  echo "Waiting for 1 hour before running the scripts again..."
  sleep 3600
done
