
## Avro Python API Reference Docs

Avro is a Data Serialization framework that converts any data format into machine and binary format. Avro supports Python3. These documentation will guide you through the Python's Avro APIs, classes, and methods. The documentation are generated using [Sphinx](https://www.sphinx-doc.org/en/master/) and pages are built using the [Myst in Sphinx](https://myst-parser.readthedocs.io/en/v0.15.1/index.html).

## Consideration before running the Docs.

- Unzip the `avro` folder into your local storage.
- Open the `avro` directory with an IDE (Recommended Pycharm).
- Open the terminal and type `pip install -r requirement.txt` to install required packages.
- You will see `conf.py` a configuration file which you can use to modify the template, extensions, and other configuration of Sphinx.
- To play with the documentation, in the terminal, type `make html` to create HTML version of pages. The HTML version of the pages are always generated and stored within the build > html folder.

## Running Docs locally

Sphinx is a Open Source Python documentation generator. The Avro documentation pages are generated using the markdown (Myst) library in Sphinx. Once the `.md` pages are converted into HTML, you can see it live on your local server by typing;
`sphinx-autobuild source build/html`. You will see the localserver has started running on `http://localhost:8000/` or `http://127.0.0.1:8000/`. 

## Sphinx Documentation Theme

The documentation is crafted on Furo theme. However, after installing the packages from `requirement.txt` and running the docs locally, if you are still seeing the default theme [`albaster`](https://alabaster.readthedocs.io/en/latest/), you can refer to the [Furo](https://sphinx-themes.org/sample-sites/furo/) docs. 

## Accessing the Example Code

Avro sample file uses DataFileReader and DataFileWriter in the `example.py` file to read/write data to Avro files. For more information, access the file from the example.py. 
If you run the code, it generates the output in the `example.avro` Avro file.



