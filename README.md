# PDF Reader and Question Answering AI Model

This is a Python-based AI model that leverages machine learning and natural language processing techniques to read PDF documents, divide them into chunks, store them in a Chroma DB, and provide question answering capabilities based on the content of the PDF. It also allows you to retrieve the source document for reference.

## Features

- PDF reading: The model can read PDF documents using a PDF parsing library and extract text from them.
- Chunking: The extracted text from the PDF is divided into smaller chunks for easier processing and storage.
- Chroma DB integration: The model stores the extracted text chunks in a Chroma DB, which is a high-performance, scalable, and distributed key-value store for storing large amounts of data.
- Question answering: The model uses natural language processing techniques to process questions and provide answers based on the content of the PDF document.
- Source document retrieval: The model allows you to retrieve the source document for reference, which can be useful for fact-checking or verifying information.

## Usage

1. Install the required dependencies by running the following command: 
    ```
    pip install -r requirements.txt
    ```

2. Run the PDF reader and question answering script by running the following command:
    ```
    python pdf_reader.py
    ```

3. Provide the path to the PDF document that you want to process. The model will read the PDF, divide it into chunks, and store them in the Chroma DB.

4. Once the PDF is processed, you can ask questions related to the content of the PDF. The model will use its question answering capabilities to provide answers based on the content stored in the Chroma DB.

5. You can also retrieve the source document for reference by using the provided function in the script.

## Contributions

Contributions to this project are welcome! If you find any issues or have ideas for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

This project was inspired by the need for efficient and accurate PDF reading and question answering capabilities. Special thanks to the developers of the PDF parsing library and Chroma DB for their excellent tools.
