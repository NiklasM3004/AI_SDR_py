from vapi import Vapi

client = Vapi(
    token="dae9c0c2-0477-4cf6-97ac-4f1bb49e7287"
)

client.calls.create(
    customer={"number": "+4915156925081"},
    assistant_id="bf961585-956f-4bf7-a02e-5f3c7169ba48"
)
