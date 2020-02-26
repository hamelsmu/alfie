# alfie <img src="alfie/data/alfie.jpeg" height="140" align="right" alt="Alfie"/>
## alignment free identification of eDNA

## Note: This is a work in progress. It is functional, but documentation and tests are still being added

Alfie is a command line tool for kingdom-level classification and processing of DNA sequence data. 



## Installation

Alfie in a python3 program that depends on the python packages: `numpy`(version >= 1.18.1) and `tensorflow`(version>=2.0.0). If you do not have these installed, it is reccomended that you install python and the required packages via [anaconda](https://www.anaconda.com/distribution/).

To install alfie, download and unzip this repository. From the terminal, enter the downloaded repository and then run the following command:
```
python3 setup.py install
```
To check that the installation was successful, open a new terminal and run the following command (it should pop up the alfie help menu).
```
alfie -h
```


## Usage 
### Command line interface
Alfie can be run as a stand alone command line interface, just specify an input `.fasta` or `.fastq` file using the `-f` flag, and alfie will conduct classification, splitting the input file into five sub files with sequences from the five kingdoms. The output will be a folder named `alfie_out`. The output folder will contain five files (names same as the input, with a prefix indicating the kingdom) that respectively contain the sequence records corrsponding to the kingdom indicated in the file prefix.

You can test this out using the example files shipped with aflie.
```
#from within the alfie folder
alfie -f alfie/data/example_data.fasta

# This will create a folder: alfie_out
# with the files: 
# animalia_example_data.fasta bacteria_example_data.fasta fungi_example_data.fasta plantae_example_data.fasta protista_example_data.fasta

```

For very large files, the input sequence file may need to be processed in a batch fashion. This will run more slowly, but less sequences will be held in memory at once. The batch size (number of sequences) is specified with the `-b` flag. This flag isn't required, and should be used only if the program is crashing (finding the optimal value for your own machine will require some trial and error).
```
alfie -f alfie/data/example_data.fastq -b 100
```

By default, alignment free classification is performed using the default feature set (4mer frequencies) and the corresponding, pre-trained neural network (trained on `COI-5P` sequence fragments of varying lenths). A user can pass an alternative neural network to make predictions with using the `-m` flag. If this option is exercised and the model has not been trained on 4mers, then the `-k` flag must be used to ensure the proper set of kmer features are generated to match the neural network input strucutre.

```
#example using the 6mer model that ships with alfie, note the -k 6 option is required
alfie -f alfie/data/example_data.fastq -m alfie/data/dnn_model_6mers -k 6
```

### The alfie library
Alfie can be used from within python via the api. manual, documentation, and examples are coming soon!
