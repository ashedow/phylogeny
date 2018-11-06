import sys
import os
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

def check_seq_file(seqs):	
	seqs=args.seq
	if(not check_file_exists(otu_map)):
		print ("Either seqs file is missing or is not readable")
		sys.exit()
	# parse output dir
	out_dir=args.out_dir
	safe_make_dir(out_dir)

def main():
	# parse otu map file
	otu_map = args.otu_map	
	if(not check_file_exists(otu_map)):
		print ("Either OTU_MAP file is missing or is not readable")
		sys.exit()
	
	check_seq_file(seqs)
	# parse OTUs interested
	otu=args.otu
	if(not check_file_exists(otu)):
		print ("Either otu file is missing or is not readable")
		sys.exit()
	
	otu_array = []
	print("Reading otu file... ...\n")
	with open(otu, "r") as f:
		for line in f:
			otu_array.append(line.rstrip())
	print("Read "+ str(len(otu_array)) +" OTUs.\n")
	
	print(otu_array)
	# read seqs fasta file
	seq_record_dict = SeqIO.index(seqs, "fasta")
	
	# read otu_map file
	otu_map_dict={}
	with open(otu_map, "r") as in_otu_map:
		for line in in_otu_map:
			tmp=line.rstrip().split("\t")
			otu_map_dict[tmp[0]]=tmp[1:]
	#print( otu_map_dict.items() )

	# loop find otu's corresponding sequences and write to file named by otu name.
	for otu_tmp in otu_array:
		if(otu_tmp in otu_map_dict):
			seq_list=otu_map_dict[otu_tmp]
			output_handle = open(out_dir+"/"+otu_tmp+".fasta", "w")
			for seq in seq_list:
				if(seq in seq_record_dict):
					out_seq_record_obj=seq_record_dict[seq]
					SeqIO.write(out_seq_record_obj, output_handle, "fasta")
			output_handle.close()

	seq_record_dict.close()


if __name__ == '__main__':
    main()
