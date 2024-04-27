The Research Paper Retrieval System project presents a sophisticated research paper retrieval system specifically tailored to the expansive domain of computer science. Utilizing the robust capabilities of Whoosh, a pure Python search engine library, the system provides an advanced text indexing and searching framework that efficiently handles large volumes of academic papers. Our system integrates a field-weighted search algorithm, BM25F, to optimize relevance scoring and ensure the high accuracy of search results. The multi-field query capability allows users to refine searches across document titles, abstracts, and content, enhancing the retrieval of pertinent literature.
The user interface is developed using Streamlit, which offers a streamlined and intuitive user experience.

I am using Python 3.10.14

Steps to execute the project:

Step1)   
pip install -r requirements.txt

This will install all the necessary modules , to instal  pdftotext module you nedd to have Visual Studio Build tools

Step2)

chmod +x create_folders.sh

this will create the folders where data will be stored

Step3)

python src/scraping.py

this will scrape the data from core website


Step4)
python src/preprocessing.py

this will preprocess the pdf data and convert it to tokens 

Step5)
python src/indexing.py
this will create  index table

Step6)
streamlit run  src/app.py
this will start streamlit


Frontend images:
![image](https://github.com/yoshhhhhhh/Research-paper-retrieval-system/assets/118333938/9096d480-10e5-4640-a632-d1221f669404)

![image](https://github.com/yoshhhhhhh/Research-paper-retrieval-system/assets/118333938/027ce72a-6550-4570-a24c-313986d28696)


