import jwt
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwOTU1NDgwMCwiaWF0IjoxNzA5NDY4NDAwLCJqdGkiOiJiYWRlZjE3NDAxYzg0Njk4YTI3OTQ3NzI3NTk3MjEyZiIsInVzZXJfaWQiOiI2MThiNGU3NS05ZmUxLTRlNjYtYjM0NC0wN2VlY2JjMzcwMTIifQ.5-VYALtPoXn_AImu07FwEndWiB0_oHmQc60MoxJqlMY"

decoded_token = jwt.decode(token, verify=False)  # Decodes the token without verification

print(decoded_token)