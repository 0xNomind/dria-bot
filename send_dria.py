import requests
import os

file_path = 'one_piece_prompts.jsonl'
api_key = 'YOUR_API_KEY'
base_url = 'https://mainnet.dkn.dria.co/api/v0'

# Step 1: Get upload URL
resp = requests.get(f'{base_url}/file/get_upload_url', headers={'x-api-key': api_key})
resp.raise_for_status()
data = resp.json()
url, file_id = data['url'], data['id']

# Step 2: Upload file to S3
with open(file_path, 'rb') as f:
    upload_resp = requests.put(url, data=f, headers={
        'Content-Type': 'binary/octet-stream',
        'Content-Length': str(os.path.getsize(file_path)),
    })
    upload_resp.raise_for_status()

# Step 3: Complete the upload
complete_resp = requests.post(f'{base_url}/batch/complete_upload',
    headers={'Content-Type': 'application/json', 'x-api-key': api_key},
    json={'id': file_id})
complete_resp.raise_for_status()

print('✅ File ID:', file_id)
print('✅ Upload completed successfully:', complete_resp.json())