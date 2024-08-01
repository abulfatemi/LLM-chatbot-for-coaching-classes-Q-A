# LLM-project-for-coaching-classes-Q-A

I developed an end-to-end LLM project using Google Gemini Flash LLM model and Langchain for a hypothetical e-learning company called Abul Coaching. Abul Coaching offers data-related courses and bootcamps. The project involves creating a Q&A system with a Streamlit-based user interface, allowing students to ask questions and receive answers. This system aims to streamline the current process where thousands of learners ask questions via Discord or email, providing a more efficient and interactive experience.



## Project Working

- I created a CSV file titled 'abul_coaching_faqs' containing all general questions asked by students and their parents 
- I loaded the data using langchain.document_loaders.csv_loader and used Hugging Face Instruct Embeddings to create embeddings and used FAISS as vector database
- A retriever is created from the vector database with a score threshold of 0.7, which means that only results with a similarity score above 0.7 will be considered.
- I created a prompt template, instructing the system to generate an answer based on the provided context. It emphasizes extracting text from the "response" section of the source document and explicitly states not to fabricate answers.
- I created a RetrievalQA chain with the specified language model (llm), retriever, and the custom prompt template . The return_source_documents=True flag ensures that the source documents used to generate the answer are also returned.
- I used Streamlit to create the user interface and Ngrok to expose the local app to the internet, making it accessible to others via a public URL.


## Sample Questions
- Do you guys provide internship and also do you offer EMI payments? 
- Do you have javascript course?

## Screenshots

![llm_coaching](https://github.com/user-attachments/assets/34f52608-9bf6-4b94-9790-9057e7679804)

## Demo Video




https://github.com/user-attachments/assets/9c602b74-1923-4a17-85a1-5b8098fa9b8f

