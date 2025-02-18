# **Paper Summarizer with GPT Integration**

This tool automates the extraction and summarization of academic papers using OpenAI's GPT models. It processes PDF documents, extracts key information such as the abstract, keywords, and summary, and generates detailed outputs, including IEEE citations. The summaries are formatted as markdown files, ready for integration with **Obsidian**, a popular knowledge management tool.

---

## **Features**
- **PDF Extraction**: Automatically extracts text from PDF papers using the **PyMuPDF** library.
- **GPT-3.5/4 Analysis**: Uses OpenAI’s GPT models to analyze the content and generate:
  - IEEE citation in the required format.
  - Keywords extracted from the paper.
  - Abstract directly copied from the paper.
  - A 1-paragraph summary of the paper.
- **Markdown File Generation**: Automatically creates **Obsidian-friendly markdown files** with paper summaries and links to related topics.
- **Obsidian Integration**: Links extracted keywords as Obsidian wiki links (`[[keyword]]`), making them easily navigable within Obsidian’s graph view.

---

## **Getting Started**

Follow these steps to get the tool running on your local machine:

### **1. Set up your environment**
First, ensure you have **Python 3.x** installed. If you don't have Python, you can download it from [here](https://www.python.org/downloads/).

#### **Install Dependencies**
Clone this repository or download the script `OpenAI_interact.py`, and then install the necessary dependencies:


pip install openai pymupdf


### **2. Get your OpenAI API Key**

To use OpenAI's GPT models, you will need an API key. Here's how to obtain it:

- Go to [OpenAI's API page](https://platform.openai.com/signup) and sign up for an account.
- After signing in, navigate to the **API Keys** section of the [OpenAI dashboard](https://platform.openai.com/account/api-keys).
- Create a new API key and copy it.

#### **Important:**
- You will need this API key to make requests to OpenAI's servers. Keep it safe and do **not** share it publicly.

### **3. Configure the Script**

Before running the script, you'll need to configure the following:

1. **Set your OpenAI API Key**:
   Open the `OpenAI_interact.py` file and add your API key in the line where it's specified:


   openai.api_key = 'your_openai_api_key'

 ### **Define the folder paths**

- **papers_folder**: Set the folder path where your PDF papers are stored (e.g., `'C:/Documents/Papers/'`).
- **Obsidian Vault Path**: Set the path to your Obsidian vault directory where the markdown files will be saved.

python
papers_folder = r'path_to_your_paper_folder'

### **4. Run the Script**

Once everything is set up, you can run the script using your preferred method (e.g., from the terminal or a Python IDE):


python OpenAI_interact.py

### **5. Check Your Obsidian Vault**

After running the script, open your Obsidian vault, and you should see the newly created markdown files for each paper in the folder. These files will contain:

- **IEEE citation**
- **Keywords** (linked to other notes in your vault)
- **Abstract**
- **1-paragraph summary**

You can visualize connections between your notes using Obsidian's **graph view**.

![alt text]( https://github.com/andrewjeyaraj/Paper_Summarizer/blob/main/graph_view.png "Logo Title Text 1")

### **How the Graph is Built Using Keywords**

In Obsidian, the **graph view** shows the relationships between notes based on the links between them. The script automatically creates **links** between papers using **keywords** extracted from each paper. For example, if two papers share the keyword `AI`, a link is created between the two papers in the markdown file.

Once you run the script, you should have the papers listed as separate pages in obsidian and when you click on each page, you should see the information listed about the paper like this:
![alt text](https://github.com/andrewjeyaraj/Paper_Summarizer/blob/main/generated_example.png "Logo Title Text 1")





