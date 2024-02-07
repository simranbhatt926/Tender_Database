import numpy as np

# language_client = TextAnalyticsClient(
#             endpoint=endpoint, 
#             credential=credentials)
# response = language_client.extract_key_phrases(documents = documents)[0]
# result = client.analyze_conversation(
#     task={
#         "kind": "Conversation",
#         "analysisInput": {
#             "conversationItem": {
#                 "participantId": "1",
#                 "id": "1",
#                 "modality": "text",
#                 "language": "en",
#                 "text": query
#             },
#             "isLoggingEnabled": False
#         },
#         "parameters": {
#             "projectName": cls_project,
#             "deploymentName": deployment_slot,
#             "verbose": True
#         }
#     }
# )
cls_project = 'Clock'
deployment_slot = 'production'

with client:
    query = userText
    result = client.analyze_conversation(
        task={
            "kind": "Conversation",
            "analysisInput": {
                "conversationItem": {
                    "participantId": "1",
                    "id": "1",
                    "modality": "text",
                    "language": "en",
                    "text": query
                },
                "isLoggingEnabled": False
            },
            "parameters": {
                "projectName": cls_project,
                "deploymentName": deployment_slot,
                "verbose": True
            }
        }
    )

top_intent = result["result"]["prediction"]["topIntent"]
entities = result["result"]["prediction"]["entities"]

print("view top intent:")
print("\ttop intent: {}".format(result["result"]["prediction"]["topIntent"]))
print("\tcategory: {}".format(result["result"]["prediction"]["intents"][0]["category"]))
print("\tconfidence score: {}\n".format(result["result"]["prediction"]["intents"][0]["confidenceScore"]))

print("view entities:")
for entity in entities:
    print("\tcategory: {}".format(entity["category"]))
    print("\ttext: {}".format(entity["text"]))
    print("\tconfidence score: {}".format(entity["confidenceScore"]))

print("query: {}".format(result["result"]["query"]))