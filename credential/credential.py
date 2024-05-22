import json
import sys

import boto3

try:
    client = boto3.client('sts')
    response = client.get_caller_identity()
    output = {
        "env": {
            "AWS": 'true',
        }
    }

except Exception as e:
    print("Please authenticate with AWS - ", e, file=sys.stderr)
    sys.exit(1)

print(json.dumps(output))
