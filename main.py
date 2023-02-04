from evaluate import load


#ref is the reference file we compare the transcription to
cer = load("cer")
#input path to reference file
ref = open('', 'r')
#input path to file you want to compare reference to
pred = open('', 'r')
#put input into string
referenceString = ''
predictionString = ''
for i in ref.read():
    if i != '' and i != '\n':
        referenceString += i
for i in pred.read():
    if i != '' and i != '\n':
        predictionString += i
#CER wants lists as input
references = [referenceString]
predictions = [predictionString]
cer_score = cer.compute(predictions=predictions, references=references)
print(cer_score)
