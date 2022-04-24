from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
import spacy
import sys
import gpt3

tokenizer = AutoTokenizer.from_pretrained("alvaroalon2/biobert_chemical_ner")

model = AutoModelForTokenClassification.from_pretrained("alvaroalon2/biobert_chemical_ner")

model_infer = pipeline('ner',model=model,tokenizer=tokenizer)

nlp = spacy.load("en_core_web_sm")

if __name__ == "__main__":

    input_file = sys.argv[1]

    sentences = open(input_file).read()

    doc = nlp(sentences)
    assert doc.has_annotation("SENT_START")
    for sent in doc.sents:
        #print(sent.text)
        entities = model_infer(sent.text)
        if len(entities) > 0:
            print (sent.text)
            res = gpt3.extract_relation("gpt3_training_metabolic.txt", sent.text.strip() + "\n")
            
            print(res)
