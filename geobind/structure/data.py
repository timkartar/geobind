import os
import json
import re
import glob

def compileRegexes(obj):
    # compile regexes loaded from JSON files
    objType = type(obj)
    if(objType is dict):
        for key in obj:
            if(type(obj[key]) is str):
                obj[key] = re.compile(obj[key])
            else:
                compileRegexes(obj[key])
    elif(objType is list):
        for i in range(len(obj)):
            if(type(obj[i]) is str):
                obj[i] = re.compile(obj[i])
            else:
                compileRegexes(obj[i])

class Data(object):
    def __init__(self):
        # standard protein residues
        self.standard_residues = [
            'ALA',
            'ARG',
            'ASN',
            'ASP',
            'CYS',
            'GLU',
            'GLN',
            'GLY',
            'HIS',
            'ILE',
            'LEU',
            'LYS',
            'MET',
            'PHE',
            'PRO',
            'SER',
            'THR',
            'TRP',
            'TYR',
            'VAL'
        ]
        
        # planar protein residues
        self.standard_planar_residues = [
            "ARG",
            "PHE",
            "TYR",
            "TRP",
            "HIS",
            "ASN",
            "ASP",
            "GLN",
            "GLU"
        ]
        
        # standard DNA nucleotides
        self.standard_DNA_nucleotides = [
            "DA",
            "DC",
            "DG",
            "DT"
        ]
        
        # map from 3 letter residue code to 1 letter
        self.long_to_short = {
            "ALA": "A",
            "ARG": "R",
            "ASN": "N",
            "ASP": "D",
            "CYS": "C",
            "GLU": "E",
            "GLN": "Q",
            "GLY": "G",
            "HIS": "H",
            "ILE": "I",
            "LEU": "L",
            "LYS": "K",
            "MET": "M",
            "PHE": "F",
            "PRO": "P",
            "SER": "S",
            "THR": "T",
            "TRP": "W",
            "TYR": "Y",
            "VAL": "V",
            "DA": "A",
            "DC": "C",
            "DG": "G",
            "DT": "T",
            "DI": "I",
            "5CM": "m",
            "DU": "U"
        }
        
        DATA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_data")
        self.data_path = DATA_PATH
        
        # Components (subset of Chemical Component Dictionary)
        with open(os.path.join(DATA_PATH, 'components.json')) as FILE:
            self.chem_components = json.load(FILE)
        
        # Regular expressions
        with open(os.path.join(DATA_PATH, 'regexes.json')) as FILE:
            self.regexes = json.load(FILE)
            compileRegexes(self.regexes)
        
        # Residue hydrophobicity data
        with open(os.path.join(DATA_PATH,'residue-hydrophobicity.json')) as FILE:
            self.residue_hydrophobicity = json.load(FILE)
        
        # Standard SASA data
        with open(os.path.join(DATA_PATH, 'standard-sasa.json')) as FILE:
            self.standard_sasa = json.load(FILE)
        
        # Standard SESA data
        with open(os.path.join(DATA_PATH, 'standard-sesa.json')) as FILE:
            self.standard_sesa = json.load(FILE)
            
        # Hydrogen bond donor/acceptor data
        with open(os.path.join(DATA_PATH,'hbond-data.json')) as FILE:
            self.hydrogen_bond_data = json.load(FILE)
        
        # Covalent bond data
        with open(os.path.join(DATA_PATH,'bond-data.json')) as FILE:
            self.covalent_bond_data = json.load(FILE)
        
        # vdw radii
        with open(os.path.join(DATA_PATH,'vdw-radii.json')) as FILE:
            self.vdw_radii = json.load(FILE)
            
        # Tripeptide conformations
        self.tripeptides = glob.glob(os.path.join(DATA_PATH, "tripeptides/*_md.pdb"))
        
        ################################# Structure class datasets #################################
        self.label_sets = {}
        with open(os.path.join(DATA_PATH, 'BINARY_STANDARD_DNA.json')) as FILE:
            self.label_sets["BINARY_STANDARD_DNA"] = json.load(FILE)
        
        with open(os.path.join(DATA_PATH, 'MULTICLASS_STANDARD_DSDNA.json')) as FILE:
            self.label_sets["MULTICLASS_STANDARD_DSDNA"] = json.load(FILE)
        
        with open(os.path.join(DATA_PATH, 'MULTICLASS_STANDARD_SSDNA.json')) as FILE:
            self.label_sets["MULTICLASS_STANDARD_SSDNA"] = json.load(FILE)

data = Data()
