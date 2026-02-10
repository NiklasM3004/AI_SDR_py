from vapi import Vapi

client = Vapi(
    base_url="https://api.vapi.ai/",
    token="dae9c0c2-0477-4cf6-97ac-4f1bb49e7287"
)

result = client.phone_numbers.create(
    request={
        "provider": "vapi",
        "number_desired_area_code": "307",
        "assistant_id": "9c3d80ff-64a4-4267-9efe-e630a8bc542e"
    }
)

print(result)