# few-shot: standard
standard_prompt = '''You are an expert chemist. Given the reactants SMILES, your task is to predict the main product SMILES using your experienced chemical Reaction Prediction knowledge. 
Please strictly follow the format, no other information can be provided. You should only reply with SMILES string notations to represent the product. The input contains the reactants and reagents which are split by '.'. The product smiles must be valid and chemically reasonable. 
Reactants+Reagents: CC(O)OCCC(c1ccccc1)(c1ccccc1)c1ccccc1.Oc1ccc(I)cc1
Products: CC(O)OCCOc1ccc(I)cc1
Reactants+Reagents: CCN(CC)CC.CN1CCC(O)N(c2nnc(C3CC3)s2)C1=O.O=C(Cl)c1ccccc1.c1ccccc1
Products: CN1CCC(OC(=O)c2ccccc2)N(c2nnc(C3CC3)s2)C1=O
Reactants+Reagents: C1CCOC1.CC(C)(C)c1ccc(OCC(=O)O)cn1.CS(=O)(=O)Nc1ccc(CN)cc1F.Cl
Products: CC(C)(C)c1ccc(OCC(=O)NCc2ccc(NS(C)(=O)=O)c(F)c2)cn1
Reactants+Reagents: CS(C)=O.O=C([O-])[O-].O=Cc1ccccc1F.SC1CCCCC1.[K+].[K+]
Products: O=Cc1ccccc1SC1CCCCC1
Reactants+Reagents: C1CCOC1.CO.Cl.N#Cc1ccc(OCC(=NNC(=O)Nc2ccc(OC(F)(F)F)cc2)c2ccccc2)cc1.[BH3-]C#N.[Na+]
Products: N#Cc1ccc(OCC(NNC(=O)Nc2ccc(OC(F)(F)F)cc2)c2ccccc2)cc1
Reactants+Reagents: CCCNCC(O)(CNc1cccc2c1cnn2-c1ccc(F)cc1)C(F)(F)F.O=C(O)c1ccsc1
Products:
'''


# one-shot: cot
cot_prompt = '''You are an expert chemist. Given the reactants SMILES, your task is to predict the main product SMILES using your experienced chemical Reaction Prediction knowledge.
Please strictly follow the format, no other information can be provided. The input contains the reactants and reagents which are split by '.'. The product smiles must be valid and chemically reasonable.
Reactants+Reagents: [Li]c1ccccc1.CC(=O)C(C)C.CCOCC
Possible Steps: 
This is a remove bond step. Taking the pair of electrons between the Li and C atoms and moving them to the C atom, giving rise to [Li+]. 
A bond is added when electrons are moved from the C atom in reactant 1 to a C atom in reactant 2. 
A pair of electrons are removed between the C and O atoms and moved to the O atom, giving rise to the one of the products CC(C)C([O-])c1ccccc1.
products: CC(C)C([O-])c1ccccc1.[Li+]
Reactants+Reagents: {input}
'''

# Prompts that generating steps by GPT, training~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
generate_steps_one_shot = '''You are an expert chemist. Given the reactants SMILES, your task is to predict the main product SMILES using your experienced chemical Reaction Prediction knowledge. Please strictly follow the format, no other information can be provided. The input contains the reactants and reagents which are split by '.'. The product smiles must be valid and chemically reasonable. 
Reactants+Reagents: [Li]c1ccccc1.CC(=O)C(C)C.CCOCC 
products: CC(C)C([O-])c1ccccc1.[Li+] 
Possible Steps:  First, this is a remove bond step, taking the pair of electrons between the Li and C atoms and moving them to the C atom, giving rise to [Li+].  Then, a bond is added when electrons are moved from the C atom in reactant 1 to a C atom in reactant 2. Then, A pair of electrons are removed between the C and O atoms and moved to the O atom, giving rise to the one of the products CC(C)C([O-])c1ccccc1. So, the products are CC(C)C([O-])c1ccccc1.[Li+].
Reactants+Reagents: {input1}
products: {input2}
Possible Steps:
'''

# few-shot cot after generating prompts by GPT testing~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
cot_prompt_testing = '''You are an expert chemist. Given the reactants SMILES, your task is to predict the main product SMILES using your experienced chemical Reaction Prediction knowledge.
Please strictly follow the format, no other information can be provided. The input contains the reactants and reagents which are split by '.'. The product smiles must be valid and chemically reasonable.
Reactants+Reagents: [Li]c1ccccc1.CC(=O)C(C)C.CCOCC
Possible Steps: 
This is a remove bond step. Taking the pair of electrons between the Li and C atoms and moving them to the C atom, giving rise to [Li+]. 
A bond is added when electrons are moved from the C atom in reactant 1 to a C atom in reactant 2. 
A pair of electrons are removed between the C and O atoms and moved to the O atom, giving rise to the one of the products CC(C)C([O-])c1ccccc1.
products: CC(C)C([O-])c1ccccc1.[Li+]
Reactants+Reagents: CC(O)OCCC(c1ccccc1)(c1ccccc1)c1ccccc1.Oc1ccc(I)cc1
Possible Steps:
This is a condensation reaction. The hydroxyl group (-OH) on the first reactant reacts with the hydrogen atom on the second reactant to form water (H2O), while the remaining portions of the reactants are combined to form the product. 
Therefore, the main product SMILES is: CC(O)OCCOc1ccc(I)cc1.
products: CC(O)OCCOc1ccc(I)cc1
Reactants+Reagents: CCN(CC)CC.CN1CCC(O)N(c2nnc(C3CC3)s2)C1=O.O=C(Cl)c1ccccc1.c1ccccc1
Possible Steps:
This is a combination reaction. The nitrogen atom on the first reactant forms a bond with the oxygen atom on the second reactant, resulting in the formation of a new bond between the two reactants. Additionally, the chlorine atom on the third reactant is replaced by the oxygen atom from the second reactant. Finally, the remaining portions of the reactants are combined to form the product. Therefore, the main product SMILES is: CN1CCC(OC(=O)c2ccccc2)N(c2nnc(C3CC3)s2)C1=O.
products: CN1CCC(OC(=O)c2ccccc2)N(c2nnc(C3CC3)s2)C1=O
Reactants+Reagents: {input}
Possible Steps:
'''


