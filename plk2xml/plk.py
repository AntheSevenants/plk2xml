import os.path
import re

class plk:
	def __init__(self, filename):
		self.filename = filename

		# Throw an error if the file does not exist
		if not os.path.exists(filename):
			raise FileNotFoundError("Could not find file {}".format(filename))

		# Read file contents and save to this object
		with open(filename, "rt", encoding="latin-1") as reader:
			self.content = reader.read()

		self.parse()

	def parse(self):
		# Will hold the PLK data as an object
		plk_data = []

		# We need to parse the file line by line
		lines = self.content.split("\n")

		for line in lines:
			# Skip empty lines
			if len(line) == 0:
				continue

			# Sentence separator found
			if line[0] == "<":
				separator_regex = re.search(r"<([aumu]{2}) id=\"(\d+)\" s=\"(.*?)\" tb=\"([\d.]+)\">",
											line)

				if separator_regex is None:
					raise Exception("Could not match separator to CGN specification")

				# Extract data from the regex
				separator = { "type": separator_regex.groups()[0],
							  "id": separator_regex.groups()[1],
							  "s": separator_regex.groups()[2],
							  "tb": separator_regex.groups()[3],
							  "tokens": [] } # will hold the tokens of this separator

				# Append to the separator
				plk_data.append(separator)
				continue
		
			# TSV content
			token_line_data = line.split("\t")

			token_data = { "form": token_line_data[0],
						   "pos": token_line_data[1],
						   "lemma": token_line_data[2],
						   "form_ids": token_line_data[3].split("|"),
						   "lemma_ids": token_line_data[4].split("|"),
						   "complex": False }

			# If the token is complex
			if len(token_line_data) > 6:
				# If line 6 is not empty, this is a complex line
				if token_line_data[5]:
					token_data = { **token_data,
								   "complex": True,
								   "lemmata_complex": token_line_data[5].split("/"),
								   "lemmata_complex_ids": token_line_data[6].split("/"),
								   "lemmata_complex_indices": list(map(lambda lemma_ids: lemma_ids.split(","),
								   								       token_line_data[7].split("/"))) }

			plk_data[-1]["tokens"].append(token_data)

		self.data = plk_data