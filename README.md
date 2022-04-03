# plk2xml
A small Python library to convert COREX plk files to XML and JSON

## What is plk2xml?

[PLK files](https://ivdnt.org/images/stories/producten/documentatie/cgn_website/doc_Dutch/topics/formats/text/plk.htm) are corpus files found in the [Corpus Gesproken Nederlands (CGN)](https://lands.let.ru.nl/cgn/). PLK seems to be a frankensteined version of XML and TSV. Speaker utterances are divided by XML-like tags, but token contents are tab separated:

```xml
<au id="1" s="N01036" tb="000.000">
ga         WW(pv,tgw,ev)    gaan        93037  30559
je         VNW(pers,...)    je          620014 135108
nou        BW()             nou         620167 135232
met        VZ(init)         met         620087 135170
de         LID(bep,...)     de          619612 134796
trein      N(soort,ev,...)  trein       317006 104897
naar       VZ(init)         naar        620133 135200
Loon       SPEC(deeleigen)  _           0      0      Loon_Op_Zand              608839        8,9,10
Op         SPEC(deeleigen)  _           0      0      Loon_Op_Zand              608839        8,9,10
Zand       SPEC(deeleigen)  _           0      0      Loon_Op_Zand              608839        8,9,10
of         VG(neven)        of          620170 135234
met        VZ(init)         met         620087 135170
de         LID(bep,...)     de          619612 134796
bus        N(soort,ev,...)  bus         54520|54521  16763|16764
?          LET()            ?           0      0
<mu id="2" s="BACKGROUND" tb="152.867">
inschenken SPEC(achter)     _           0      0
water.     SPEC(achter)     _           0      0
<au id="3" s="N01265" tb="175.824">
ja         TSW()            ja          141336 45366
Partij     SPEC(deeleigen)  _           0      0      Partij_Van_De_Arbeid      610975        2,3,4,5
Van        SPEC(deeleigen)  _           0      0      Partij_Van_De_Arbeid      610975        2,3,4,5
De         SPEC(deeleigen)  _           0      0      Partij_Van_De_Arbeid      610975        2,3,4,5
Arbeid     SPEC(deeleigen)  _           0      0      Partij_Van_De_Arbeid      610975        2,3,4,5
is         WW(pv,tgw,ev)    zijn        141101 122511
iets       VNW(onbep,...)   iets        619991 135089
vooruit    BW()             vooruit     620510 135518 vooruitgaan               504346        8,9
gegaan     WW(vd,vrij,...)  gaan        98566  30559  vooruitgaan/achteruitgaan 504346/500431 8,9/9,13
't         LID(bep,...)     het         619904 135669
CDA        N(eigen,ev,...)  CDA         381902 125724
iets       VNW(onbep,...)   iets        619991 135089
achteruit  BW()             achteruit   619374 134626 achteruitgaan             500431        9,13
SP         N(eigen,ev,...)  SP          393723 132419
verdubbeld WW(vd,...)       verdubbelen 333336 109296
.          LET()            .           0      0
```

It seems like this format was supported in [COREX](https://www.mpi.nl/COREX/), the "Corpus Exploitation Software for CGN", but that program seems long dead ("last update: May 30, 2005"). plk2xml aims to keep these corpus files alive by allowing conversion to two popular (not to mention *standard*) formats: XML and JSON.

## Installing plk2xml

plk2xml is not available on any Python package manager (yet). To use it, simply clone this repository to local machine. From there, you can simply call the `plk2xml.py` script, or import plk2xml's libraries for use in your own program.

## Using plk2xml

### Command line conversion

You can quickly convert PLK files to XML and JSON by using the supplied `plk2xml.py` file. Refer to the following snippet to learn how to use the script:

```bash
# Converts the input PLK file to XML
python3 plk2xml.py "fn000131.plk" "fn000131.xml"

# Converts the input PLK file to JSON
python3 plk2xml.py "fn000131.plk" "fn000131.json"
```

### Library use

#### Pythonic representation

You can also use plk2xml in your own programs. To simply get a Pythonic representation of a PLK file, import the `plk` class and supply the PLK file's filename:
```python
from plk2xml.plk import plk
plk_file = plk("fn000131.plk")
```
You can then access the file's contents as an object using the `.data` property:
```python
plk_file.data
```
The data structure of this object is the same as the JSON output.

You can also use the built-in converters, if you so desire.

#### Conversion to XML

```python
from plk2xml.plk import plk
from plk2xml.plk2xml import plk2xml

plk_file = plk("fn000131.plk")
xml = plk2xml(plk_file)
```

You can supply the `indent=False` argument to disable XML pretty printing. This will greatly improve conversion time.

#### Conversion to JSON

```python
from plk2xml.plk import plk
from plk2xml.plk2json import plk2json

plk_file = plk("fn000131.plk")
json = plk2json(plk_file, indent=4)
``` 

You can supply a custom indentation by passing the number of indentation spaces as the `indent` argument. To disable indentation, set `indent=None`

## Example output

These examples are snippets and do not represent the full output.

### XML

```xml
<?xml version="1.0" ?>
<plk>
	<au id="53" s="N00163" tb="134.849">
		<token id="1">
			<form>mijn</form>
			<pos>VNW(bez,det,stan,vol,1,ev,prenom,zonder,agr)</pos>
			<lemma>mijn</lemma>
			<form_ids>
				<id>620111</id>
			</form_ids>
			<lemma_ids>
				<id>135182</id>
			</lemma_ids>
		</token>
		<token id="2">
			<form>directeur</form>
			<pos>N(soort,ev,basis,zijd,stan)</pos>
			<lemma>directeur</lemma>
			<form_ids>
				<id>69422</id>
			</form_ids>
			<lemma_ids>
				<id>22728</id>
			</lemma_ids>
		</token>
		<token id="3">
			<form>prees</form>
			<pos>WW(pv,verl,ev)</pos>
			<lemma>prijzen</lemma>
			<form_ids>
				<id>243874</id>
			</form_ids>
			<lemma_ids>
				<id>80725</id>
			</lemma_ids>
			<complex>
				<lemmata>
					<lemma>aanprijzen</lemma>
				</lemmata>
				<lemmata_ids>
					<id>500214</id>
				</lemmata_ids>
				<indices>
					<lemma form="aanprijzen">
						<index>3</index>
						<index>5</index>
					</lemma>
				</indices>
			</complex>
		</token>
		<token id="4">
			<form>dat</form>
			<pos>VNW(aanw,pron,stan,vol,3o,ev)</pos>
			<lemma>dat</lemma>
			<form_ids>
				<id>619602</id>
			</form_ids>
			<lemma_ids>
				<id>134794</id>
			</lemma_ids>
		</token>
		<token id="5">
			<form>aan</form>
			<pos>VZ(fin)</pos>
			<lemma>aan</lemma>
			<form_ids>
				<id>619352</id>
			</form_ids>
			<lemma_ids>
				<id>134606</id>
			</lemma_ids>
			<complex>
				<lemmata>
					<lemma>aanprijzen</lemma>
				</lemmata>
				<lemmata_ids>
					<id>500214</id>
				</lemmata_ids>
				<indices>
					<lemma form="aanprijzen">
						<index>3</index>
						<index>5</index>
					</lemma>
				</indices>
			</complex>
		</token>
		<token id="6">
			<form>.</form>
			<pos>LET()</pos>
			<lemma>.</lemma>
			<form_ids>
				<id>0</id>
			</form_ids>
			<lemma_ids>
				<id>0</id>
			</lemma_ids>
		</token>
	</au>
</plk>
```

### JSON

```json
[
    {
        "type": "au",
        "id": "53",
        "s": "N00163",
        "tb": "134.849",
        "tokens": [
            {
                "form": "mijn",
                "pos": "VNW(bez,det,stan,vol,1,ev,prenom,zonder,agr)",
                "lemma": "mijn",
                "form_id": "620111",
                "lemma_id": "135182",
                "complex": false
            },
            {
                "form": "directeur",
                "pos": "N(soort,ev,basis,zijd,stan)",
                "lemma": "directeur",
                "form_id": "69422",
                "lemma_id": "22728",
                "complex": false
            },
            {
                "form": "prees",
                "pos": "WW(pv,verl,ev)",
                "lemma": "prijzen",
                "form_id": "243874",
                "lemma_id": "80725",
                "complex": true,
                "lemmata_complex": [
                    "aanprijzen"
                ],
                "lemmata_complex_ids": [
                    "500214"
                ],
                "lemmata_complex_indices": [
                    [
                        "3",
                        "5"
                    ]
                ]
            },
            {
                "form": "dat",
                "pos": "VNW(aanw,pron,stan,vol,3o,ev)",
                "lemma": "dat",
                "form_id": "619602",
                "lemma_id": "134794",
                "complex": false
            },
            {
                "form": "aan",
                "pos": "VZ(fin)",
                "lemma": "aan",
                "form_id": "619352",
                "lemma_id": "134606",
                "complex": true,
                "lemmata_complex": [
                    "aanprijzen"
                ],
                "lemmata_complex_ids": [
                    "500214"
                ],
                "lemmata_complex_indices": [
                    [
                        "3",
                        "5"
                    ]
                ]
            },
            {
                "form": ".",
                "pos": "LET()",
                "lemma": ".",
                "form_id": "0",
                "lemma_id": "0",
                "complex": false
            }
        ]
    }
]
```

## Future work

- find a faster XML indentation process
- add more output formats