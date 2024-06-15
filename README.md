# topic_surveyor_ml

This project builds on exploratory work done by [Eric French](https://github.com/ericfrench2015/topic_surveyor/tree/main) that endeavors to pull disaster summary data from common humnitarian data sources and perform several key function:

1) Summarize the information concisely to allow response and recovery teams to quickly understand the rough shape of what's happening

2) Extract quantitative information to allow dashboarding and visualization of key statistics (killed, injured, displaced, etc)

3) Use the above inforamtion to decorate a dataset that can be used to build visualization and dashboarding data products

## ML Experimentation

In addition to data extraction, Eric explored the use of natural language processing (NLP) using Python's Spacy module to tokenize commonly occurring phrases and extract key information. I've tried to extend this work using generally available machine learning models. In particular, I explored the `transformers` library from HuggingFace, focusing on pipelines for text summarization and question and answer.

## Disclaimers

1) I am not a machine learning expert, so there's likely lots of room for improvement on this work

2) The models I am using are pretrained on datasets that are not specific to humanitarian constructs

    a. I did some experimentation with [Humbert](https://huggingface.co/nlp-thedeep/humbert) but found that other models performed better for this task. (could be user error, tbh)

    b. I did not attempt to fine tune or retrain any of these models, so consider this a baseline that could be improved (possibly substantially) with more effort   

    c. I did not experiment with commercial LLMs like GPT, Claude or Gemini. These models generally incur costs per use - they are probably worth exploring, but we'd need to understand how to manage operational costs.

    d. At this stage, I am not using any [RAG](https://blogs.nvidia.com/blog/what-is-retrieval-augmented-generation/) techniques. Using RAG could further improve resultes, but greatly increases the size of the prompt so will increase costs on usage-based models like GPT.

## Methodology
TODO

### Code and Data References
TODO

## Findings so far
TODO


### Summarization Data Quality Considerations
TODO

### NER / Extraction Data Quality Considerations
TODO

### Operational / Performance Considerations
TODO

## Recommended Next steps
TODO
