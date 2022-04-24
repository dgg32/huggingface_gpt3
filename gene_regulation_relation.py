from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
import spacy
import sys
import gpt3

tokenizer = AutoTokenizer.from_pretrained("alvaroalon2/biobert_genetic_ner")

model = AutoModelForTokenClassification.from_pretrained("alvaroalon2/biobert_genetic_ner")

model_infer = pipeline('ner',model=model,tokenizer=tokenizer)

nlp = spacy.load("en_core_web_sm")

verbs = ["up", "promot", "down", "suppress" "overexpress"]

if __name__ == "__main__":
    input_file = sys.argv[1]

    sentences = open(input_file).read()

    doc = nlp(sentences)
    assert doc.has_annotation("SENT_START")
    for sent in doc.sents:
        #print(sent.text)
        entities = model_infer(sent.text)
        if len(entities) > 0:
            has_verb = False
            for v in verbs:
                if v in sent.text:
                    has_verb = True
            
            if has_verb == True:

                res = gpt3.extract_relation("gpt3_training_gene_regulation.txt", sent.text.strip() + "\n")
            
                print(res)
    