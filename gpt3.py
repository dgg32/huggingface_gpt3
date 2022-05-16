import os
import sys
import openai


openai.api_key = os.getenv("OPENAI_API_KEY")

#print ("in Gpt3")

def extract_relation (training_file, text):

    training = "\n".join([x.strip() for x in open(training_file, 'r').readlines()]) + "\n\n"
    my_prompt = training + text
    
    #print (my_prompt)
    response = openai.Completion.create(
        engine="text-curie-001",
        prompt=my_prompt,
        temperature=0,
        max_tokens=70,
        top_p=0,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response.choices[0].text.lstrip()

if __name__ == "__main__":

    training_file = sys.argv[1]
    input_file = sys.argv[2]

    training = "\n".join(open(training_file, 'r').readlines()) + "\n"

    with open(input_file, 'r') as file_in:
        for line in file_in:
            if len(line.strip()) > 0:
                res = extract_relation(training, line.strip() + "\n")

                print(res)