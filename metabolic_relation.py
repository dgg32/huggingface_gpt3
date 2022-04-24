from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
import spacy

tokenizer = AutoTokenizer.from_pretrained("alvaroalon2/biobert_chemical_ner")

model = AutoModelForTokenClassification.from_pretrained("alvaroalon2/biobert_chemical_ner")

model_infer = pipeline('ner',model=model,tokenizer=tokenizer)

nlp = spacy.load("en_core_web_sm")
