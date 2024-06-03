
URL to this blog: [](https://www.simplismart.ai/blog/how-vodex-decreased-latency-by-50-percent-and-saved-100k-dollar-in-compute-costs)

# Vodex Success Story: Cutting Latency, Saving Costs | SimpliSmart
How Vodex Decreased Latency by 50% and Saved $100k in Compute Costs
-------------------------------------------------------------------

Contents

*   TL;DR
    
*   Some context about Vodex:
    
*   Generative AI Product Suite from Simplismart
    *   How does Simplismart decrease latency and save costs?
*   Conclusion:
    

TL;DR
-----

> Vodex was facing latency issues in their contact centre automation tool. To make their calls seem human-like, they wanted a latency less than 1 second. We optimised their whole model pipeline including STT and LLMs, decreasing the latency by more than 50% and saving more than $100k in costs.

Some context about Vodex:  

----------------------------

In the call centre automation space, **Vodex is a category leader**, offering advanced solutions to streamline operations and elevate customer experiences. Having raised more than $2 Million in funding from Unicorn India Ventures and Pentathlon Ventures, they are positioned to disrupt the generative AI calling space.

Latency issues faced by Vodex:  

In call centre operations, minimizing latency is crucial for maintaining high-quality customer interactions and operational efficiency. Even slight delays can lower customer satisfaction and lead to call drop-offs. Latency below one second is vital for natural-sounding calls and trust-building. Before collaborating with Simplismart, Vodex faced latency issues averaging 2.4 seconds, impacting smooth customer interactions. It was rigorous to keep users engaged on a system having these latencies. Addressing latency is not just technical, it is essential for customer satisfaction and reducing churn in contact centre automation companies.

Generative AI Product Suite from Simplismart
--------------------------------------------

Vodex used our Generative AI Product Suite to overcome latency challenges. Our comprehensive suite of AI-powered solutions is meticulously designed to optimize call centre operations and reduce latency to unprecedented levels.

At the heart of the solution lie open-source APIs: 

*   OpenAI Whisper (Simpliscribe)
*   Llama by Meta (SimpliLLM)
*   Tortoise Model by James Betker

These APIs smoothly fit into Vodex's calling process, handling everything from converting speech to text, answering questions, and then converting text to speech.

Simplismart's suite of APIs revolutionizes Vodex's calling workflow by enhancing STT accuracy, enabling intelligent question answering, and delivering natural-sounding TTS, thus ensuring a cohesive and engaging customer experience.

### How does Simplismart decrease latency and save costs?

We have made a lot of optimisations on all levels to speed up the ML model inference engine.

!Simplismart Model Optimisations

1.  **Simplismart Universal Serving Layer:** We have tested and benchmarked the most used ML model servers like vLLM and Triton. The Simplismart serving layer automatically chooses the fastest inference servers depending on the model and deploys it to production.  
    
2.  **Simplismart Universal Model Backend:** The Simplismart universal model backend employs frameworks like Onnx and TRT-LLM to access hardware acceleration.
3.  **Quantisation:** With the help of Simplismart, Vodex employed fp16 and int8 Quantisation of models to decrease their size, increasing compute speeds.
4.  **Efficient Finetuning:** With the help of efficient fine-tuning techniques like LoRA and PEFT, we trained models in Hindi and Regional Indic languages, giving Vodex a massive competitive advantage in the Indian market.

Conclusion:
-----------

Reducing latency and compute costs was crucial for Vodex to retain its audience and increase customer experience. We have helped them fine-tune and deploy models using our custom inference engine:

1.  This decreased their latency from 2.4 seconds to 0.9 seconds.
2.  Saved $100k in costs in the last year.