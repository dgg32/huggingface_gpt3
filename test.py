import gpt3
import entity_linkage

res = gpt3.extract_relation("gpt3_training_cazy.txt", "#Discovery and screening of novel metagenome-derived GH107 enzymes targeting sulfated fucans from brown algae" + "\n")

results = res.split(",")

if len(results) == 3:
    disam = entity_linkage.name_disambiguation(results[2])
    results[2] = disam

    print (",".join(results))