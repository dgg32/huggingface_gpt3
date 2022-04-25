from crosslingual_coreference import Predictor

predictor = Predictor(language="en_core_web_sm", device=-1, model_name="info_xlm")

def resolve_pronoun (raw_text):
    text = (raw_text)

    return (predictor.predict(text)["resolved_text"])


if __name__ == "__main__":

    raw_text = "In chicken, adiposity is influenced by hepatic stearoyl-CoA desaturase (SCD) 1. This gene is up-regulated by low-fat high-carbohydrate diet and down-regulated by addition of polyunsaturated fatty acids (PUFA)."
    print (resolve_pronoun(raw_text))