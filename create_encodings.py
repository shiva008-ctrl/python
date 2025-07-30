import os
import json

# Create database directory if it doesn't exist
os.makedirs('database', exist_ok=True)

# Create empty encodings file
with open('database/face_encodings.json', 'w') as f:
    json.dump({}, f)

print("Database directory and encoding file created!")