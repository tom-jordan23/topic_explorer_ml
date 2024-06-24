# topic_explorer_ml

This project builds on exploratory work done by [Eric French](https://github.com/ericfrench2015/topic_surveyor/tree/main) that endeavors to pull disaster summary data from common humanitarian data sources and perform several key function:

1) Summarize the information concisely to allow response and recovery teams to quickly understand the rough shape of what's happening

2) Extract quantitative information to allow dashboarding and visualization of key statistics (killed, injured, displaced, etc)

3) Use the above information to decorate a dataset that can be used to build visualization and dashboarding data products

## ML Experimentation

In addition to data extraction, Eric explored the use of natural language processing (NLP) using Python's Spacy module to tokenize commonly occurring phrases and extract key information. I've tried to extend this work using generally available machine learning models. In particular, I explored the `transformers` library from HuggingFace, focusing on pipelines for text summarization and question and answer.

## Disclaimers

1) I am not a machine learning expert, so there's likely lots of room for improvement on this work

2) The models I am using are pretrained on datasets that are not specific to humanitarian constructs

    a. I did some experimentation with [Humbert](https://huggingface.co/nlp-thedeep/humbert) but found that other models performed better for this task. Humbert (and the underlying [Humset](https://huggingface.co/datasets/nlp-thedeep/humset)) are geared towards multi-label classification rather than summarization or Q&A, but may be a good source of training data for other models.

    b. I did not attempt to fine tune or retrain any of these models, so consider this a baseline that could be improved (possibly substantially) with more effort   

    c. I did not experiment with commercial LLMs like GPT, Claude or Gemini. These models generally incur costs per use - they are probably worth exploring, but we'd need to understand how to manage operational costs.

    d. At this stage, I am not using any [RAG](https://blogs.nvidia.com/blog/what-is-retrieval-augmented-generation/) techniques beyond providing context in the pipeline. Using RAG could further improve resultes, but greatly increases the size of the prompt so will increase costs on usage-based models like GPT.

## Results

Results for both summarization and Q&A can be found in the respective CSV files. My impressions overall:

1) Summarization using an existing pretrained model is not terrible, and can probably be made better through fine-tuning based on humanitarian data from [TheDeep](https://huggingface.co/nlp-thedeep) or other humanitarian sources.

2) Q&A using an existing pretrained model against reliefweb summaries is not as good - we would definitely need to invest some time into fine tuning (and possibly retraining) the models that I've tested. Foundation models could also perform better, but we'll incur usage costs.

3) However well we do, we need to make sure that we decorate the data with some identification about which components were AI/ML derived.

4) In testing on my local workstation, inference time varied from a few seconds to 30+ seconds. We'd have to consider performance as an architectural constraint. At this point, I'm assuming we probably would not try to do inference in realtime in an interactive user session. Instead,  we'd collect the data, run inferences in batch mode and use the inference data to supplement a dataset we'd then use for analytical apps and data products.

## Recommended next steps

1) Assuming that we feel there's value, I can continue experimentation with fine-tuning or retraining summarization models based on reliefweb data to see how much better we can get.

2) I'd like to try fine-tuning some of the Q&A models to see how much they improve with training on a humanitarian dataset. 

3) It would be good to examine how the foundation models do in this space - AWS Bedrock might be a good way to do some sandboxing / experimentation, but I'm not familiar with how we address usage costs for exploration.

## GANNET - another option to explore

As I was finishing this work, I received an invitation from [Data Friendly Space](https://www.datafriendlyspace.org/) to preview [GANNET](gannet.ai), a ChatGPT style generative AI platform for humanitarian applications. A few samples of the GANNET UI and search results:
- [chat interface](gannet_preview/gannet_ui.png)
- [map summary](gannet_preview/gannet_map.png)
- [chart of references](gannet_preview/gannet_chart.png)

At first glance, this looks like a promising option for handling some of the summarization, NLP and data extraction needs. More exploration is needed to understand whether we can interface with GANNET via API, what the cost model will be, etc. 



