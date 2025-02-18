import os
import openai
import fitz  # PyMuPDF for PDF parsing
from datetime import datetime

# Set your OpenAI API key
openai.api_key = ''

# Define the folder path where papers are located
papers_folder = r''

# Define the function to extract text from a PDF
def extract_text_from_pdf(pdf_path):
    # Open the PDF file
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()  # Extract text from each page
    return text

# Define the function to call GPT for analysis
def analyze_paper(paper_text, prompt):
    # Create a structured list for 'messages' to send to the API
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"{prompt}\n\n{paper_text}"}
    ]
    
    # Request to GPT with the provided prompt using the correct chat model API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use the appropriate GPT model (e.g., gpt-3.5-turbo, gpt-4)
        messages=messages,  # Ensure messages are properly passed
        max_tokens=1500,  # Adjust based on paper length
        temperature=0.7,
    )
    return response['choices'][0]['message']['content'].strip()


# Function to extract keywords from GPT response
def extract_keywords(gpt_response):
    # Assuming the keywords are in the format "Keywords: keyword1, keyword2, ..."
    # Extract keywords from the GPT response (simple regex to capture them)
    import re
    match = re.search(r"Keywords:\s*(.*)", gpt_response)
    if match:
        keywords = match.group(1).split(',')  # Split keywords by commas
        return [keyword.strip() for keyword in keywords]
    return []


MAX_INPUT_TOKENS = 3500  # Set the maximum tokens for input text (approx.)


def truncate_input_text(paper_text, max_tokens=MAX_INPUT_TOKENS):
    # Estimate the number of tokens by splitting text on spaces (very rough estimation)
    tokens = paper_text.split()  # A simple tokenization by spaces
    if len(tokens) > max_tokens:
        return " ".join(tokens[:max_tokens])  # Truncate to the first max_tokens tokens
    return paper_text




# Define the function to save output as Obsidian markdown
def save_as_markdown(output_text, file_name, keywords=None):
    # Include keyword links in the content if keywords are provided
    if keywords:
        # Create links for each keyword
        keyword_links = [f"[[{keyword}]]" for keyword in keywords]
        keyword_section = "\n\n**Related Topics:**\n" + "\n".join(keyword_links)
        output_text += keyword_section
    
    # Define the file path for Obsidian markdown
    file_path = os.path.join(r'', file_name + '.md') #Set path to the obsidian vault
    with open(file_path, 'w') as f:
        f.write(output_text)

# Define the prompt template
prompt_template = """
Analyze the following paper and provide:
1. IEEE Citation in the format [Author(s), Year]
2. Keywords (List of important keywords that represent the content of the paper)
3. Abstract (directly copied from the paper)
4. A 1-paragraph summary of the paper.

Paper:
"""

# Iterate through the papers in the folder
for filename in os.listdir(papers_folder):
    if filename.endswith(".pdf"):
        # Full file path
        pdf_path = os.path.join(papers_folder, filename)
        
        
        
        # Extract text from the PDF
        paper_text = extract_text_from_pdf(pdf_path)
        
        paper_text = truncate_input_text(paper_text)
        
        # Get the analysis from GPT
        analysis = analyze_paper(paper_text, prompt_template)
        
        # Extract the keywords from the GPT response
        keywords = extract_keywords(analysis)

        # Assuming the author's name and year of publication can be extracted from the filename
        author_year = filename.split('.')[0]  # Adjust based on your file naming format

        # Format the output
        markdown_content = f"# {author_year}\n\n{analysis}"

        # Save the result as an Obsidian markdown file, linking related topics (keywords)
        save_as_markdown(markdown_content, author_year, keywords)

        print(f"Processed and saved: {author_year}")
