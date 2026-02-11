STATUS QUO: For now I can not do an outbound call since the free numbers from vapi ai dont allow this.

1. Define the Model and what it does for an inbound call. 
2. Assign the Model to an Assisstant
3. Try to do a Call to an Inbound Assisstant created via Code
4. Build the wrapper as a backend version: Define Parameters for the Inbound Voice Agent to collect, write a file which collects them and a file which uses them to setup the assisstant with its number
5. Build the Frontend and Database

Ongoing: In ongoing phases we can still add things other numbers via f. e. twilio and outbound calls


......

"1. Functions to create assisstant create_assisstant(system_message, first_message, phone_number - return assisstant_id)
2. Functions to do the calls call_list(dict[customers: names:numbers], assisstent_id - return list[transcripts])
Test with same number or more numbers bought via twilio or vapi ai
3. Speicherung von Transcripts save_transcript(transcripts)
4. extract_meeting_data_from_transcript(transcripts)
4. Create Meeting (via composio), create_meeting(Meeting_Data)"