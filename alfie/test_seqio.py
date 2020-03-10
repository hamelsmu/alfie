
import os 
import unittest

from seqio import file_type, outfile_dict, read_fasta, read_fastq
from alfie import ex_fasta_file, ex_fastq_file

class SeqioTests(unittest.TestCase):
	"""Unit tests for the seqio functions"""
	@classmethod
	def setUpClass(self):
		"""Initiate the test class instance."""
		self._expected_kingdom_dict = {0: 'alfie_out/animalia_test.fasta',
										 1: 'alfie_out/bacteria_test.fasta',
										 2: 'alfie_out/fungi_test.fasta',
										 3: 'alfie_out/plantae_test.fasta',
										 4: 'alfie_out/protista_test.fasta'}
		
		self._fasta_infile = ex_fasta_file
		self._fastq_infile = ex_fastq_file

	@classmethod
	def tearDown(self):
		"""After unit tests, remove the temporary outputs."""
		try:
			os.rmdir("alfie_out")
		except OSError:
			pass

	def test_file_type(self):
		"""Test that the file type is properly identified."""
		self.assertEqual(file_type("file_1.fa"), 
						"fasta")
		self.assertEqual(file_type("file_1.fasta"),
						"fasta")
		self.assertEqual(file_type("in.file_1.fa"),
						"fasta")
		self.assertEqual(file_type("file_2.fq"),
						"fastq")
		self.assertEqual(file_type("file_2.fastq"),
						"fastq")
		self.assertEqual(file_type("in.file_2.fq"),
						"fastq")

		with self.assertRaises(ValueError):
			self.assertEqual(file_type("infile_2.txt"))
	
		with self.assertRaises(ValueError):
			self.assertEqual(file_type("in.file_2.csv"))

	def test_outfile_builder(self):
		"""Test that the output file set is generated properly."""
		self.assertEqual(outfile_dict("test.fasta"), 
						self._expected_kingdom_dict)

		self.assertEqual(outfile_dict("in_data/test.fasta"), 
				self._expected_kingdom_dict)

	def test_fasta_reader(self):
		""" Test the fasta reader functions."""
		self._fasta_read = read_fasta(self._fasta_infile)
		
		self.assertEqual(len(self._fasta_read), 100)
		
		self.assertEqual(self._fasta_read[0]['name'], 
						"seq1_plantae")
		self.assertEqual(self._fasta_read[1]['name'], 
						"seq2_bacteria")
		self.assertEqual(self._fasta_read[2]['name'], 
						"seq3_protista")

		self.assertEqual(self._fasta_read[0]['sequence'][:25], 
						"TTCTAGGAGCATGTATATCTATGCT")
		self.assertEqual(self._fasta_read[1]['sequence'][:25],
						"ACGGGCTTATCATGGTATTTGGTGC")
		self.assertEqual(self._fasta_read[2]['sequence'][:25],
						"AGTATTAATTCGTATGGAATTAGCA")

	def test_fastq_reader(self):
		""" Test the fastq reader functions."""
		self._fastq_read = read_fastq(self._fastq_infile)

		self.assertEqual(len(self._fastq_read), 100)
	
		for i in range(len(self._fastq_read)):
			self.assertEqual(list(self._fastq_read[i].keys()),
							['name', 'sequence', 'strand', 'quality'])

		self.assertEqual(self._fastq_read[0]['sequence'][:25], 
						"ttctaggagcatgtatatctatgct")
		self.assertEqual(self._fastq_read[1]['sequence'][:25],
						"acgggcttatcatggtatttggtgc")
		self.assertEqual(self._fastq_read[2]['sequence'][:25],
						"agtattaattcgtatggaattagca")


if __name__ == '__main__':
	unittest.main()

