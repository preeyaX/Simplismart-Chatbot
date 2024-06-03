
URL to this blog: [](https://www.simplismart.ai/blog/what-is-a-voicebot-and-how-to-build-a-generative-ai-voicebot)

# Voicebot Explained: Building Your AI Voicebot | SimpliSmart
> This blog is an introduction to building voicebots with Simplismart's Generative AI APIs, namely Whisper, Llama and Tortoise. We'll also take you through the basics of Voicebots and their usecases, how they help with call-centre automation and customer success and how you can build an MVP version of your own voicebot with Simplismart APIs.  

What is a Voicebot?
-------------------

A voicebot, also known as a conversational AI or virtual assistant, is an AI-powered software that communicates with users in natural language, interpreting their inquiries and providing appropriate responses. In the context of call centre automation, voicebots revolutionize customer service by handling repetitive queries and streamlining processes. For instance, when a customer seeks to block a credit card, a voicebot can efficiently guide them through the necessary steps without human intervention, enhancing efficiency and customer satisfaction.

Moreover, in the realm of customer success, voicebots play a pivotal role in enhancing user experience by providing instant support and resolving issues promptly. With advancements in machine learning (ML) and the advent of tools like LLMs and ChatGPT,  modern voicebots can simulate human-like conversations, making interactions seamless and personalized.

In essence, voice bots epitomize the fusion of AI technology and customer service, offering businesses a scalable and efficient solution to cater to the evolving needs of their clientele.

### Use cases of Voicebots:  

There are a lot of use cases for Generative AI Voicebots. They are very useful for Call Centres which can automate some parts of manual calling, providing up to 30% productivity gain and massive ROI. Here are the flows call centres can easily automate with Generative AI Voicebots:

*   Post-purchase customer support calls
*   Pre-Purchase queries
*   Booking and Reservation
*   Parcel Tracking
*   Telemarketing Calls
*   Payment Reminder
*   Feedback Collection

How to build a Voicebot?
------------------------

### **What are the Multiple AI layers in a voicebot?**

There are 3 models that you'd have to run in series to generate human-like responses. Here is a small user-flow that will follow:  

!Generative AI Voicebot

​**Automatic Speech Recognition Model**: Converts spoken words into text. Utilizes the Whisper Large v3 model. Simplismart has optimised Whisper for 30x faster transcriptions than real-time. We are also the only company to fine-tune Whisper on Hindi and Regional Indic languages, giving far better results for Indian use-cases.

**Text Generation Model**: This part of the ML pipeline formulates responses to user queries. It relies on the Mistral-7B Instruct v0.2 model, you can also use the Llama-7b model, and connect your own RAG wherever you need answers from a specific knowledge base. Another thing you can do is make an Intent or flow-based voicebot with journeys and fallbacks.

**Text-to-Audio Model**: Transforms text responses into speech using the Bark, Tortoise or XTTS model. Simplismart takes a response time of just 7.5 sec for a one-minute audio. This part of the pipeline can also be streamed to get real-time results.​

### Developing your Voicebot:  

This blog will give a step-by-step guide on how using Simplismart’s deployment suite, one can easily set-up a voice conversational bot. The next section is divided into three parts giving an in-depth explanation on how to work with the complete ML pipeline.  

### Firstly, Speech to text

The idea is to use **Whisper**, a fast speech to text detection model that converts human speech into text, with maximum accuracy, and lowest latency. For maximum accuracy, the model should detect the input language and should be fine-tuned on it. All of this is possible with Simplitrain, but first, let's start by building out the MVP for our voicebot. For that, you'd want to test out Simpliscribe, our in-house pay-as-you-go transcription API.

You need to get the API key from the Simpliscribe webapp and run the given python script. Here is how you can generate the API access key and secret access key:  
1\. Log in to the Simpliscribe Dashboard.  
2\. On the Left please go to the **"Connect"** tab, and then generate a **"NEW API key"**.

!NEW API key

3\. Once generated please keep the secret key saved in for future reference, it cannot be viewed again.

Here is the **sample python script** to run Simpliscribe:

```
import requests
url ="https://simpliscribe.simplismart.ai/api/transcribe/"
payload = {
     "audiofile_name": "testing1",
     "translate": False,
     "language": "en",
     "initial_prompt": "",
     "beam_size": None,
     "best_of": None,
     "patience": None,
     "length_penalty": None,
     "without_timestamps": False,
     "vad_filter": True,
     "audio_sample_rate": 16000,
     "speech_threshold": 0.6,
     "min_speech_duration_ms": 250,
     "max_speech_duration_s": None,
     "min_silence_duration_ms": 1000,
     "diarization": False,
     "num_speakers": 0,
     "word_timestamps": False,
}
files = [
     (
         "file",
         (
             "sample.mp3",
             open(
                 "sample.mp3",
                 "rb",
             ),
             "audio/mpeg",
         ),
     )
]
headers = {
   "access-key": "<access-key>",
   "secret-key": "<secret-key>",
}
response = requests.request("POST", url, headers=headers, data=payload, files=files)
import json
answer = json.loads(response.text)
print(answer)

```


You can also check out our documentation to change these default parameters and fine-tune transcriptions for your usecase.

### Generating Responses from Large Language Models

This will be the next part of the pipeline. Generate response from LLMs (Preferred Mistral-7B-Instruct or LLama2-7B) that have capability to give accurate and crisp response to the query.  

Here is how you can use SimpliLLM to generate LLM inferences:

```
from openai import OpenAI
token = "<Your Token Here>"
client = OpenAI(base_url="<Your LLM URL here>", api_key=token)
stream = client.chat.completions.create(
     model = "mistral",
     messages=[{"role": "user", "content": "how many bones are there in human body?"}],
     stream=True,
     max_tokens=64,
     temperature=0.9
)
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
```


Connect with the Simplismart team to get your LLM Token. 

### Finally, Speech Generation

The last part of the Voicebot puzzle is to generate a human-like response in clear audio as output. The tortoise model is best suited for this task, as it is a pretty light model giving a highly efficient output. You can also choose the voice sample for this model.

You can find the tortoise model on Github and easily deploy it using the Simplismart platform.

Challenges and Closing Remarks
------------------------------

Developing a generative AI Voicebot can enhance call centre operations, yet it poses distinct challenges in the Indian context:

**Models not nicely trained for Non-English Languages**: The performance of ASR Models, LLMs and Speech-to-text models for Indian languages is often subpar. If the call centre caters to multiple Indian languages, addressing this gap technologically becomes imperative. Simplismart has finetuned the OpenAI Whisper and Meta Llama Models model on Indic datasets to make it better for Indian languages.​

**Audio Quality**: Variations in audio quality are prevalent in Indian call centers due to factors like background noise and varying accents. Extensive data processing is necessary to refine audio files.

**Performance vs. Cost**: STT and TTS models demand substantial computational resources. Balancing performance accuracy with GPU cost efficiency is crucial. This involves optimizing GPU utilization, facilitating GPU sharing, and dynamically scaling workloads to minimize expenses.

**Data Privacy**: Indian call centers handle sensitive customer data, including financial information. Safeguarding this data and ensuring compliance with privacy regulations are paramount concerns that the team must address effectively.​

After navigating these challenges, a generative AI call centre application can significantly elevate call centre performance while ensuring quality, regulatory requirements and cost-effectiveness.

Want to start building Voicebots?

Connect with us if you want to build out your Voicebots with Simplismart.

​