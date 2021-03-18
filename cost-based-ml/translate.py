import boto3

translate = boto3.client(service_name='translate',region_name='us-east-1', use_ssl=True)
t = "How are you"
result = translate.translate_text(Text=t,SourceLanguageCode="en",TargetLanguageCode="de")

print(t)
print('TranslatedText: ' + result.get('TranslateText'))
print('SourceLanguageCode: ' + result.get('SourceLanguageCode'))
print('TargetLanguageCode: ' + reslut.get('TargetLanguageCode'))
