from xml.etree.ElementTree import Element, SubElement, tostring
from xml.etree import ElementTree
from xml.dom import minidom

def plk2xml(plk):
	root = Element('plk')

	for separator in plk.data:
		# Create a parent element for each separator in the data
		separator_element = SubElement(root, separator["type"])

		# Set its attributes
		for key in separator:
			# We of course don't want to set an attribute for "tokens"
			# Type is already encoded as the element itself
			if key in ["tokens", "type"]:
				continue

			separator_element.set(key, separator[key])

		# Now, create token children for all tokens under this separator
		i = 1 # All other documentation is 1-based... so I thought I'd just follow
		for token in separator["tokens"]:
			token_element = SubElement(separator_element, "token")
			token_element.set("id", str(i))

			# Again, create children for the different token attributes
			for key in token:
				# We handle this separately
				if key in [ "complex", "lemmata_complex", "lemmata_complex_ids",
							"lemmata_complex_indices", "form_ids", "lemma_ids" ]:
					continue

				key_element = SubElement(token_element, key)
				key_element.text = token[key]

			# Set form ids and lemma ids
			form_ids_element = SubElement(token_element, "form_ids")
			for form_id in token["form_ids"]:
					form_id_element = SubElement(form_ids_element, 'id')
					form_id_element.text = form_id

			lemma_ids_element = SubElement(token_element, "lemma_ids")
			for lemma_id in token["lemma_ids"]:
					lemma_id_element = SubElement(lemma_ids_element, 'id')
					lemma_id_element.text = lemma_id

			# If complex, add the required elements
			if token["complex"]:
				complex_element = SubElement(token_element, 'complex')

				# Add all complex lemmata
				lemmata_element = SubElement(complex_element, 'lemmata')
				for lemma in token["lemmata_complex"]:
					lemma_element = SubElement(lemmata_element, 'lemma')
					lemma_element.text = lemma

				# Add all complex lemmata ids
				lemmata_ids_element = SubElement(complex_element, 'lemmata_ids')
				for lemma_id in token["lemmata_complex_ids"]:
					lemma_id_element = SubElement(lemmata_ids_element, 'id')
					lemma_id_element.text = lemma_id

				# Add all corresponding indices
				lemmata_indices_element = SubElement(complex_element, 'indices')
				j = 0
				for lemma_indices in token["lemmata_complex_indices"]:
					lemma_element = SubElement(lemmata_indices_element, "lemma")
					lemma_element.set("form", token["lemmata_complex"][j])

					for lemma_index in lemma_indices:
						lemma_index_element = SubElement(lemma_element, "index")
						lemma_index_element.text = lemma_index

					j += 1

			i += 1



	return tostring(root, "UTF-8").decode("UTF-8")