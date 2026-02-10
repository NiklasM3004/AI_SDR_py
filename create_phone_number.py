from vapi import Vapi

client = Vapi(
    token="YOUR_TOKEN_HERE"
)

client.phone_numbers.create(
    request={
        "provider": "byo-phone-number",
        "credential_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    }
)
