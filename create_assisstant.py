from vapi import Vapi

client = Vapi(
    token="dae9c0c2-0477-4cf6-97ac-4f1bb49e7287"
)

print (client)

result = client.assistants.create()

print (result.id)

"""
transcriber=None 
model=None 
voice=None 
first_message=None 
first_message_interruptions_enabled=None 
first_message_mode=None 
voicemail_detection=None 
client_messages=None 
server_messages=None 
max_duration_seconds=None 
background_sound=None 
model_output_in_messages_enabled=None 
transport_configurations=None 
observability_plan=None 
credentials=None 
hooks=None 
name=None 
voicemail_message=None 
end_call_message=None 
end_call_phrases=None 
compliance_plan=None 
metadata=None 
background_speech_denoising_plan=None 
analysis_plan=None 
artifact_plan=None 
start_speaking_plan=None 
stop_speaking_plan=None 
monitor_plan=None 
credential_ids=None 
server=None 
keypad_input_plan=None 
id='ed670658-772b-4b4a-ab86-bebafec76f72' 
org_id='12106f7c-cfe2-44b8-b0a4-08014b6c63c4' 
created_at=datetime.datetime(2026, 2, 10, 15, 58, 7, 882000, tzinfo=datetime.timezone.utc) 
updated_at=datetime.datetime(2026, 2, 10, 15, 58, 7, 882000, tzinfo=datetime.timezone.utc) 
isServerUrlSecretSet=False
"""