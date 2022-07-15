from evaluate import load

cer = load("cer")
ref = open('/Users/intern/PycharmProjects/pythonProject/F512_ref_file.txt', 'r')
pred = open('/Users/intern/PycharmProjects/pythonProject/F512F509-7916-49C0-BFF7-73C702BF2A66_transcript.txt', 'r')
referenceString = ''
predictionString = ''
for i in ref.read():
    if i != '' and i != '\n':
        referenceString += i
for i in pred.read():
    if i != '' and i != '\n':
        predictionString += i
references = [referenceString]
predictions = [predictionString]
cer_score = cer.compute(predictions=predictions, references=references)
print(cer_score)